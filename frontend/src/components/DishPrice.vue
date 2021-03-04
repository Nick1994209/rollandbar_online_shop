<template>
  <div>
    <div v-if="dish.price === dish.total_dish_price">{{ dish.total_dish_price }}</div>
    <div v-else>
      <div class="priceWithoutDiscount">{{ dish.price }}</div>
      <div>{{ dish.total_dish_price }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    dish: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped lang="scss">
.priceWithoutDiscount {
  text-decoration: line-through;
  font-size: x-small;
}
</style>