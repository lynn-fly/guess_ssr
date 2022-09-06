<template>
  <div class="openPopup" v-if="visible">
    <div
      class="main"
      :class="[
        popupData.type == 'luckDraw'
          ? popupData.name
            ? 'luckDrawPopup'
            : 'luckDrawPopupNot'
          : '',
      ]"
    >
      <img class="popupMain" :src="popupData.icon" alt="" />

      <div v-if="popupData.type == 'luckDraw' && popupData.name">
        <div class="msg">
          <div class="left">恭喜！</div>
          <div class="name">
            {{ popupData.name }}
          </div>
        </div>
        <img
          @click="clicks(item.value, popupData.subject.index)"
          v-for="(item, index) in popupData.button"
          :src="item.icon"
        />
      </div>
      <div class="buttons" v-else-if="popupData.button && popupData.subject">
        <img
          @click="clicks(item.value, popupData.subject.index)"
          v-for="(item, index) in popupData.button"
          :src="item.icon"
        />
      </div>
      <div class="buttons" v-else-if="popupData.button">
        <img
          @click="clicks(item.value)"
          v-for="(item, index) in popupData.button"
          :src="item.icon"
        />
      </div>
      <div class="subject" v-else-if="popupData.subject">
        <div class="land">
          {{ lands }}
          <!-- popupData.subject.number  -->
        </div>
        <div
          v-if="popupData.subject.type != 'image'"
          class="title"
          v-html="popupData.subject.title"
        >
          <!-- {{ popupData.subject.title }} -->
        </div>
        <div v-else class="title">
          <img :src="require('@/assets/guess/obj/' + popupData.subject.icon)" alt="" />
        </div>
        <div class="answer">
          <div
            class="answerOnce"
            @click="chooseAnswer(item, index)"
            v-for="(item, index) in answer"
          >
            <div class="left" :class="[item.style ? 'style' : '']">
              <img :src="item.icon" alt="" />
            </div>
            <div class="right" :style="{ width: rightwidth + 'px' }">
              {{ item.content }}
            </div>
          </div>
        </div>
      </div>
      <div>
        <img
          class="closeIcon"
          @click="clicks('关闭')"
          src="@/assets/guess/result/ddc.png"
          alt=""
        />
      </div>
    </div>
  </div>
</template>

<script>
import { requireFileAsExpression } from "webpack/lib/ParserHelpers";

export default {
  name: "Home",
  props: ["popupData", "visible"],
  data() {
    return {
      answer: [],
      chouse: require("@/assets/guess/dt/dt1.png"),
      noChouse: require("@/assets/guess/dt/dt2.png"),
      land: ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"],
      rightwidth: 10,
    };
  },
  watch: {
    visible() {
      if (this.visible) {
        if (this.popupData.subject) {
          let title = this.popupData.subject.title;
          title = title.split("(").join("<br/>(");
          title = "<p>" + title + "<p/>";
          // console.log(title);
          this.popupData.subject.title = title;
          // let num = this.popupData.subject.number + "";
          // num = num.split("");
          // for (let k in num) {
          //   num[k] = this.land[num[k] - 1];
          // }
          // this.popupData.subject.number = num.join("");
          this.answer = [];
          let leng = 0;
          for (let k in this.popupData.subject.answer) {
            let len = this.popupData.subject.answer[k].content.length;
            if (leng < len) {
              leng = len;
            }
            this.answer.push({
              ...this.popupData.subject.answer[k],
              icon: this.noChouse,
              style: false,
            });
          }
          this.rightwidth = leng * 20;
          console.log(this.answer);
        }
      }
    },
  },
  computed: {
    lands() {
      let num = this.popupData.subject.number + "";
      num = num.split("");
      for (let k in num) {
        num[k] = this.land[num[k] - 1];
      }
      console.log(num, "nnnnnnnnnnnnnnnn");
      return num.join("");
    },
  },
  methods: {
    clicks(val, subjectIndex) {
      if (val == "答对" || val == "答错" || val == "继续") {
        this.$emit("close", val + "-" + subjectIndex);
      } else {
        this.$emit("close", val);
      }
    },
    chooseAnswer(item, index) {
      var selected = this.answer.find((x) => x.number == item.number);
      if (selected.check) {
        this.visible = false;
        this.$emit("rightChoose", this.popupData.subject.index + 1);
      } else {
        this.visible = false;
        this.$emit("wrongChoose", this.popupData.subject.index + 1);
      }
      //debugger
      for (let k in this.answer) {
        if (k == index) {
          this.answer[k].icon = this.chouse;
          this.answer[k].style = true;
          continue;
        }
        this.answer[k].icon = this.noChouse;
        this.answer[k].style = false;
      }
    },
  },
};
</script>

<style scoped>
.openPopup {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url(../assets/guess/result/mb.png);
  background-size: 100% 100%;
  background-repeat: no-repeat;
}
.main {
  width: 80%;
  border-radius: 0.5rem;
  box-sizing: border-box;
  position: relative;
}
.main img {
  width: 100%;
}
.buttons {
  position: absolute;
  bottom: 5%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.buttons img {
  width: 85%;
}
.closeIcon {
  width: 0.8rem !important;
  position: absolute;
  bottom: -10%;
  margin-left: calc(50% - 0.4rem);
}

.luckDrawPopup.main {
  background-color: #fff !important;
  box-shadow: 0 0 6px 6px #c53939;
}
.luckDrawPopup.main .popupMain {
  border-radius: 0.7rem;
}
.luckDrawPopup.main .closeIcon {
  bottom: -15% !important;
}
.luckDrawPopup .msg {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  padding: 0.25rem;
}
.luckDrawPopup .msg .left {
  color: #f30e41;
  font-weight: 600;
  font-size: 0.7rem;
  min-width: 2.2rem;
}
.luckDrawPopup .msg .name {
  font-size: 0.3rem;
}
.luckDrawPopup .buttons {
  position: relative !important;
}
.luckDrawPopupNot .buttons {
  bottom: 10% !important;
}
.luckDrawPopupNot .buttons img {
  width: 70% !important;
}

.subject {
  position: absolute;
  color: #fff;
  left: 0;
  top: 0.8rem;
  width: 100%;
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  font-size: 0.4rem;
}
.subject .land {
  margin: 0.25rem;
}
.subject .title {
  /* margin-bottom: 1.8rem; */
  line-height: 0.48rem;
  margin: 0.45rem 0;
  word-break: break-all;
  max-width: 4rem;
}
.subject .answer {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: 100%;
  padding-bottom: 4rem;
}
.subject .answer .answerOnce {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.2rem;
  /* height: 0.5rem; */
}
.subject .answer .answerOnce .left {
  margin: 0 0.3rem;
  width: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.subject .answer .answerOnce .left img {
  width: 0.5rem;
  height: 0.5rem;
}
.style img {
  width: 0.7rem !important;
  height: 0.7rem !important;
}
.subject .answer .answerOnce .right {
  word-break: break-all;
  line-height: 0.48rem;
  max-width: 3.1rem;
}
</style>
