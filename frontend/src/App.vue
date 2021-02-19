<template>
  <div id="nav">
    <router-link :to="{ name: 'home'}">Home</router-link> |
    <router-link :to="{ name: 'dishes'}">Блюда</router-link> |
    <router-link :to="{ name: 'basket'}">Корзина {{ priceDishesInBasket }} [{{ numberDishesInBasket }}]</router-link>
  </div>
  <router-view/>
</template>

<script>
export default {
  computed: {
    numberDishesInBasket() { return this.$store.getters['basket/numberDishes'] },
    priceDishesInBasket() { return this.$store.getters['basket/priceDishes'] },
  },
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
