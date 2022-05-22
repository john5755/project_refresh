const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
// const MOVIES = 'movies/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    
    delete: userPk => HOST + ACCOUNTS + `delete/${userPk}/`,
    
    changepassword: () => HOST + ACCOUNTS + 'password/change/',
    passwordReset: () => HOST + ACCOUNTS + 'reset/',
    passwordResetConfirm : () => HOST + ACCOUNTS + 'reset/confirm/',

    resetHistory: (userPk,partnerPk) => HOST + ACCOUNTS + `history/reset/${userPk}/${partnerPk}/`,


    
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  // articles: {
  //   // /articles/
  //   articles: () => HOST + ARTICLES,
  //   // /articles/1/
  //   article: articlePk => HOST + ARTICLES + `${articlePk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
  //   comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
  //   comment: (articlePk, commentPk) =>
  //     HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  // },
}