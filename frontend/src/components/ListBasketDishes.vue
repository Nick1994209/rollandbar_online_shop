<template>
  <div>
    <div class="text-primary is-size-5 has-text-weight-semibold">Просмотр продуктов в корзине</div>

    <div class="box" v-for="dishInfo in dishes" :key="dishInfo.dish.id">
      <div>{{ dishInfo.dish.name }} [{{ dishInfo.amount }}]</div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    dishes() {
      return this.$store.state.basket.chosenDishes;
    }
  }
}
</script>