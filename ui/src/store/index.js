import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const baseURI = 'http://127.0.0.1:8000/'

export default new Vuex.Store({
  state: {
    projects: [],
    autoUpdate: null,
    lastUpdate: 0,
    statusValues: [
      { value: 0, name: '0 - Requested'},
      { value: 1, name: '1 - Development'},
      { value: 2, name: '2 - Alpha'},
      { value: 3, name: '3 - Beta'},
      { value: 4, name: '4 - Final'},
      { value: 5, name: '5 - Completed'},     
    ],
  },
  mutations: {
    SET_Projects(state, data) {
      state.projects = data
    },
    UPDATE_Projects(state, data) {
      data.forEach(project => {
        const idx = state.projects.findIndex(obj => obj.id == project.id)
        if (idx < 0) {
          state.projects.push(project)
        }
        else {
          // Object.assign(state.projects[idx], project)
          state.projects.splice(idx, 1, project)
        }
      });
    },
    ADD_Project(state, data) {
      state.projects.push(data)
    },
    DEL_Project(state, id) {
      state.projects = state.projects.filter(prj => prj.id!=id)
    },    
    PATCH_Project(state, data) {
      const index = state.projects.findIndex(prj => prj.id==data.id)
      state.projects.splice(index, 1, data)
    },
  },

  // ========================================================
  actions: {
    initializeProjects({commit}) {
      axios.get(baseURI + 'projects/')
      .then((result) => {
        commit('SET_Projects', result.data)
      })
    },
    addProject({commit}, prjdata) {
      axios.post(baseURI + 'projects/', prjdata)
      .then((result) => {
        commit('ADD_Project', result.data)
      })
    },
    delProject({commit}, prjid) {
      axios.delete(baseURI + 'projects/'+prjid+'/')
      .then((result) => {
        commit('DEL_Project', prjid)
      })
    },
    saveProject({commit}, prjdata) {
      if (!prjdata.id)
        throw new Error('No ID specified !!!')
      axios.patch(baseURI + 'projects/'+prjdata.id+'/', prjdata)
      .then((result) => {
        commit('PATCH_Project', result.data)
      })      
    },
    setAutoUpdate({ state, commit, dispatch }, value) {
      state.autoUpdate = value
      if (value)
        dispatch('checkProjectUpdates')
    },
    checkProjectUpdates({ state, commit, dispatch }) {
      console.log('STORE >> Checking for project updates since ', state.lastUpdate)
      if (!state.autoUpdate)
        return
      const timeStamp = new Date().getTime() //.toISOString() //.substr(0, 23) //.replace('T', ' ')

      console.log('HTTP: ', 'update/?time='+state.lastUpdate);
      return axios.get(baseURI + 'update/?time='+state.lastUpdate).then(res => {
        const prjupd = JSON.parse(res.data)
        console.log('RES: ', prjupd, typeof(prjupd))
        if (prjupd.length > 0) {
          axios.get(baseURI + 'projects/?id='+prjupd.join(',')).then(result => {
            console.log('GOT result:', result.data);
            commit('UPDATE_Projects', result.data)
          })
        } else {
          console.log('STORE >> NO UPDATE');
        }
        state.lastUpdate = timeStamp
        state.autoUpdate = true
        setTimeout(() => {
          console.log('Update!');
          dispatch('checkProjectUpdates')
        }, 3000)
      }).catch(err => console.error('ERROR', err))
    },     
  },
  modules: {
  }
})
