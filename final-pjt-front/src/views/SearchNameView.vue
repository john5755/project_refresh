<template>
<div>
  <h1>SEARCH</h1>
  <name-search-form></name-search-form>
  <div v-if="now">
    <char-name-movie
    :charMovies="charMovies"></char-name-movie>
    <actor-name-movie
    :actorMovies="actorMovies"></actor-name-movie>
  </div>
</div>
</template>

<script>
import NameSearchForm from '@/components/NameSearchForm.vue'
import CharNameMovie from '@/components/CharNameMovie.vue'
import ActorNameMovie from '@/components/ActorNameMovie.vue'
import { mapGetters } from 'vuex'
// import { mapActions } from 'vuex'

export default {
  components: { CharNameMovie, ActorNameMovie, NameSearchForm },
  name: 'SearchNameView',
  data(){
    return{
    now: this.$route.params.query
  }},
  computed: {
    ...mapGetters(['actorMovies', 'charMovies'])
  },
  // methods:{
  //   ...mapActions(['fetchCharMovies'])
  // },

  // created(){
  //   const query = this.$route.params.query
  //   this.fetchCharMovies(query)
  // }
}
</script>

<style>

</style>