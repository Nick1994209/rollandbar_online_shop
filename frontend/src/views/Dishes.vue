<template>
  <div class="about">
    <h1>Список блюд</h1>

    <div class="columns">

      <ListDishes class="column is-two-fifths" v-on:chose-dish="chooseDish" :dishes="dishes"/>
      <div class="column">
        <router-view class="column"/>
      </div>

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