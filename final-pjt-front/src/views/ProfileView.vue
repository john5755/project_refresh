<template>
  <div>
    <h1>{{ profile.username }}'s profile</h1>


   

    <div class="container justify-content-center">
      
      <div class="row d-flex justify-content-center">
      <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-8 col-md-offset-2">
      
      <!-- 프로필 form -->
      <!-- 위치: componet/SigupForm  -->
      <signup-form :profile="profile" action="EDIT">
      </signup-form> 

      
      
      <!-- modal trigger -->
      
        <!-- 1. 탈퇴 -->
        <button type="button" class="btn btn-primary mx-1" data-bs-toggle="modal" data-bs-target="#withdraw" id="profile-button">
          회원 탈퇴
        </button>
        <!-- 2. 로그인 기록 삭제 + 파트너 기록 반환 -->
        <button type="button" class="btn btn-primary mx-1" data-bs-toggle="modal" data-bs-target="#resetHistory" id="profile-button">
          시청 기록 삭제
        </button>
      
      
      <!-- modal -->
        
        <!-- 1. 탈퇴 -->
          <div class="modal fade" id="withdraw" tabindex="-1" aria-labelledby="withdrawLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="withdrawLabel">회원 탈퇴</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                  </button>
                </div>
                <div class="modal-body">
                  정말 탈퇴하실거에요???
                </div>
                <div class="modal-footer">
                  <button @click="deleteUser(profile.pk)" type="button" class="btn btn-primary close">탈퇴</button>
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                </div>
              </div>
            </div>
          </div>
        <!-- 2. 로그인 기록 삭제 + 파트너 기록 반환 -->
          <div class="modal fade" id="resetHistory" tabindex="-1" aria-labelledby="resetHistoryLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="resetHistoryLabel">BREAK UP</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                  </button>
                </div>
                <div class="modal-body">
                  정말 기억을 삭제하시겠습니까?
                </div>
                <div class="modal-footer">
                  <button @click="onResetHistory" type="button" class="btn btn-primary close">삭제</button>
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                </div>
              </div>
            </div>
          </div>


    
    <!-- <button @click="deleteUser(profile.pk)">profile delete</button> -->
    <!-- <button @click="onResetHistory">그/그녀와의 기억 지우기 ㅋㅋ</button> -->
    <!-- <p>{{profile.partner_id}} </p> -->
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

<style>
  
</style>
