<template>
    <!-- background-color: rgba(244, 243, 243, 0.5); -->
    <v-row
        style="height: 70px; margin-bottom: 6px;"
    >
        <v-col
            cols="3"
            class="pa-0 menu-area"
            @click="toHome"
        >
        <!-- style="border-right: 1px solid rgba(200, 200, 200, 0.5);" -->
            <p class="text-center menu-text">
                ホーム
                <!-- <i class='bx bx-home'></i> -->
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            @click="showCustomerDetail"
        >
        <!-- style="border-right: 1px solid rgba(200, 200, 200, 0.5);" -->
            <p class="text-center menu-text">
                顧客情報
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            @click="showOrderDetail"
        >
        <!-- style="border-right: 1px solid rgba(200, 200, 200, 0.5);" -->
            <p class="text-center menu-text">
                注文情報
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            @click="showSeatDetail"
        >
            <p class="text-center menu-text">
                席情報
            </p>
        </v-col>

        <v-divider
            class="order_header_divider"
        />

        <CustomerDetailDialog
            ref="customerDetailDialog"
        />
        <OrderDetailDialog
            ref="orderDetailDialog"
        />
        <SeatDetailDialog
            ref="seatDetailDialog"
            @updateSalesData="updateSalesData"
        />
    </v-row>
</template>

<script>

import CustomerDetailDialog from '@/components/account/dialog/CustomerDetailDialog'
import OrderDetailDialog from '@/components/account/dialog/OrderDetailDialog'
import SeatDetailDialog from '@/components/account/dialog/SeatDetailDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'ProductCategoryItem',
    props: {
        headerInfo: {
            type: Object,
            required: false,
        }
    },
    data: () => ({
        // headerInfo: null,
    }),
    components: {
        CustomerDetailDialog,
        OrderDetailDialog,
        SeatDetailDialog,
    },
    created () {
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
    },
    methods: {
        ...mapMutations([
            'initSelectedProduct',
        ]),
        ...mapActions([
        ]),
        toHome () {
            this.$router.push({
                name: 'AccountHome'
            })
        },
        showCustomerDetail () {
            this.$refs.customerDetailDialog.open(this.headerInfo.customer)
        },
        showOrderDetail () {
            this.$refs.orderDetailDialog.open(this.headerInfo)
        },
        showSeatDetail () {
            this.$refs.seatDetailDialog.open(this.headerInfo)
        },
        updateSalesData (salesData) {
            this.$emit('updateSalesData', salesData)
        },
    }
}
</script>

<style lang="scss" scoped>
    .menu-text {
        font-size: 12px;
        padding-top: 25px;
    }

    .menu-area {
        cursor: pointer;
    }

    .order_header_divider {
        padding-top: 3px;
        background-color: rgba(173, 173, 173, 0.5);
    }
</style>
