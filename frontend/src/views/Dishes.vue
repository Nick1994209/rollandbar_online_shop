<template>
  <div class="about">
    <h1>This is dishes page</h1>

    <div class="grid">
      <ListDishes v-on:chose-dish="chosenDish = $event" v-bind:dishes="dishes"></ListDishes>
      <Dish v-if="chosenDish" v-bind:dish="chosenDish"></Dish>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

import ListDishes from '../components/ListDishes.vue'
import Dish from '../components/Dish.vue'

export default {
  components: {Dish, ListDishes},
  data() {
    return {
      chosenDish: null,
    }
  },
  computed: mapState({
    dishes: state => state.dishes.dishes,
  }),
  beforeCreate() {
    this.$store.dispatch('dishes/getDishes');
  },
}
</script>

<style>
.grid {
  display: grid;
  grid-template-columns: 30% 70%;
}
</style>