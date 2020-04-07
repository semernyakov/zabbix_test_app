<template>
    <div id="app">
        <div class="container">
            <Home msg="Дубликаты узлов сети"/>
        </div>
    </div>
</template>

<script>
  import Home from './components/Home.vue'

  export default {
    name: 'App',
    components: {Home}
  }
</script>

<style>

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        overflow-y: scroll;
    }

</style>
