import {
  login,
  getInfo,
  loginAdmin,
  goodLucky
} from '@/api/user'
import {
  getToken,
  setToken,
  removeToken,
  getUser,
  setUser,
  removeUser,
  getName,
  setName,
  removeName,
  getheart,
  setheart,
  removeheart,
} from '@/utils/auth'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: getName() || '',
    roles: [],
    userInfor: getUser(),
    heart: getheart()
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  },
  SET_HEARTVALUE: (state, value) => {
    state.userInfor.heartValue = value
  },
  SET_HEART_IS_MAX: (state, value) => {
    state.userInfor.isAnswerMax = value
  },
  SET_USER_INFO: (state, value) => {
    state.userInfor = value
  },
  SET_LOTTERY_COUNT: (state, value) => {
    state.userInfor.lotteryCount = value
  },
  SET_IS_UPLOAD: (state, value) => {
    state.userInfor.isUpload = value
  },
  SET_ANSWERED_IDS: (state, value) => {
    state.userInfor.answeredIds = value
  },
}

const actions = {
  login({
    commit
  }, userInfo) {
    const {
      username,
      password
    } = userInfo
    return new Promise((resolve, reject) => {
      login({
        nick_name: username.trim(),
        username: password
      }).then(response => {
        const {
          data
        } = response
        commit('SET_NAME', data['userName'])
        commit('SET_TOKEN', data['access_token'])
        commit('SET_USER_INFO', data)
        setToken(data['access_token'])
        setUser(data)
        setName(data['userName'])
        setheart(data['heartValue'])
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },

  loginAdmin({
    commit
  }, userInfo) {
    const {
      username,
      password
    } = userInfo
    return new Promise((resolve, reject) => {
      loginAdmin({
        username: username.trim(),
        password: password
      }).then(response => {
        const {
          data
        } = response
        commit('SET_TOKEN', data['access_token'])
        setToken(data['access_token'])
        setUser(data)
        setName(data['userName'])
        setheart(data['heartValue'])
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  // get user info
  getInfo({
    commit,
    state
  }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const {
          data
        } = response
        if (!data) {
          reject('?????????????????????????????????')
        }
        console.log(data, 'getinfor')
        commit('SET_USER_INFO', data)
        setheart(data['heartValue'])
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // luckyDraw
  luckyDraw({
    commit,
    state
  }) {
    return new Promise((resolve, reject) => {
      goodLucky().then(res => {
          const {
            lotteryNumber,
            lotteryCount,
            heartValue
          } = res.data;
          commit('SET_LOTTERY_COUNT', lotteryCount)
          commit('SET_HEARTVALUE', heartValue)
          resolve({
            lotteryNumber,
            lotteryCount,
            heartValue
          });
        })
        .catch(err => {
          reject(err);
        })
    })
  },
  // logout
  logout({
    commit,
    state
  }) {
    return new Promise((resolve, reject) => {
      try {
        removeToken()
        commit('RESET_STATE')
        resolve()
      } catch (error) {
        reject(error)
      }
    })
  },
  // remove token
  resetToken({
    commit
  }) {
    return new Promise(resolve => {
      removeToken()
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
