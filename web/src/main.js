import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
import store from '@/store'
import http from '@/plugins/http'
import eventHub from '@/plugins/eventHub'
import Vuesax from 'vuesax'
import VueSession from 'vue-session'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import VueApexCharts from 'vue-apexcharts'
import truncate from '@/filters/truncate'
import priceLocaleString from '@/filters/priceLocaleString'

import 'vuesax/dist/vuesax.css'
import 'boxicons/css/boxicons.min.css'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
require('@/assets/scss/main.scss')

Vue.prototype.$store = store
Vue.config.productionTip = false

Vue.use(http)
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(eventHub)
Vue.use(VueApexCharts)
Vue.component('VueApexCharts', VueApexCharts)
Vue.use(Vuesax)

Vue.use(VueSession)
Vue.filter('truncate', truncate)
Vue.filter('priceLocaleString', priceLocaleString)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#main')
