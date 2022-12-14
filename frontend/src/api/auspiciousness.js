import request from '@/utils/request'

export function upFile(data) {
  const form = new FormData()
  const keys = Object.keys(data)
  keys.forEach(key => {
    form.append(key, data[key])
  })
  return request({
    url: '/user/save_upload',
    data: form,
    method: 'post',
  })
}

// 祈福列表
export function getupload_list(data = false) {
  //   const form = new FormData()
  //   const keys = Object.keys(data)
  //   keys.forEach(key => {
  //     form.append(key, data[key])
  //   })
  return request({
    url: '/user/upload_list?isFirst=' + data,
    // data: data,
    method: 'get',
  })
}


// 点赞
export function setsave_thumbed(id) {
  //   const form = new FormData()
  //   const keys = Object.keys(data)
  //   keys.forEach(key => {
  //     form.append(key, data[key])
  //   })
  return request({
    url: '/user/save_thumbed/' + id,
    // data: data,
    method: 'post',
  })
}
