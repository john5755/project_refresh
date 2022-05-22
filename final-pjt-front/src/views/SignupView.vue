<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
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
      <!-- first/last name -->
      <div>
        <label for="first_name">첫번째이름: </label>
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

      <!-- favorite genre & seasson -->
      
      
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
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          favorite_genre:'',
          favorite_season:'',
          first_name:'',
          last_name:'',
          email:'',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
