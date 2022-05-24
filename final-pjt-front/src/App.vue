<template>
  
  <div id="app">
    <nav-bar
    v-if="partnerLoggedIn&&userLoggedIn"></nav-bar>
    <router-view
    :key="$route.fullPath"></router-view>
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
import NavBar from './components/NavBar.vue'

export default {
  name : "App",
  components:{
    NavBar

  },
  computed:{
    ...mapGetters(['partnerLoggedIn', 'userLoggedIn'])
  }
    
  
}
</script>





<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
