import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

import customerMutations from './mutations/customer'
import castMutations from './mutations/cast'
import questionMutations from './mutations/question'
import bottleMutations from './mutations/bottle'
import bookingMutations from './mutations/booking'
import salesMutations from './mutations/sales'
import attendanceMutations from './mutations/attendance'
import productMutations from './mutations/product'
import accountMutations from './mutations/account'
import seatMutations from './mutations/seat'
import settingMutations from './mutations/setting'
import serviceMutations from './mutations/service'

import customerActions from './actions/customer'
import castActions from './actions/cast'
import questionActions from './actions/question'
import bottleActions from './actions/bottle'
import bookingActions from './actions/booking'
import salesActions from './actions/sales'
import attendanceActions from './actions/attendance'
import productActions from './actions/product'
import accountActions from './actions/account'
import seatActions from './actions/seat'
import settingActions from './actions/setting'

import router from '@/router'

Vue.use(Vuex)

const initialState = {
    isAuth: false,
    token: '',
    loginUser: '',
    initStatus: false,
    currentTime: '',
    customer: [],
    customerTopActive: 0,
    sales: [],
    salesTopActive: 0,
    attendance: [],
    cast: [],
    castTopActive: 0,
    question: [],
    booking: [],
    bottle: [],
    product: [],
    popularProduct: [],
    productByCategory: [],
    selectedProduct: [],
    selectedProductSalesId: null,
    seat: [],
    setting: [],
    service: [],
    accountData: [],
}


export default new Vuex.Store({
    strict: true,
    state: {
        ...{},
        ...initialState
    },
    getters: {
        isAuth: state => state.isAuth,
        token: state => state.token,
        loginUser: state => state.loginUser,
        initStatus: state => state.initStatus,
        currentTime: state => state.currentTime,
        customer: state => state.customer,
        customerTopActive: state => state.customerTopActive,
        sales: state => state.sales,
        salesTopActive: state => state.salesTopActive,
        attendance: state => state.attendance,
        cast: state => state.cast,
        castTopActive: state => state.castTopActive,
        question: state => state.question,
        booking: state => state.booking,
        bottle: state => state.bottle,
        product: state => state.product,
        popularProduct: state => state.popularProduct,
        productByCategory: state => state.productByCategory,
        selectedProduct: state => state.selectedProduct,
        selectedProductSalesId: state => state.selectedProductSalesId,
        seat: state => state.seat,
        setting: state => state.setting,
        service: state => state.service,
        accountData: state => state.accountData,
    },
    mutations: {
        ...customerMutations,
        ...castMutations,
        ...questionMutations,
        ...bottleMutations,
        ...bookingMutations,
        ...salesMutations,
        ...attendanceMutations,
        ...productMutations,
        ...accountMutations,
        ...seatMutations,
        ...settingMutations,
        ...serviceMutations,

        setAuthToken (state, payload) {
            state.isAuth = true
            state.token = payload.data.token
            state.loginUser = payload.requestData.username
        },
        setInitStatus (state, payload) {
            state.initStatus = true
        },
        initAuthToken (state, payload) {
            state.isAuth = false
            state.token = ''
            state.loginUser = ''
        },
        initState (state, payload) {
            state.initStatus = false
            state.currentTime = ''
            state.customer = []
            state.customerTopActive = 0
            state.sales = []
            state.salesTopActive = 0
            state.attendance = []
            state.cast = []
            state.castTopActive = 0
            state.question = []
            state.booking = []
            state.bottle = []
            state.product = []
            state.popularProduct = []
            state.productByCategory = []
            state.selectedProduct = []
            state.selectedProductSalesId = null
            state.seat = []
            state.setting = []
            state.service = []
            state.accountData = []
        },
        setCurrentTime (state, payload) {
            state.currentTime = payload
        },
    },
    actions: {
        ...customerActions,
        ...castActions,
        ...questionActions,
        ...bookingActions,
        ...bottleActions,
        ...salesActions,
        ...attendanceActions,
        ...productActions,
        ...accountActions,
        ...seatActions,
        ...settingActions,

        checkAuthToken (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'POST',
                    url: '/auth/',
                    data: kwargs
                })
                .then(res => {
                    console.log('認証結果', res)
                    this.commit('setAuthToken', res)
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    this.commit('initAuthToken')
                    reject(e)
                })
            })
        },
        getCurrentTime (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'GET',
                    url: '/api/time/get_current_time/',
                    data: kwargs
                })
                .then(res => {
                    this.commit('setCurrentTime', res.data.data)
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    if (e.response.status == 401) {
                        this.commit('initAuthToken')
                        router.push('/')
                    }
                    reject(e)
                })
            })
        },
        appInitAction (ctx, kwargs) {
			return new Promise((resolve, reject) => {
	        	Vue.prototype.$axios({
	        		url: '/api/appinit/',
	        		method: 'GET',
	        	})
	        	.then(res => {
	        		console.log('アプリ初期描画', res)
					this.commit('setCustomerList', res.data.customers)
					this.commit('setProductList', res.data.product)
					this.commit('setPopularProductList', res.data.popular)
                    this.commit('setProductByCategoryList', res.data.product_by_category)
                    this.commit('setSalesList', res.data.sales)
                    this.commit('setBottleList', res.data.bottle)
                    this.commit('setSeatList', res.data.seat)
                    this.commit('setSettingList', res.data.setting)
                    this.commit('setServiceList', res.data.service)
                    // this.commit('setCastList', res.data.cast)
                    // this.commit('setQuestionList', res.data.question)
					resolve(res)
	        	})
	        	.catch(e => {
	        		console.log('初期データ取得失敗:', e.response)
	        		reject(e)
	        	})
			})
		},
    },
    modules: {
    },
    plugins: [
        VuexPersistedstate({
            storage: window.localStorage
        })
    ]
})
