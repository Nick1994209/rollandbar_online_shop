<template>
  <div class="dish">
    <p>{{ dish.name }}</p>
    <p>{{ dish.price }}</p>

    <div>
      <img class="photo" v-if="dish.photo" alt="dish" :src="dish.photo">
    </div>

    <Markdown :text="dish.ingredients"/>

    <div v-if="amountInBasket" class="button">
      <button @click="deleteDishFromBasket(dish)">-</button>
      <span>({{ amountInBasket }}) Цена: {{ priceInBasket }}</span>
      <button @click="addDishToBasket(dish)">+</button>
    </div>
    <button class="button" v-else @click="addDishToBasket(dish)">Добавить в корзину</button>
  </div>

</template>

<script>
import Markdown from '@/components/Markdown.vue'

export default {
  name: 'Dish',
  components: {Markdown},
  props: {
    dish: Object,
  },
  computed: {
    amountInBasket: function () {
      return this.$store.getters['basket/getDishAmount'](this.dish.id)
    },
    priceInBasket: function () {
      return this.$store.getters['basket/getDishPrice'](this.dish.id)
    },
  },
  methods: {
    addDishToBasket(dish) {
      this.$store.commit('basket/addDish', dish);
    },
    deleteDishFromBasket(dish) {
      this.$store.commit('basket/deleteDish', dish);
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

.button {
  background-color: #42b983;
  color: #e3efd0;
  padding: 12px 28px;
  border-radius: 4px;
}
</style>

