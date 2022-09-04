<template>
  <div class="buttons">
    <div class="name" v-if="msg" @click="$emit('back', msg)">
      {{ msg }}
    </div>
    <div class="login" v-else @click="$emit('back', 'login')">
      <img src="@/assets/home/login.png" alt="" />
    </div>
  </div>
</template>

<script>
export default {
  name: "buttons",
  props: ["msg"],
};
</script>

<style scoped>
.name {
  padding: 0.08rem 0.3rem;
  background-image: linear-gradient(to right, #fc1dce, #962de7);
  color: #fff;
  font-size: 0.4rem;
  border-radius: 0.3rem;
  text-align: center;
  line-height: 0.4rem;
  min-width: 1.2rem;
}

.login {
  width: 2rem;
}

.login img {
  width: 100%;
  height: 100%;
}
</style>
