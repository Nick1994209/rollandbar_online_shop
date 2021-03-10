<template>
  <div v-if="dish" class="dish">
    <dish-component :dish="dish"/>
  </div>
  <div v-else>...</div>
</template>

<script>
import DishComponent from '@/components/Dish.vue'

export default {
  name: 'DishView',
  components: {
    'dish-component': DishComponent,
  },
  computed: {
    dish: function () {
      return this.$store.getters['dishes/getDishByID'](Number(this.$route.params.id))
    },
  },
}
</script>
