<template>
  <div class="login">
    <img class="theme" src="@/assets/login/title.png" alt="" srcset="" />
    <div class="inputs flex-c-c">
      <div class="once flex-c-c">
        <div class="title">
          <img class="titleImg" src="@/assets/login/number2.png" alt="" srcset="" />
        </div>
        <input type="text" v-model="form.username" placeholder="请输入姓名" />
      </div>
      <div class="once flex-c-c">
        <div class="title">
          <img class="titleImg" src="@/assets/login/number1.png" alt="" srcset="" />
        </div>
        <input type="text" v-model="form.password" placeholder="请输入工号" />
      </div>
    </div>
    <img
      class="luckDraw"
      @click="loging"
      src="@/assets/login/login.png"
      alt=""
      srcset=""
    />
  </div>
</template>

<script>
import { gotopPage } from "@/utils/index";

export default {
  name: "Login",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      rules: {
        username: [{ required: true, trigger: "blur", message: "用户名不能为空" }],
        password: [{ required: true, trigger: "blur", message: "密码不能为空" }],
      },
    };
  },
  methods: {
    loging() {
      this.$store
        .dispatch("user/login", {
          username: this.form.username + "",
          password: this.form.password,
        })
        .then((res) => {
          this.$router.replace({ path: "/home" });
        })
        .catch((err) => {
          if (err) {
            alert("姓名或工号错误！");
          }
        });
    },
  },
};
</script>

<style scoped>
.login {
  /* background-color: #000; */
  width: 100vw;
  /* height: 100vh; */
  min-height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background-image: url(../../assets/login/bj.png);
  padding: 2rem;
  box-sizing: border-box;
  justify-content: center !important;
  flex-direction: column;
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.theme {
  width: 100%;
  margin-bottom: 1rem;
  margin-top: 1rem;
}

.luckDraw {
  width: 100%;
}

.inputs {
  width: 100%;
  flex-direction: column;
  margin-bottom: 1rem;
}

.inputs .once {
  width: 100%;
  margin: 0.5rem 0;
}

.inputs .once .title {
  color: #fff;
  font-size: 0.4rem;
  margin-right: 0.2rem;
  width: 1rem;
}

.inputs .once .title img {
  width: 1.2rem;
}

.inputs .once input {
  border-radius: 0.15rem;
  padding: 0.1rem;
  width: 100%;
}
</style>
