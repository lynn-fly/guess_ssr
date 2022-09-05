<template>
  <div class="mainOut">
    <!-- :style="{ height: mainHeight + 'px' }" -->
    <div class="luckDraw">
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <LampNumber :num="startNum" />
      </div>
      <img
        class="background"
        id="background"
        v-show="false"
        src="../../assets/auspiciousness/bj.jpg"
        alt=""
        srcset=""
      />
      <img class="themes" src="@/assets/auspiciousness/msg.png" alt="" srcset="" />
      <img class="themes1" src="@/assets/auspiciousness/back.png" alt="" srcset="" />
      <div class="upImg">
        <img
          class="upImgs"
          @click="upImg"
          src="@/assets/auspiciousness/upDown.png"
          alt=""
          srcset=""
        />
      </div>
      <div class="upImg">
        <input
          class="upInput"
          v-model="textUp"
          type="text"
          placeholder="在这里写下你的祝福，100字以内"
        />
      </div>
      <div class="upImg">
        <img class="upImgs2" src="@/assets/auspiciousness/ty.png" alt="" srcset="" />
      </div>
      <div class="centent" :style="{ height: contentHeight + 'px' }">
        <div class="cententOnce" v-for="(item, index) in imgData">
          <img
            class="imgs"
            :style="{ height: imgHeight + 'px' }"
            :src="item.icon"
            alt=""
            srcset=""
          />
          <div class="label">{{ item.name }}</div>
          <div classs="uppppp" style="width: 100% !important; color: #fff">
            <img
              src="@/assets/auspiciousness/up.png"
              alt=""
              @click="upClick(item, index)"
            />
            {{ item.numUp }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";
import LampNumber from "@/components/home/lampNumber.vue";
import Buttons from "@/components/home/buttons.vue";
export default {
  components: {
    Buttons,
    LampNumber,
  },
  data() {
    return {
      name: "返回首页",
      state: false,
      startNum: 50,
      imgData: [
        {
          icon: require("@/assets/luckDraw/1.png"),
          name: "户外桌椅-灰",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/2.png"),
          name: "阿峰塔定制保温杯",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/3.png"),
          name: "城市画展系列T恤衫-XL ",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/4.png"),
          name: "户外超声波防潮野餐地垫-灰",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/5.png"),
          name: "户外折叠整理箱-灰",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/6.png"),
          name: "AVATR环保東口包",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/7.png"),
          name: "AVATR精品帆布包(含定制徽章)",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/8.png"),
          name: "杜邦电脑包",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/E66.png"),
          name: "E值-66",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/7.png"),
          name: "AVATR精品帆布包(含定制徽章)",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/8.png"),
          name: "杜邦电脑包",
          numUp: 200,
        },
        {
          icon: require("@/assets/luckDraw/E66.png"),
          name: "E值-66",
          numUp: 200,
        },
      ],
      imgHeight: "auto",
      mainHeight: 800,
      contentHeight: "auto",
      textUp: "",
    };
  },
  mounted() {
    let imgs = document.getElementsByClassName("imgs");
    let imgw = imgs[0];
    imgw.onload = () => {
      this.imgHeight = imgw.clientWidth / 1.8;
    };
    // let main = document.getElementsByClassName("mainOut")[0];
    // this.mainHeight = main.clientHeight;
    // this.changeSIze((res) => {
    //   let cententDom = document.getElementsByClassName("centent")[0];
    //   let contentTop = this.addTopHeight(["upImgs2"]);
    //   console.log(res, contentTop, cententDom.clientHeight, res - contentTop - 60);
    //   let lastHeight = res - contentTop - 60;
    //   this.contentHeight =
    //     cententDom.clientHeight > lastHeight ? lastHeight : cententDom.clientHeight;
    // });
  },
  methods: {
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
        gotopPage("/");
      }
    },
    upImg() {
      let that = this;
      function inputUpload() {
        that.upLoad(this.files);
      }
      let input = document.createElement("input");
      input.type = "file";
      input.accept = "image/*";
      input.onchange = inputUpload;
      input.click();
    },
    upLoad(files) {
      console.log(this.files);
    },
    upClick(tiem, index) {
      console.log(tiem, index);
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
  background-image: url(../../assets/auspiciousness/bj.jpg);
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
  right: 0.5rem;
  top: 1.5rem;
  width: 2.6rem;
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
.uppppp {
  width: 100% !important;
}
</style>
