import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

export default {
  state: {
    musicMovies: [],
    groundMovies: [],
  },

  getters: {
    musicMovies: state => state.musicMovies,
    groundMovies: state => state.groundMovies,
  },

  mutations: {
    SET_MUSIC_MOVIES: (state, musicMovies) => state.musicMovies = musicMovies,
    SET_GROUND_MOVIES: (state, groundMovies) => state.groundMovies = groundMovies,
  },

  actions: {
    fetchMusicMovies({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.musiclist(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MUSIC_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchGroundMovies({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.groundlist(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_GROUND_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
  },
}