<template>
  <div class="home">
    <!-- <LampNumber :num="startNum" /> -->
    <img
      class="background"
      v-show="true"
      src="../../assets/home/background.png"
      alt=""
      srcset=""
    />
    <div class="main" v-show="true">
      <div class="top">
        <Buttons :msg="name" @backLogin="backLogin" />
        <LampNumber :num="startNum" />
      </div>
      <div class="cententTop">
        <img class="up" src="@/assets/home/otherTitle.png" alt="" />
        <img class="down" src="@/assets/home/theme.png" alt="" />
        <img class="time" src="@/assets/home/time.png" alt="" />
      </div>
      <div class="rabbit">
        <img class="rabbitImg" src="@/assets/home/rabbit.png" alt="" />
        <img class="wearetoImg" src="@/assets/home/weareto.png" alt="" />
      </div>
      <div class="buttonsOur">
        <div class="buttonsCenter">
          <img class="guess" @click="guess" src="@/assets/home/guess.png" alt="" />
          <img
            class="auspiciousness"
            @click="auspiciousness"
            src="@/assets/home/auspiciousness.png"
            alt=""
          />
        </div>
        <img class="luckDraw" @click="luckDraw" src="@/assets/home/luckDraw.png" alt="" />
      </div>
      <div class="bottomImg">
        <img class="bottomImgs" src="@/assets/home/introduce.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import Buttons from "@/components/home/buttons.vue";
import LampNumber from "@/components/home/lampNumber.vue";
import { mapGetters } from "vuex";
import { gotopPage } from "@/utils/index";
export default {
  name: "Home",
  components: {
    Buttons,
    LampNumber,
  },
  data() {
    return {
      startNum: 50,
    };
  },
  computed: {
    ...mapGetters(["name"]),
  },
  methods: {
    guess() {
      console.log("guess");
      gotopPage("/guess");
    },
    auspiciousness() {
      gotopPage("/auspiciousness");
      console.log("auspiciousness");
    },
    luckDraw() {
      gotopPage("/luckDraw");
      console.log("luckDraw");
    },
    backLogin() {
      gotopPage("/login");
    },
  },
  created() {
    console.log("Home");
  },
};
</script>

<style scoped>
.home {
  position: fixed;
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  /* background-color: #000; */
}

.background {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1;
}

.main {
  width: 100vw;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}

.main .top {
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.2rem 0.4rem;
  position: relative;
  box-sizing: border-box;
  top: 0.3rem;
}

.cententTop {
  position: relative;
  width: 100%;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.cententTop .up {
  width: 6.5rem;
  height: 6.5rem;
}

.cententTop .down {
  position: absolute;
  width: 5rem;
  top: 2.1rem;
  left: calc(50% -2.5rem);
}

.cententTop .time {
  position: absolute;
  width: 2.1rem;
  height: 0.7rem;
  bottom: 0;
}

.rabbit {
  position: relative;
  width: 100%;
  /* top: 7rem; */
  display: flex;
  align-items: center;
  justify-content: center;
}

.rabbit .rabbitImg {
  width: 4rem;
  transform: rotateY(180deg);
}

.rabbit .wearetoImg {
  width: 2.5rem;
  position: absolute;
  right: 1rem;
  top: 0;
}

.buttonsOur {
  position: relative;
  /* top: 7rem; */
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.buttonsOur .buttonsCenter {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.buttonsOur .buttonsCenter img {
  width: 3.5rem;
}

/* .buttonsOur .buttonsCenter img:first-child {
  position: relative;
  left: 1.2rem;
}

.buttonsOur .buttonsCenter img:last-child {
  position: relative;
  right: 1.2rem;
} */

.luckDraw {
  margin: 0.2rem;
  width: 6rem;
}

.bottomImg {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  top: -0.2rem;
}

.bottomImg .bottomImgs {
  width: 6.5rem;
}
</style>
