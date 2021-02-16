import {createStore} from "vuex";


export default createStore({
  state: {
      dishesIDs: [],
      userInfo: {
        name: null,
        phone: null,
      },
  },
  getters: {},
  mutations: {
    addDishToBasket (state, dishID) {
      state.dishesIDs.push(dishID)
    }
  },
  actions: {},
})