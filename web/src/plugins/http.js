import Vue from 'vue'
import axios from 'axios'


export default {
    install: function (Vue, options) {
        const http = axios.create({
            // baseURL: 'http://localhost:8000/',
            baseURL: process.env.NODE_ENV !== 'production' ? 'http://localhost:8000/' : `${process.env.VUE_APP_AUTH_REDIRECT_URI}/`,
            xsrfCookieName:'csrftoken',
			xsrfHeaderName: 'X-CSRFTOKEN',
			timeout: 30000,
            // headers: {
			// 	common: {
			// 		'Content-Type': 'application/json;charset=utf-8',
			// 		'Access-Control-Allow-Origin': 'http://localhost:8000/',
			// 		'X-Requested-With': 'XMLHttpRequest',
			// 		'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, X-HTTP-Method-Override, Accept',
			// 		'Access-Control-Allow-Methods': 'PUT, DELETE, OPTIONS, POST, GET'
			// 	}
			// }
        })

        http.interceptors.request.use((config) => {
			// ヘッダーに認証済みのToken埋め込み
			if (Vue.prototype.$store.state.isAuth) {
				config.headers = {
					Authorization: `JWT ${Vue.prototype.$store.state.token}`,
					'Content-Type': 'application/json'
				}
				if (!('params' in config)) config.params = {}
				if (config.method === 'get') config.params.loginUser = Vue.prototype.$store.state.loginUser
			}
			return config
		})
		// レスポンスのデフォルト定義
		http.interceptors.response.use((res) => {
			// リクエストデータのJSON解析
			try {
				var requestData = (res.config.data !== undefined) ? JSON.parse(res.config.data) : null
				res.requestData = requestData
			} catch (e) {
                console.log('えらー')
				console.log(e)
			}
			return res
		})

        Vue.prototype.$axios = http
    }
}
