<template>
  <div>
    <!-- 대표이미지 -->
    <div><img :src="tmdb+movie.poster_path" alt="poster"></div>
    
    <!-- provider links -->
    <div v-for= 'provider in movie.providers' :key='provider.provider_name'>
      <div v-if="provider.provider_name === 'Watcha'">
        <a href="https://www.watcha.com/">
        <img :src="require(`@/assets/${provider.provider_name}.jpg`)" alt="">
        </a>
      </div>
      <div v-if="provider.provider_name === 'Netflix'">
        <a href="https://www.netflix.com/">
        <img :src="require(`@/assets/${provider.provider_name}.jpg`)" alt="">
        </a>
      </div>

      <a href="`https://www.${provider.provider_name}.com/`">
        <img :src="require(`@/assets/${provider.provider_name}.jpg`)" alt="">
      </a>
      
    </div>
    
    
    <h1>{{ movie.title }}</h1>
    
    <!-- <p>
      {{ article.content }}
    </p>
   
   
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>

    
    
    <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    
    
    <comment-list :comments="article.comments"></comment-list>  -->
    

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  // import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'MovieDetail',
    // components: { CommentList },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
        tmdb:'https://image.tmdb.org/t/p/w500/',
        providerImg:"@/assets/",
        jpg:'.jpg',
        'Netfilx':'https://www.netflix.com',
        Watcha :'https://watcha.com/',
        links: {
        'Netfilx':'https://www.netflix.com',
        'Amazon Prime Video': 'https://www.primevideo.com/',
        'Watcha':'https://watcha.com/',
        }
      }
    },
    computed: {
      ...mapGetters(['movie']),
      linkGet() {
        // const ott = sdf
        return this.links['Netflix']
      },
      // ...mapGetters(['isAuthor', 'article']),
      // likeCount() {
      //   return this.article.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchMovie',
        // 'likeArticle',
        // 'deleteArticle',
      ])
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style></style>
