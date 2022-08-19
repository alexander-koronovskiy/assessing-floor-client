<!-- Use preprocessors via the lang attribute! e.g. <template lang="pug"> -->
<template>
  <div id="app">
    <div v-if="data" class="container">
      <img
        :src="data.plan_image.image_thumb"
        :width="data.plan_image.width"
        :height="data.plan_image.height"
        class="container__image"/>
      <div class="container__hint">
        <svg :viewBox="`0 0 ${data.plan_image.width} ${data.plan_image.height}`" xmlns="http://www.w3.org/2000/svg">
          <template :key="flat.id" v-for="flat in data.flats">
            <polygon :points="flat.area_points" fill="red" />
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
      data: null
    };
  },
  methods: {
    doSomething() {
      alert('Hello!');
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
