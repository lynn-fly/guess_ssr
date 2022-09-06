<template>
  <div class="mainOut">
    <!-- :style="{ height: mainHeight + 'px' }" -->
    <div class="luckDraw">
      <div class="top">
        <Buttons :msg="name" @back="back" />
        <LampNumber :num="userInfor.heartValue" />
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
      <div class="upImg" v-if="!this.userInfor.isUpload">
        <img
          class="upImgs"
          @click="upImg"
          src="@/assets/auspiciousness/upDown.png"
          alt=""
          srcset=""
        />
      </div>
      <div class="upImg" v-if="!this.userInfor.isUpload">
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
        <div class="cententOnce" v-for="(item, index) in imgData" :key="index">
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
            {{ item.thumbed.split(",").length - 1 }}
          </div>
        </div>
      </div>
      <div class="buttonDowns">
        <div class="buttonDown" @click="changeLists">换一批</div>
      </div>
    </div>
    <Popup :popupData="resultData" :visible="popupVisible" @close="close">
      <!-- @rightChoose="rightChoose"
      @wrongChoose="wrongChoose" -->
    </Popup>
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";
import { getUser } from "@/utils/auth";
import LampNumber from "@/components/home/lampNumber.vue";
import Buttons from "@/components/home/buttons.vue";
import { upFile, getupload_list, setsave_thumbed } from "@/api/auspiciousness";
import Popup from "@/components/popup.vue";
import { mapGetters } from "vuex";
export default {
  components: {
    Buttons,
    LampNumber,
    Popup,
  },
  data() {
    return {
      name: "返回首页",
      state: false,
      startNum: 50,
      imgData: [],
      imgHeight: "auto",
      mainHeight: 800,
      contentHeight: "auto",
      textUp: "",
      isUploaded: false,
      popupVisible: false,
      resultData: {},
      result: {
        success: {
          icon: require("@/assets/auspiciousness/result/cg2.png"),
          button: [
            {
              icon: require("@/assets/auspiciousness/result/cg1.png"),
              value: "成功",
            },
          ],
        },
        error: {
          icon: require("@/assets/auspiciousness/result/sb2.png"),
          button: [
            {
              icon: require("@/assets/auspiciousness/result/sb1.png"),
              value: "失败",
            },
          ],
        },
        luck: {
          icon: require("@/assets/auspiciousness/result/cj2.png"),
          button: [
            {
              icon: require("@/assets/auspiciousness/result/cj1.png"),
              value: "抽奖",
            },
          ],
        },
      },
    };
  },
  mounted() {
    let imgs = document.getElementsByClassName("imgs");
    let imgw = imgs[0];
    if (imgw) {
      imgw.onload = () => {
        this.imgHeight = imgw.clientWidth / 1.8;
      };
    }
    this.getList(true);
    console.log("userinfo:", this.userInfor);
    this.isUploaded = this.userInfor.isUpload;
  },
  computed: {
    ...mapGetters(["userInfor"]),
  },
  methods: {
    getList(isFirst) {
      this.imgData = [];
      let d = false;
      if (isFirst) {
        d = true;
      }
      getupload_list(d).then((res) => {
        const { config, data } = res;
        const { baseURL } = config;
        for (let k in data) {
          this.imgData.push({
            //icon: "http://129.226.227.171" + data[k].upload_file_url,
            icon: baseURL.substring(0, baseURL.length - 7) + data[k].upload_file_url,
            name: data[k].upload_comment,
            ...data[k],
          });
        }
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
    upImg() {
      if (this.userInfor.isUpload) {
        // if(this.isUploaded) {
        alert("你已经祈福过啦，请看看其他人的祝福吧！");
        return;
      }
      if (!this.textUp) {
        alert("需要先填写祝福语");
        return;
      }

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
      let size = this.getfilesize(files[0].size);
      let type = ["jpeg", "jpg", "png", "image/png", "image/jpg", "image/jpeg"];
      if (!type.includes(files[0].type)) {
        alert("图片格式为jpeg,jpg,png");
        return;
      }
      if (size[1] == "MB") {
        alert("图片需要小于5M");
        if (+size[0] >= 5) return;
      }
      let d = {
        upload_file: files[0],
        comment: this.textUp,
      };
      upFile(d)
        .then((res) => {
          console.log(res);
          if (res.status == 201) {
            this.textUp = "";
            this.getList();
            this.isUploaded = true;
            this.$store.commit("user/SET_IS_UPLOAD", true);
            this.$store.commit("user/SET_HEARTVALUE", res.data.heartValue);
            this.$store.commit("user/SET_LOTTERY_COUNT", res.data.lotteryCount);
          }
          this.openPopup("luck");
        })
        .catch((error) => {
          this.openPopup("error");
          // alert("图片上传失败,请联系管理员");
        });
    },
    openPopup(num) {
      this.resultData = {};
      this.resultData = this.result[num];
      console.log(this.result[num], "1111111111111");
      setTimeout(() => {
        this.popupVisible = true;
      }, 200);
    },
    upClick(item, index) {
      debugger
      // console.log(tiem, index, this.userInfor.userId);
      var thumbedList = item.thumbed.split(',');
      for (let k in thumbedList) {
        if (thumbedList[k] == this.userInfor.userId) {
          alert("不可重复点赞");
          return;
        }
      }
      setsave_thumbed(this.userInfor.userId)
        .then((res) => {
          console.log(res);
          this.getList();
        })
        .catch((error) => {
          alert("点赞失败,请联系管理员");
          this.getList();
        });
    },
    close(item) {
      console.log(item);
      if (item == "关闭") {
        this.popupVisible = false;
      }
    },
    getfilesize(size) {
      //把字节转换成正常文件大小
      if (!size) return "";
      var num = 1024.0; //byte
      let n = 0,
        type = "";
      if (size < num) {
        n = size;
        type = "B";
        return [n, type];
      }
      if (size < Math.pow(num, 2)) {
        n = (size / num).toFixed(2);
        type = "KB";
        return [n, type];
      }
      // if (size < Math.pow(num, 3)) {
      n = (size / Math.pow(num, 2)).toFixed(2);
      type = "MB";
      return [n, type];
      // }
      // if (size < Math.pow(num, 4)) {
      //   n = (size / Math.pow(num, 3)).toFixed(2);
      //   type = "GB";
      //   return [n, type];
      // }
      // n = (size / Math.pow(num, 4)).toFixed(2);
      // type = "TB";
      return [n, type];
    },
    changeLists() {
      this.getList(false);
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
  padding-bottom: 0.7rem;
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
.buttonDowns {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 0.5rem;
}
</style>
