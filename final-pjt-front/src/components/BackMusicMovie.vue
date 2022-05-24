<template>
  <div>
    <h2>배경음악 좋은 영화</h2>
    <ul v-for="musicMovie in musicMovies" :key="musicMovie.movie_id">
      <li>{{ musicMovie.title }}</li>
      <li>{{ musicMovie.tagline }}</li>
      <!-- <li>{{ musicMovie.poster_path }}</li>  -->
      <li>{{ musicMovie.overview }}</li>
      <li>{{ musicMovie.rate_users}}</li>
       
    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { movieId: musicMovie.movie_id } }">
      <!-- <img :src='posrterUrl( movie.poster_path )' alt="poster"> -->
      <img :src="tmdb+musicMovie.poster_path" alt="poster">
    </router-link>
    <hr>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'BackMusicMovie',
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
    musicMovies: Array
  }

}
</script>

<style>

</style>