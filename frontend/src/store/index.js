import { createStore } from 'vuex'
import dishes from './dishes'
import basket from './basket'
import user from './user'

export default createStore({
  modules: {dishes, basket, user},
  state: {},
  getters: {},
  mutations: {},
  actions: {},
})
