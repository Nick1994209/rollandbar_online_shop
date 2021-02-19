<template>
  <div class="listDishes">
    <div class="dish" v-on:click="$emit('chose-dish', dish)"
         v-for="dish in dishes" :key="dish.id">
      <p>{{ dish.name }}</p>
      <p>{{ dish.price }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ListDishes',
  data() {
    return {
      name: 'rollandbar',
    }
  },
  props: {
    dishes: Array,
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

