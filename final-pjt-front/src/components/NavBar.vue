<template>
  <nav>
    <ul>
    <li>
      <router-link :to="{ name: 'home' }">Home</router-link>
    </li>
    <li>
      <router-link :to="{ name: 'background' }">
        BGM
      </router-link>
    </li>
    <li>
      <router-link :to="{ name: 'searchname', params:{query:''} }">
        NAME
      </router-link>
    </li>
    <li v-if="isLoggedIn">
      <router-link :to="{ name: 'logout' }">Logout</router-link>
    </li>

    </ul>
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

<style></style>
