<template>
<div id="app">
  <input type="file" @change="onFileChange" />

  <div id="container">
    <img v-if="url" :src="url" class="container__image"/>
  </div>

  <div class="container__hint">
    <svg :viewBox="`0 0 100 100`" xmlns="http://www.w3.org/2000/svg">
      <!-- <template :key="flat.id" v-for="flat in data.flats">
        <polygon :points="flat.area_points" fill="red" />
      </template> -->
    </svg>
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
        alert(JSON.stringify(data))
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
