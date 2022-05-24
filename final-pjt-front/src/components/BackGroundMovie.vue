<template>
  <div>
    <h2>배경으로 좋은 영화</h2>
    <ul v-for="groundMovie in groundMovies" :key="groundMovie.movie_id">
      <li>{{ groundMovie.title }}</li>
      <li>{{ groundMovie.tagline }}</li>
      <!-- <li>{{ groundMovie.poster_path }}</li>  -->
      <li>{{ groundMovie.overview }}</li>
      <li>{{ groundMovie.rate_users}}</li>
       
    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { movieId: groundMovie.movie_id } }">
      <!-- <img :src='posrterUrl( movie.poster_path )' alt="poster"> -->
      <img :src="tmdb+groundMovie.poster_path" alt="poster">
    </router-link>
    <hr>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'BackGroundMovie',
  data(){
      return {
        tmdb:'https://image.tmdb.org/t/p/w500/',
      }
    },
  computed: {
    posterUrl (poster_path){
      return `https://image.tmdb.org/t/p/w500`+ poster_path
      }
      
    },
  props: {
    groundMovies: Array
  }

}
</script>

<style>

</style>