import Vue from 'vue'

const bottleActions = {
    getBottleList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/bottle/',
            })
            .then(res => {
                console.log('getBottleList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    },
    endBottleListAction (ctx, kwargs) {
        Vue.prototype.$axios({
            url: '/api/bottle/end_bottle_data/',
            method: 'PUT',
            data: kwargs
        })
        .then(res => {
            console.log(res)
            // storeの飲終フラグを更新
            this.commit('updateBottleList', res.data.data)
        })
        .catch(e => {
            console.log(e)
        })
    },
    deleteBottleListAction (ctx, kwargs) {
        // Vue.prototype.$axios({
        //     url: '/api/bottle/delete_bottle_data/',
        //     method: 'DELETE',
        //     data: kwargs
        // })
        // .then(res => {
        //     console.log(res)
        //     // storeの削除フラグを更新
        //     this.commit('updateBottleList', res.data.data)
        // })
        // .catch(e => {
        //     console.log(e)
        // })
        Vue.prototype.$axios({
            url: `/api/bottle/${kwargs.id}/`,
            method: 'DELETE',
        })
        .then(res => {
            console.log(res)
            this.commit('deleteBottleList', kwargs)
        })
        .catch(e => {
            console.log(e)
        })
    }
}

export default bottleActions
