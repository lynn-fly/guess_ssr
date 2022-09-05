<template>
  <div class="mainOut">
    <div class="luckDraw" :style="{ height: mainHeight + 'px' }">
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <LampNumber :num="startNum" />
      </div>
      <img
        class="background"
        id="background"
        v-show="false"
        src="../../assets/guess/bj.jpg"
        alt=""
        srcset=""
      />
      <img class="themes" src="@/assets/guess/msg.png" alt="" srcset="" />
      <img class="themes1" src="@/assets/guess/back.png" alt="" srcset="" />
      <div class="centent" :style="{ height: contentHeight + 'px' }">
        <div class="cententOnce" v-for="(item, index) in imgData">
          <img
            class="imgs"
            :style="{ height: imgHeight + 'px' }"
            :src="item.icon"
            alt=""
            srcset=""
            @click="openAnwser(index)"
          />
          <div class="label">{{ index + 1 }}</div>
        </div>
      </div>
      <img class="down" src="@/assets/guess/down.png" alt="" srcset="" />
    </div>
    <Popup :popupData="resultData" :visible="popupVisible" @close="close"> </Popup>
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";
import LampNumber from "@/components/home/lampNumber.vue";
import Buttons from "@/components/home/buttons.vue";
import Popup from "@/components/popup.vue";
import subject from "./subject.js";
export default {
  components: {
    Buttons,
    LampNumber,
    Popup,
  },
  data() {
    return {
      name: "返回首页",
      startNum: 50,
      imgData: [
        {
          icon: require("@/assets/guess/once.png"),
        },
      ],
      imgHeight: "auto",
      mainHeight: 600,
      contentHeight: "auto",
      popupVisible: false,
      resultData: {},
      result: {
        answer: {
          icon: require("@/assets/guess/result/dd2.png"),
          button: [
            {
              icon: require("@/assets/guess/result/dd1.png"),
              value: "答对",
            },
          ],
        },
        incorrectly: {
          icon: require("@/assets/guess/result/dc2.png"),
          button: [
            {
              icon: require("@/assets/guess/result/dc1.png"),
              value: "答错",
            },
          ],
        },
        Accept: {
          icon: require("@/assets/guess/result/jq3.png"),
          button: [
            {
              icon: require("@/assets/guess/result/jq2.png"),
              value: "立即",
            },
            {
              icon: require("@/assets/guess/result/jq1.png"),
              value: "继续",
            },
          ],
        },
        answering: {
          icon: require("@/assets/guess/dt/dtbj.png"),
          type: "answering",
          subject: {},
        },
      },
    };
  },
  mounted() {
    let imgs = document.getElementsByClassName("imgs");
    let imgw = imgs[0];
    imgw.onload = () => {
      this.imgHeight = imgw.clientWidth / 2.5;
    };

    this.changeSIze();
    for (let i = 0; i < 29; i++) {
      this.imgData.push(this.imgData[0]);
    }
  },
  methods: {
    close(val) {
      console.log(val);
      let close = ["关闭", "答对", "答错", "继续"];
      if (close.includes(val)) {
        this.popupVisible = false;
      } else if (val == "立即") {
        gotopPage("/luckDraw");
      }
      this.resultData = {};
    },
    addTopHeight(arr) {
      let top = 0;
      for (let a in arr) {
        let dom = document.getElementsByClassName(arr[a])[0];
        top += dom.offsetTop;
        console.log(dom.offsetTop, arr[a]);
      }
      return top;
    },
    changeSIze(fn) {
      let backDom = document.getElementById("background");
      let that = this;
      backDom.onload = function () {
        let ph = window.screen.height,
          pw = window.screen.width,
          scale = this.height / this.width;
        // console.log(this.width, pw, this.height, ph, scale)
        let lastHeight = scale * pw;
        that.mainHeight = ph > lastHeight ? ph : lastHeight;
        if (fn) {
          fn(that.mainHeight);
        }
      };
    },
    back(val) {
      if (val == "返回首页") {
        gotopPage("/home");
      }
    },
    openAnwser(i) {
      //答题
      this.popupVisible = true;
      this.resultData = this.result.answering;
      console.log(subject[i]);
      this.resultData.subject = subject[i];
    },
  },
};
</script>

<style scoped>
.background {
  position: fixed;
  left: 0;
  top: 0;
  /* width: 100vw; */
  /* height: 100vh; */
  z-index: 1;
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

.luckDraw {
  background-color: black;
  padding: 0 0.5rem;
  /* position: fixed; */
  /* top: 0; */
  /* left: 0; */
  width: calc(100vw - 1rem);
  background-image: url(../../assets/guess/bj.jpg);
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.top {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.7rem;
  padding-top: 0.5rem;
}

.top .theme {
  width: 5rem;
}

.themes {
  width: 7.8rem;
  margin-bottom: 0.5rem;
}

.themes1 {
  position: absolute;
  right: 1.3rem;
  top: 0rem;
  width: 2rem;
}

.upImg {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.upImg .upImgs {
  width: 80%;
  margin: 0.3rem auto 0.5rem;
}

.upImg .upImgs2 {
  width: 60%;
  margin: 0.3rem auto 0.5rem;
}

.upImg .upInput {
  padding: 0.15rem;
  width: calc(80% - 0.3rem);
  box-shadow: 0 0 6px 3px #f323ca;
  border-radius: 0.15rem;
}

.centent {
  margin: 0 auto;
  width: 95%;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 0.7rem;
  flex-wrap: wrap;
  position: relative;
  overflow-y: auto;
  overflow-x: hidden;
}

.centent .cententOnce {
  width: 48%;
  margin-left: 1.5%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-bottom: 0.4rem;
  position: relative;
}

.centent .cententOnce .imgs {
  width: 90%;
}

.centent .cententOnce .label {
  position: absolute;
  right: 1rem;
  top: 0.33rem;
  color: #e1e327;
  text-align: center;
  font-size: 0.4rem;
  margin-top: 0.2rem;
}
.down {
  width: 70%;
  margin-left: 15%;
}
</style>
