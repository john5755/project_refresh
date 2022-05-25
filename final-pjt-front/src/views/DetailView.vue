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
    
    
    
    
    
    <!-- 틀 -->
    <div class="my-5">
      <hr>
    </div>
    <div class="container">
      <div class="">
        
        <!-- poster & provider -->
        <div class="row row-cols-1 row-cols-sm-2 " name="poster-provider" >
          <!-- :style="`background-image:url(${tmdb+movie.poster_path}); overflow:hidden;`" -->
            <div class="col poster container">
                <img :src="tmdb+movie.poster_path" class="row-8 poster">
  
                <div class="row-2">
                  <div class="col">
                    <h3>BGM RATES:{{movie.rate_average}}</h3>
                  </div>
                  <star-rating 
                      v-model='rating'
                      v-bind:increment="1"
                      v-bind:max-rating="5"
                      @rating-selected = "setRating"
                      >
                      
                  </star-rating>
                </div>
                <div class="row-2">
                 <h3>WATCH ON</h3>
                 <div v-for= 'provider in movie.providers' :key='provider.provider_name'>
                  <a :href="provider.address">
                    <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
                  </a>
                 </div>
                </div>
            
            </div>
          
          <!-- title&star&overview -->  
            <div class="col">
              <div class="row">
                <h1>{{movie.title}}</h1>
              </div>
              <div class="row">
                <h5>{{movie.original_title}}</h5>
              </div>
              <div class="row">
                <h5>{{movie.release_date}}</h5>
              </div>
              <div class="row">
                <h5>{{movie.runtime}}</h5>
              </div>
              <div class="row">
                <h5 v-for="genre in movie.genres" :key='genre.genre_name'>{{genre.genre_name}}</h5>
              </div>
                <hr>
              <div class="row">
                <h3>{{movie.overview}}</h3>
              </div>
              
              
            
            </div>
        </div>
        
        <div class="row" name="title-star-overview">
          <div class="row" name="title-star">
            
          </div>
          
        </div>

        
        <!-- overview -->
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

    

</style>
