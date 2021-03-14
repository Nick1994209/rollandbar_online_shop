import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Dish from '../views/Dish.vue'
import Dishes from '../views/Dishes.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/dishes',
    name: 'dishes',
    component: Dishes,
    children: [{
      path: ':id',
      component: Dish
    }],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
