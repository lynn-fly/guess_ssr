  import audios from '@/utils/audios.js'
  const getDefaultState = () => {
    return {
      audios: new audios(),
    }
  }

  const state = getDefaultState()

  const mutations = {
    createAudios: (state, option) => {
      state.audios.createAudioDom(option)
    },
    play: (state, id) => {
      state.audios.play(id)
    },
    puse: (state, id) => {
      state.audios.pause(id)
    },
    getPaused: (state, id) => {
      return state.audios.getPause(id)
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
