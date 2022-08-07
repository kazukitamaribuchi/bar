<template>
    <div
        class="account_order_check_wrap"
        :class="{'selected_product_padding': isShowSelectedProductFooter}"
    >
        <AccountPageTitleArea
            to="AccountOrder"
            title="注文内容"
        />

        <OrderList
        />
        <SelectedProductFooter
            v-show="selectedProduct != undefined && selectedProduct.length != 0"
        />
    </div>
</template>

<script>

import OrderList from '@/components/account/OrderList'
import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountOrderCheckItem',
    data: () => ({
        // headerInfo: {},
    }),
    mounted: function () {
        // if (this.$store.state.isAuth) {
        //     this.$router.push({name: 'AccountHome'})
        // } else {
        //     this.$router.push({name: 'AccountLogin'})
        // }
    },
    components: {
        OrderList,
        AccountPageTitleArea,
        SelectedProductFooter,
    },
    created () {
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
    }
}
</script>
<style lang="scss" scoped>
    .account_order_check_wrap {
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
