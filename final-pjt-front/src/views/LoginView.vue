<template>
  <div>
  
  <b-container>
    <!-- login/partner login -->
    <h1 v-if="!isLoggedIn" >Login</h1>
    <h1 v-if="userLoggedIn">Partner Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <!-- profile 수정 버튼 -->
    <div v-if="userLoggedIn">
      <router-link :to="{ name: 'profile', params: { username } }">
        {{ currentUser.username }} 프로필수정
      </router-link>
    </div>
    

    <!-- ID/PASSWORD 입력 -->
    <b-card>
      
      <b-form @submit.prevent="onSubmit(credentials)">
      <container-fluid>  
        <div>
          <label for="username">username: </label>
          <b-form-input v-model="credentials.username" type="text" id="username" required />
        </div>

        <div>
          <label for="password">password: </label>
          <b-form-input v-model="credentials.password" type="password" id="password" required />
        </div>
      </container-fluid>
     
      <fluid>
        <b-button variant="secondary">Login</b-button>
      </fluid>
      </b-form>
    </b-card>
 

    <!-- navbar for login -->
    <nav>
      <div v-if="userLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </div>
    </nav>
  </b-container>
  
  
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
