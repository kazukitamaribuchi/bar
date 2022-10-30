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
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                url: `/api/customer/${kwargs.id}/`,
                method: 'DELETE',
            })
            .then(res => {
                console.log('deleteCustomerListAction', res, ' kwargs', kwargs)
                this.commit('deleteCustomerList', kwargs)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    },
}

export default customerActions
