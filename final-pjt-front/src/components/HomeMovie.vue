<template>
  <div>
    <div :style="{'backgroundImage':'url('+ tmdb + movie.poster_path +')',
    'backgroundSize':'cover'}">   
      <li>{{ movie.title }}</li>
      <li>{{ movie.tagline }}</li>
      <li>{{ movie.overview }}</li>
      <li>{{ movie.rate_users}}</li>    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { movieId: movie.movie_id } }">
      <!-- <img :src='posrterUrl( movie.poster_path )' alt="poster"> -->
      <img :src="tmdb+movie.poster_path" alt="poster">
    </router-link>
    <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeMovie',
  props:{
    movie: Object,
  },
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
}

</script>

<style>

</style>