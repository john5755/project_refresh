import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '' ,
    
    userPk : '',
    partnerPk: '',  

    currentUser: {},
    profile: {},
    authError: null,
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    isLoggedIn: state => !!state.token,

    userLoggedIn : state => !!state.userPk,
    partnerLoggedIn : state => !!state.partnerPk,


    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    
    SET_USER_LOGGEND_IN: (state, userPk) => state.userPk = userPk,
    SET_PARTNER_LOGGED_IN: (state, partnerPk) => state.partnerPk = partnerPk
  },

  actions: {
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    saveUserLoggedIn({ commit }, userPk) {
      commit('SET_USER_LOGGEND_IN', userPk)
    },

    savePartnerLoggedIn({ commit }, partnerPk) {
      commit('SET_PARTNER_LOGGED_IN', partnerPk)
    },

    removeUserLoggedIn({ commit }) {
      commit('SET_USER_LOGGEND_IN', '')
    },

    removePartnerLoggedIn({ commit }) {
      commit('SET_PARTNER_LOGGND_IN', '')
    },


    //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    //README에 쓸것
    //userLoggedIn값과 partnerLoggedIn값이 user(pk=0)에대해 작동하지않음
    //0번 user는 관리자이므로 작동하지 않음이 더욱 적절하다.


    login({ commit, getters, dispatch }, credentials) {
      // 토큰이 없는 경우 userLoggedIn 초기화
      if (!getters.isLoggedIn) {
        dispatch('removeUserLoggedIn')
        axios({
          url: drf.accounts.login(),
          method: 'post',
          data: credentials
        })
          .then(res => { 
            const token = res.data.key
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            console.log(getters.userLoggedIn)
            // dispatch('logout')
            // router.push({ name: 'login' })
            
          })
          .catch(err => {
            console.error(err.response.data)
            commit('SET_AUTH_ERROR', err.response.data)
          })
          // .finally( function(){
          //   dispatch('logout')
          // })
          

      }else if (getters.userLoggedIn && !getters.partnerLoggedIn){
        //partner login 시키기 전에 user logout부터 시킴
        
        
        // dispatch('logout')
        
        axios(
           {
            url: drf.accounts.login(),
            method: 'post',
            data: credentials
          })
          .then(res => { 
            const token = res.data.key
            dispatch('saveToken', token)
            dispatch('fetchCurrentUser')
            // dispatch('savePartnerLoggedIn',getters.currentUser.pk)
            router.push({ name: 'login' }) //// 2번째 로그인까지 완료된 후 띄울 화면 (나중에 바꿔야함)
          })
          .catch(err => {
            console.error(err.response.data)
            commit('SET_AUTH_ERROR', err.response.data)
          })
        
        axios({
            url: drf.accounts.login(),
            method: 'post',
            data: credentials
        })
      
     } 





    },

    signup({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 signup URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articles' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      if (getters.userLoggedIn && !getters.partnerLoggedIn) {
      
          axios({
          url: drf.accounts.logout(),
          method: 'post',
          // data: {},
          headers: getters.authHeader,
        })
          .then(() => {
            dispatch('removeToken')
            router.push({ name: 'login' })
          })
          .error(err => {
            console.error(err.response)
          })
        }else if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.logout(),
          method: 'post',
          // data: {},
          headers: getters.authHeader,
        })
          .then(() => {
            dispatch('removeToken')
            dispatch('removeUserLoggedIn')
            dispatch('removePartnerLoggedIn')
            router.push({ name: 'login' })
          })
          .error(err => {
            console.error(err.response)
          })
        }
    },

      

    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER', res.data)
            
            if (!getters.userLoggedIn) {
               commit('SET_USER_LOGGEND_IN',res.data.pk)
              
              }else {
                commit('SET_PARTNER_LOGGED_IN',res.data.pk)
              }})

          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },
  },
}
