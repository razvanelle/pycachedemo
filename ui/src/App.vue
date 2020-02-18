<template>
  <div id="app">
    <ProjectList />
    <ProjectForm />
  </div>
</template>

<script>
import ProjectList from '@/components/ProjectList'
import ProjectForm from '@/components/ProjectForm'

export default {
  name: 'app',
  components: { ProjectList, ProjectForm },

}
</script>

<style>
* { 
  margin: 0; 
  padding: 0; 
}

body {
  background: #bdbdbd;
}

h1 {
  font-size: 25px;  
  margin-bottom: 20px;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* color: #2c3e50;
  margin: 20px 10px; */
}

.button {
  display: inline-block;
  background-color: rgb(179, 177, 177);
  color: rgb(3, 3, 3);
  margin: 5px 10px;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
}

.button:hover {
  background-color: rgb(128, 128, 128);
  color: white;
}

.buttonload {
  background-color: #4CAF50; /* Green background */
  border: none; /* Remove borders */
  color: white; /* White text */
  padding: 12px 24px; /* Some padding */
  font-size: 16px; /* Set a font-size */
  border-radius: 4px;
}

.buttonload:hover {
  background-color: #1b5520;
}


.fa {
  margin: 0px 4px;
}
.hcontainer {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;  
}

.spacer {
  flex-grow: 1;
}

.card {
  text-align: left;
  background: grey;
  color: rgb(223, 223, 223);
  border-radius: 5px;
  margin: 20px 10px;
  padding: 20px 10px;
}

input[type=text], select {
  font-size: 15px;
  font-weight: bold;
  color: rgb(26, 26, 26);
  background: #dfdfdf;
  width: 100%;
  padding: 8px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

select option {
	font-weight:bold;
}

input[type=submit] {
  font-size: 15px;
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #1b5520;
}

.hitem {
  margin: 0px 20px;
}

.warn {
  color: red;
}

.success {
  color: #45a049
}

.color-0 {
  background:rgb(107, 214, 110);
}
.color-1 {
  background:rgb(247, 243, 51);
}
.color-2 {
  background:rgb(233, 112, 64);
}
.color-3 {
  background:rgb(242, 73, 248);
}
.color-4 {
  background:rgb(76, 130, 247);
}
.color-5 {
  background:rgb(159, 155, 160);
}
</style>
