import Vue from 'vue'

const castMutations = {
    setCastList (state, payload) {
        state.cast = payload
    },
    addCastList (state, payload) {
        state.cast.push(payload.data)
    },
    updateCastList (state, payload) {
        const index = state.cast.findIndex(c => c.id === payload.id)
        Vue.set(state.cast, index, payload)
    },
    deleteCastList (state, payload) {
        if (state.cast != undefined) {
            const index = state.cast.findIndex(s => s.id === payload.id)
            if (index !== -1) state.cast = state.cast.filter((_, i) => i !== index)
        }
    },
    setCastTopActive (state, payload) {
        state.castTopActive = payload
    },
}

export default castMutations
