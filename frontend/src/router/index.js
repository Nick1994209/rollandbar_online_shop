import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dishes from '../views/Dishes.vue'
import Basket from '../views/Basket.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/dishes',
    name: 'dishes',
    component: Dishes
  },
  {
    path: '/Basket',
    name: 'basket',
    component: Basket
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
