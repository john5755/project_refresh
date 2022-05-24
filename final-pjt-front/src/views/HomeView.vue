<template>
  <div>
    <h1>Home</h1>
    <router-link 
      :to="{ name: 'background' }">
      BGM
    </router-link>
    <router-link
      :to="{ name: 'searchname', parmas:{query:''} }">
      NAME
    </router-link>
    <ul v-for="movie in movies" :key="movie.movie_id">
      <li>{{ movie.title }}</li>
      <li>{{ movie.tagline }}</li>
      <li>{{ movie.poster_path }}</li> 
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
    </ul>
    
   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'HomeView',
    data(){
      return {
        tmdb:'https://image.tmdb.org/t/p/w500/',
      }
    },
    computed: {
      ...mapGetters(['movies']),
      posterUrl (poster_path){
        return `https://image.tmdb.org/t/p/w500`+ poster_path
      }
      
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style></style>
