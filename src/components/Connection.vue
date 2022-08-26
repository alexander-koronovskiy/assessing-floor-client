<template>
<div class="container">
  <div v-show="loading" class="donut"></div>
  <input type="file" v-show="!loading" @change="onFileChange" />
  <div class="container__image">
    <img v-if="url" :src="url" :width="imageWidth" :height="imageHeight" class="container__image--img"/>
    <div v-show="flats.length" class="container__image--hint">
      <svg :viewBox="`0 0 ${imageWidth} ${imageHeight}`" xmlns="http://www.w3.org/2000/svg">
        <template :key="id" v-for="(flat, id) in flats">
          <polygon :points="flat" fill="green" fill-opacity="0.4" />
        </template>
      </svg>
    </div>
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
      loading: false,
    }
  },
  methods: {
    onFileChange(e) {
      this.flats = [];
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
      const prefetchImage = new Image();
      prefetchImage.src = this.url;
      prefetchImage.onload = () => {
        this.imageWidth = prefetchImage.width;
        this.imageHeight = prefetchImage.height;
      }
      this.loading = true;

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
        this.loading = false;
      });
    }
  }
};
</script>

<style>
.container__image {
  position: relative;
}
.container__image--hint {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.container__image--img {
  width: 100%;
  object-fit: contain;
  height: auto;
}

@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #52e235;
  border-radius: 50%;
  width: 300px;
  height: 300px;
  animation: donut-spin 1.2s linear infinite;
  margin-left: auto;
  margin-right: auto;
}
</style>
