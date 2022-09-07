const getDefaultState = () => {
  return {
    audios: [],
  }
}

const state = getDefaultState()

const mutations = {
  createAudios: (state, option) => {
    console.log(11111111)
    let dom = document.createElement('div');
    let img = document.createElement('img')
    img.src = require('@/assets/home/heard.png')
    img.style.width = '0.6rem';
    dom.append(img)
    dom.style.filter = 'drop-shadow(0 0 0.08rem #14c9c9) drop-shadow(0 0 0.08rem #14c9c9)';
    dom.style.position = 'fixed';
    // dom.style.top = option.top + 'px';
    // dom.style.left = option.left + 'px';
    dom.style.top = '50%';
    dom.style.left = '50%';
    dom.className = 'heardsss';
    dom.style.transition = "all 3s"
    document.body.appendChild(dom)
    setTimeout(() => {
      let wrap = document.getElementById('wrap')
      console.log(wrap.offsetLeft)
      console.log(wrap.offsetTop)
      dom.style.top = wrap.offsetHeight + 'px'
      dom.style.left = wrap.offsetLeft + 'px'
      setTimeout(() => {
        document.body.removeChild(dom)
      }, 3000);
    }, 200);
  },
}

const actions = {
  initAudio({
    commit
  }, option) {


  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
