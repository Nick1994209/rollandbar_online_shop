<template>
  <div>
    <div class="is-size-5">Ваши данные</div>

    {{ name }} {{ phone }}

    <div class="box">
      <div class="field">
        <label class="label">
          Имя
          <input v-model="name" type="text" class="input">
        </label>
      </div>

      <div class="field">
        <label class="label">
          Телефон
          <input v-model="phone" type="tel" class="input">
        </label>
      </div>

      <button :disabled="!isDataFilled" class="button" v-on:click="createOrder">Сделать заказ</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: this.$store.state.user.name,
      phone: this.$store.state.user.phone,
    }
  },
  computed: {
    isDataFilled() {
      return Boolean(this.name) && Boolean(this.phone)
    }
  },
  methods: {
    createOrder() {
      const client = {
          "name": this.name,
          "phone": this.phone,
        }

      const payload = {
        "dishes": this.$store.getters['basket/listDishesIDs'],
        client,
      }

      this.$store.commit('user/setInfo', client)

      axios.post('http://localhost:8000/api/v1/orders/', payload).then(
          (response) => {
            alert(response.data.id)
          }
      ).catch(
          (error) => {
            alert(error)
          }
      )
    }
  }
}
</script>
