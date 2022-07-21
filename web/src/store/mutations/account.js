import Vue from 'vue'
import _ from 'lodash'

const accountMutations = {
    addSelectedProduct (state, payload) {
        const index = state.selectedProduct.findIndex(s => s.id === payload.id)
        if (index !== -1) {
            payload.taxFree = state.selectedProduct[index].taxFree
            payload.fixedPrice = state.selectedProduct[index].fixedPrice
            Vue.set(state.selectedProduct, index, payload)
        } else {
            state.selectedProduct.push(payload)
        }
    },
    pushSelectedProduct (state, payload) {
        state.selectedProduct.push(payload)
    },
    updateSelectedProduct (state, payload) {
        const index = state.selectedProduct.findIndex(s => s.id === payload.id)
        Vue.set(state.selectedProduct, index, payload)
    },
    updateSelectedProductQuantity (state, payload) {
        if (payload.quantity == 0) {
            this.commit('deleteSelectedProduct', payload)
        } else {
            const index = state.selectedProduct.findIndex(s => s.id === payload.id)
            if (index != -1) {
                payload.taxFree = state.selectedProduct[index].taxFree
                payload.fixedPrice = state.selectedProduct[index].fixedPrice
                Vue.set(state.selectedProduct, index, payload)
            } else {
                state.selectedProduct.push(payload)
            }
        }
    },
    deleteSelectedProduct (state, payload) {
        if (state.selectedProduct != undefined) {
            const index = state.selectedProduct.findIndex(s => s.id === payload.id)
            if (index !== -1) state.selectedProduct = state.selectedProduct.filter((_, i) => i !== index)
        }
    },
    initSelectedProduct (state, payload) {
        state.selectedProduct = []
    },
    setSelectedProductSalesId (state, payload) {
        state.selectedProductSalesId = payload
    },
    initSelectedProductSalesId (state, payload) {
        state.selectedProductSalesId = null
    },
    initSelectedProductData (state, payload) {
        state.selectedProduct = []
        state.selectedProductSalesId = null
    },
}

export default accountMutations
