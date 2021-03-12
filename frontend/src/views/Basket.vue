<template>
  <div class="about">
    <h1>Выполнить заказ</h1>

    <div class="grid">
      <EditUser/>
      <ListBasketDishes/>
    </div>
  </div>
</template>

<script>
import ListBasketDishes from '../components/ListBasketDishes.vue'
import EditUser from '../components/EditUser.vue'

export default {
  name: "BasketView",
  components: {ListBasketDishes, EditUser},
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