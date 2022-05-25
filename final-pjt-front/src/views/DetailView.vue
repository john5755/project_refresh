<template>
  <div>
    
    
    
<!--    
    <div><img :src="tmdb+movie.poster_path" alt="poster"></div>
    
   
    <div v-for= 'provider in movie.providers' :key='provider.provider_name'>
      <a :href="provider.address">
        <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
      </a>
    </div>
    
    <p>{{ movie.rate_average }}</p>
    <hr> -->
    <star-rating 
    v-model='rating'
    v-bind:increment="1"
    v-bind:max-rating="5"
    @rating-selected = "setRating">

    </star-rating>
    
    <comment-list :comments="movie.comments">
    </comment-list> 

    <!-- 틀 -->
    <div class="container">
      <div class="">
        
        <!-- poster & provider -->
        <div class="row container vw-100" name="poster-provider" >
          <!-- :style="`background-image:url(${tmdb+movie.poster_path}); overflow:hidden;`" -->
            <div class="col-6 poster container">
                <img :src="tmdb+movie.poster_path" class="poster">
              
           
            </div>
            <div class="col-6">
              <div class="row-2">
                provider
              </div>
            </div>
        </div>
        
        <!-- title&star&overview -->
        <div class="row" name="title-star-overview">
          <div class="row" name="title-star">
            <div class="col">
              title
            </div>
            <div class="col">
              star
            </div>
          </div>
          
          <div class="row">overview</div>
        </div>

        
        <!-- overview -->
        <div class="row">comment
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
