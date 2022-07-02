import Vue from 'vue'

const salesActions = {
    getSalesList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/sales/',
            })
            .then(res => {
                console.log('getSalesList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    },
    deleteSalesListAction (ctx, kwargs) {
        Vue.prototype.$axios({
            url: `/api/sales/${kwargs.id}/`,
            method: 'DELETE',
        })
        .then(res => {
            console.log(res)
            this.commit('deleteSalesList', kwargs)
        })
        .catch(e => {
            console.log(e)
        })
    }
}

export default salesActions
