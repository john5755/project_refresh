<template>
  <div>
    <h2 class="my-5">내 이름의 배우가 나오는 영화</h2>
    <div id="actor-item-example" class="carousel slide carousel-multi-item" data-bs-ride="carousel">
      <!--Controls-->
      <div class="controls-top">
        <!-- <a class="btn-floating carousel-control-prev" href="#actor-item-example" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
        <a class="btn-floating carousel-control-next" href="#actor-item-example" data-slide="next"><i class="fa fa-chevron-right"></i></a> -->
      <button class="carousel-control-prev" type="button" data-bs-target="#actor-item-example" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#actor-item-example" data-bs-slide="next">
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
                  <div v-for="(cast, idx) in firstMovie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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
                  <div v-for="(cast, idx) in movie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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
            <div class="col-md-3 page">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+secondMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ secondMovie.title }}</h4>
                  <p class="card-text">{{ secondMovie.overview }} </p>
                  <div v-for="(cast, idx) in secondMovie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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
                  <div v-for="(cast, idx) in movie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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
            <div class="col-md-3 page">
              <div class="card mb-2 wrapper">
                <img class="card-img-top" :src="tmdb+thirdMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ thirdMovie.title }}</h4>
                  <p class="card-text">{{ thirdMovie.overview }} </p>
                  <div v-for="(cast, idx) in thirdMovie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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
                  <div v-for="(cast, idx) in movie.casts" :key="idx">
                    <p v-if="cast.actor_name.includes(query) || cast.actor_name.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.actor_name }}역할을 합니다.
                    </p>
                  </div>
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

      <!-- <li>{{ actorMovie.title }}</li>
      <li>{{ actorMovie.tagline }}</li>
      <li>{{ actorMovie.overview }}</li>
      <li>{{ actorMovie.rate_users}}</li> -->

    
    <!-- detail 연결 -->
    <!-- <router-link 
      :to="{ name: 'detail', params: { movieId: actormovie_id } }">
      <img :src="tmdb+actorMovie.poster_path" alt="poster">
    </router-link>
    <hr> -->
    </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'actorNameMovie',
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
      return this.actorMovies[0]
    },
    forFirstMovies (){
      return this.actorMovies.slice(1,4)
    },
    secondMovie(){
      return this.actorMovies[4]
    },
    forSecondMovies (){
      return this.actorMovies.slice(5,8)
    },
    thirdMovie(){
      return this.actorMovies[8]
    },
    forThirdMovies(){
      return this.actorMovies.slice(9,12)
    },
    query(){
      return this.$route.params.query
    },
  },
  methods:{
    capitalizeStirng(string){
      const first =  string[0].toUpperCase()
      const extra = string.slice(1)
      return first + extra
    }
  },
  props: {
    actorMovies: Array
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