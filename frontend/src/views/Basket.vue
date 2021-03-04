<template>
  <div class="about">
    <h1>This is basket page</h1>

    <div class="grid">
      <ListDishes v-on:chose-dish="chosenDish = $event" :dishes="dishes"/>
      <Dish v-if="chosenDish" :dish="chosenDish"/>
    </div>
  </div>
</template>

<script>
import ListDishes from '../components/ListDishes.vue'
import Dish from '../components/Dish.vue'

export default {
  components: {Dish, ListDishes},
  data() {
    return {
      chosenDish: null,
    }
  },
  computed: {
    dishes() {
      return this.$store.getters['basket/listDishes']
    },
  },
}
</script>

<style scoped lang="scss">
.grid {
  display: grid;
  grid-template-columns: 40% 60%;
}
</style>