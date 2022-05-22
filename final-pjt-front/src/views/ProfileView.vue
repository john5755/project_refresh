<template>
  <div>
    <h1>{{ profile.username }}</h1>

    
    
    <!-- <h2>작성댓글(시간남으면)</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul> -->
    
    
    <button @click="deleteUser(profile.pk)">profile delete</button>
    <button @click="onResetHistory">그/그녀와의 기억 지우기 ㅋㅋ</button>
    <p>{{profile.partner_id}} </p>
  </div>
</template>

<script>
import { mapGetters, mapActions, } from 'vuex'


export default {
  name: 'ProfileView',
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
