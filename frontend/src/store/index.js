import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import user from './modules/user'
import heart from './modules/heart'
import audio from './modules/audio'
import permission from './modules/permission'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    user,
    permission,
    audio,
    heart
  },
  getters
})

export default store
