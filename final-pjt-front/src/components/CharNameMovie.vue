<template>
  <div>
    <h2>내 이름이 나오는 영화</h2>
    <ul v-for="charMovie in charMovies" :key="charMovie.movie.movie_id">
      <li>{{ charMovie.movie.title }}</li>
      <li>{{ charMovie.movie.tagline }}</li>
      <!-- <li>{{ charMovie.poster_path }}</li>  -->
      <li>{{ charMovie.movie.overview }}</li>
      <li>{{ charMovie.movie.rate_users}}</li>
      <li>{{ charMovie.character }}</li>
      <li>{{ charMovie.actor_name }}</li>
       
       
    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { movieId: charMovie.movie.movie_id } }">
      <!-- <img :src='posrterUrl( movie.poster_path )' alt="poster"> -->
      <img :src="tmdb+charMovie.movie.poster_path" alt="poster">
    </router-link>
    <hr>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'CharNameMovie',
  data(){
      return {
        tmdb:'https://image.tmdb.org/t/p/w500/',
      }
    },
  computed: {
    posterUrl (poster_path){
      return `https://image.tmdb.org/t/p/w500`+ poster_path
      },
      
    },
  props: {
    charMovies: Array
  },

  

}
</script>

<style>

</style>