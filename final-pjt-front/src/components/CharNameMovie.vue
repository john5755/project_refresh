<template>
  <div>
    <h2 class="my-5">내 이름의 배역이 나오는 영화</h2>
    <div id="multi-item-example" class="carousel slide carousel-multi-item d-flex justify-content-center" data-bs-ride="carousel">
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
                  <div v-for="(cast, idx) in firstMovie.casts" :key="idx">
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
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
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
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
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
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
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
                    </p>
                  </div>
                    <router-link 
                      :to="{ name: 'detail', params: { movieId:movie.movie_id } }"
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
                <img class="card-img-top block" :src="tmdb+thirdMovie.poster_path"
                    alt="Card image cap">
                <div class="card-body content">
                  <h4 class="card-title">{{ thirdMovie.title }}</h4>
                  <p class="card-text">{{ thirdMovie.overview }} </p>
                  <div v-for="(cast, idx) in thirdMovie.casts" :key="idx">
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
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
                <div class="card-body" content>
                  <h4 class="card-title">{{ movie.title }}</h4>
                  <p class="card-text">{{ movie.overview }} </p>
                  <div v-for="(cast, idx) in movie.casts" :key="idx">
                    <p v-if="cast.character.includes(query) || cast.character.includes(capitalizeStirng(query))">
                      {{ cast.actor_name }}이(가)&nbsp;{{ cast.character }}역할을 합니다.
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

      <!-- <li>{{ charMovie.title }}</li>
      <li>{{ charMovie.tagline }}</li>
      <li>{{ charMovie.overview }}</li>
      <li>{{ charMovie.rate_users}}</li> -->

    
    <!-- detail 연결 -->
    <!-- <router-link 
      :to="{ name: 'detail', params: { movieId: charmovie_id } }">
      <img :src="tmdb+charMovie.poster_path" alt="poster">
    </router-link>
    <hr> -->
    </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'CharNameMovie',
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
      return this.charMovies[0]
    },  
    forFirstMovies (){
      return this.charMovies.slice(1,4)
    },
    secondMovie(){
      return this.charMovies[4]
    },
    forSecondMovies (){
      return this.charMovies.slice(5,8)
    },
    thirdMovie(){
      return this.charMovies[8]
    },
    forThirdMovies(){
      return this.charMovies.slice(9,12)
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
    charMovies: Array
  }

}
</script>

<style>

.card-text{
  -webkit-line-clamp: 5;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}

.namechar{
  -webkit-line-clamp: 5;
  overflow: scroll;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}


.page { 
  position: relative;
  width: 23vw; 
  height: 50vh;
}

.content {
   width: 100%;
}

.wrapper {
  position: relative;
  width: 100%; 
  height: 100%; 
  padding: 0; 
  overflow-y: scroll; 
  overflow-x: hidden; 
  border: 1px solid #ddd;
  background-color: rgb(46, 69, 89);
}

.page::after { 
  content:'';
  position: absolute;
  z-index: -1;
  height: calc(100% - 20px);
  top: 10px;
  right: -1px;
  width: 5px;
  background: #666;
}

.wrapper::-webkit-scrollbar {
    display: block;
    width: 5px;
}
.wrapper::-webkit-scrollbar-track {
    background: transparent;
}
    
.wrapper::-webkit-scrollbar-thumb {
    background-color: rgb(143, 203, 217);
    border-right: none;
    border-left: none;
}

.wrapper::-webkit-scrollbar-track-piece:end {
    background: transparent;
    margin-bottom: 10px; 
}

.card-img-top{
    width: 100%;

    object-fit: cover;
    object-position: center;
}
</style>