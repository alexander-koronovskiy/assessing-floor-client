<template>
  <Draw />
</template>

<script>
import Draw from './components/Draw.vue';
// Connection
// Draw
// Popup

export default {
  name: 'App',
  components: {
    Draw,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
