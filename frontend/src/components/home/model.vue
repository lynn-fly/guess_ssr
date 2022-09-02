<template>
    <div class="buttons">
        {{ msg }}
    </div>
</template>
  
  <script>
export default {
    name: 'Home',
    props: ['msg', 'type', 'clickName'],
}
</script>
  
  <style scoped >
  .buttons {
      padding: 10px;
      background-image: linear-gradient(#fc1dce, #962de7);
      color: #fff;
  }
  </style>
  