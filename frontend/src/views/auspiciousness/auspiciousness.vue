<template>
  <div class="mainOut">
    <div class="luckDraw" :style="{ height: mainHeight + 'px' }">
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <LampNumber :num="startNum" />
      </div>
      <img class="background" id="background" v-show="false" src="../../assets/home/background.png" alt="" srcset="" />
      <img class="themes" src="@/assets/luckDraw/msg.png" alt="" srcset="">
      <div class="centent">
        <div class="cententOnce" :class="[chouseIndex == index ? 'avtive' : '']" v-for="(item, index) in imgData">
          <img class="imgs" :style="{ height: imgHeight + 'px' }" :src="item.icon" alt="" srcset="">
          <div class="label">{{ item.name }}</div>
        </div>
      </div>
      <div class="butBom">
        <img src="@/assets/luckDraw/begin.png" @click="beginChouse" alt="" srcset="">
        <img src="@/assets/luckDraw/yue.png" alt="" srcset="">
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
    Buttons, LampNumber
  },
  data() {
    return {
      name: '返回首页',
      chouseIndex: 0,
      state: false,
      startNum: 50,
      imgData: [
        {
          icon: require('@/assets/luckDraw/1.png'),
          name: '户外桌椅-灰'
        },
        {
          icon: require('@/assets/luckDraw/2.png'),
          name: '阿峰塔定制保温杯'
        }, {
          icon: require('@/assets/luckDraw/3.png'),
          name: '城市画展系列T恤衫-XL '
        }, {
          icon: require('@/assets/luckDraw/4.png'),
          name: '户外超声波防潮野餐地垫-灰'
        }, {
          icon: require('@/assets/luckDraw/5.png'),
          name: '户外折叠整理箱-灰'
        }, {
          icon: require('@/assets/luckDraw/6.png'),
          name: 'AVATR环保東口包'
        }, {
          icon: require('@/assets/luckDraw/7.png'),
          name: 'AVATR精品帆布包(含定制徽章)'
        }, {
          icon: require('@/assets/luckDraw/8.png'),
          name: '杜邦电脑包'
        }, {
          icon: require('@/assets/luckDraw/E66.png'),
          name: 'E值-66'
        }
      ],
      imgHeight: 'auto',
      mainHeight: 600,
      probability: [
        [1, 50],
        [50, 60],
        [60, 70],
        [70, 80],
        [80, 90],
        [90, 95],
        [95, 98],
        [98, 99],
        [99, 101]
      ]
    }
  },
  mounted() {
    let imgs = document.getElementsByClassName('imgs');
    let imgw = imgs[0];
    imgw.onload = () => {
      this.imgHeight = imgw.clientWidth
    }
    this.changeSIze()
    // setTimeout(() => {
    //   this.beginChouse()
    // }, 2000);
  },
  methods: {
    changeSIze() {
      let backDom = document.getElementById('background')
      let that = this;
      backDom.onload = function () {
        let ph = window.screen.height, pw = window.screen.width, scale = this.height / this.width;
        // console.log(this.width, pw, this.height, ph, scale)
        let lastHeight = scale * pw
        console.log(lastHeight)
        that.mainHeight = ph > lastHeight ? ph : lastHeight;
      }
    },
    back(val) {
      if (val == '返回首页') {
        gotopPage("/");
      }
    },
    beginChouse() {
      // if (this.state) return
      this.state = true;
      let nums = parseInt(Math.random() * 100 + 1), num = 8;

      for (let k in this.probability) {
        if (nums >= this.probability[k][0] && nums < this.probability[k][1]) {
          num = k
        }
      }
      console.log(nums, num)
      let nowNum = 0;
      let doit = () => {
        setTimeout(() => {
          nowNum++
          this.addIndex()
          if (nowNum > 30 && this.chouseIndex == num) {
            this.state = false;
            this.chouseIndex = num
            console.log(num + 1)

            return
          } else {
            doit()
          }
        }, nowNum * 10);
      }
      doit()
    },
    addIndex() {
      if (this.chouseIndex == 8) {
        this.chouseIndex = 0
      } else {
        this.chouseIndex++
      }
    }
  }
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
  box-shadow: 0 0 6px 6px #f323ca
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
