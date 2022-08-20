<template>
    <div>
        <div v-if="loading" style="text-align: center;">
            <v-progress-circular
                indeterminate
                color="primary"
                style="text-align: center;"
            ></v-progress-circular>
        </div>
        <v-row v-else>
            <v-col
                v-if="items.length == 0"
                cols="12"
            >
                <v-card-text>商品が選択されていません。</v-card-text>
            </v-col>
            <v-col
                v-else
                cols="12"
                v-for="(item, i) in items"
                :key="i"
                class="py-1"
            >
                <v-divider
                    v-if="i != 0"
                    class="mx-4"
                />
                <v-card
                    flat
                    class="pt-4 pb-4"
                    style="cursor: pointer;"
                    @click="toProductDetail(item)"
                >
                    <v-row style="max-width: 100%; margin: 0 auto;">
                        <v-col cols="4" class="pl-1 pt-2">
                            <v-img
                                v-if="item.thumbnail != null"
                                class="white--text align-end"
                                mix-height="120px"
                                :src="item.thumbnail"
                                contain
                            >
                            </v-img>
                            <v-img
                                v-else
                                class="white--text align-end"
                                height="120px"
                                src="http://localhost:8000/media/upload/酒2.png"
                                contain
                            >
                            </v-img>
                            <v-chip
                                v-if="item.isBottle"
                                class="ml-7"
                                color="success"
                            >
                                ボトル有
                            </v-chip>
                        </v-col>
                        <v-col cols="8" class="pl-2 pt-0">
                            <v-row>
                                <v-col
                                    cols="12"
                                    class="py-0"
                                >
                                    <div
                                        class="pl-2"
                                        style="min-height: 70px;"
                                    >
                                        <label style="font-size: 12px; color: rgba(0, 0, 0, 0.64);">商品名</label>
                                        <p
                                            style="font-size: 15px; line-height: 1.7;"
                                            class="mb-0 text-h7"
                                        >{{ item.name }}</p>
                                    </div>
                                    <div
                                        class="pl-2"
                                    >
                                        <label style="font-size: 12px; color: rgba(0, 0, 0, 0.64);">定価</label>
                                        <p
                                            style="font-size: 11px; line-height: 1.7; display: inline; float: right;"
                                            class="mb-0"
                                        > <i class='bx bx-yen'></i> {{ item.price | priceLocaleString }}</p>
                                    </div>
                                    <div
                                        class="pl-2"
                                    >
                                        <label style="font-size: 12px; color: rgba(0, 0, 0, 0.64);">実価格</label>
                                        <v-text-field
                                            v-model="item.fixedPrice"
                                            placeholder="実価格"
                                            class="right-input pt-0"
                                            @blur="focusOutFixedPrice(item)"
                                        ></v-text-field>
                                    </div>
                                </v-col>
                                <!-- <v-col cols="3">
                                    1
                                </v-col>
                                <v-col cols="3">
                                    2
                                </v-col> -->
                            </v-row>
                        </v-col>
                        <!-- <v-row> -->
                            <div style="display: flex; justify-content: space-around;">
                                <div>
                                    <label style="font-size: 12px; color: rgba(0, 0, 0, 0.64);">数量</label>
                                    <b-form-spinbutton
                                        id="sb-inline"
                                        v-model="item.quantity"
                                        @change="updateQuantity(item)"
                                    ></b-form-spinbutton>
                                </div>
                                <div>
                                    <!-- <v-checkbox
                                        v-model="item.taxFree"
                                        label="非課税"
                                        @change="updateTaxFree(item)"
                                    ></v-checkbox> -->
                                    <vs-checkbox
                                        class="mt-4"
                                        v-model="item.taxFree"
                                        @change="updateTaxFree(item)"
                                    >非課税</vs-checkbox>
                                </div>
                                <div>
                                    <vs-button
                                        class="mt-4"
                                        circle
                                        icon
                                        danger
                                        @click="deleteProduct(item)"
                                    >
                                        <i class='bx bx-trash' ></i>
                                    </vs-button>
                                </div>
                            </div>
                        <!-- </v-row> -->
                    </v-row>
                </v-card>


            </v-col>

            <v-card
                flat
            >
                <v-divider
                    class="mx-4"
                />
                <v-card-title class="text-h7 py-0">
                    総計
                </v-card-title>
                <v-card-text class="text-right text-h7 py-2">
                    注文数 : <SelectedProductTotalCnt/>
                </v-card-text>
                <v-card-text class="text-right text-h7 py-2">
                    総計(税抜) : <SelectedProductTotalPrice/>
                </v-card-text>
                <v-card-text class="text-right text-h7 py-2">
                    総計(税込) : <SelectedProductTotalPrice :tax=true />
                </v-card-text>
            </v-card>
        </v-row>
    </div>
