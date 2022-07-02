import Vue from 'vue'

const bookingActions = {
    getBookingList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/booking/',
            })
            .then(res => {
                console.log('getBookingList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default bookingActions
