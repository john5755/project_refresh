<template>
  <div class="container  mt-5">
    
    
    
   
    <!-- <div><img :src="tmdb+movie.poster_path" alt="poster"></div>
    
   
    <div v-for= 'provider in movie.providers' :key='provider.provider_name'>
      <a :href="provider.address">
        <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
      </a>
    </div>
    
    <p>{{ movie.rate_average }}</p>
    <hr> -->
    
    
    <!-- <star-rating 
    v-model='rating'
    v-bind:increment="1"
    v-bind:max-rating="5"
    @rating-selected = "setRating">

    </star-rating> -->
    
    <!-- :style="`background-image:url(${tmdb+movie.poster_path}); overflow:hidden;`" -->
    
    
    
    
  
    <div class="my-5">

    </div>
    <div class="container">
      <div class="">
        
        <!-- poster & provider -->
        <div class="row row-cols-1 row-cols-sm-2 " name="poster-provider" >
            
            <!-- 왼쪽 (포스터 별점 OTT) -->
            <div class="col poster container">
                <img :src="tmdb+movie.poster_path" class="row-8 poster">
                <hr>
                <!-- bgmRate/starRate/Watch on/ -->
                <div class="row-2 row-cols-sm-2 container">
                  <star-rating 
                      v-model='rating'
                      v-bind:increment="1"
                      v-bind:max-rating="5"
                      @rating-selected = "setRating"
                      class="col"
                      >
                      
                  </star-rating>
                  
                 
                </div>
                <hr>
                <div class="row-2 d-flex align-items-center">
                  
                    <div class="col-5 text-start"><h5><b>&nbsp;&nbsp;&nbsp;WATCH ON</b></h5></div>
                    <div class="col-7 text-start my-2 mx-4" v-for= 'provider in movie.providers' :key='provider.provider_name'>
                      <a :href="provider.address">
                      <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
                      </a>
                    </div>
                    <!-- <div class="col-8">d </div> -->
                 
                <!-- <div class="col-6"></div>
                <div class="col-6" v-for= 'provider in movie.providers' :key='provider.provider_name'>
                  <a :href="provider.address">
                    <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
                  </a>
                </div> -->
                
                </div>
            
            </div>
          
          <!-- title&star&overview -->  
            <div class="col detail">
              <div class="row">
                <hr>
                <h1 class="fw-bold">{{movie.title}}</h1>
              </div>
              <div class="row">
                <h5>{{movie.original_title}}</h5>
              </div>
              <div class="row">
                <hr>
                <h5 class="text-start">BGM RATES&nbsp;&nbsp;&nbsp;</h5>
                <h1 class="text-start">{{movie.rate_average}}</h1>
              </div>
              <hr>
              <div class="row">
                <div class="col">
                  <h5 class="text-start">상영시간 : {{movie.runtime}}분</h5>
                  <h5 class="text-start">개봉일 : {{movie.release_date}}</h5>
                  <div class="row">
                    <div class="col-3"><h4 class="text-start" >장르:</h4></div>
                    <div class="col-9">
                      <h5 class="text-start" v-for="genre in movie.genres" :key='genre.genre_name'>{{genre.genre_name}}</h5>
                    </div>    
                  </div>
                </div>
                <div class="col">
                </div>
              </div>
              
              
                <hr>
              <div class="row">
                <h3 class="text-start">{{movie.overview}}</h3>
              </div>
            </div>
        </div>
        
        <div class="row" name="title-star-overview">
          <div class="row" name="title-star">
            
          </div>
          
        </div>

        
        <!-- overview -->
        <br>
        <hr class="hr-height">
        <br>
        <br>
        <div class="row">
          <comment-list :comments="movie.comments">
          </comment-list> 
        </div>
      </div>
    </div>
    </div>
   
</template>




<script>
  import StarRating from 'vue-star-rating'
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'MovieDetail',
    // components: { CommentList },
    components:{
      StarRating,
      CommentList,
    },
    data() {
      return {
        movieId: this.$route.params.movieId,
        tmdb:'https://image.tmdb.org/t/p/w500/',
        bgm_rate:0
      }
    },
    computed: {
      ...mapGetters(['movie']),
      // ...mapGetters(['isAuthor', 'article']),
      // likeCount() {
      //   return this.article.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchMovie',
        'createRating',
        // 'likeArticle',
        // 'deleteArticle',
      ]),
      setRating: function(bgm_rate){
        this.bgm_rate = bgm_rate
        this.createRating({ movieId: this.movie.movie_id, bgm_rate: this.bgm_rate, })
      },
    },
    created() {
      this.fetchMovie(this.movieId)
    },
  }
</script>

<style>
.poster{
  max-width: 100%;
  
}
.vw-100{
  width: 100vw;
}
.star {
  flex-shrink:0;
  flex-grow:0;
}
.hr-height {
  border:1;
  height: 5px;
  background : #525252;
}
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
.detail{
  font-family: 'Black Han Sans', sans-serif;
}



    

</style>
