<template>
  <div>
    <back-ground-movie></back-ground-movie>
    <back-music-movie></back-music-movie>

  </div>
</template>

<script>
import BackGroundMovie from '@/components/BackGroundMovie.vue'
import BackMusicMovie from '@/components/BackMusicMovie.vue'
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'

export default {
  components: { BackGroundMovie, BackMusicMovie },
  name: 'BackGround',
  computed: {
  ...mapGetters(['musicMovies', 'groundMovies']),
  
    },
    methods: {
      ...mapActions(['fetchMusicMovies', 'fetchGroundMovies'])
    },
    created() {
      this.fetchMusicMovies()
      this.fetchGroundMovies()
    },
}
</script>

<style>

</style>