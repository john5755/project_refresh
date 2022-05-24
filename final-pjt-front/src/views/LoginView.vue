<template>
  <div class='loginview d-flex flex-column justify-content-center'>
  
  <div class="container justify-content-center ">
    <!-- login/partner login -->
    <div>
      <h1 v-if="!isLoggedIn" >Login</h1>
      <h1 v-if="userLoggedIn">Partner Login</h1>
    </div>
    <account-error-list v-if="authError"></account-error-list>

   
    

    <!-- ID/PASSWORD 입력 -->
    <div class="row d-flex justify-content-center">
      <div class="card col-6">
        
        <form @submit.prevent="onSubmit(credentials)"  class="form">
          
          <div class='my-3'>
            <label for="username"><b>username</b> </label>
            <input class="form-control" v-model="credentials.username" type="text" id="username" required />
          </div>

          <div class='my-3'>
            <label for="password" ><b>password</b> </label>
            <input class="form-control" v-model="credentials.password" type="password" id="password" required />
          </div>
          
          <div >
            <button class='my-2 login-button btn btn-secondary'>Login</button>
          </div>
      
        </form>
     
        <!-- <div class=" d-flex justify-content-center logout-button"> -->
          <!-- <nav> -->
            <div v-if="isLoggedIn">
              <router-link :to="{ name: 'logout' }">
                <button class='my-2 logout-button btn btn-secondary '>
                Logout
                </button>
              </router-link>
            </div>
          <!-- </nav> -->
        <!-- </div> -->
            <div v-if="!userLoggedIn">
              <router-link :to="{ name: 'signup' }">
                <button class='my-2 logout-button btn btn-secondary '>
                Sign Up
                </button>
              </router-link>
            </div>
     
      </div>
      
    </div>
     <!-- profile 수정 버튼 -->
    <div v-if="userLoggedIn" class="row d-flex justify-content-center my-2">
      <div class='col-6 row justify-content-end mx-0'>
      <router-link :to="{ name: 'profile', params: { username } }" class="col-6 row justify-content-end" >
        <!-- {{ currentUser.username }} -->
        <button class="btn btn-outline-secondary edit-button" >
          Profile
        </button>
      </router-link>
      </div>
      
    </div>

    <!-- navbar for login -->


  </div> 
  
  
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

<style>
.loginview {
  height : 100%;
}
.login-button {
  
  width : 100%;
}
.logout-button {
  width : 100%;
}
.edit-button {
  height : 1.6rem;
  font-size : .25rem; 
}
</style>
