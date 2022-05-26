<template>
  <div>
  <form @submit.prevent="onSubmit">
    <label for="search">Name: </label>
    <input type="text" id="search" v-model="content" required>
    <button>Search</button>
  </form>
  <p v-if="!query" class="mt-2">
    <b>이름</b>을 <b>영어</b>로 입력하시면 그 이름의 배우가 등장하는 영화와 그 이름의 배역이 등장하는 영화를 찾아드립니다.
  </p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  'name': 'NameSearchForm',
  data() {
    return {
      content: ''
    }
  },
  methods: {
    ...mapActions(['fetchCharMovies', 'fetchActorMovies']),
    onSubmit() {
      this.fetchCharMovies(this.content)
      this.fetchActorMovies(this.content)
      this.$router.push({name:'searchname', params:{query:this.content}})
      this.content = ''
    }
  },
  computed: {
    ...mapGetters(['charMovies']),
    
    query(){
      return this.$route.params.query
    },
  }
}
</script>

<style>

</style>