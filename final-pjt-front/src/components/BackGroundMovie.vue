<template>
  <div>
    <h2 class="mb-4">배경으로 좋은 영화</h2>
    <hr>
    <div id="multi-item-example" class="carousel slide carousel-multi-item" data-bs-ride="carousel">
      <!--Controls-->
      <div class="controls-top">
        <!-- <a class="btn-floating carousel-control-prev" href="#multi-item-example" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
        <a class="btn-floating carousel-control-next" href="#multi-item-example" data-slide="next"><i class="fa fa-chevron-right"></i></a> -->
      <button class="carousel-control-prev" type="button" data-bs-target="#multi-item-example" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#multi-item-example" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>      
      </div>
      <!--/.Controls-->
      <!--Slides-->
      <div class="carousel-inner" role="listbox">

        <!--First slide-->
        <div class="carousel-item active">

          <div class="row">
            <div class="col-md-3 page">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+firstMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ firstMovie.title }}</h4>
                  <p class="card-text">{{ firstMovie.overview }} </p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: firstMovie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>

            <div class="col-md-3 clearfix d-none d-md-block page"
                  v-for="movie in forFirstMovies" :key="movie.movie_id">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ movie.title }}</h4>
                  <p class="card-text">{{ movie.overview }} </p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: movie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--/.First slide-->

        <!--Second slide-->
        <div class="carousel-item">

          <div class="row">
            <div class="col-md-3 page">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+secondMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ secondMovie.title }}</h4>
                  <p class="card-text">{{ secondMovie.overview }} </p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: secondMovie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>

            <div class="col-md-3 clearfix d-none d-md-block page"
                  v-for="movie in forSecondMovies" :key="movie.movie_id">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ movie.title }}</h4>
                  <p class="card-text">{{ movie.overview }}</p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: movie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--/.Second slide-->

        <!--Third slide-->
        <div class="carousel-item">

          <div class="row">
            <div class="col-md-3 page">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+thirdMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ thirdMovie.title }}</h4>
                  <p class="card-text">{{ thirdMovie.overview }} </p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: thirdMovie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>

            <div class="col-md-3 clearfix d-none d-md-block page"
                  v-for="movie in forThirdMovies" :key="movie.movie_id">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ movie.title }}</h4>
                  <p class="card-text">{{ movie.overview }} </p>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId: movie.movie_id } }"
                      class="btn btn-primary">
                      GO TO DETAIL
                    </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--/.Third slide-->



      <!-- <li>{{ groundMovie.title }}</li>
      <li>{{ groundMovie.tagline }}</li>
      <li>{{ groundMovie.overview }}</li>
      <li>{{ groundMovie.rate_users}}</li> -->

    
    <!-- detail 연결 -->
    <!-- <router-link 
      :to="{ name: 'detail', params: { movieId: groundMovie.movie_id } }">
      <img :src="tmdb+groundMovie.poster_path" alt="poster">
    </router-link>
    <hr> -->
    </div>
    </div>
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
      },
    firstMovie (){
      return this.groundMovies[0]
    },  
    forFirstMovies (){
      return this.groundMovies.slice(1,4)
    },
    secondMovie(){
      return this.groundMovies[4]
    },
    forSecondMovies (){
      return this.groundMovies.slice(5,8)
    },
    thirdMovie(){
      return this.groundMovies[8]
    },
    forThirdMovies(){
      return this.groundMovies.slice(9,12)
    }
  },
  props: {
    groundMovies: Array
  }

}
</script>

<style>
.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: contain;
}
</style>