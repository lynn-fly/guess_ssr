export function getToken() {
  return localStorage.getItem('Token')
}

export function setToken(token) {
  return localStorage.setItem('Token', token)
}

export function removeToken() {
  return localStorage.removeItem('Token')
}

export function getUser() {
  return JSON.parse(localStorage.getItem('user'))
}

export function setUser(infor) {
  return localStorage.setItem('user', JSON.stringify(infor))
}

export function removeUser() {
  return localStorage.removeItem('user')
}


export function getName() {
  return localStorage.getItem('name')
}

export function setName(name) {
  return localStorage.setItem('name', name)
}

export function removeName() {
  return localStorage.removeItem('name')
}



export function getheart() {
  return localStorage.getItem('heart')
}

export function setheart(heart) {
  return localStorage.setItem('heart', heart)
}

export function removeheart() {
  return localStorage.removeItem('heart')
}
