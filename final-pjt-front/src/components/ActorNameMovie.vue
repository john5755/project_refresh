<template>
  <div>
    <h2>내 이름의 배우가 나오는 영화</h2>
    <ul v-for="actorMovie in actorMovies" :key="actorMovie.movie.movie_id">
      <li>{{ actorMovie.movie.title }}</li>
      <li>{{ actorMovie.movie.tagline }}</li>
      <!-- <li>{{ actorMovie.poster_path }}</li>  -->
      <li>{{ actorMovie.movie.overview }}</li>
      <li>{{ actorMovie.movie.rate_users}}</li>
      <li>{{ actorMovie.character }}</li>
      <li>{{ actorMovie.actor_name }}</li>
       
       
    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { movieId: actorMovie.movie.movie_id } }">
      <!-- <img :src='posrterUrl( movie.poster_path )' alt="poster"> -->
      <img :src="tmdb+actorMovie.movie.poster_path" alt="poster">
    </router-link>
    <hr>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'ActorNameMovie',
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
    actorMovies: Array
  },

  

}
</script>

<style>

</style>