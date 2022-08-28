import Vue from 'vue'
export default {
    methods: {
        searchCustomerNo (val) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'get',
                    url: '/api/customer/search_customer_by_customer_no/',
                    params: {
                        customer_no: val
                    }
                })
                .then(res => {
                    resolve(res)
                })
                .catch(e => {
                    reject(e)
                })
            })
        },
        checkCustomerNoDuplicate (val) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'get',
                    url: '/api/customer/get_customer_no_duplicate/',
                    params: {
                        customer_no: val
                    }
                })
                .then(res => {
                    resolve(res)
                })
                .catch(e => {
                    reject(e)
                })
            })
        },
    }
}
