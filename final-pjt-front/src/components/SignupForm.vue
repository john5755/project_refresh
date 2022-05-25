<template>
  <!-- <div>
    <account-error-list v-if="authError"></account-error-list>
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="card card-registration col-8">  
        <form @submit.prevent="signup(credentials)" class="form">
        <div class="form-outline">
          <label for="username">Username: </label>
          <input  v-model="credentials.username" type="text" id="username" required/>
        </div> 
        <div>
          <label for="password1">Password: </label>
          <input v-model="credentials.password1" type="password" id="password1" required />
        </div>
        <div>
          <label for="password2">Password Confirmation:</label>
          <input v-model="credentials.password2" type="password" id="password2" required />
        </div>
       
        <div>
          <label for="first_name">첫번째이름름: </label>
          <input v-model="credentials.first_name" id="first_name" required />
        </div>
        <div>
          <label for="last_name">마지막이름: </label>
          <input v-model="credentials.last_name" id="last_name" required />
        </div>
        <div>
          <label for="email">이메일: </label>
          <input v-model="credentials.email" id="email" required />
        </div> 

       
        
        
        <div>
          <label for="favorite_genre">페이보리트 젠르:</label>
          <select v-model="credentials.favorite_genre" id='favoirte_genre'>
            <option disabled value="">Please Select</option>
            <option value='액션'>액션</option>
            <option>모험</option>
            <option>애니메이션</option>
            <option>코미디</option>
            <option>범죄</option>
            <option>다큐멘터리</option>
            <option>드라마</option>
            <option>가족</option>
            <option>판타지</option>
            <option>역사</option>
            <option>공포</option>
            <option>음악</option>
            <option>미스터리</option>
            <option>로맨스</option>
            <option>SF</option>
            <option>TV 영화</option>
            <option>스릴러</option>
            <option>전쟁</option>
            <option>서부</option>
          </select>  
        </div>
        
        <div>
          <label for="favorite_season">페이보리트 시즌:</label>
          <select v-model="credentials.favorite_season" id='favoirte_season'>
            <option disabled value="">Please Select</option>
            <option>봄</option>
            <option>여름</option>
            <option>가을</option>
            <option>겨울</option>
          </select>  
        </div>


        <div>
          <button>Signup</button>
        </div>
        </form>
      </div>
    </div>   
  </div> -->
  <div>
    <account-error-list v-if="authError"></account-error-list>
  <!-- <div class="container">
  <div class="row">
  <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-8 col-md-offset-2"> -->
  
  <form @submit.prevent="onSubmit()" class="form-horizontal">
  <br>
  <fieldset>
    <!-- <b>SIGN UP</b>		 -->
              <div class="form-group" >
                <label for="firstname" class="cols-sm-2 control-label">First Name</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
                    <input v-model="credentials.first_name" type="text" class="form-control" id="firstname"  placeholder="Firstname" required>
                  </div>
                </div>
              </div>

              <div class="form-group">
                <label for="lastname" class="cols-sm-2 control-label">Last Name</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
                    <input v-model="credentials.last_name" type="text" class="form-control" id="lastname"  placeholder="Lastname" required>
                  </div>
                </div>
              </div>
  
              <div class="form-group">
                <label for="email" class="cols-sm-2 control-label">Your Email</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
                    <input v-model="credentials.email" type="text" class="form-control" id="email"  placeholder="Enter your Email"/>
                  </div>
                </div>
              </div>
  
              <div class="form-group" v-if="!isLoggedIn">
                <label for="username" class="cols-sm-2 control-label">Username</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
                    <input v-model="credentials.username" type="text" class="form-control" name="username" id="username"  placeholder="Enter your Username"/>
                  </div>
                </div>
              </div>
  
              <div class="form-group" v-if="!isLoggedIn">
                <label for="password1" class="cols-sm-2 control-label">Password</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                    <input v-model="credentials.password1" type="password" class="form-control" name="password1" id="password1"  placeholder="Enter your Password"/>
                  </div>
                </div>
              </div>

              <div class="form-group" v-if="!isLoggedIn">
                <label for="password2" class="cols-sm-2 control-label">Confirm Password</label>
                <div class="cols-sm-10">
                  <div class="input-group">
                    <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                    <input v-model="credentials.password2" type="password" class="form-control" name="password2" id="password2"  placeholder="Confirm your Password"/>
                  </div>
                </div>
              </div>

              <div class="form-group">
                <label for="favorite_genre" class="cols-sm-2 control-label">페이보리트 젠르:</label>
                <div class="cols-sm-10">
                  <select v-model="credentials.favorite_genre" class="form-select" aria-label="Default select example" id='favoirte_genre' required>
                    <option selected>Please Select</option>
                    <option>액션</option>
                    <option>모험</option>
                    <option>애니메이션</option>
                    <option>코미디</option>
                    <option>범죄</option>
                    <option>다큐멘터리</option>
                    <option>드라마</option>
                    <option>가족</option>
                    <option>판타지</option>
                    <option>역사</option>
                    <option>공포</option>
                    <option>음악</option>
                    <option>미스터리</option>
                    <option>로맨스</option>
                    <option>SF</option>
                    <option>TV 영화</option>
                    <option>스릴러</option>
                    <option>전쟁</option>
                    <option>서부</option>
                  </select>
                </div> 
              </div>
            
              <div class="form-group">
                <label for="favorite_season" class="cols-sm-2 control-label">페이보리트 시즌:</label>
                <select v-model="credentials.favorite_season" class="form-select" id='favoirte_season'>
                  <option disabled value="">Please Select</option>
                  <option>봄</option>
                  <option>여름</option>
                  <option>가을</option>
                  <option>겨울</option>
                </select>  
              </div>
  
  
  
              <div class="form-group ">
                <button type="submit" class="btn btn-info btn-lg btn-block login-button">{{action}}</button>
              </div>
   </fieldset>
            </form>
  
  </div>
  

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupForm',
    components: {
      AccountErrorList,
    },
    props: {
      profile:Object,
      action:String
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',          
          favorite_genre: this.profile.favorite_genre,
          favorite_season: this.profile.favorite_season,
          first_name: this.profile.first_name,
          last_name: this.profile.last_name,
          email: this.profile.email,
        }
      }
    },
    computed: {
      ...mapGetters(['authError','isLoggedIn'])
    },
    methods: {
      ...mapActions(['signup','updateProfile']),
      onSubmit() {
        
        if (this.action === 'SIGNUP') {
          this.signup(this.credentials)
        } else if (this.action === 'EDIT') {
          const payload = {
            ...this.credentials,
          }
          this.updateProfile(payload)
        }
      },
    },
  }
</script>

<style>
body{background:royalblue}
fieldset{padding:50px}
.form-group{
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>