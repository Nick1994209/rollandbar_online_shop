<template>
  <div>
    <h1 class="is-size-3 has-text-weight-semibold">Выполнить заказ</h1>

    <div class="columns">
      <CreateOrder class="column"/>
      <ListBasketDishes class="column"/>
    </div>
  </div>
</template>

<script>
import CreateOrder from '../components/CreateOrder';
import ListBasketDishes from '../components/ListBasketDishes';

export default {
  components: {
    ListBasketDishes,
    CreateOrder,
  }
}
</script>
