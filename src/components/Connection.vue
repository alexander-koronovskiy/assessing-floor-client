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
</style>
