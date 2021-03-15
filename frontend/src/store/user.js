export default {
  namespaced: true,
  modules: {},
  state: {
    name: '',
    phone: '',
  },
  getters: {},
  mutations: {
    setInfo(state, {name, phone}) {
      state.name = name
      state.phone = phone
    }
  },
  actions: {},
}