import Vue from 'vue'

const customerActions = {
    getCustomerList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/customer/',
            })
            .then(res => {
                console.log('getCustomerList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    },
    deleteCustomerListAction (ctx, kwargs) {
        Vue.prototype.$axios({
            url: `/api/customer/${kwargs.id}/`,
            method: 'DELETE',
        })
        .then(res => {
            console.log(res)
            this.commit('deleteCustomerList', kwargs)
        })
        .catch(e => {
            console.log(e)
        })
    }
}

export default customerActions
