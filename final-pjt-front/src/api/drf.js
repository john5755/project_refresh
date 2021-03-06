const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    
    delete: userPk => HOST + ACCOUNTS + `delete/${userPk}/`,
    
    changepassword: () => HOST + ACCOUNTS + 'password/change/',
    passwordReset: () => HOST + ACCOUNTS + 'reset/',
    passwordResetConfirm : () => HOST + ACCOUNTS + 'reset/confirm/',

    resetHistory: (userPk, partnerPk) => HOST + ACCOUNTS + `history/reset/${userPk}/${partnerPk}/`,
    updateHistory: function (userPk, partnerPk) { 
      return HOST + ACCOUNTS + `history/${userPk}/${partnerPk}/`},

    updateProfile: (userPk) => HOST +  ACCOUNTS + `update/${userPk}/`,

    
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    // /movies 메인 페이지/
    movies: () => HOST + MOVIES+ 'movielist/',
    // /movies/1/
    movie: movieId => HOST + MOVIES + `${movieId}/`,

    // /movies/comments/
    comments: movieId => HOST + MOVIES + `${movieId}/` + COMMENTS,
    comment: (movieId, commentPk) => HOST + MOVIES + `${movieId}/` + COMMENTS + `${commentPk}/`,

    ///rating

    ratings: movieId => HOST + MOVIES + `${movieId}/` + 'rating/',

    /// BGM

    musiclist: () => HOST + MOVIES + 'musiclist/',
    groundlist: () => HOST + MOVIES + 'groundlist/',
    
    /// search

    character: (character) => HOST + MOVIES + 'character/' + `${character}`,
    actorname: (actorname) => HOST + MOVIES + 'actorname/' + `${actorname}`,
    
  },
}
