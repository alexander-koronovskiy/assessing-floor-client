<template>
<div id="app">
  <input type="file" @change="onFileChange" />

  <div id="container">
    <img v-if="url" :src="url" class="container__image"/>
  </div>

  <div class="container__hint">
    <svg :viewBox="`0 0 ${imageWidth} ${imageHeight}`" xmlns="http://www.w3.org/2000/svg">
      <template :key="id" v-for="(flat, id) in flats">
        <polygon :points="flat" fill="red" />
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
      imageWidth: 100,
      imageHeight: 100,
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
      }).then(function(data) {
        this.flats = data.data.map(flat => {
          return String.valueOf(flat); // TODO: convert flat to string 
        })

        alert(this.flats)
      }).catch(() => alert('ошибка'));
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
  display: none;
}
.container__image {
  width: 100%;
  object-fit: contain;
  height: auto;
}
</style>
