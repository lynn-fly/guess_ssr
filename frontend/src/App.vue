<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { setUser, setToken } from "@/utils/auth";

export default {
  name: 'App',
  computed: {
    ...mapGetters(["userInfor"]),
  },
  mounted() {
    debugger
    console.log('APP mounted', window.location.pathname);
    if (window.location.pathname == '/login' || window.location.pathname == '/') {
      setToken('');
      setUser([]);
      this.$store.commit('user/SET_USER_INFO', [])
    } else {
      this.$store.dispatch("user/getInfo")
      .then(data=>{})
      .catch(err=>{})
    }
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
