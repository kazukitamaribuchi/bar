<template>
    <div>
        <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            注文内容
        </p>
        <OrderList/>
        <SelectedProductFooter
            v-show="selectedProduct != undefined && selectedProduct.length != 0"
        />
    </div>
</template>

<script>

import OrderList from '@/components/account/OrderList'
import SelectedProductFooter from '@/components/account/SelectedProductFooter'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountOrderCheckItem',
    mounted: function () {
        // if (this.$store.state.isAuth) {
        //     this.$router.push({name: 'AccountHome'})
        // } else {
        //     this.$router.push({name: 'AccountLogin'})
        // }
    },
    components: {
        OrderList,
        SelectedProductFooter,
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
    },
    methods: {
        undo () {
            this.$router.push({
                name: 'AccountOrder',
                params: {
                    id: this.$route.params.id
                }
            })
        },
    }
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
