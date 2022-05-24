import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import NotFound404 from '../views/NotFound404.vue'
import ProfileView from '../views/ProfileView.vue'
import SignupView from '../views/SignupView.vue'
import HomeView from '../views/HomeView.vue'
import DetailView from  '../views/DetailView.vue'
import BackGround from '../views/BackGround.vue'
import SearchNameView from '../views/SearchNameView.vue'

Vue.use(VueRouter)

const routes = [
// accounts
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/profile/:username',  // /profile/neo
    name: 'profile',
    component: ProfileView,
  },


  // movies
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  }, 
  {
    path: '/detail/:movieId',
    name: 'detail',
    component: DetailView,
  }, 
  {
    path: '/background',
    name: 'background',
    component: BackGround,
  },
  {
    path: '/searchname/:query',
    name: 'searchname',
    component: SearchNameView,
  },
  
  
  
  
  
  // 404 
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  
  {
   path:'*',
   redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
