import Vue from 'vue'

const settingActions = {
    getSettingList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/setting/',
            })
            .then(res => {
                console.log('getSettingList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default settingActions
