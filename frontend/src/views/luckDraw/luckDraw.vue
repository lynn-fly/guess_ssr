<template>
  <div class="mainOut">
    <div class="luckDraw" :style="{ height: mainHeight + 'px' }">
      <img
        class="background"
        id="background"
        v-show="false"
        src="../../assets/home/background.png"
        alt=""
        srcset=""
      />
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <img class="theme" src="@/assets/luckDraw/title.png" alt="" srcset="" />
      </div>
      <img class="themes" src="@/assets/luckDraw/msg.png" alt="" srcset="" />
      <div class="centent">
        <div
          class="cententOnce"
          :class="[chouseIndex == index ? 'avtive' : '']"
          v-for="(item, index) in imgData"
          :key="index" 
        >
          <img
            class="imgs"
            :style="{ height: imgHeight + 'px' }"
            :src="item.icon"
            alt=""
            srcset=""
          />
          <div class="label">{{ item.name }}</div>
        </div>
      </div>
      <div class="butBom">
        <img src="@/assets/luckDraw/begin.png" @click="beginChouse2" alt="" srcset="" />
        <img src="@/assets/luckDraw/yue.png" alt="" srcset="" />
      </div>
    </div>
    <Popup :popupData="result" :visible="popupVisible" @close="close" />
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";
import Popup from "@/components/popup.vue";
import Buttons from "@/components/home/buttons.vue";

