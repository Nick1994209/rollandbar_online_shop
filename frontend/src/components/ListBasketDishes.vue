<template>
  <div>
    <div class="box" v-for="dish in dishes" :key="dish.id">
      <div>{{ dish.name }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ListBasketDishes',
  computed: {
    dishes() {
      return this.$store.getters['basket/listDishes']
    },
  }
}
</script>
