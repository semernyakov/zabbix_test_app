<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col"><h1>{{ msg }}</h1></div>
      <div class="col ml-auto pt-2">
        <b-button variant="outline-primary" v-on:click="fetch" class="small float-right">Обновить</b-button>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <p v-if="items[0]">Полученные результаты:</p>
        <p class="mt-" v-else>О, нет 😢 !!! Произошла, ошибка или данные небыли предоставлены!</p>
      </div>
      <b-table striped hover :items="items" class="mt-3"></b-table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
    name: 'Home',
    props: {
      msg: String,
    },
    data() {
      return {
        items: [],
        loading: false,
        error: null
      }
    },
    mounted() {
      axios
        .get('http://localhost:8080/')
        .then(response => (this.items = response.data));
    },
    methods: {
      fetch: function (event) {
        axios
          .get('http://localhost:8080/')
          .then(response => (this.items = response.data));
        if (event) {
          alert('Подтвердите обновление данных!')
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
