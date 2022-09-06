<template>
  <div class="mainOut">
    <div class="luckDraw" :style="{ height: mainHeight + 'px' }">
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <LampNumber :num="userInfor.heartValue" />
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
      <div class="themes1">
        <img class="t1" src="@/assets/v2/dm/d1.png" alt="" srcset="" />
        <img class="t2" src="@/assets/v2/dm/d2.png" alt="" srcset="" />
        <img class="h1" src="@/assets/v2/dm/h1.png" alt="" srcset="" />
        <img class="h2" src="@/assets/v2/dm/h2.png" alt="" srcset="" />
        <img class="h3" src="@/assets/v2/dm/h1.png" alt="" srcset="" />
        <img class="h4" src="@/assets/v2/dm/h2.png" alt="" srcset="" />
      </div>
      <div class="centent" :style="{ height: contentHeight + 'px' }">
        <div
          class="cententOnce"
          @click="openAnwser(index)"
          v-for="(item, index) in subObj"
          :key="index"
        >
          <img
            class="imgs"
            :style="{
              height: imgHeight + 'px',
              animation: 'fade ' + getMath(item.notDo),
            }"
            :src="item.icon"
            :class="[item.notDo ? 'notDo' : '']"
            alt=""
            srcset=""
          />
          <div class="label">{{ index + 1 }}</div>
        </div>
      </div>
      <img class="down" src="@/assets/guess/down.png" alt="" srcset="" />
    </div>
    <Popup
      :popupData="resultData"
      :visible="popupVisible"
      @close="close"
      @rightChoose="rightChoose"
      @wrongChoose="wrongChoose"
    >
    </Popup>
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";
import LampNumber from "@/components/home/lampNumber.vue";
import Buttons from "@/components/home/buttons.vue";
import Popup from "@/components/popup.vue";
import subject from "./subject.js";
import { mapGetters } from "vuex";
import { setsave_answer } from "@/api/guess";

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
      subObj: [],
    };
  },
  mounted() {
    this.subObj = this.shuffle(subject);
    for (let k in this.subObj) {
      var did = false;
      if (this.userInfor.answeredIds.indexOf(this.subObj[k].number + "") > -1) {
        did = true;
      }
      this.subObj[k] = {
        ...this.subObj[k],
        i: ++k,
        notDo: did,
        icon: require("@/assets/guess/once.png"),
      };
    }

    // let imgs = document.getElementsByClassName("imgs");
    // let imgw = imgs[0];
    // imgw.onload = () => {
    //   this.imgHeight = imgw.clientWidth / 2.5;
    // };
    this.find((imgw) => {
      imgw.onload = () => {
        this.imgHeight = imgw.clientWidth / 2.5;
      };
    });

    this.changeSIze();
    for (let i = 0; i < 29; i++) {
      this.imgData.push(this.imgData[0]);
    }
  },
  computed: {
    ...mapGetters(["userInfor"]),
  },
  methods: {
    find(fn) {
      let imgs = document.getElementsByClassName("imgs");
      let imgw = imgs[0];
      if (!imgw) {
        setTimeout(() => {
          this.find(fn);
        }, 200);
      } else {
        fn(imgw);
      }
    },
    getMath(val) {
      if (val) return 1111111111111111;
      return Math.random() * 500 + 800 + "ms infinite";
    },
    shuffle(arr) {
      for (let i = 0; i < arr.length; i++) {
        const randomIndex = Math.round(Math.random() * (arr.length - 1 - i)) + i;
        [arr[i], arr[randomIndex]] = [arr[randomIndex], arr[i]];
      }
      return arr;
    },
    close(val) {
      this.popupVisible = false;
      var subjectIndex = -1;
      if (val.indexOf("-") > -1) {
        subjectIndex = parseInt(val.split("-")[1]);
        val = val.split("-")[0];
      }
      let close = ["关闭", "答对", "答错", "继续"];
      if (close.includes(val)) {
        this.resultData = {};
        //this.popupVisible = false;
        console.log(val, subjectIndex, "4444444");
        if (val == "答对") {
          this.openAnwser(subjectIndex + 1);
        } else if (val == "答错") {
          this.openAnwser(subjectIndex);
        } else if (val == "继续") {
          this.openAnwser(subjectIndex + 1);
        }
      } else if (val == "立即") {
        this.resultData = {};
        gotopPage("/luckDraw");
      } else {
        this.resultData = {};
      }
    },
    rightChoose(val) {
      this.popupVisible = false;
      this.$nextTick(() => {
        setsave_answer(val, 1)
          .then((res) => {
            debugger;
            //更新list
            this.$store.commit("user/SET_ANSWERED_IDS", res.data.answeredIds);
            var currentItem = this.subObj.find((x) => x.number == val);
            currentItem.notDo = true;
            var nextIndex = currentItem.i;
            for (var startIndex = nextIndex; startIndex < 30; startIndex++) {
              var nextItem = this.subObj.find((x) => x.i == startIndex);
              if (!nextItem.notDo) {
                nextIndex = startIndex;
              }
            }

            if (this.userInfor.isAnswerMax) {
              //直接继续答题
              this.resultData = {};
              this.resultData = this.result.answer;
              this.resultData.subject = this.subObj[nextIndex];
              this.popupVisible = true;
            } else {
              if (res.data.answerId.length == 6) {
                this.resultData = {};
                this.resultData = this.result.Accept;
                this.resultData.subject = this.subObj[nextIndex];
                this.$store.commit("user/SET_HEART_IS_MAX", true);
                this.$store.commit("user/SET_LOTTERY_COUNT", res.data.lotteryCount);
                this.popupVisible = true;
              } else {
                this.resultData = {};
                this.resultData = this.result.answer;
                this.resultData.subject = this.subObj[nextIndex];
                this.popupVisible = true;
              }
            }
            this.$store.commit("user/SET_HEARTVALUE", res.data.heartValue);
          })
          .catch((error) => {});
      });
    },
    wrongChoose(val) {
      this.popupVisible = false;
      this.$nextTick(() => {
        setsave_answer(val, 0)
          .then((res) => {
            this.resultData = {};
            this.popupVisible = true;
            this.resultData = this.result.incorrectly;
            this.resultData.subject = subject[val - 1];
          })
          .catch((erro) => {});
      });
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
    openAnwser(index) {
      //已经答过了就不答了
      var currentItem = this.subObj.find((x) => x.i == index + 1);
      if (currentItem.notDo) {
        return;
      }

      this.popupVisible = true;
      this.resultData = this.result.answering;
      console.log(subject[index]);
      this.resultData.subject = subject[index];
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
  right: 1rem;
  top: 0rem;
  width: 2rem;
}
.themes1 .t1 {
  z-index: 20;
  position: relative;
  width: 75%;
}
.themes1 .t2 {
  position: absolute;
  left: -0.7rem;
  width: 1.2rem;
}
.h1,
.h2,
.h3,
.h4 {
  width: 80%;
  position: absolute;
  z-index: 10;
  width: 0.8rem;
}
.h2 {
  top: 1.1rem;
  right: 2rem;
  animation: movesR100 9000ms infinite;
  -webkit-animation: movesR100 9000ms infinite;
}
.h4 {
  top: 4rem;
  animation: movesL100 11000ms infinite;
  -webkit-animation: movesL100 11000ms infinite;
}
.h3 {
  width: 0.8rem;
  top: 3rem;
  right: 1.5rem;
  animation: movesR50 7000ms infinite;
  -webkit-animation: movesR50 7000ms infinite;
}
.h1 {
  width: 0.8rem;
  top: 1.8rem;
  right: 0.2rem;
  animation: movesL50 10000ms infinite;
  -webkit-animation: movesL50 10000ms infinite;
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
  /* animation: fade 600ms infinite;
  -webkit-animation: fade 600ms infinite; */
}
.notDo {
  opacity: 0.5 !important;
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
