import Vue from 'vue'

const questionActions = {
    getQuestionList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/question/',
            })
            .then(res => {
                console.log('getQuestionList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default questionActions
