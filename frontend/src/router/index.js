import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'

Vue.use(Router)
export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    //redirect: '/home',
    children: [{
      path: 'home',
      name: 'home',
      component: () => import('@/views/home/index')
    }, {
      path: 'answer',
      name: 'answer',
      component: () => import('@/views/answer/index')
    }, {
      path: 'upload',
      name: 'upload',
      component: () => import('@/views/upload/index')
    }, {
      path: 'prize',
      name: 'prize',
      component: () => import('@/views/prize/index')
    }, {
      path: 'login',
      name: 'login',
      component: () => import('@/views/login/index')
    }, {
      path: 'guess',
      name: 'guess',
      component: () => import('@/views/guess/guess')
    }, {
      path: 'auspiciousness',
      name: 'auspiciousness',
      component: () => import('@/views/auspiciousness/auspiciousness')
    }, {
      path: 'luckDraw',
      name: 'luckDraw',
      component: () => import('@/views/luckDraw/luckDraw')
    },{
      path: 'manage',
      name: 'manage',
      component: () => import('@/views/manage/index'),
      //meta: { roles: ['admin'] }
    }]
  }
]

export const asyncRoutes = [
  {
    path: '/',
    component: Layout,
    children: [{
      path: 'manage',
      name: 'manage',
      component: () => import('@/views/manage/index'),
      meta: { roles: ['admin'] }
    }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
