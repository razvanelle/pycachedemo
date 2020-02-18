<template>
  <div class="card">
    <div class="hcontainer">
      <h1>Projects: </h1>
      <div class="spacer"></div>
      <div class="hitem">
        <!-- <input class="warn" type="submit" @click="autoUpdate=!autoUpdate" :value="updateStatus"> -->
        <button class="buttonload" @click="autoUpdate=!autoUpdate">
          Loading
          <i class="fa fa-spinner fa-spin" v-if="autoUpdate"></i>
          <span v-else> OFF</span>
        </button>            
      </div>
    </div>
    <ul class="projectlist">
      <li class="vcontainer" v-for="prj in projects" :key="prj.id">
        <div class="project hcontainer">
          <span class="hitem">{{prj.name}}</span>
          <div class="spacer"></div>

          <div class="hitem">
            <select id="pstatus" name="status" :value="prj.status" @input="onStateChange(prj, $event)" :class="'color-'+prj.status">
              <option v-for="st in statusValues" :key="st.value" :value="st.value" :class="'color-'+st.value">{{st.name}}</option>
            </select>
          </div>

          <div class="hitem">
            <input class="warn" type="submit" @click.prevent.stop="delProject(prj.id)" value="Delete">
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  data: () => {
    return {
    }
  },
  computed: {
    ...mapState(['projects', 'statusValues']),
    autoUpdate: {
      // getter
      get: function () {
        console.log(this.$store.state.autoUpdate);
        return this.$store.state.autoUpdate
      },
      // setter
      set: function (val) {
        // this.$store.dispatch('setAutoUpdate', val)        
        this.setAutoUpdate(val)
      }
    },
    updateStatus() {
      const text = 'AutoUpdate: ' + (this.autoUpdate ? 'ON' : 'OFF')
      console.log('Update Status: ', text);
      return text
    }
  },
  methods: {
    ...mapActions(['initializeProjects', 'delProject', 'saveProject', 'setAutoUpdate']),
    onStateChange(prj, event) {
      console.log(prj, event.target.value);
      this.saveProject({id: prj.id, status: event.target.value})
    }
  },
  created() {
    this.initializeProjects()
  }
}
</script>

<style scoped>

.projectlist {
  list-style: none;
  list-style-type: none;
}

.project {
  font-weight: bold;
  margin: 8px 0;
  color: rgb(206, 206, 206);
  background: rgb(52, 52, 53);
  border-radius: 5px;
  text-align: left;
  transition: 0.2s;
}

.project:hover {
  /* box-shadow: 2px 2px 10px 3px rgba(0,0,0,0.2); */
  /* transform:scale(1.01,1.01); */
  background: rgb(78, 78, 78);
}
</style>