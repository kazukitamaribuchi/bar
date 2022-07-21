import Vue from 'vue'

const seatActions = {
    getSeatList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/seat/',
            })
            .then(res => {
                console.log('getSeatList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default seatActions
