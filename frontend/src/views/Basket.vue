<template>
  <div class="about">
    <h1>Выполнить заказ</h1>

    <div class="columns">
      <div class="column">
        <CreateOrder/>
      </div>
      <div class="column">
        <ListBasketDishes/>
      </div>
    </div>
  </div>
</template>

<script>
import ListBasketDishes from '../components/ListBasketDishes.vue'
import CreateOrder from '../components/CreateOrder.vue'

export default {
  name: "BasketView",
  components: {ListBasketDishes, CreateOrder},
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
