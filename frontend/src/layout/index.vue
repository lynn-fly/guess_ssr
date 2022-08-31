<template>
  <div>
    <div class="container" style="margin-top: 15px;">
      <section class="app-main">
        <transition name="fade-transform" mode="out-in">
          <router-view :key="key" />
        </transition>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  computed: {
    key() {
      return this.$route.path
    }
  }
}
</script>

<style scoped>

</style>
