import Vue from 'vue'

const serviceMutations = {
    setServiceList (state, payload) {
        state.service = payload
    },
    addServiceList (state, payload) {
        if (Array.isArray(payload)) {
            for (const i in payload) {
                state.service.push(payload[i])
            }
        } else {
            state.service.push(payload)
        }
    },
    updateServiceList (state, payload) {
        const index = state.service.findIndex(b => b.id === payload.id)
        Vue.set(state.service, index, payload)
    },
    deleteServiceList (state, payload) {
        if (state.service != undefined) {
            const index = state.service.findIndex(b => b.id === payload.id)
            Vue.set(state.service, index, payload)
        }
    }
}

export default serviceMutations
