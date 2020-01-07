<template>
  <div class="card">
    <form id="projectform" class="projectform" action="submit">
      <h1>Add Project: </h1>
      <div class="hcontainer">

        <div class="hitem">
          <label for="pname">Project Name</label>
          <input type="text" id="pname" placeholder="Project name ..." v-model="projectData.name">
        </div>

        <div class="hitem">
          <label for="pstatus">ProjectStatus:</label>
          <select id="pstatus" name="status" v-model="projectData.status" :class="'color-'+projectData.status">
            <option v-for="st in statusValues" :key="st.value" :value="st.value" :class="'color-'+st.value">{{st.name}}</option>
          </select>
        </div>

        <div class="spacer"></div>

        <div class="hitem">
          <input type="submit" id="psubmit" name="submit" value="Submit" @click.prevent="submit">
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  data() {
     return {
      projectData: {}
     }
  },
  computed: {
    ...mapState(['statusValues']),
  },
  methods: {
    ...mapActions(['addProject']),
    submit() {
      this.addProject(this.projectData)
      this.projectData={}
    }
  },
}
</script>

<style scoped>

</style>