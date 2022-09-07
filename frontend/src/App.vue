<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { setUser, setToken } from "@/utils/auth";

export default {
  name: "App",
  computed: {
    ...mapGetters(["userInfor"]),
  },
  mounted() {
    //初始化音乐
    this.$store.commit("audio/createAudios", {
      id: "bj",
      src: "http://129.226.227.171/upload/7scmx-u2mhm-4.mp3",
      state: true,
      loop: true,
    });
    // setTimeout(() => {
    //   console.log(this.$store.commit("audio/getPaused", "bj"));
    //   this.$store.commit("audio/play", "bj");
    // }, 3000);

    this.$store.commit("audio/createAudios", {
      id: "lucky",
      src: "http://129.226.227.171/upload/lucky.mp3",
      state: false,
    });
    this.$store.commit("audio/createAudios", {
      id: "wrong",
      src: "http://129.226.227.171/upload/wrong.wav",
      state: false,
    });
    this.$store.commit("audio/createAudios", {
      id: "ok",
      src: "http://129.226.227.171/upload/ok.wav",
      state: false,
    });
    // setTimeout(() => {
    //   this.$store.commit("audio/play", "ok");
    // }, 5000);
    // setTimeout(() => {
    //   this.$store.commit("audio/play", "wrong");
    // }, 6000);
    //
    console.log("APP mounted", window.location.pathname);
    if (window.location.pathname == "/login" || window.location.pathname == "/") {
      setToken("");
      setUser([]);
      this.$store.commit("user/SET_USER_INFO", []);
    } else {
      this.$store
        .dispatch("user/getInfo")
        .then((data) => {})
        .catch((err) => {});
    }
  },
};
</script>

<style>
@import "./keyframes.css";
* {
  font-family: "ph Dinpro" !important;
}
.flex-c-c {
  display: flex;
  justify-content: center;
  justify-content: center;
}
.heardsss {
  z-index: 9999999 !important;
}
</style>
