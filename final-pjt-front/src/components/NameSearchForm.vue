<template>
  <div>
  <form @submit.prevent="onSubmit">
    <label for="search">Name: </label>
    <input type="text" id="search" v-model="content" required>
    <button>Search</button>
  </form>
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
    ...mapGetters(['charMovies'])
  }
}
</script>

<style>

</style>