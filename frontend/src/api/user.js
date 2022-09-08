import request from '@/utils/request'

// 用户登陆
export function login(data) {
  return request({
    url: '/login/user',
    method: 'post',
    data: data
  })
}

// 管理员登陆
export function loginAdmin(data) {
  const form = new FormData()
  const keys = Object.keys(data)
  keys.forEach(key => {
    form.append(key, data[key])
  })
  return request({
    url: '/login/access-token',
    method: 'post',
    data: form
  })
}

export function getInfo() {
  return request({
    url: '/login/info',
    method: 'get'
  })
}

export function goodLucky() {
  return request({
    url: '/user/get_prize',
    method: 'post'
  })
}

//获取人数
export function getUserCount() { 
  return request({
    url: '/user/get_cy',
    method: 'get',
  })
}
 