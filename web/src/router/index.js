import Vue from 'vue'
import VueRouter from 'vue-router'
import pages from './pages'
import customer from './customer'
import cast from './cast'
import sales from './sales'
import attendance from './attendance'
import booking from './booking'
import bottle from './bottle'
import account from './account'
import kitchen from './kitchen'

Vue.use(VueRouter)

const routes = [
    ...pages,
    {...customer},
    {...cast},
    {...sales},
    {...attendance},
    {...bottle},
    {...booking},
    {...account},
    {...kitchen},
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
    router['toPage'] = to
    router['referrer'] = from
    router['nextPage'] = next
	next()
})

export default router
