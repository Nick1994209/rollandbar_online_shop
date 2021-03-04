export default {
  namespaced: true,
  state: {
      chosenDishes: {
        // key: id
        // value: {dish: dishObject, amount: int}
      },
      userInfo: {
        name: null,
        phone: null,
      },
  },
  getters: {
    getDishAmount: state => {
      return (dishID) => state.chosenDishes[dishID]?.amount
    },
    getDishPrice: state => {
      return (dishID) => {
        const dishInfo = state.chosenDishes[dishID]
        if (dishInfo === null) return null

        return dishInfo.amount * dishInfo.dish.total_price
      }
    },
    listDishes: state => {
      return Object.values(state.chosenDishes).map((v) => v.dish);
    },
    numberDishes: state => {
      return Object.keys(state.chosenDishes).length;
    },
    priceDishes: state => {
      const reduceFunc = (
        accumulator, { dish: {total_price}, amount}
      ) => accumulator + total_price * amount
      return Object.values(state.chosenDishes).reduce(reduceFunc, 0);
    },
  },
  mutations: {
    addDish (state, dish) {
      if (dish.id in state.chosenDishes) {
        state.chosenDishes[dish.id].amount += 1
      } else {
        state.chosenDishes[dish.id] = {
          dish,
          amount: 1,
        }
      }
    },
    deleteDish (state, dish) {
      const dishInfo = state.chosenDishes[dish.id]
      if (dishInfo === null) return null

      dishInfo.amount -= 1
      if (dishInfo.amount === 0) {
        delete state.chosenDishes[dish.id]
      }
    },
  },
  actions: {},
}
