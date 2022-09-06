<template>
  <div class="home">
    <!-- <LampNumber :num="startNum" /> -->
    <img
      class="background"
      id="background"
      v-show="false"
      src="../../assets/home/background.png"
      alt=""
      srcset=""
    />
    <div class="mainOut">
      <div class="main" v-show="true" :style="{ height: mainHeight + 'px' }">
        <div class="top">
          <Buttons :msg="name" :key="name" @back="back" />
          <LampNumber :num="userInfor.heartValue" />
        </div>
        <img
          src="../../assets/home//music.png"
          style="width: 50px; height: 50px"
          class="img"
          :class="[muteBgMusic ? 'pause' : 'start']"
          @click="playMusic"
        />
        <!-- <audio
          style="display: none; height: 0"
          id="bg-music"
          autoplay="autoplay"
          src="http://129.226.227.171/upload/7scmx-u2mhm-4.mp3 "
          loop="loop"
        ></audio> -->
        <div class="cententTop">
          <!-- <img class="up" src="@/assets/home/otherTitle.png" alt="" />
          <img class="down" src="@/assets/home/theme.png" alt="" />
          <img class="time" src="@/assets/home/time.png" alt="" /> -->
          <img class="backs" src="@/assets/home/month.png" alt="" />
          <img class="up" src="@/assets/home/123.png" alt="" />
        </div>
        <div class="rabbit" :class="[onloadRabbit ? 'onloadRabbit' : '']">
          <img class="rabbitImg" src="@/assets/home/rabbit.png" alt="" />
          <img
            class="wearetoImg"
            :class="[onloadRabbitTime ? 'onloadRabbitTime' : '']"
            src="@/assets/home/weareto.png"
            alt=""
          />
        </div>
        <div class="buttonsOur">
          <div class="buttonsCenter">
            <img
              class="guess"
              @click="guess"
              src="@/assets/home/guess.png"
              alt=""
              v-if="userInfor.isLocal"
            />
            <img
              class="auspiciousness"
              @click="auspiciousness"
              src="@/assets/home/auspiciousness.png"
              alt=""
            />
          </div>
          <img
            class="luckDraw"
            @click="luckDraw"
            src="@/assets/home/luckDraw.png"
            alt=""
          />
        </div>
        <div class="bottomImg">
          <img class="bottomImgs" src="@/assets/home/introduce.png" alt="" />
        </div>
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
      mainHeight: 600,
      muteBgMusic: false,
      onloadRabbit: false,
      onloadRabbitTime: false,
    };
  },
  watch: {
    muteBgMusic(newValue, oldValue) {
      if (newValue) {
        // 开启静音
        // var audio = document.getElementById("bg-music");
        this.$store.commit("audio/play", "bj");
        // audio.pause();
      } else {
        // 关闭 静音
        // var audio = document.getElementById("bg-music");
        this.$store.commit("audio/puse", "bj");
        // audio.play();
      }
    },
  },
  mounted() {
    setTimeout(() => {
      this.onloadRabbit = true;
      setTimeout(() => {
        this.onloadRabbitTime = true;
      }, 3500);
    }, 200);
    this.changeSIze();
    const userAgent = window.navigator.userAgent;
    const IS_IN_IOS = !!userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
    const IS_IN_WX = /MicroMessenger/i.test(userAgent);

    if (IS_IN_WX) {
      // 是否微信环境
      if (IS_IN_IOS) {
        // var audio = document.getElementById("bg-music");
        this.$store.commit("audio/play", "bj");
        // audio.play();
      }
    } else {
      // var audio = document.getElementById("bg-music");
      this.$store.commit("audio/play", "bj");
      // audio.play();
    }
  },
  computed: {
    ...mapGetters(["name", "userInfor"]),
  },
  methods: {
    playMusic() {
      this.muteBgMusic = !this.muteBgMusic;
    },
    changeSIze() {
      let backDom = document.getElementById("background");

      let that = this;
      backDom.onload = function () {
        let ph = window.screen.height,
          pw = window.screen.width,
          scale = this.height / this.width;
        // console.log(this.width, pw, this.height, ph, scale)
        let lastHeight = scale * pw;
        console.log(lastHeight);
        that.mainHeight = ph > lastHeight ? ph : lastHeight;
      };
    },
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
    back(val) {
      if (val == "login") {
        gotopPage("/login");
      }
    },
  },
  created() {
    console.log("Home");
    console.log(this.userInfor);
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
  /* width: 100vw; */
  /* height: 100vh; */
  z-index: 1;
}

.main {
  width: 100vw;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
  background-image: url(../../assets/home/background.png);
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.mainOut {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  z-index: 10;
  overflow-x: hidden;
  overflow-y: auto;
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
  margin: 1.2rem;
  width: 6.5rem;
  height: 6.5rem;
  z-index: 10;
}

.cententTop .backs {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 5;
  width: 100%;
}
/* .cententTop .down {
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
} */

.rabbit {
  position: relative;
  width: 180%;
  /* top: 7rem; */
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 3s;
}
.onloadRabbit {
  width: 70%;
  left: 1rem;
  /* justify-content: center; */
}
.onloadRabbitTime {
  opacity: 1 !important;
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
  transition: all 1s;
  opacity: 0;
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

<style scoped>
.img {
  position: fixed !important;
  right: 20px;
  top: 55px;
  z-index: 1000;
}
.start {
  animation: music 10s infinite linear;
}
.pause {
  z-index: 1000;
}
@keyframes music {
  0% {
    transform: rotate(0deg);
  }

  10% {
    transform: rotate(36deg);
  }

  20% {
    transform: rotate(72deg);
  }

  30% {
    transform: rotate(108deg);
  }

  40% {
    transform: rotate(144deg);
  }

  50% {
    transform: rotate(180deg);
  }

  60% {
    transform: rotate(216deg);
  }

  70% {
    transform: rotate(252deg);
  }

  80% {
    transform: rotate(288deg);
  }

  90% {
    transform: rotate(324deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
