import request from '@/utils/request'

export function getNameList(data) {
    const form = new FormData()
    const keys = Object.keys(data)
    keys.forEach(key => {
      form.append(key, data[key])
    })
    return request({
      url: '/user/result',
      method: 'post',
      data: form
    })
  }

export function getExcel(data) {
    const form = new FormData()
    const keys = Object.keys(data)
    keys.forEach(key => {
      form.append(key, data[key])
    })
    return request({
      url: '/user/export',
      method: 'post',
      data: form,
      responseType: 'blob' 
    })
  }