const bookingMutations = {
    setBookingList (state, payload) {
        state.booking = payload.data
    }
}

export default bookingMutations
