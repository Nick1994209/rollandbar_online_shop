import { createStore } from 'vuex'
import { dishes } from './dishes'
import { basket } from './basket'

const axios = require('axios');

export default createStore({
  modules: {dishes, basket},
  state: {
    dishes: [],
    basket: {
      dishesIDs: [],
      userInfo: {
        name: null,
        phone: null,
      },
    }
  },
  getters: {},
  mutations: {
    setDishes (state, dishes) {
      state.dishes = dishes;
    },
    addDishToBasket (state, dishID) {
      state.basket.dishesIDs.push(dishID)
    }
  },
  actions: {
    getDishes({ commit }) {
      axios.get('http://127.0.0.1:8000/api/v1/dishes/').then(
          (response) => {
            commit('setDishes', response.data)
          }
      )
    },
  },
})
