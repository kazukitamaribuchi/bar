import Vue from 'vue'

const bottleMutations = {
    setBottleList (state, payload) {
        state.bottle = payload
    },
    addBottleList (state, payload) {
        if (Array.isArray(payload)) {
            for (const i in payload) {
                state.bottle.push(payload[i])
            }
        } else {
            state.bottle.push(payload)
        }
    },
    addBottleListTop (state, payload) {
        state.bottle.splice(0, 0, payload)
    },
    updateBottleList (state, payload) {
        const index = state.bottle.findIndex(b => b.id === payload.id)
        Vue.set(state.bottle, index, payload)
    },
    deleteBottleList (state, payload) {
        if (state.bottle != undefined) {
            const index = state.bottle.findIndex(b => b.id === payload.id)
            if (index !== -1) state.bottle = state.bottle.filter((_, i) => i !== index)
        }
    }
}

export default bottleMutations
