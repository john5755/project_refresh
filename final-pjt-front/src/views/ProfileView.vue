<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <div class="container justify-content-center">
      <h1>SIGN UP</h1>
      <div class="row d-flex justify-content-center">
      <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-8 col-md-offset-2">
      
      <signup-form :profile="profile" action="EDIT">
      </signup-form> 

    <!-- <form @submit.prevent="onSubmit">
      <div>
        <label for="title">title: </label>
        <input v-model="newArticle.title" type="text" id="title" />
      </div>
    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newArticle.content" type="text" id="content"></textarea>
    </div>
    
    <div>
      <button>{{ action }}</button>
    </div>
  </form> -->
    
      <h1>{{profile.favorite_genre}}</h1> 
    
    
    
    <button @click="deleteUser(profile.pk)">profile delete</button>
    <button @click="onResetHistory">그/그녀와의 기억 지우기 ㅋㅋ</button>
    <p>{{profile.partner_id}} </p>
  </div>
  </div>
  
  </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, } from 'vuex'
import SignupForm from '@/components/SignupForm.vue'


export default {
  name: 'ProfileView',
  components : {
    SignupForm,
  },
  data(){
    return {
      payload2:{
        userPk : this.$store.getters.profile.pk,
        partnerPk : this.$store.getters.profile.partner_id,
      },
    }
  },
  computed: {
    ...mapGetters(['profile']),
    // ...mapState(['userPk'])

  },
  methods: {
    ...mapActions(['fetchProfile','deleteUser','resetHistory']),
    onResetHistory () {
      // console.log(this.payload2)
      this.resetHistory(this.payload2)
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
