<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: 'App',
  computed: {
    ...mapGetters(["userInfor"]),
  },
  mounted() {
    console.log('APP mounted');
    
      this.$store.dispatch("user/getInfo")
      .then(data=>{})
      .catch(err=>{

      })
  }
}
</script>

<style>
* {
  font-family: "ph Dinpro" !important;
}
.flex-c-c{
  display: flex;
  justify-content: center;
  justify-content: center;
}
</style>
