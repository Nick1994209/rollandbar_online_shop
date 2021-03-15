<template>
  <div>
    <div class="is-size-5">Список блюд</div>

    <div class="box" v-for="dish in dishes" :key="dish.id">
      {{ dish.name }}
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    dishes() {
      return this.$store.getters['basket/listDishes']
    }
  }
}
</script>

<style>

</style>