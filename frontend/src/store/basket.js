export default {
  namespaced: true,
  state: {
      dishesIDs: [],
      userInfo: {
        name: null,
        phone: null,
      },
  },
  getters: {
    numberDishes: state => {
      return state.dishesIDs.length;
    }
  },
  mutations: {
    addDish (state, dishID) {
      state.dishesIDs.push(dishID)
    }
  },
  actions: {},
}
