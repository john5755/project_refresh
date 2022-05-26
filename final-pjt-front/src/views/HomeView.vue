<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner d-flex">
        <div class="carousel-item active">
          <div :style="{'backgroundImage':'url('+ tmdb + first_movie.poster_path +')',
                        'backgroundSize':'cover',
                        'filter': 'brightness(88%)'}" 
                id="background1"
                class="justify-content-center d-flex">
            <h1 class="mt-5">TOP 5 BACK GROUND MOVIE</h1>
            <div class="card mb-3 row-2 homeback" style="max-width: 540px;" id="first">
              <div class="row g-0">
                <div class="col-md-4">
                  <img :src="tmdb+first_movie.poster_path" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                  <div class="card-body">
                    <h5 class="card-title">{{ first_movie.title }}</h5>
                    <p class="card-text">{{ first_movie.overview }}</p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: first_movie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
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
      <div>
        <ol class="carousel-indicators">
          <li data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"
          :style="{'backgroundImage':'url('+ tmdb + first_movie.poster_path +')',
          'backgroundSize':'cover',
          'width': '8rem',
          'height': '10rem',
          'position': 'relative',
          'margin': '10px' }">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="1" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[1].poster_path +')',
          'backgroundSize':'cover',
          'width': '8rem',
          'height': '10rem',
          'position': 'relative',
          'margin': '10px' }">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="2" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[2].poster_path +')',
          'backgroundSize':'cover',
          'width': '8rem',
          'height': '10rem',
          'position': 'relative',
          'margin': '10px'}">
          <!-- <img :src="tmdb+ movies[0].poster_path" alt="" data-bs-target="#carouselExampleControls" data-bs-slide-to="0" class="active"> -->
        </li>
        <li data-bs-target="#carouselExampleControls" data-bs-slide-to="3" class="active"
          :style="{'backgroundImage':'url('+ tmdb + movies[3].poster_path +')',
          'backgroundSize':'cover',
          'width': '8rem',
          'height': '10rem',
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
    </div>
        <!-- <div class="container">
      <div class="row">
        <div class="col-6">
          <div class="card">
            <div class="card-body">
              <router-link 
                :to="{ name: 'detail', params: { movieId: first_movie.movie_id } }">
                <img :src="tmdb+first_movie.poster_path" alt="poster">
              </router-link>
            </div>
          </div>
        </div>
        <div class="col-6">
          <div class="card">
            <div class="card-header">{{ first_movie.title }}</div>
              <div class="card-body">
                <h5 class="card-title">{{ first_movie.tagline }}</h5>
                <p class="card-text">{{ first_movie.overview }}</p>
              </div>
          </div>
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
  height:90vh;
  display: flex;
}

#background1{
  background: linear-gradient(to top, black, rgb(10, 28, 38));
  height: 100vh;
}

#first{
  height: 37vh;
  position: relative;
  top: 13em; 
}

/* .carousel-inner{
  width: 100px;
} */

.card-text{
  -webkit-line-clamp: 5;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}

</style>
