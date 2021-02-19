import { createStore } from 'vuex'
import dishes from './dishes'
import basket from './basket'

export default createStore({
  modules: {dishes, basket},
  state: {},
  getters: {},
  mutations: {},
  actions: {},
})
