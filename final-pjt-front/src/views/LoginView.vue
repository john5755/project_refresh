<template>
  <div>
    <nav>
      <div v-if="userLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </div>
    </nav>
    <h1 v-if="!isLoggedIn" >Login</h1>
    <h1 v-if="userLoggedIn">Partner Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <div v-if="userLoggedIn">
      <router-link :to="{ name: 'profile', params: { username } }">
        {{ currentUser.username }} 프로필수정
      </router-link>
    </div>
    
    <form @submit.prevent="onSubmit(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>

      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>Login</button>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError','userLoggedIn','isLoggedIn','currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      ...mapActions(['login', 'fetchProfile']),
    onSubmit(credentials) {
      this.login(credentials)
      this.credentials.username = ''
      this.credentials.password = ''
    }
    },
  }
</script>

<style></style>
