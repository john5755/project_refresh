<template>
  <div>
    <br>
  <li class="comment-list-item d-flex justify-content-between">
    <!-- <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>:  -->

      <span v-if="!isEditing"><h4>&nbsp;&nbsp;&nbsp;&nbsp;{{ payload.content }}</h4></span>

      <span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button class="btn btn-secondary" @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancle</button>
      </span>

      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <button class="btn btn-outline-secondary" @click="switchIsEditing">Edit</button> |
        <button class="btn btn-secondary btn-sm" @click="deleteComment(payload)">Delete</button>
      </span>
  </li>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        movieId: this.comment.movie,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  /* border: 1px solid green; */
  /* margin: 0rem; */
}
</style>