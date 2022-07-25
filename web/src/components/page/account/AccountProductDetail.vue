<template>
    <div>
        <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            {{ categoryName }}
        </p>
        <OrderHeader/>
        <ProductDetailList/>
        <SelectedProductFooter
            v-if="selectedProduct != undefined && selectedProduct.length != 0"
        />
    </div>
</template>

<script>

import OrderHeader from '@/components/account/OrderHeader'
import { Const } from '@/assets/js/const'
import { mapGetters, mapMutations, mapActions } from 'vuex'
const Con = new Const()
import ProductDetailList from '@/components/account/ProductDetailList'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'

export default {
    name: 'AccountProductDetailItem',
    data: () => ({
    }),
    components: {
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
            const large = this.$route.params.large
            const middle = this.$route.params.middle
            const small = this.$route.params.small
            return Con.PRODUCT_CATEGORY_DICT[large][middle][small]
        }
    },
    methods: {
        ...mapMutations([
        ]),
        ...mapActions([
        ]),
        undo () {
            this.$router.push({
                name: 'AccountOrder',
                params: {
                    id: this.$route.params.id
                }
            })
        },
    },
    mixins: [],
}
</script>
<style lang="scss" scoped>
    .undo-btn {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
