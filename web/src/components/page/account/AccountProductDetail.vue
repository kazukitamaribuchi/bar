<template>
    <v-dialog
        v-model="dialog"
        fullscreen
        class="account_product_detail_wrap"
        :class="{'selected_product_padding': isShowSelectedProductFooter}"
    >
        <v-card
            flat
        >
            <v-toolbar
                dark
                color="primary"
            >
                <v-btn
                    dark
                    icon
                    @click="dialog = false"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>{{ categoryName }}</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
        <!-- <AccountPageTitleArea
            to="AccountOrder"
            :title="categoryName"
            :params="params"
        />

        <OrderHeader/> -->
        <ProductDetailList
            :large="large"
            :middle="middle"
            :small="small"
            :headerInfo="headerInfo"
            :key="updKey"
        />
        <SelectedProductFooter
            v-if="selectedProduct != undefined && selectedProduct.length != 0"
        />
        </v-card>
    </v-dialog>
</template>

<script>

import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
import OrderHeader from '@/components/account/OrderHeader'
import { Const } from '@/assets/js/const'
import { mapGetters, mapMutations, mapActions } from 'vuex'
const Con = new Const()
import ProductDetailList from '@/components/account/ProductDetailList'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'

export default {
    name: 'AccountProductDetailItem',
    props: {
        headerInfo: {
            type: Object,
            required: false,
        }
    },
    data: () => ({
        dialog: false,
        large: 1,
        middle: 0,
        small: 0,
        updKey: 0,
    }),
    components: {
        AccountPageTitleArea,
        OrderHeader,
        ProductDetailList,
        SelectedProductFooter,
    },
    created () {
    },
    mounted: function () {
    },
    computed: {
        ...mapGetters([
            'selectedProduct'
        ]),
        categoryName () {
            // const large = this.$route.params.large
            // const middle = this.$route.params.middle
            // const small = this.$route.params.small
            return Con.PRODUCT_CATEGORY_DICT[this.large][this.middle][this.small]
        },
        params () {
            return {id: this.$route.params.id}
        },
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
        open (item) {
            this.large = item.large_category
            this.middle = item.middle_category
            this.small = item.small_category
            this.updKey++
            this.dialog = true
        },
        close () {
            this.dialog = false
        },

    },
    mixins: [],
}
</script>
<style lang="scss" scoped>
    .selected_product_padding {
        padding-bottom: 120px;
    }
</style>
