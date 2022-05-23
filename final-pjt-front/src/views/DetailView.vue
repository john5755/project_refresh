<template>
  <div>
    
    <h1>{{ movie.title }}</h1>
    
    <!-- 대표이미지 -->
    <div><img :src="tmdb+movie.poster_path" alt="poster"></div>
    
    <!-- provider links -->
    <div v-for= 'provider in movie.providers' :key='provider.provider_name'>
      <a :href="provider.address">
        <img :src="tmdb+provider.logo_path" alt="logo" width="50" height="50">
      </a>
    </div>
    
    <p>{{ movie.rate_average }}</p>
    <hr>
    <star-rating 
    v-model='rating'
    v-bind:increment="1"
    v-bind:max-rating="5"
    @rating-selected = "setRating">

    </star-rating>
    
    <comment-list :comments="movie.comments">
    </comment-list> 
    

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

<style></style>
