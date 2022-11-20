<template>
    <div>
        <b-modal
            v-model="dialog"
            size="lg"
            screenable
            title="選択商品"
            header-bg-variant="primary"
            header-text-variant="light"
        >
            <b-container
                fluid
                class="product_item_area"
            >
                <b-row>
                    <b-col cols="4">
                        <div class="selected_product_area">
                            <div v-if="selectedProduct != null">
                                <img
                                    v-if="selectedProduct.thumbnail != null"
                                    class="product_item_thumbnail"
                                    :src="getImgLink(selectedProduct.thumbnail)"
                                >
                                <img
                                    v-else
                                    class="product_item_thumbnail"
                                    src="@/static/img/noimage8.png"
                                >
                            </div>
                        </div>
                    </b-col>
                    <b-col cols="8">
                        <div class="product_item_name">
                            <b-card-sub-title>
                                商品名
                            </b-card-sub-title>
                            <b-card-text v-if="selectedProduct != null">
                                {{ selectedProduct.name }}
                            </b-card-text>
                            <b-card-text v-else>
                                -
                            </b-card-text>
                        </div>
                        <div class="product_item_price">
                            <b-card-sub-title>
                                価格
                            </b-card-sub-title>
                            <b-card-text v-if="selectedProduct != null">
                                <b-icon icon="currency-yen"></b-icon> {{ selectedProduct.price | priceLocaleString }}
                            </b-card-text>
                            <b-card-text v-else>
                                -
                            </b-card-text>
                        </div>
                        <!-- <div class="product_item_num">
                            <b-card-sub-title>
                                数量
                            </b-card-sub-title>
                            <b-form-spinbutton
                                v-model="selectedProductQuantity"
                                min="1"
                                max="100"
                                size="lg"
                            ></b-form-spinbutton>
                        </div> -->
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12">
                        <b-card-sub-title>
                            数量
                        </b-card-sub-title>
                        <b-form-spinbutton
                            v-model="selectedProductQuantity"
                            min="1"
                            max="100"
                            size="lg"
                        ></b-form-spinbutton>
                    </b-col>
                </b-row>
            </b-container>
            <template #modal-footer>
                <!-- <b-container fluid> -->
                    <b-row>
                        <b-col align="right" class="add_sales_detail_product_footer_col">
                            <b-button
                                variant="secondary"
                                @click="close"
                                class="btn_close"
                                style="margin-right: 15px;"
                            >
                                閉じる
                            </b-button>
                            <b-button
                                variant="primary"
                                :disabled=isDisabled
                                @click="add"
                            >
                                追加
                            </b-button>
                        </b-col>
                    </b-row>
                <!-- </b-container> -->
            </template>
        </b-modal>
    </div>
</template>

<script>
import _ from 'lodash'
import { Const } from '@/assets/js/const'
const Con = new Const()
import SelectForm from '@/components/common/parts/SelectForm'
import utilsMixin from '@/mixins/utils'
import Vue from 'vue'

export default {
    name: 'InputSalesAddDetailProductDialogItem',
    props: {
    },
    components: {
        SelectForm,
    },
    data: () => ({
        dialog: false,

        selectedProduct: null,
        selectedProductQuantity: 1,
    }),
    computed: {
        isDisabled () {
            // if (this.customerNo == ''
            //     || this.customerNoError.length > 0
            //     || this.customerInfo == null) {
            //     return true
            // }
            return false
        },
    },
    watch: {
    },
    created () {
    },
    mounted () {
    },
    methods: {
        init () {
            this.selectedProduct = null
            this.selectedProductQuantity = 1
        },
        close () {
            this.dialog = false
        },
        initClose () {
            this.init()
            this.dialog = false
        },
        open (data) {
            this.dialog = true
            this.selectedProduct = data
        },
        add () {
            this.$emit('addStack', this.selectedProduct, this.selectedProductQuantity)
            this.initClose()
        },
    },
    mixins: [
        utilsMixin,
    ]
}

</script>

<style lang="scss" scoped>

    .product_item_area {
        .product_item_thumbnail {
            height: 100%;
            width: 140px;
            margin: 0 auto;
            display: block;
        }

        .product_item_name {
            height: 65%;
        }
        .product_item_price {
            height: 35%;
        }
    }

    .add_sales_detail_product_footer_col {

    }
</style>
