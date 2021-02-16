<template>
  <div id="nav">
    <router-link :to="{ name: 'home'}">Home</router-link> |
    <router-link :to="{ name: 'about'}">About</router-link> |
    <router-link :to="{ name: 'dishes'}">Блюда</router-link> |
    <router-link :to="{ name: 'basket'}">Корзина {{ numberDishesInBasket }}</router-link>
  </div>
  <router-view/>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: mapState({
    numberDishesInBasket: (state) => { state.basket.dishesIDs.length },
  }),
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
