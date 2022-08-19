import Vue from 'vue'

const settingMutations = {
    setSettingList (state, payload) {
        state.setting = payload
    },
    addSettingList (state, payload) {
        if (Array.isArray(payload)) {
            for (const i in payload) {
                state.setting.push(payload[i])
            }
        } else {
            state.setting.push(payload)
        }
    },
    updateSettingList (state, payload) {
        const index = state.setting.findIndex(b => b.id === payload.id)
        Vue.set(state.setting, index, payload)
    },
    deleteSettingList (state, payload) {
        if (state.setting != undefined) {
            const index = state.setting.findIndex(b => b.id === payload.id)
            Vue.set(state.setting, index, payload)
        }
    }
}

export default settingMutations
