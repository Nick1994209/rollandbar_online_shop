<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

<!--    <router-link to="/bar">Перейти к Bar</router-link>-->
    <router-link :to="{ name: 'Dishes'}">Блюда</router-link>


    <HelloWorld msg="Welcome to Your Vue.js App"/>

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
