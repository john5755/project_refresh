<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active justify">
           <div :style="{'backgroundImage':'url('+ tmdb + first_movie.poster_path +')',
    'backgroundSize':'cover',
    'filter': 'brightness(88%)'}">   
            <h1 class="text-body display-1 fw-bold text-start">{{ first_movie.title }}</h1>
            <p class="display-2">{{ first_movie.tagline }}</p>
            <p class="display-5 fw-bold">{{ first_movie.overview }}</p>
            <p>{{ first_movie.rate_average}}</p>    
            <hr>
            <!-- detail 연결 -->
            <router-link 
              :to="{ name: 'detail', params: { movieId: first_movie.movie_id } }">
              <img :src="tmdb+first_movie.poster_path" alt="poster">
            </router-link>
            <hr>
          </div>
        </div>      
        <div v-for="movie in forMovies" :key="movie.movie_id" class="carousel-item">
        <home-movie
        :movie="movie"
        ></home-movie>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>   
      <ol class="carousel-indicators">
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"
          :style="{'backgroundImage':'url('+ tmdb + first_movie.poster_path +')',
          'backgroundSize':'cover',
          'width': '90px',
          'height': '90px',
          'position': 'relative',
          'margin': '10px' }">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="1" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[1].poster_path +')',
          'backgroundSize':'cover',
          'width': '90px',
          'height': '90px',
          'position': 'relative',
          'margin': '10px' }">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="2" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[2].poster_path +')',
          'backgroundSize':'cover',
          'width': '90px',
          'height': '90px',
          'position': 'relative',
          'margin': '10px'}">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="3" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[3].poster_path +')',
          'backgroundSize':'cover',
          'width': '90px',
          'height': '90px',
          'position': 'relative',
          'margin': '10px'}">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="4" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[4].poster_path +')',
          'backgroundSize':'cover',
          'width': '8rem',
          'height': '10rem',
          'position': 'relative',
          'margin': '10px'}">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
      </ol>
    </div>
        <!-- <div class="container">
      <div class="row">
        <div class="col-4">
          <div class="card">1</div>
        </div>
        <div class="col-4">
          <div class="card">1</div>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import HomeMovie from '@/components/HomeMovie.vue'
import { mapActions, mapGetters } from 'vuex'

  export default {
  components: { HomeMovie},
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
      },
      first_movie (){
        return this.movies[0]
      },
      forMovies (){
        return this.movies.slice(1,5)
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

<style>
.carousel-indicators{
    list-style: none;
}
.carousel-indicators li{
    width: 90px;
    height: 90px;
    position: relative;
    margin: 10px;           
}
/* .carousel-indicators img{
    width: 100%;
    border-radius: 50%;
    height: 100%;
    top: 0;
    left: 0;
    margin: 0px auto;
} */  
.justify {
  text-align: justify;
  text-justify: inter-word;
}

.paragraph {
  text-align-last: left;
}

#carouselExampleControls{
  height: 100vh;
}

</style>
