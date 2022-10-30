<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            :title="title"
            header-bg-variant="primary"
            header-text-variant="light"
        >
            <b-form class="create_bottle_form">
                <b-container fluid>
                    <b-row>
                        <b-col cols="12">
                            <!-- <b-card> -->
                                <label>
                                    {{ msg }}
                                    <!-- 会計をした会員を選択してください。 -->
                                </label>
                                <b-container>
                                    <b-row>
                                        <b-col
                                            cols="4"
                                            v-for="(item, i) in customerList"
                                            :key="i"
                                            class="pa-0"
                                        >
                                            <b-card
                                                bg-variant="light"
                                                @click="selectCustomer(i)"
                                                style="cursor: pointer;"
                                            >
                                                <div>
                                                    <label>
                                                        顧客情報{{ i + 1 }}
                                                    </label>
                                                </div>
                                                <b-container>
                                                    <b-row>
                                                        <b-col cols="4">
                                                            <div>
                                                                <img
                                                                    src="@/assets/img/男性3.jpg"
                                                                    class="customer_detail_customer_icon"
                                                                >
                                                            </div>
                                                            <b-card-sub-title style="font-size: 12px; margin-top: 10px;">
                                                                会員No
                                                            </b-card-sub-title>
                                                            <b-card-text style="font-size: 13px;">
                                                                {{ item.customer_no }}
                                                            </b-card-text>
                                                        </b-col>
                                                        <b-col cols="8">
                                                            <div style="margin-left: 15px;">
                                                                <b-card-sub-title>
                                                                    名前
                                                                </b-card-sub-title>
                                                                <b-card-text style="font-size: 15px;">
                                                                    {{ item.name }}
                                                                </b-card-text>
                                                                <b-card-sub-title>
                                                                    ランク
                                                                </b-card-sub-title>
                                                                <b-card-text style="font-size: 15px;">
                                                                    {{ getStrInData(item.rank_name) }}
                                                                </b-card-text>
                                                            </div>
                                                        </b-col>
                                                    </b-row>
                                                </b-container>

                                            </b-card>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            <!-- </b-card> -->
                        </b-col>
                    </b-row>
                </b-container>
            </b-form>
            <template #modal-footer>
                <b-container fluid>
                    <b-row>
                        <b-col align="right" class="add_sales_detail_footer_col">
                            <b-button
                                variant="secondary"
                                @click="close"
                                class="btn_close"
                            >
                                閉じる
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>
    </div>
</template>

<script>
import _ from 'lodash'
import { Const } from '@/assets/js/const'
const Con = new Const()

import utilsMixin from '@/mixins/utils'
import customerMixin from '@/mixins/customer'
import Vue from 'vue'

export default {
    name: 'InputSalesSelectCustomerDialogItem',
    props: {
        customerList: {
            type: Array,
            required: true,
            default: () => ([])
        },
        title: {
            type: String,
            required: true,
        },
        msg: {
            type: String,
            required: true,
        }
    },
    components: {
    },
    data: () => ({
        customerInfo: null,
        dialog: false,
        mode: 0,
        updateIdx: 0,
    }),
    computed: {
    },
    watch: {
    },
    created () {
    },
    mounted () {
    },
    methods: {
        init () {
            this.customerInfo = null
            this.mode = 0
            this.updateIdx = 0
        },
        close () {
            this.dialog = false
        },
        initClose () {
            this.init()
            this.dialog = false
        },
        open (val, idx) {
            this.dialog = true
            this.init()

            console.log('mode: ', val)
            console.log('updateIdx: ', idx)

            if (val) this.mode = val
            if (idx) this.updateIdx = idx

        },
        selectCustomer (idx) {
            // this.customerInfo.amountPaid = 0
            // this.customerInfo.cardPayment = false
            // this.customerInfo.basicPlanCardTax = 0

            if (this.mode == 0) {
                this.$emit('selectCustomer', idx)
            } else if (this.mode == 1) {
                this.$emit('selectCustomerProductList', idx, this.updateIdx)
            } else if (this.mode == 2) {
                this.$emit('selectBottleCustomerProductList', idx, this.updateIdx)
            }

            this.initClose()
        },
    },
    mixins: [
        utilsMixin,
        customerMixin,
    ]
}

</script>

<style lang="scss" scoped>
    .create_bottle_form {
        .input-group-text {
            height: 100%;
            border-radius: 5px 0 0 5px !important;
        }
    }

    .invalid {
        color: red;
    }

    .form_required:after{
        content: '*';
        color: red;
    }

    .create_bottle_customer_icon {
        border-radius: 50%;
        width: 50px;
        height: 50px;
    }

    .customer_detail_customer_icon {
        border-radius: 50%;
        width: 50px;
        height: 50px;
    }
</style>
