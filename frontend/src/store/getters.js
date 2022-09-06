const getters = {
  name: state => state.user.name,
  token: state => state.user.token,
  roles: state => state.user.roles,
  permission_routes: state => state.permission.routes,
  userInfor: state => state.user.userInfor,
  heart: state => state.user.heart
}
export default getters
