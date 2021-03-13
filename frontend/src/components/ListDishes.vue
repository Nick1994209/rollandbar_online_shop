<template>
  <div class="listDishes">
    <div class="dish block" v-on:click="$emit('chose-dish', dish)"
         v-for="dish in dishes" :key="dish.id">
      <p>{{ dish.name }}</p>
      <DishPrice :dish="dish"/>
    </div>
  </div>
</template>

<script>
import DishPrice from './DishPrice.vue'

export default {
  name: 'ListDishes',
  data() {
    return {
      name: 'rollandbar',
    }
  },
  components: {
    DishPrice,
  },
  props: {
    dishes: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped lang="scss">
.listDishes {
  overflow: scroll;
  height: 100%;
}

.dish {
  color: #42b983;
  text-align: right;
  margin: 20px;

  :hover {
    cursor: pointer;
    border: 2px #8efa9b;
  }
}
</style>

