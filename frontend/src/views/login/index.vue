<template>
  <div class="login">
    <!--<h1>登录</h1>-->
    <div class="row" style="margin-top: 100px;">
      <div class="offset-3 col-md-6">
        <button @click="handleLogin">登陆</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: undefined,
        password: undefined
      },
      rules: {
        username: [{ required: true, trigger: 'blur', message: '用户名不能为空' }],
        password: [{ required: true, trigger: 'blur', message: '密码不能为空' }]
      }
    }
  },
  methods: {
    handleLogin() {
      // this.$refs['form'].validate(valid => {
      //   if (valid) {
      //     this.$store.dispatch('user/login', this.form).then(() => {
      //       this.$router.push({ name: 'manage' })
      //     }).catch(() => {

      //     })
      //   }
      // })
          this.$store.dispatch('user/login', {username: 'admin', password: 'admin'}).then(() => {
            this.$router.push({ name: 'manage' })
          }).catch(() => {

          })
    }
  }
}
</script>

<style scoped>

</style>
