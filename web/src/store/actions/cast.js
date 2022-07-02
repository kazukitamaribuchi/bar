import Vue from 'vue'

const castActions = {
    getCastList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/cast/',
            })
            .then(res => {
                console.log('getCastList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    },
    deleteCastListAction (ctx, kwargs) {
        Vue.prototype.$axios({
            url: `/api/cast/${kwargs.id}/`,
            method: 'DELETE',
        })
        .then(res => {
            console.log(res)
            this.commit('deleteCastList', kwargs)
        })
        .catch(e => {
            console.log(e)
        })
    }
}

export default castActions
