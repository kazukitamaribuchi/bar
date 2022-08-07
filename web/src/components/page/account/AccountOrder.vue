<template>
    <div
        class="account_order_wrap"
        :class="{'selected_product_padding': isShowSelectedProductFooter}"
    >

        <AccountPageTitleArea
            to="AccountOrderSelect"
            title="商品カテゴリ"
        />

        <OrderHeader
            :headerInfo="headerInfo"
            @updateSalesData="updateSalesData"
        />
        <ProductCategory
            :headerInfo="headerInfo"
        />
        <SelectedProductFooter
            v-show="isShowSelectedProductFooter"
            class="selected_product_footer_wrap"
        />
    </div>
</template>

<script>

import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
import OrderHeader from '@/components/account/OrderHeader'
import ProductCategory from '@/components/account/ProductCategory'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountOrderItem',
    data: () => ({
        headerInfo: {},
        updKey: 0,
    }),
    components: {
        AccountPageTitleArea,
        OrderHeader,
        ProductCategory,
        SelectedProductFooter,
    },
    created () {
        this.$axios({
            method: 'get',
            url: `/api/sales/${this.$route.params.id}/`
        })
        .then(res => {
            console.log(res)
            this.headerInfo = res.data
        })
        .catch(e => {
            console.log(e)
        })
    },
    mounted: function () {
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ]),
        isShowSelectedProductFooter () {
            if (this.selectedProduct != undefined && this.selectedProduct.length != 0) {
                return true
            }
            return false
        },
    },
    methods: {
        ...mapMutations([
        ]),
        ...mapActions([
        ]),
        updateSalesData (headerInfo) {
            this.headerInfo = headerInfo
        }
    },
    mixins: [],
}
</script>
<style lang="scss" scoped>
    .account_order_wrap {
        padding-bottom: 10px;
        // min-height: 100vh;
        // position: relative;
        // padding-bottom: 120px;
        // box-sizing: border-box;
    }

    .selected_product_padding {
        padding-bottom: 100px;
    }

</style>