import { mapGetters } from "vuex";
export default {
  components: {
    Buttons,
    Popup,
  },
  data() {
    return {
      name: "返回首页",
      chouseIndex: 0,
      state: false,
      drawing: false,
      imgData: [
        {
          icon: require("@/assets/luckDraw/111.png"),
          name: "AVATR户外桌椅-灰",
        },
        {
          icon: require("@/assets/luckDraw/222.png"),
          name: "AVATR定制保温杯",
        },
        {
          icon: require("@/assets/luckDraw/333.png"),
          name: "AVATR城市画展系列T恤衫",
        },
        {
          icon: require("@/assets/luckDraw/444.png"),
          name: "AVATR户外折叠整理箱-灰",
        },
        {
          icon: require("@/assets/luckDraw/555.png"),
          name: "AVATR户外超声波防潮野餐地垫-灰",
        },
        {
          icon: require("@/assets/luckDraw/666.png"),
          name: "AVATR环保束口包",
        },
        {
          icon: require("@/assets/luckDraw/777.png"),
          name: "AVATR精品帆布包",
        },
        {
          icon: require("@/assets/luckDraw/888.png"),
          name: "AVATR杜邦电脑包",
        },
        {
          icon: require("@/assets/luckDraw/e1.png"),
          name: "E值",
        },
      ],
      imgDataRseult: [
        {
          icon: require("@/assets/luckDraw/result/1/1.png"),
          name: "AVATR户外桌椅-灰",
        },
        {
          icon: require("@/assets/luckDraw/result/1/2.png"),
          name: "AVATR定制保温杯",
        },
        {
          icon: require("@/assets/luckDraw/result/1/3.png"),
          name: "AVATR城市画展系列T恤衫",
        },
        {
          icon: require("@/assets/luckDraw/result/1/4.png"),
          name: "AVATR户外折叠整理箱-灰",
        },
        {
          icon: require("@/assets/luckDraw/result/1/5.png"),
          name: "AVATR户外超声波防潮野餐地垫-灰",
        },
        {
          icon: require("@/assets/luckDraw/result/1/6.png"),
          name: "AVATR环保束口包",
        },
        {
          icon: require("@/assets/luckDraw/result/1/7.png"),
          name: "AVATR精品帆布包",
        },
        {
          icon: require("@/assets/luckDraw/result/1/8.png"),
          name: "AVATR杜邦电脑包",
        },
        {
          icon: require("@/assets/luckDraw/result/1/9.png"),
          name: "E值",
        },
      ],
      imgHeight: "auto",
      mainHeight: 600,
      probability: [
        [1, 50, 9],
        [50, 60, 8],
        [60, 70, 7],
        [70, 80, 6],
        [80, 90, 5],
        [90, 95, 4],
        [95, 98, 3],
        [98, 99, 2],
        [99, 100, 1],
        [100, 101, 0],
      ],
      popupVisible: false,
      wz: require("@/assets/luckDraw/result/wz1.png"),
      zj: require("@/assets/luckDraw/result/zj1.png"),
      wzMain: require("@/assets/luckDraw/result/wz2.png"),
      result: {
        type: "luckDraw",
        icon: "",
        name: "",
        button: [
          {
            icon: "",
            value: "首页",
          },
        ],
      },
    };
  },
  mounted() {
    let imgs = document.getElementsByClassName("imgs");
    let imgw = imgs[0];
    imgw.onload = () => {
      this.imgHeight = imgw.clientWidth;
    };
    this.changeSIze();
    // setTimeout(() => {
    // this.beginChouse();
    // }, 2000);
    this.$store
      .dispatch("user/getInfo")
      .then((data) => {})
      .catch((err) => {});
  },
  computed: {
    ...mapGetters(["userInfor"]),
  },
  methods: {
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
    back(val) {
      if (this.drawing) return;
      if (val == "返回首页") {
        gotopPage("/home");
      }
    },
    async sleep(delay = 1000) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve();
        }, delay);
      });
    },

    async beginChouse2() {

      if (this.userInfor.lotteryCount < 1) {
        alert("抽奖次数已用完~(The number of lucky draws has been used up^_^)");
        return;
      }

      if (this.state || this.drawing) {
        alert("奖品正在路上，祝君好运~");
        return;
      }

      
      
      this.state = true;
      this.drawing = true;
      try {
        const data = await this.$store.dispatch("user/luckyDraw");
        const { lotteryNumber, lotteryCount, heartValue } = data;
        // this.$store.commit("user/SET_HEARTVALUE", heartValue);
        // this.$store.commit("user/SET_LOTTERY_COUNT", lotteryCount);
        let num = lotteryNumber < 1 ? 9 : lotteryNumber - 1;
        let nowNum = 0;
        let draw = true;
        while (draw) {
          await this.sleep(nowNum * 10);
          nowNum++;
          this.addIndex();
          if (nowNum > 30 && this.chouseIndex == num) {
            this.state = lotteryCount < 1;
            this.drawing = false;
            this.chouseIndex = num;
            console.log("中奖：", num);
            draw = false;
            this.$store.commit("audio/play", "lucky");
            this.getResult(num);
          } else if (nowNum > 30 && num == 9) {
            this.state = lotteryCount < 1;
            this.drawing = false;
            console.log("未中奖：", num);
            this.chouseIndex = num;
            draw = false;
            this.getResult(num);
          }
        }
      } catch (err) {
        this.drawing = false;
        console.log(err);
        let msg = "抽奖失败!";
        if (err && err.response && err.response.data && err.response.data.detail) {
          msg += err.response.data.detail;
        }
        alert(msg);
        gotopPage("/home");
      }
    },

    addIndex() {
      if (this.chouseIndex >= 8) {
        this.chouseIndex = 0;
      } else {
        this.chouseIndex++;
      }
    },
    getResult(num) {
      let icon = this.zj;
      let main = this.wzMain;
      let name = "";
      if (num == 9) {
        icon = this.wz;
      } else {
        main = this.imgData[num].icon;
        name = this.imgData[num].name;
      }
      main = this.imgDataRseult[num].icon;
      console.log(main);
      this.result.button[0].icon = icon;
      this.result.icon = main;
      this.result.name = name;
      console.log(this.result);
      this.popupVisible = true;
    },
    close(val) {
      if (val == "关闭") {
        this.popupVisible = false;
      } else {
        gotopPage("/home");
      }
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
  background-image: url(../../assets/luckDraw/bj.jpg);
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
  width: 6rem;
  margin-bottom: 0.5rem;
}

.centent {
  margin: 0 auto;
  width: 95%;
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-bottom: 0.7rem;
  flex-wrap: wrap;
}

.centent .cententOnce {
  width: 33%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-bottom: 0.2rem;
}

.centent .cententOnce .imgs {
  width: 90%;
}

.centent .cententOnce .label {
  width: 100%;
  height: 0.8rem;
  color: #fff;
  text-align: center;
  font-size: 0.2rem;
  margin-top: 0.2rem;
}

.centent .cententOnce.avtive .imgs {
  box-shadow: 0 0 6px 6px #f323ca;
}

.butBom {
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.butBom img {
  margin-bottom: 0.7rem;
  width: 60%;
}
</style>
