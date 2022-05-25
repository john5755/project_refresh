<template>
  <div>
    <div :style="{'backgroundImage':'url('+ tmdb + movie.poster_path +')',
    'backgroundSize':'cover'}"
    class="justify-content-center d-flex">   
        <div class="card mb-3" style="max-width: 540px;">
          <div class="row g-0">
          <div class="col-md-4">
            <img :src="tmdb+movie.poster_path" class="img-fluid rounded-start" alt="...">
          </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
        </div>
        </div>
    <hr>
    <!-- detail 연결 -->
    <!-- <router-link 
      :to="{ name: 'detail', params: { movieId: movie.movie_id } }">
      <img :src='posrterUrl( movie.poster_path )' alt="poster">
      GO TO DETAIL
    </router-link>
    <hr> -->
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