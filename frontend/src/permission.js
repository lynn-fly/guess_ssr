import router from './router'
import store from './store'
import { getToken } from './utils/auth'

const noTokenWhiteList = ['/login']
// , '/home', '/', '/guess',
//   '/auspiciousness',
//   '/luckDraw']
const tokenAdminWhiteList = ['/manage']
const tokenCustomWhiteList = ['/home', '/answer', '/upload', '/prize']


router.beforeEach(async (to, from, next) => {
  const hasToken = getToken()
  if (hasToken) {
    const hasRoles = store.getters.roles && store.getters.roles.length > 0
    var isAdminRole = store.getters.roles.indexOf('admin') > -1
    if (hasRoles) {
      if (isAdminRole) {
        if (tokenAdminWhiteList.indexOf(to.path) !== -1) {
          next()
        } else {
          next(`/manage`) //永远去manage
        }
      } else {
        if (tokenCustomWhiteList.indexOf(to.path) !== -1) {
          next()
        } else {
          next(`/home`) //永远去home
        }
      }
    } else {
      try {
        const { roles } = await store.dispatch('user/getInfo')
        // 根据角色生成路由
        const accessRoutes = await store.dispatch('permission/generateRoutes', roles)
        // 动态添加可访问路由
        router.addRoutes(accessRoutes)
        next({ ...to, replace: true })
      } catch (e) {
        await store.dispatch('user/resetToken')
        next(`/home`)
      }
    }
  } else {
    if (noTokenWhiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next(`/login`)
    }
  }
})

