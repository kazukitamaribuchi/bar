import Vue from 'vue'

const seatMutations = {
    setSeatList (state, payload) {
        state.seat = payload
    },
    addSeatList (state, payload) {
        if (Array.isArray(payload)) {
            for (const i in payload) {
                state.seat.push(payload[i])
            }
        } else {
            state.seat.push(payload)
        }
    },
    updateSeatList (state, payload) {
        const index = state.seat.findIndex(b => b.id === payload.id)
        Vue.set(state.seat, index, payload)
    },
    deleteSeatList (state, payload) {
        if (state.seat != undefined) {
            const index = state.seat.findIndex(b => b.id === payload.id)
            Vue.set(state.seat, index, payload)
        }
    }
}

export default seatMutations
