import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movies: [],
    movie: {},
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // isAuthor: (state, getters) => {
    //   return state.movie.user?.username === getters.currentUser.username
    // },
    // ismovie: state => !_.isEmpty(state.movie),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_COMMENTS: (state, comments) => (state.movie.comments = comments),
    // SET_MOVIE_RATINGS: (state, ratings) => (state.movie.comments = comments),
  },

  actions: {
    fetchMovies({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, movieId) {
      /* 단일 게시글 받아오기
      GET: movie URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동 
      */
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

//     createmovie({ commit, getters }, movie) {
//       /* 게시글 생성
//       POST: movies URL (게시글 입력정보, token)
//         성공하면
//           응답으로 받은 게시글을 state.movie에 저장
//           movieDetailView 로 이동
//         실패하면
//           에러 메시지 표시
//       */
      
//       axios({
//         url: drf.movies.movies(),
//         method: 'post',
//         data: movie,
//         headers: getters.authHeader,
//       })
//         .then(res => {
//           commit('SET_movie', res.data)
//           router.push({
//             name: 'movie',
//             params: { movieId: getters.movie.pk }
//           })
//         })
//     },

//     updatemovie({ commit, getters }, { pk, title, content}) {
//       /* 게시글 수정
//       PUT: movie URL (게시글 입력정보, token)
//         성공하면
//           응답으로 받은 게시글을 state.movie에 저장
//           movieDetailView 로 이동
//         실패하면
//           에러 메시지 표시
//       */
//       axios({
//         url: drf.movies.movie(pk),
//         method: 'put',
//         data: { title, content },
//         headers: getters.authHeader,
//       })
//         .then(res => {
//           commit('SET_movie', res.data)
//           router.push({
//             name: 'movie',
//             params: { movieId: getters.movie.pk }
//           })
//         })
//     },

//     deletemovie({ commit, getters }, movieId) {
//       /* 게시글 삭제
//       사용자가 확인을 받고
//         DELETE: movie URL (token)
//           성공하면
//             state.movie 비우기
//             AritcleListView로 이동
//           실패하면
//             에러 메시지 표시
//       */
      
//       if (confirm('정말 삭제하시겠습니까?')) {
//         axios({
//           url: drf.movies.movie(movieId),
//           method: 'delete',
//           headers: getters.authHeader,
//         })
//           .then(() => {
//             commit('SET_movie', {})
//             router.push({ name: 'movies' })
//           })
//           .catch(err => console.error(err.response))
//       }
//     },

//     likemovie({ commit, getters }, movieId) {
//       /* 좋아요
//       POST: likemovie URL(token)
//         성공하면
//           state.movie 갱신
//         실패하면
//           에러 메시지 표시
//       */
//       axios({
//         url: drf.movies.likemovie(movieId),
//         method: 'post',
//         headers: getters.authHeader,
//       })
//         .then(res => commit('SET_movie', res.data))
//         .catch(err => console.error(err.response))
//     },

    // 평점 입력 

		createRating({ getters},{ movieId, bgm_rate }) {
      const rating = { bgm_rate }

      axios({
        url: drf.movies.ratings(movieId),
        method: 'post',
        data: rating,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          // commit('SET_MOVIE_RATINGS', res.data)
        })
        .catch(err => console.error(err.response))
    },







    //댓글 

    createComment({ commit, getters }, { movieId, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.movies.comments(movieId),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { movieId, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.movies.comment(movieId, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { movieId, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.movie의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.comment(movieId, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
  },
}
