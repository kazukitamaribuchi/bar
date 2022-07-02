import Vue from 'vue'

const attendanceActions = {
    getAttendanceList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/attendance/',
            })
            .then(res => {
                console.log('getAttendanceList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default attendanceActions
