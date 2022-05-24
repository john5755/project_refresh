<template>
  <nav  class="navbar navbar-expand-lg bg-secondary">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarSupportedContent">        
        <ul class="navbar-nav justify-content-between">
          <li class="nav-item d-flex">
            <router-link :to="{ name: 'background' }" class="nav-link active text-light" aria-current="page" >
              BGM
            </router-link>
            <router-link :to="{ name: 'searchname', params:{query:''} }" class="nav-link active text-light" aria-current="page" >
              NAME
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'home' }" class="nav-link active text-light home-btn" aria-current="page" >Home</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link :to="{ name: 'logout' }" class="nav-link active text-light" aria-current="page" >Logout</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn']),
    },
  }
</script>

<style>
.navbar-nav{
  width: 100%;
}

.home-btn{
  position: relative;
  right: 1.65em;
}

</style>
