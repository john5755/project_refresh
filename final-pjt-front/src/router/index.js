import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import NotFound404 from '../views/NotFound404.vue'



Vue.use(VueRouter)

const routes = [
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
