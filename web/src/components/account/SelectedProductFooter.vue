<template>
    <!-- <v-card
        class="overflow-hidden mx-auto"
        height="200"
        max-width="500"
    > -->
        <v-bottom-navigation
            fixed
            height="80"
            class="selected_product_footer_wrap"
        >
            <!-- <v-row class="selected_product_footer_wrap"> -->
                <div
                    class="order_check"
                    @click="orderCheck"
                    v-if="!isOrderComfirm"
                >注文を確認 ({{ totalOrderCnt }}点)</div>

                <div
                    class="order_confirm"
                    @click="orderConfirm"
                    v-else
                >注文を確定</div>

                <!-- <v-col cols="7" class="order_detail pr-0">
                    <v-card-subtitle class="ma-0 pb-1 pt-0 px-0">
                        注文数 : <SelectedProductTotalCnt/>点
                    </v-card-subtitle>
                    <v-card-subtitle class="ma-0 pb-1 pt-0 px-0">
                        総計(税抜) : <SelectedProductTotalPrice/>
                    </v-card-subtitle>
                    <v-card-subtitle class="ma-0 py-0 px-0">
                        総計(税込) : <SelectedProductTotalPrice :tax=true />
                    </v-card-subtitle>
                </v-col>
                <v-col cols="5" class="order_check" @click="orderCheck" :class="{order_confirm: isOrderComfirm}">
                    <p class="order_check_text">{{ orderCheckText }}</p>
                </v-col> -->

                <v-dialog
                    v-model="dialog"
                    persistent
                >
                    <v-card>
                        <v-card-title>
                            {{ dialogText }}
                        </v-card-title>
                        <v-card-actions>
                            <v-btn
                                color="green darken-1"
                                text
                                @click="toHome"
                            >
                                OK
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            <!-- </v-row> -->

        </v-bottom-navigation>
    <!-- </v-card> -->
</template>

<script>

import { mapGetters, mapMutations } from 'vuex'
import SelectedProductTotalCnt from '@/components/account/parts/SelectedProductTotalCnt'
import SelectedProductTotalPrice from '@/components/account/parts/SelectedProductTotalPrice'

export default {
    name: 'SelectedProductFooterItem',
    data: () => ({
        dialog: false,
        dialogText: '',
        sendStatus: false,
    }),
    components: {
        SelectedProductTotalCnt,
        SelectedProductTotalPrice,
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
            'selectedProductSalesId',
        ]),
        totalOrderCnt () {
            if (this.selectedProduct != undefined) {
                let totalCnt = 0
                for (const i of this.selectedProduct) {
                    totalCnt += i.quantity
                }
                return totalCnt
            }
            return ''
        },
        totalOrderPrice () {
            if (this.selectedProduct != undefined) {
                let totalPrice = 0
                console.log(this.selectedProduct)
                for (const i of this.selectedProduct) {
                    totalPrice += Number(i.fixedPrice) * i.quantity
                }
                return totalPrice
            }
            return 0
        },
        orderCheckText () {
            if (this.isOrderComfirm) {
                return '注文確定'
            }
            return '注文確認'
        },
        isOrderComfirm () {
            if (this.$route.name == 'AccountOrderCheck') {
                return true
            }
            return false
        }
    },
    methods: {
        ...mapMutations([
            'initSelectedProductData',
        ]),
        orderCheck () {
            if (this.isOrderComfirm) {
                this.orderConfirm()
            } else {
                this.$router.push({
                    name: 'AccountOrderCheck',
                    params: {
                        id: this.$route.params.id
                    }
                })
            }
        },
        orderConfirm () {
            console.log('売上伝票追加', this.selectedProduct, this.selectedProductSalesId, this.$route.params)
            this.$axios({
                method: 'POST',
                url: '/api/sales/add_sales_detail/',
                data: {
                    sales_header_id: this.$route.params.id,
                    sales_detail_list: this.selectedProduct,
                }
            })
            .then(res => {
                console.log(res)
                this.dialogText = '注文が完了しました。'
                this.sendStatus = true
                this.dialog = true
            })
            .catch(e => {
                console.log(e)
                this.dialogText = '注文送信時にエラーが発生しました。'
                this.dialog = true
                this.sendStatus = false
            })
        },
        toHome () {
            this.initSelectedProductData()
            if (this.sendStatus) {
                this.$router.push({
                    name: 'AccountHome',
                })
            }
            this.dialog = false
        }
    }
}
</script>

<style lang="scss" scoped>
    // .selected_product_footer_wrap {
    //     margin: 0;
    //     z-index: 1000;
    //     position: fixed;
    //     height: 110px;
    //     width: 100%;
    //     bottom: 0;
    //     background: white;
    //
    //     .order_detail {
    //         background-color: rgb(142, 142, 142);
    //         color: white;
    //     }
    //
    //     .order_check {
    //         cursor: pointer;
    //         border-left: 1px solid rgba(112, 104, 104, 0.7);
    //         // background-color: rgba(193, 80, 80, 0.7);
    //         background-color: rgba(0, 78, 227, 0.7);
    //         color: white;
    //         .order_check_text {
    //             line-height: 75px;
    //             text-align: center;
    //         }
    //     }
    //     .order_check:hover {
    //         // background-color: rgba(193, 60, 60, 1);
    //         background-color: rgba(0, 78, 227, 1);
    //         transition: 0.5s;
    //     }
    //     .order_confirm {
    //         background-color: rgba(193, 80, 80, 1);
    //     }
    //     .order_confirm:hover {
    //         background-color: rgba(243, 80, 80, 1);
    //         transition: 0.5s;
    //     }
    // }

    .selected_product_footer_wrap {
        z-index: 1000 !important;
    }

    .order_check {
        cursor: pointer;
        margin: 10px;
        width: 90%;
        background-color: rgb(33, 33, 33);
        color: white;
        text-align: center;
        line-height: 60px;
        border-radius: 4px;
    }

    .order_confirm {
        cursor: pointer;
        margin: 10px;
        width: 90%;
        // background-color: rgb(53, 53, 53);
        color: white;
        text-align: center;
        line-height: 60px;
        border-radius: 4px;
        background-color: rgba(193, 80, 80, 1);
    }
</style>
