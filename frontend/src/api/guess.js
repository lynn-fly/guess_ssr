import request from '@/utils/request'
// 答对
export function setsave_answer(id, isOk) {
    return request({
    url: '/user/save_answer/' + id + '/' + isOk,
    method: 'post',
    })
}
    