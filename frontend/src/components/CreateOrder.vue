<template>
  <div>
    <div class="text-primary is-size-5 has-text-weight-semibold">Создание заказа</div>

    <div>
      {{ name }} {{ phone }}
    </div>

    <div class="box mb-4">
      <div class="field">
        <label class="label">
          Имя
          <input v-model="name" class="input">
        </label>
      </div>

      <div class="field">
        <label class="label">
          Телефон
          <input v-model="phone" class="field input">
        </label>
      </div>

      <div class="field is-horizontal">
        <button :disabled="!isDataEmpty" class="button" v-on:click="createOrder">
          Сделать заказ
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      'name': '',
      'phone': '',
    }
  },
  computed: {
    isDataEmpty() {
      return Boolean(this.phone) && Boolean(this.name)
    }
  },
  methods: {
    createOrder() {
      const payload = {
        "dishes": this.$store.getters['basket/listDishesIDs'],
        "client": {
          "name": this.name,
          "phone": this.phone,
        }
      }

      axios.post('http://localhost:8000/api/v1/orders/', payload).then(
          (response) => {
            alert(response.data.id)
          }
      ).catch(
          (error) => {
            alert(error)
          }
      )
    },
  }
}

</script>
