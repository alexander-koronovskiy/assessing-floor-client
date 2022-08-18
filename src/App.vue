<template>
  <Draw />
  <!-- <Connection /> -->
  <!-- <Popup /> -->
</template>

<script>
import Draw from './components/Draw.vue';
// import Connection from './components/Connection.vue';
// import Popup from './components/Popup.vue';

export default {
  name: 'App',
  components: {
    Draw,
    // Connection,
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
