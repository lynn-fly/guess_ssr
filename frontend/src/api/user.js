import request from '@/utils/request'

// 用户登陆
export function login(data) {
  const form = new FormData()
  const keys = Object.keys(data)
  keys.forEach(key => {
    form.append(key, data[key])
  })
  return request({
    url: '/login/user',
    method: 'post',
    data: form
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

// 管理员登陆
