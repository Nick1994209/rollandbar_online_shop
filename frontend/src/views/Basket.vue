<template>
  <div>
    <div class="is-size-3">Создание заказа</div>

    <div class="columns">
      <CreateOrder class="column"/>
      <DishesList class="column"/>
    </div>
  </div>
</template>

<script>
import CreateOrder from '@/components/BasketCreateOrder.vue'
import DishesList from '@/components/BasketDishesList.vue'

export default {
  components: {
    CreateOrder,
    DishesList,
  }
}
</script>
