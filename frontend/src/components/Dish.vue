<template>
  <div class="dish">
    <p>{{ dish.name }}</p>
    <p>{{ dish.price }}</p>

    <div>
      <img class="photo" v-if="dish.photo" alt="dish" :src="dish.photo">
    </div>

    <button @click="addDishToBasket(dish)">Добавить в корзину</button>
  </div>

</template>

<script>
export default {
  name: 'Dish',
  props: {
    dish: Object,
  },
  methods: {
    addDishToBasket(dish) {
      this.$store.commit('basket/addDish', dish);
    },
  },
}
</script>

<style scoped lang="scss">
.dish {
  color: #42b983;
  margin: 20px;
}

.photo {
  width: 40%;
  height: auto;
}

button {
  background-color: #42b983;
  padding: 12px 28px;
  border-radius: 4px;
}

</style>

