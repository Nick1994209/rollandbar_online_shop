<template>
  <div class="about">
    <h1>Список блюд</h1>

    <div class="grid">
      <ListDishes v-on:chose-dish="chooseDish" :dishes="dishes"/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex';

import ListDishes from '../components/ListDishes.vue'

export default {
  name: "DishesView",
  components: {ListDishes},
  data() {
    return {
      chosenDish: null,
    }
  },
  methods: {
    chooseDish(dish) {
      this.$router.push(`/dishes/${dish.id}`)
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

<style scoped lang="scss">
.grid {
  display: grid;
  grid-template-columns: 40% 60%;
}
</style>