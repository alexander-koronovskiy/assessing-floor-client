<template>
<div class="container">
  <input type="file" @change="onFileChange" />
  <img v-if="url" :src="url" :width="imageWidth" :height="imageHeight" class="container__image"/>
  <div v-show="flats.length" class="container__hint">
    <svg :viewBox="`0 0 ${imageWidth} ${imageHeight}`" xmlns="http://www.w3.org/2000/svg">
      <template :key="id" v-for="(flat, id) in flats">
        <polygon :points="flat" fill="green" fill-opacity="0.4" />
      </template>
    </svg>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      url: null,
      imageWidth: 0,
      imageHeight: 0,
      flats: [],
    }
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
      const prefetchImage = new Image();
      prefetchImage.src = this.url;
      prefetchImage.onload = () => {
        this.imageWidth = prefetchImage.width;
        this.imageHeight = prefetchImage.height;
      }
      
      let Data = new FormData();
      Data.append('image', file);
      fetch('http://127.0.0.1:8000/image', {
        method: "POST",
        body: Data
      }).then(response => {
        if (response.status !== 200) {
          return Promise.reject();
        }
        return response.json();
      }).then(data => {
        this.flats = data.data.map(flat => {
          return flat.join(' ');
        });
      })
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
  margin-top: -1.5%;
}
</style>
