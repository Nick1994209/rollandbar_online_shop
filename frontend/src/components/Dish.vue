<template>
  <div class="dish">
    <div>{{ dish.name }}</div>

    <DishPrice :dish="dish"/>

    <div>
      <img class="photo" v-if="dish.photo" alt="dish" :src="dish.photo">
    </div>

    <Markdown :text="dish.ingredients"/>

    <div v-if="amountInBasket" class="buyButton">
      <div class="basketButton" @click="deleteDishFromBasket(dish)">-</div>
      <div class="dishInfoInButton">
        <div>Количество: {{ amountInBasket }}</div>
        <div>Цена: {{ priceInBasket }}</div>
      </div>
      <div class="basketButton" @click="addDishToBasket(dish)">+</div>
    </div>
    <button class="buyButton basketButton" v-else @click="addDishToBasket(dish)">
      Добавить в корзину
    </button>
  </div>
</template>

<script>
import Markdown from '@/components/Markdown.vue'
import DishPrice from '@/components/DishPrice.vue'

export default {
  name: 'Dish',
  components: {Markdown, DishPrice},
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

.buyButton {
  background-color: #42b983;
  color: #e3efd0;
  padding: 12px 28px;
  border-radius: 4px;

  margin-left: auto;
  margin-right: auto;

  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 50%;
}

.basketButton {
  cursor: pointer;
  font-size: large;

  &:hover {
    color: #f1dcaa;
  }
}

.dishInfoInButton {
  display: flex;
  flex-direction: column;
  font-size: small;
}

</style>