</template>

<script>

import SpinButton from '@/components/account/SpinButton'
import SelectedProductTotalCnt from '@/components/account/parts/SelectedProductTotalCnt'
import SelectedProductTotalPrice from '@/components/account/parts/SelectedProductTotalPrice'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'
import Vue from 'vue'

export default {
    name: 'OrderListItem',
    data: () => ({
        items: [],
        headerInfo: {},
        loading: true,
    }),
    props: {
    },
    components: {
        SpinButton,
        SelectedProductTotalCnt,
        SelectedProductTotalPrice,
    },
    beforeCreate () {
    },
    created () {

        const large = this.$route.params.large
        const middle = this.$route.params.middle
        const small = this.$route.params.small

        this.getHeaderInfo()
        .then(res=> {
            const customerBottleList = _.cloneDeep(this.headerInfo.customer.bottle)
            this.items = _.cloneDeep(this.selectedProductList).map(function(ele) {
                const bottleIdx = customerBottleList.findIndex(e => e.id == ele.id)

                if (bottleIdx != -1) {
                    ele.isBottle = true
                } else {
                    ele.isBottle = false
                }
                return ele
            })
            this.loading = false
        })
        .catch(e => {
            this.items = _.cloneDeep(this.selectedProduct)
            this.loading = false
        })
    },
    beforeMount () {
    },
    mounted () {
    },
    beforeUpdate () {
    },
    update () {
    },
    beforeDestroy () {
    },
    destoryd () {
    },
    computed: {
        ...mapGetters([
            'product',
            'popularProduct',
            'productByCategory',
            'selectedProduct',
        ]),
    },
    watch: {
    },
    methods: {
        ...mapMutations([
            'addSelectedProduct',
            'updateSelectedProduct',
            'deleteSelectedProduct',
            'initSelectedProduct',
        ]),
        toProductDetail (item) {
            // console.log('toProductDetail', item)
        },
        addCart (data, idx) {
            // console.log('addSelectedProduct', item)
            this.addSelectedProduct(_.cloneDeep(data))
            this.items[idx].quantity = 1
        },
        updateQuantity (item) {
            const payload = _.cloneDeep(item)
            this.updateSelectedProduct(payload)
        },
        deleteProduct (item) {
            this.deleteSelectedProduct(item)
            const index = this.items.findIndex(s => s.id === item.id)
            if (index !== -1) this.items = this.items.filter((_, i) => i !== index)
        },
        updateTaxFree (item) {
            const payload = _.cloneDeep(item)
            this.updateSelectedProduct(payload)
            // ↓いらんかった
            // const index = this.items.findIndex(s => s.id === payload.id)
            // Vue.set(this.items, index, payload)
        },
        getHeaderInfo () {
            return new Promise((resolve, reject) => {
                this.$axios({
                    method: 'get',
                    url: `/api/sales/${this.$route.params.id}/`
                })
                .then(res => {
                    console.log(res)
                    this.headerInfo = res.data
                    resolve(res.data)
                })
                .catch(e => {
                    console.log(e)
                    reject(e)
                })
            })
        },
        focusOutFixedPrice (item) {
            console.log('focusOutFixedPrice', item)
            this.updateSelectedProduct(item)
        }
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
    }
    .undo-btn {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
