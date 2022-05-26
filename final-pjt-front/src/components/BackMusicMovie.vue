<template>
  <div>
    <h2>배경음악 좋은 영화</h2>
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
            <div class="col-md-4">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+firstMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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

            <div class="col-md-4 clearfix d-none d-md-block"
                  v-for="movie in forFirstMovies" :key="movie.movie_id">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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
        <div class="carousel-item" v-if="secondMovie">

          <div class="row">
            <div class="col-md-4">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+secondMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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

            <div class="col-md-4 clearfix d-none d-md-block"
                  v-for="movie in forSecondMovies" :key="movie.movie_id">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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
        <div class="carousel-item" v-if="thirdMovie">

          <div class="row">
            <div class="col-md-4">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+thirdMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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

            <div class="col-md-4 clearfix d-none d-md-block"
                  v-for="movie in forThirdMovies" :key="movie.movie_id">
              <div class="card mb-2">
                <img class="card-img-top" :src="tmdb+movie.poster_path"
                    alt="Card image cap">
                <div class="card-body">
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
        <!--/.Second slide-->

      <!-- <li>{{ musicMovie.title }}</li>
      <li>{{ musicMovie.tagline }}</li>
      <li>{{ musicMovie.overview }}</li>
      <li>{{ musicMovie.rate_users}}</li> -->

    
    <!-- detail 연결 -->
    <!-- <router-link 
      :to="{ name: 'detail', params: { movieId: musicMovie.movie_id } }">
      <img :src="tmdb+musicMovie.poster_path" alt="poster">
    </router-link>
    <hr> -->
    </div>
    </div>
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
      },
    firstMovie (){
      return this.musicMovies[0]
    },  
    forFirstMovies (){
      return this.musicMovies.slice(1,3)
    },
    secondMovie(){
      return this.musicMovies[3]
    },
    forSecondMovies (){
      return this.musicMovies.slice(4,6)
    },
    thirdMovie(){
      return this.musicMovies[6]
    },
    forThirdMovies(){
      return this.musicMovies.slice(7,9)
    }
  },
  props: {
    musicMovies: Array
  }

}
</script>

<style>

.card-img-top {
    width: 150%;
    height: 30vw;
    object-fit: contain;
}

</style>