export default {
  namespaced: true,
  state: {
    name: '',
    phone: '',
  },
  getters: {
    getDishByID: state => {
      return (dishID) => state.dishes.find((dish) => dish.id === dishID)
    },
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    },
    setUserInfo(state, {name, phone}) {
      state.name = name;
      state.phone = phone;
    },
    setPhone(state, phone) {
      state.phone = phone;
    },
  },
  actions: {},
  modules: {}
}
