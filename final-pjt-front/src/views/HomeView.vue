<template>
  <div>
    <h1>Home</h1>
    <ul v-for="movie in movies" :key="movie.movie_id">
      <li>{{ movie.title }}</li>
      <li>{{ movie.tagline }}</li>
      <li>{{ movie.poster_path }}</li> 
      <li>{{ movie.overview }}</li>
      <li>{{ movie.rate_users}}</li>
       
        

        <!-- 댓글 개수/좋아요 개수 -->
        <!-- =>
        ({{ article.comment_count }}) | +{{ article.like_count }} -->
    
    <hr>
    <!-- detail 연결 -->
    <router-link 
      :to="{ name: 'detail', params: { moviePk: movie.movie_id } }">
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
        tmdb:'https://image.tmdb.org/t/p/w500/'
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
