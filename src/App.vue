<template>
  <Connection />
  <!-- <Draw /> -->
  <!-- <Popup /> -->
</template>

<script>
import Connection from './components/Connection.vue';
// import Draw from './components/Draw.vue';
// import Popup from './components/Popup.vue';

export default {
  name: 'App',
  components: {
    Connection,
    // Draw,
    // Popup
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
