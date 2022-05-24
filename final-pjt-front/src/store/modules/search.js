import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

export default {
  state: {
    charMovies: [],
    actorMovies: [],
  },

  getters: {
    charMovies: state => state.charMovies,
    actorMovies: state => state.actorMovies,
  },

  mutations: {
    SET_CHAR_MOVIES: (state, charMovies) => state.charMovies = charMovies,
    SET_ACTOR_MOVIES: (state, actorMovies) => state.actorMovies = actorMovies,
  },

  actions: {
    fetchCharMovies({ commit, getters }, character) {
      /* 게시글 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.character(character),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_CHAR_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchActorMovies({ commit, getters }, actorname) {
      /* 게시글 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.actorname(actorname),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ACTOR_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
  },
}