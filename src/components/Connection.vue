<template>
<div id="app">
  <input type="file" @change="onFileChange" />

  <div id="preview">
    <img v-if="url" :src="url" />
  </div>


</div>
</template>

<script>
export default {
  data() {
  return {
    url: null,
  }
},
methods: {
  onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
  }
}
};
</script>

<style>
  .container {
    position: relative;
  }
  .container__hint {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  .container__image {
    width: 100%;
    object-fit: contain;
    height: auto;
  }
</style>
