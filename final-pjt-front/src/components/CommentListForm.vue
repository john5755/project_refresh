<template>
  <form @submit.prevent="onSubmit" class="comment-list-form container">
    <!-- <label class="col-2" for="comment">comment: </label> -->
    <input class="col-10 transparent-input" type="text" id="comment" v-model="content" placeholder="leave your comment...." required>
    <button class="col-1 mx-1 btn btn-outline-secondary">post</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ movieId: this.movie.movie_id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 2px solid #525252 ;
  /* margin: 1rem; */
  padding: 0.5rem;
}
.transparent-input{
  background-color: rgba(0,0,0,0) !important;
  border:none !important;
}
input, select, textarea{
    color: #BEB9B9 !important;
    
}
</style>