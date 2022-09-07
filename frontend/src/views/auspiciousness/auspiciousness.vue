<template>
  <div class="mainOut">
    <!-- :style="{ height: mainHeight + 'px' }" -->
    <div id="useInput" v-show="false"></div>
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
      <div class="upImg">
        
        <img
          class="upImgs"
          @click="upImgs"
          :src="upState ? upImgLogin : upImg"
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
        <div class="cententOnce" v-for="(item, index) in imgData" :key="index">
          <div
            class="cententOnceIn"
            :ref="'cententOnceIn_' + index"
            :style="{ height: imgHeight + 'px !important' }"
          >
            <!-- :style="{ height: imgHeight + 'px !important' }" -->
            <img
              class="imgs cententimgs"
              :ref="'cententimgs_' + index"
              :src="item.icon"
              alt=""
              srcset=""
              @click="openBigIcon(item)"
            />
          </div>

          <!-- <div class="label">{{ item.nick_name }}</div> -->
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
        <!-- <div class="buttonDown" @click="changeLists"></div> -->
        <Buttons :msg="'换一批'" @back="changeLists"></Buttons>
      </div>
    </div>
    <Popup :popupData="resultData" :visible="popupVisible" @close="close">
      <!-- @rightChoose="rightChoose"
      @wrongChoose="wrongChoose" -->
    </Popup>
    <div v-if="seeBigIcon" @click="closeBigIcon" class="seeBigIcon">
      <img class="imgs" :src="seeBigIconSrc" alt="" />
      <div class="msg">
        {{ seeBigIconMsg }}
      </div>
    </div>
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
      imgHeight: "",
      mainHeight: 800,
      contentHeight: "auto",
      textUp: "",
      heartValue: 0,
      isUploaded: false,
      popupVisible: false,
      seeBigIcon: false,
      seeBigIconSrc: "",
      seeBigIconMsg: "",
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
      upState: false,
      upImg: require("@/assets/auspiciousness/upDown.png"),
      upImgLogin: require("@/assets/auspiciousness/upDown.png"),
    };
  },
  mounted() {
    // let imgs = document.getElementsByClassName("imgs");
    // let imgw = imgs[0];
    // imgs.then(() => {
    //   console.log(imgs[0], 5555555555);
    // });
    // if (imgw) {
    //   imgw.onload = () => {
    //     this.imgHeight = imgw.clientWidth / 1.8;
    //     console.log(this.imgHeight, 5555555555);
    //   };
    // }
    // this.find((imgw) => {
    //   console.log(imgw.width, 5555555);
    //   this.imgHeight = imgw.width / 1.5;
    //   if (!this.imgHeight) this.imgHeight = 144;
    //   console.log(this.imgHeight, 5555555555);

    //   this.imgData.forEach((val,index,arr)=>{
    //         const imgw2 = this.$refs[`cententimgs_${index}`][0];

    //         if(index > 0 )
    //         {
    //           let h = imgw2.offsetHeight;
    //           console.log(imgw2)
    //           if(h< this.imgHeight) {
    //             imgw2.style.height= this.imgHeight + 'px'
    //           }
    //         }
    //       })
    // });
    this.find((imgs) => {
      let avralH = 0;
      for (let i = 0; i < imgs.length; i++) {
        console.log(imgs[i].width, 44444444444);
        avralH += imgs[i].width / 1.5;
      }

      if (imgs.length > 0) {
        this.imgHeight = avralH / imgs.length;
      }
      if (!this.imgHeight) this.imgHeight = 144;

      console.log(this.imgHeight, 5555555555);

      this.imgData.forEach((val,index,arr)=>{
            const imgw2 = this.$refs[`cententimgs_${index}`][0];    
            
            let h = imgw2.offsetHeight;
            let h2 = imgw2.clientHeight;
            console.log('mounted：',h,h2,this.imgHeight)
            if(  h < this.imgHeight) {
              imgw2.style.height= this.imgHeight + 'px';
              imgw2.style.width= '150%';
            }
              
          })
    });
    this.getList(true);
    this.$store
      .dispatch("user/getInfo")
      .then((data) => {})
      .catch((err) => {});
    console.log("userinfo:-------", this.userInfor);
    //this.isUploaded = this.userInfor.isUpload;
    //this.heartValue = this.userInfor.heartValue;
  },
  computed: {
    ...mapGetters(["userInfor"]),
  },
  methods: {
    find(fn) {
      let imgs = document.getElementsByClassName("cententimgs");
      let imgw = imgs[0];
      let loadAll = true;
      for (let i = 0; i < imgs.length; i++) {
        if (!imgs[i].width) {
          loadAll = false;
          break;
        }
      }
      if (!imgw || !loadAll) {
        setTimeout(() => {
          this.find(fn);
        }, 200);
      } else {
        fn(imgs);
      }
    },

    adjustImgs() {},

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
        this.$nextTick(() => {
                  this.find((imgw) => {     
                    this.imgData.forEach((val,index,arr)=>{
                    const imgw2 = this.$refs[`cententimgs_${index}`][0]; 
                    
                      let h = imgw2.offsetHeight;
                      let h2 = imgw2.clientHeight;
                      console.log('nextTick:',h,h2,this.imgHeight)
                      if( h < this.imgHeight) {
                        imgw2.style.height= this.imgHeight + 'px'
                        imgw2.style.width= '150%'
                      }
                       
                  })
            });   
        })
      });
    },
    // getUrl(url) {
    //   return new URL(url, import.meta.url).href;
    // },
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
      if(this.upState) return;
      if (val == "返回首页") {
        gotopPage("/home");
      }
    },
    upImgs() {
      if(this.upState){
        alert("正在努力接受你的祝福，请稍后……(I am trying to accept your blessing, please hold on...)");
        return;
      }
      // if (this.userInfor.isUpload) {
      //   // if(this.isUploaded) {
      //   alert("你已经祈福过啦，请看看其他人的祝福吧！(You have prayed, please look at the blessings of others!)");
      //   return;
      // }
      if (!this.textUp) {
        alert("需要先填写祝福语！(You need to fill out a message first!)");
        return;
      }
      let inputDom = document.getElementById("useInput");
      let that = this;
      function inputUpload() {
        that.upState = true;
        that.upLoad(this.files);
      }
      let input = document.createElement("input");
      input.type = "file";
      input.accept = "image/*";
      input.onchange = inputUpload;
      input.click();
      inputDom.appendChild(input);
    },
    upLoad(files) {
      let size = this.getfilesize(files[0].size);
      let type = ["jpeg", "jpg", "png", "image/png", "image/jpg", "image/jpeg"];
      if (!type.includes(files[0].type)) {
        this.upState = false;
        alert("图片格式为(The image format is)jpeg,jpg,png");
        
        return;
      }
      if (size[1] == "MB" && +size[0] >= 5) {
        this.upState = false;
        alert("图片需要小于(The image needs to be less than)5M");
        
        return;
      }
      if(this.textUp.length > 100 ) {
        this.upState = false;
        alert("亲，100字足以表达你的真诚的祝福！(Dear, 100 words is enough to express your sincere blessing)");
        
        return;
      }
      let d = {
        upload_file: files[0],
        comment: this.textUp,
      };
      upFile(d)
        .then((res) => {
          console.log("upload data:", res);
          this.upState = false;
          
          this.textUp = "";
          this.getList();
          //this.isUploaded = true;
          //this.$store.commit("user/SET_IS_UPLOAD", true);
          this.$store.commit("user/SET_HEARTVALUE", res.data.heartValue);
          this.$store.commit("user/SET_LOTTERY_COUNT", res.data.lotteryCount);
          if( res.data.isFirst) {
            this.openPopup("luck");
          }
          else {
            alert("你的祝福已经送达！"); //上传完成 
          }
        })
        .catch((error) => {
          this.upState = false;
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
      // console.log(tiem, index, this.userInfor.userId);
      var thumbedList = item.thumbed.split(",");
      for (let k in thumbedList) {
        if (thumbedList[k] == this.userInfor.userId) {
          alert("不可重复点赞");
          return;
        }
      }
      setsave_thumbed(item.id)
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
      } else if (item == "抽奖") {
        gotopPage("/luckDraw");
      } else {
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
    openBigIcon(item) {
      this.seeBigIconSrc = item.icon;
      this.seeBigIconMsg = item.name;
      this.seeBigIcon = true;
    },
    closeBigIcon() {
      this.seeBigIcon = false;
      this.seeBigIconSrc = "";
      this.seeBigIconMsg = "";
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
  min-height: 100%;
  /* min-width: 100vh; */
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
  top: 1.3rem;
  width: 2.6rem;

  animation: fadeLongs 10000ms infinite;
  -webkit-animation: fadeLongs 10000ms infinite;
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
  position: relative;
  overflow: hidden;
}
.centent .cententOnce .cententOnceIn {
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.centent .cententOnce .imgs {
  width: 90%;
}

.centent .cententOnce .label {
  line-height: 0.5rem !important;
  width: 90%;
  text-align: left !important;
  min-height: 1.5rem;
  color: #fff;
  text-align: center;
  font-size: 0.2rem;
  margin-top: 0.2rem;

  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  word-break: break-all;
  letter-spacing: 0.03rem; 
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
  font-size: 0.42rem;
  padding: 0.5rem;
  box-sizing: border-box;
}

.seeBigIcon {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  background-image: url(../../assets/guess/result/mb.png);
  background-size: 100% 100%;
  background-repeat: no-repeat;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.seeBigIcon .imgs {
  max-width: 80%;
  box-shadow: 0 0 10px 3px #f323ca;
  border-radius: 0.4rem;
  margin: 0 auto;
  margin-bottom: 0.8rem;
}
.seeBigIcon .msg {
  font-size: 0.4rem;
  margin-top: 0.8rem;
  max-width: 80%;
  margin: 0 auto;
  word-break: break-all;
}
</style>
