<template>
<div id="app">
  <input type="file" @change="onFileChange" />
  <div class="container">
    <img 
      v-if="url"
      :src="data.plan_image.image_thumb"
      :width="data.plan_image.width"
      :height="data.plan_image.height"
      class="container__image"
    />
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
},
mounted () {
  fetch('https://api.gkosnova.tech/public/api/v1/building-objects/2/floor/1/1/-1?fullList=1')
  .then(res => res.json())
  .then(({ data }) => {
    this.data = data
  })
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
