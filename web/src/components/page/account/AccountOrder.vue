<template>
    <div>
        <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            商品カテゴリ
        </p>
        <OrderHeader/>
        <ProductCategory/>
        <SelectedProductFooter
            v-show="selectedProduct != undefined && selectedProduct.length != 0"
        />
    </div>
</template>

<script>

import OrderHeader from '@/components/account/OrderHeader'
import ProductCategory from '@/components/account/ProductCategory'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountOrderItem',
    data: () => ({
    }),
    components: {
        OrderHeader,
        ProductCategory,
        SelectedProductFooter,
    },
    created () {
    },
    mounted: function () {
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
    },
    methods: {
        ...mapMutations([
        ]),
        ...mapActions([
        ]),
        undo () {
            // カートに商品があったら確認メッセージ
            if (this.selectedProduct.length != 0) {
                console.log('カートの中身破棄するか確認する')
                this.initSelectedProduct()
                this.$router.push({
                    name: 'AccountOrderSelect'
                })
            } else {
                this.$router.push({
                    name: 'AccountOrderSelect'
                })
            }
        },
    },
    mixins: [],
}
</script>
<style lang="scss" scoped>
    .undo-btn {
        font-size: 35px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
