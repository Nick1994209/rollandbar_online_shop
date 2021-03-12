<template>
  <div>
    <Form :validation-schema="schema" @submit="onSubmit" :initial-values="initialFormValues">
      <Field placeholder="Имя:" name="name" class="input"/>
      <ErrorMessage name="name" as="div"/>

      <Field placeholder="Телефон:" name="phone" class="input"/>
      <ErrorMessage name="phone" as="div"/>

      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input class="input" type="text" placeholder="e.g Alex Smith">
        </div>
      </div>

      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" type="email" placeholder="e.g. alexsmith@gmail.com">
        </div>
      </div>

      <button>Выполнить заказ</button>
    </Form>

    <div></div>
  </div>
</template>

<script>
import {Field, Form, ErrorMessage, configure} from 'vee-validate';
import * as yup from 'yup';

const axios = require('axios');

configure({
  validateOnChange: true,
  validateOnInput: true,
});

export default {
  name: 'EditUser',
  components: {
    Field,
    Form,
    ErrorMessage,
  },
  data() {
    return {
      schema: yup.object({
        name: yup.string().required('Обязательно').min(3).label('Name'),
        phone: yup.number().required().min(8).label('Phone'),
      }),
      initialFormValues: {
        name: this.$store.state.user.name,
        phone: this.$store.state.user.phone,
      }
    }
  },
  methods: {
    onSubmit(values) {
      this.$store.commit('user/setUserInfo', values);

      axios.post('http://127.0.0.1:8000/', {
        client: values,
        dishes: this.$store.getters['basket/listDishesIDs'],
      }).then((response) => {
        console.log(response);
      }, (error) => {
        console.log(error);
      });
    },
  },
}
</script>
