<template>
  <div class="buttons">
    <!-- <div class="wrap"> -->
    <img class="wrap" id="wrap" src="@/assets/home/heard.png" alt="" />
    <!-- <div class="wrap1">
        <img src="@/assets/home/heard.png" alt="" />
      </div> -->
    <!-- </div> -->
    <div class="num">
      {{ num }}
      <!-- <div class="num1">
                {{ num }}
            </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: ["num", "type", "clickName"],
};
</script>

<style scoped>
.buttons {
  color: #fff;
  /* font-size: 0.4rem; */
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.5rem;
}

.num {
  font-size: 0.42rem;
  position: relative;
  margin-left: 0.1rem;
  font-weight: 600;
  filter: drop-shadow(0 0 0.08rem #14c9c9) drop-shadow(0 0 0.08rem #14c9c9);
  /* text-shadow: 0 0 0.3rem #14c9c9 0 0 0.3rem #14c9c9 0 0 0.3rem #14c9c9 0 0 0.3rem #14c9c9; */
}

.wrap {
  position: relative;
  width: 0.6rem;
  /* height: 0.6rem; */
  filter: drop-shadow(0 0 0.08rem #14c9c9) drop-shadow(0 0 0.08rem #14c9c9);
}

img {
  /* width: 100%; */
  /* height: 100%; */
}
</style>
