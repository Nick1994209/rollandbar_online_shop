export default {
  namespaced: true,
  state: {
      chosenDishes: {
        // key: id
        // value: {dish: dishObject, number: int}
      },
      userInfo: {
        name: null,
        phone: null,
      },
  },
  getters: {
    numberDishes: state => {
      return Object.keys(state.chosenDishes).length;
    },
    priceDishes: state => {
      const reduceFunc = (accumulator, { dish: {price}, number}) => accumulator + price * number
      return Object.values(state.chosenDishes).reduce(reduceFunc, 0);
    },
  },
  mutations: {
    addDish (state, dish) {
      if (dish.id in state.chosenDishes) {
        state.chosenDishes[dish.id].number += 1
      } else {
        state.chosenDishes[dish.id] = {
          dish,
          number: 1,
        }
      }
    },
    deleteDish (state, dish) {
      state.chosenDishes.push(dish)
    },
  },
  actions: {},
}



const a = {
  1: {dish: {amount: 100}, number: 2},
  2: {dish: {amount: 120}, number: 1},
  3: {dish: {amount: 120}, number: 10},
}

const reduceFunc = (accumulator, { dish: {amount}, number}) => accumulator + amount * number
console.log(Object.values(a).reduce(reduceFunc))
