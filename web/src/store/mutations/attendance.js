const attendanceMutations = {
    setAttendanceList (state, payload) {
        state.attendance = payload.data
    }
}

export default attendanceMutations
