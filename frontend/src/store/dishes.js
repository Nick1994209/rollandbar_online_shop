const axios = require('axios');

export default {
  namespaced: true,
  state: {
    dishes: [],
  },
  getters: {
    getDishByID: state => {
      return (dishID) => state.dishes.find((dish) => dish.id === dishID)
    },
  },
  mutations: {
    setDishes(state, dishes) {
      state.dishes = dishes;
    },
  },
  actions: {
    getDishes({commit}) {
      axios.get('http://127.0.0.1:8000/api/v1/dishes/')
        .then(
          (response) => {
            commit('setDishes', response.data)
          }
        ).catch(
        (error) => {
          alert(`Fail getting dishes. Error=${error}`)
        }
      )
    },
  },
  modules: {}
}
