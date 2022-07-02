const productMutations = {
    setProductList (state, payload) {
        state.product = payload
    },
    addProductList (state, payload) {
        state.product.push(payload.data)
    },
    setPopularProductList (state, payload) {
        // state.popularProduct = payload.data
        state.popularProduct = payload
    },
    addPopularProductList (state, payload) {
        state.popularProduct.push(payload.data)
    },
    setProductByCategoryList (state, payload) {
        state.productByCategory = payload
    },
    addProductByCategoryList (state, payload) {
        state.productByCategory.push(payload.data)
    },

}

export default productMutations
