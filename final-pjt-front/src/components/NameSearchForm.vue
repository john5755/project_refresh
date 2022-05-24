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
import { mapActions } from 'vuex'

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
      this.content = ''
    }
  }
}
</script>

<style>

</style>