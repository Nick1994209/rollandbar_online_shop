<template>
  <div class="about">
    <h1>This is dishes page</h1>

    <div v-for="dish in dishes" :key="dish.id">
      <p>{{ dish.id }}</p>
      <p>{{ dish.name }}</p>

      <button @click="addDishToBasket(dish.id)">Добавить в корзину</button>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
  computed: mapState({
    dishes: state => state.dishes,
  }),
  methods: {
    addDishToBasket(dishID) {
      this.$store.commit('addDishToBasket', dishID);
    },
  },
  beforeCreate() {
    this.$store.dispatch('getDishes');
  },

}
</script>