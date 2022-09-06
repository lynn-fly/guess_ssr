import axios from 'axios'
import store from '@/store'
import { getToken } from '@/utils/auth'
// import { MessageBox, Message } from 'element-ui'

// 创建一个axios实例
console.log(process.env)
console.log(process.env.API_URL)
const service = axios.create({
  baseURL: process.env.API_URL,
  timeout: 120 * 1000 // 请求超时时间
})

// 设置请求拦截器
service.interceptors.request.use(
  config => {
    if (store.getters.token) {
      config.headers['Authorization'] = 'Bearer ' + getToken()
    }
    return config
  },
  error => {
    console.log(error) // for debug
    return Promise.reject(error)
  }
)
// 设置响应拦截器
service.interceptors.response.use(
  response => {
    console.log(response.data)
    return response
  },
  error => {
    if (!error.response) {
      return Promise.reject(error)
    }
    if (error.response.status === 403) {
      
        store.dispatch('user/resetToken').then(() => {
          location.reload()
        })
      
    }
    console.log('err' + error) // for debug
    return Promise.reject(error)
  }
)

export default service
