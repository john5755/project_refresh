<template>
<div>
  <h1>SEARCH</h1>
  <name-search-form></name-search-form>
  <char-name-movie
  :charMovies="charMovies"></char-name-movie>
  <actor-name-movie
  :actorMovies="actorMovies"></actor-name-movie>
</div>
</template>

<script>
import NameSearchForm from '@/components/NameSearchForm.vue'
import CharNameMovie from '@/components/CharNameMovie.vue'
import ActorNameMovie from '@/components/ActorNameMovie.vue'
import { mapGetters } from 'vuex'

export default {
  components: { CharNameMovie, ActorNameMovie, NameSearchForm },
  name: 'SearchNameView',
  computed: {
    ...mapGetters['actorMovies', 'charMovies']
  }
}
</script>

<style>

</style>