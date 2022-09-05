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
} from '@/utils/auth'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: getName() || '',
    roles: [],
    userInfor: getUser()
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
  }
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
        // const data = {
        //   access_token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjMwNzcxNTQsInN1YiI6IjIifQ.cQmYSh1A-nA3EEME2ZgTnsIaKVsvMUSKSN_Xm1_zMuU",
        //   heartValue: 100,
        //   isAnswerMax: true,
        //   isLocal: true,
        //   isUpload: true,
        //   lotteryCount: 0,
        //   userId: 2,
        //   userName: "谭本宏",
        // }
        commit('SET_TOKEN', data['access_token'])
        setToken(data['access_token'])
        setUser(data)
        setName(data['userName'])
        resolve()
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
          reject('验证失败，请重新登录。')
        }
        const {
          name,
          roles
        } = data
        // console.log(data)
        // if (!roles || roles.le <= 0) {
        //   reject('getInfo: roles must be a non-null array!')
        // }
        commit('SET_ROLES', roles)
        commit('SET_NAME', name)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  // luckyDraw
  luckyDraw({commit,state}) {
    return new Promise((resolve,reject) => {
      goodLucky().then(res=>{
        const {lotteryNumber,lottery_count} = res.data;
        let num = lotteryNumber < 1? 9: lotteryNumber - 1;
        resolve(num);
      })
      .catch(err=>{
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
