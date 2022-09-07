'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  //API_URL: '"http://129.226.227.171/api/v1"'
  API_URL: '"http://127.0.0.1:8000/api/v1"'
})
