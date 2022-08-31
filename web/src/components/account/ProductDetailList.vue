<template>
    <v-container
        fluid
        :class="{'selected_product_padding': isShowSelectedProductFooter}"
        class="px-4"
    >
        <KanaFilterBtn
            @kanaFilter="kanaFilter"
        />
        <div v-if="loading" style="text-align: center;">
            <v-progress-circular
                indeterminate
                color="primary"
                style="text-align: center;"
            ></v-progress-circular>
        </div>
        <v-row v-else class="px-1">
            <v-col v-if="dispItems == undefined || dispItems == null || dispItems.length == 0">
                <v-card-subtitle>
                    対象の商品は存在しません。
                </v-card-subtitle>
            </v-col>
            <v-col
                cols="12"
                v-for="(item, i) in dispItems"
                :key="i"
                class="px-1 py-2"
            >
            <!-- class="pt-4" -->
                <v-card
                    flat
                    @click.stop="toProductDetail(item)"
                    :ripple="false"
                >
                    <v-container fluid>
                        <v-row>
                            <v-col cols="9" class="px-0">
                                <v-card-subtitle style="font-size: 12px;" class="pb-1 pr-0">
                                    {{ item.name }}
                                </v-card-subtitle>
                                <v-card-text style="font-size: 12px;" class="pb-0 pr-0">
                                    <v-chip
                                        v-if="item.taxFree"
                                        :ripple="false"
                                        small
                                    >
                                        非課税
                                    </v-chip>
                                    <span
                                        v-if="item.fixed"
                                        class="text-right"
                                        style="font-size: 12px; color: rgba(50, 50, 50, 0.8);"
                                    >
                                        <i class='bx bx-yen'></i>
                                        {{ item.fixedPrice | priceLocaleString }}
                                    </span>
                                    <span
                                        style="font-size: 12px;"
                                        :class="{'is_fixed': isFixed(item)}"
                                    >
                                        <i class='bx bx-yen'></i>
                                        {{ item.price | priceLocaleString }}
                                    </span>
                                </v-card-text>
                                <v-card-actions class="pt-0">
                                    <b-form-spinbutton
                                        id="sb-inline"
                                        v-model="item.quantity"
                                        size="sm"
                                        min="0"
                                        style="width: 200px;"
                                        class="ml-4"
                                        @change="changeQuantity(item, i)"
                                    ></b-form-spinbutton>
                                    <vs-button
                                        icon
                                        circle
                                        border
                                        primary
                                        @click="openAddOption(item, i)"
                                        :disabled="isDisabled(item)"
                                    >
                                        <i class='bx bx-plus'></i>
                                    </vs-button>
                                </v-card-actions>
                                <!-- <v-card-actions>
                                    <vs-button
                                        style="width: 200px; border-radius: 13px;"
                                        @click.stop="addCart(item, i)"
                                    >
                                        追加
                                    </vs-button>
                                </v-card-actions> -->
                                <v-chip
                                    v-if="item.isBottle"
                                    color="primary"
                                    class="ml-4"
                                    small
                                >
                                    ボトル有
                                </v-chip>
                            </v-col>
                            <v-col cols="3" class="px-0">
                                <v-badge
                                    right
                                    :content="selectedValue(item)"
                                    :value="selectedValue(item)"
                                    style="width: 100%; height: 100%;"
                                    offset-x="30"
                                    offset-y="20"
                                    class="pt-4"
                                >
                                    <!-- <v-img
                                        v-if="item.thumbnail != null"
                                        class="white--text align-end"
                                        height="120px"
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
                                    </v-img> -->
                                    <img
                                        v-if="item.thumbnail != null"
                                        style="height: 100px; width: 100%;"
                                        :src="item.thumbnail"
                                    >
                                    <img
                                        v-else
                                        style="height: 100px; width: 100%;"
                                        src="@/static/img/noimage5.png"
                                    >

                                    <!-- <img
                                        v-if="item.thumbnail == null && item.category.large_category == 1"
                                        src="@/static/img/酒2.png"
                                        style="height: 100px; width: 100%;"
                                    >
                                    <img
                                        v-if="item.thumbnail == null && item.category.large_category == 2"
                                        src="@/static/img/天ぷら1.jpg"
                                        style="height: 100px; width: 100%;"
                                    > -->

                                </v-badge>
                            </v-col>
                        </v-row>
                    </v-container>

                    <!-- <v-row style="max-width: 100%; margin: 0 auto;">
                        <v-col cols="3" class="pl-1 pt-0">
                            <v-badge
                                left
                                :content="selectedValue(item)"
                                :value="selectedValue(item)"
                                offset-x="30"
                                offset-y="20"
                                style="width: 80px; height: 120px;"
                            >
                                <v-img
                                    v-if="item.thumbnail != null"
                                    class="white--text align-end"
                                    height="120px"
                                    :src="item.thumbnail"
                                    contain
                                >
                                </v-img>
                                <v-img
                                    v-else
                                    class="white--text align-end"
                                    height="120px"
                                    src="http://localhost:8000/media/upload/酒6.png"
                                    contain
                                >
                                </v-img>
                            </v-badge>
                            <v-chip
                                v-if="item.isBottle"
                                class="ml-2"
                                color="success"
                            >
                                ボトル有
                            </v-chip>
                        </v-col>
                        <v-col cols="9" class="pl-2 pt-0">
                            <v-row>
                                <v-col
                                    cols="12"
                                    class="py-0"
                                >
                                    <div
                                        class="pl-2"
                                        style="height: 40px;"
                                    >
                                        <p
                                            style="font-size: 11px; line-height: 1.7;"
                                            class="mb-0"
                                        >
                                            {{ item.name }}
                                        </p>
                                    </div>
                                    <div
                                        class="pl-2 mt-1"
                                        style="height: 20px;"
                                    >
                                        <p
                                            class="mb-0"
                                            style="font-size: 16px; text-align: right;"
                                        >
                                            <span
                                                v-if="item.taxFree"
                                            >非課税</span>
                                            <span
                                                v-if="item.fixed"
                                                class="text-right"
                                                style="font-size: 16px; color: red;"
                                            >
                                                <i class='bx bx-yen'></i>
                                                {{ item.fixedPrice | priceLocaleString }}
                                            </span>
                                            <i class='bx bx-yen'></i>
                                            <span
                                                style="font-weight: 200;"
                                                :class="{'is_fixed': isFixed(item)}"
                                            >
                                                {{ item.price | priceLocaleString }}
                                            </span>
                                        </p>
                                    </div>
                                    <div class="mt-1 mb-2">
                                        <b-form-spinbutton
                                            id="sb-inline"
                                            v-model="item.quantity"
                                            size="sm"
                                            min="0"
                                            @change="changeQuantity(item, i)"
                                        ></b-form-spinbutton>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;" class="mt-5 mb-2">
                                        <vs-button
                                            style="width: 160px; border-radius: 13px;"
                                            @click.stop="addCart(item, i)"
                                        >
                                            追加
                                        </vs-button>
                                        <vs-button
                                            border
                                            success
                                            @click="openAddOption(item, i)"
                                            :disabled="isDisabled(item)"
                                        >
                                            詳細
                                            <i class='bx bx-plus' ></i>
                                        </vs-button>
                                    </div>

                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row> -->
                </v-card>
            </v-col>

            <v-col
                cols="12"
                class="pt-4 pb-9 mb-5"
            >
                <v-pagination
                    v-model="currentPage"
                    :length="pageNum"
                    @input="changePage"
                    circle
                />
            </v-col>
        </v-row>
        <AccountAddOption
            ref="accountAddOption"
            @addSelectedProductOpt="addOpt"
        />
    </v-container>
</template>

<script>

import Vue from 'vue'
import AccountAddOption from '@/components/account/dialog/AccountAddOption'
import SpinButton from '@/components/account/SpinButton'
import KanaFilterBtn from '@/components/account/parts/KanaFilterBtn'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'

export default {
    name: 'ProductDetailListItem',
    props: {
        large: {
            type: Number,
            required: true,
            default: 1,
        },
        middle: {
            type: Number,
            required: true,
            default: 0,
        },
        small: {
            type: Number,
            required: true,
            default: 0,
        },
        headerInfo: {
            type: Object,
            required: false,
        }
    },
    data: () => ({
        // 全体の配列
        items: [],
        currentPage: 1,
        pageNum: 0,

        // 表示用
        dispItems: [],

        loading: true,
    }),
    components: {
        SpinButton,
        AccountAddOption,
        KanaFilterBtn,
    },
    beforeCreate () {
    },
    created () {
        this.loading = true

        // カートの中身
        const selectedProductList = _.cloneDeep(this.selectedProduct)

        // 顧客のボトルリスト
        const customerBottleList = _.cloneDeep(this.headerInfo.customer.bottle)

        // 選んだカテゴリの商品を取得しディープコピー
        const copyItems = _.cloneDeep(this.productByCategory[this.large][this.middle][this.small])

        console.log('copyItems', copyItems)

        // 選択中の商品か、
        // 顧客がボトル所持しているか、
        let items = copyItems.map(function(ele) {
            const selectedIdx = selectedProductList.findIndex(e => e.id == ele.id)
            const bottleIdx = customerBottleList.findIndex(e => e.product.id == ele.id)
            if (selectedIdx != -1) {
                ele.quantity = selectedProductList[selectedIdx].quantity
                ele.fixedPrice = selectedProductList[selectedIdx].fixedPrice
                ele.taxFree = selectedProductList[selectedIdx].taxFree
                ele.fixed = selectedProductList[selectedIdx].fixed
            } else {
                ele.quantity = 0
                ele.taxFree = false
            }

            if (bottleIdx != -1) {
                ele.isBottle = true
            } else {
                ele.isBottle = false
            }

            return ele
        })

        this.items = items
        console.log('this.items', items)
        let slicedArray = this.divideArrIntoPieces(_.cloneDeep(items), 5)
        this.dispItems = slicedArray[0]
        this.pageNum = slicedArray.length

        this.loading = false
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
        isShowSelectedProductFooter () {
            if (this.selectedProduct != undefined && this.selectedProduct.length != 0) {
                return true
            }
            return false
        },
    },
    methods: {
        ...mapMutations([
            'addSelectedProduct',
            'updateSelectedProduct',
            'updateSelectedProductQuantity',
            'deleteSelectedProduct',
            'initSelectedProduct',
            'setSelectedProductSalesId',
        ]),
        toProductDetail (item) {
            // console.log('toProductDetail', item)
        },
        addCart (data, idx) {
            let index = idx + ((this.currentPage - 1) * 5)
            this.dispItems[idx].quantity += 1
            this.items[index].quantity += 1
            this.setSelectedProductSalesId(this.$route.params.id)
            this.addSelectedProduct(_.cloneDeep(data))
        },
        selectedValue (item) {
            // const target = _.cloneDeep(this.selectedProduct).filter(s => s.id == item.id)
            // console.log('target', target)
            // let cnt = 0
            // for (const i of target) {
            //     cnt += i.quantity
            // }
            // return cnt
            const index = this.selectedProduct.findIndex(s => s.id == item.id)
            if (index !== -1) return this.selectedProduct[index].quantity
            return 0
        },
        openAddOption (item, idx) {
            this.$refs.accountAddOption.open(item, idx)
        },
        changeQuantity (item, idx) {
            console.log('changeQuantity', item, idx)
            this.updateSelectedProductQuantity(item)

            let fixed = true
            if (item.quantity == 0 || item.price == item.fixedPrice) {
                fixed = false
                item.fixedPrice = item.price
                item.taxFree = false
            }
            item.fixed = fixed

            const index1 = this.items.findIndex(s => s.id == item.id)
            console.log('index1', index1)
            if (index1 != -1) {
                Vue.set(this.items, index1, item)
            }

            const index2 = this.dispItems.findIndex(s => s.id == item.id)
            console.log('index2', index2)
            if (index2 != -1) {
                Vue.set(this.dispItems, index2, item)
            }
        },
        addOpt (item, index) {
            console.log('addOpt', item)
            let fixed = true
            if (item.quantity == 0 || item.price == item.fixedPrice) {
                fixed = false
                item.fixedPrice = item.price
            }
            item.fixed = fixed

            const index1 = this.items.findIndex(s => s.id == item.id)
            if (index1 != -1) {
                Vue.set(this.items, index1, item)
            }

            const index2 = this.dispItems.findIndex(s => s.id == item.id)
            if (index2 != -1) {
                Vue.set(this.dispItems, index2, item)
            }

            console.log('item', item, index)
            console.log('this.items', this.items)
            console.log('this.dispItems', this.dispItems)

            // this.items[index].quantity = item.quantity
            // this.items[index].taxFree = item.taxFree
            // this.items[index].fixed = true
            // this.items[index].fixedPrice = item.fixedPrice
            // this.dispItems[index].quantity = item.quantity
            // this.dispItems[index].fixed = true
            // this.dispItems[index].fixedPrice = item.fixedPrice
            // this.dispItems[index].taxFree = item.taxFree
        },
        isDisabled (item) {
            // 2022-08-19プラスの制御はとりあえずやめる。
            // ☞今後、定価データ、追加データを別々に注文出来るようにする？
            // if (item.quantity != 0) {
            //     return true
            // }
            return false
        },
        kanaFilter (key) {
            this.loading = true

            // カートの中身
            const selectedProductList = _.cloneDeep(this.selectedProduct)

            // 顧客のボトルリスト
            const customerBottleList = _.cloneDeep(this.headerInfo.customer.bottle)

            // 選んだカテゴリの商品を取得しディープコピー
            let copyItems = _.cloneDeep(this.productByCategory[this.large][this.middle][this.small])

            console.log('copyItems', copyItems)

            // フィルター全選択じゃなければ
            if (key != 10) {
                copyItems = copyItems.filter(item => item.filter_key == key)
            }

            // 選択中の商品か、
            // 顧客がボトル所持しているか、
            let items = copyItems.map(function(ele) {
                const selectedIdx = selectedProductList.findIndex(e => e.id == ele.id)
                const bottleIdx = customerBottleList.findIndex(e => e.product.id == ele.id)
                if (selectedIdx != -1) {
                    ele.quantity = selectedProductList[selectedIdx].quantity
                    ele.fixedPrice = selectedProductList[selectedIdx].fixedPrice
                    ele.taxFree = selectedProductList[selectedIdx].taxFree
                    ele.fixed = selectedProductList[selectedIdx].fixed
                } else {
                    ele.quantity = 0
                    ele.taxFree = false
                }

                if (bottleIdx != -1) {
                    ele.isBottle = true
                } else {
                    ele.isBottle = false
                }
                return ele
            })

            this.items = items
            this.currentPage = 1
            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(items), 5)
            this.dispItems = slicedArray[0]
            this.pageNum = slicedArray.length

            this.loading = false
        },
        sliceArray (array, number) {
            const length = Math.ceil(array.length / number)
            console.log('length', length)
            return new Array(length).fill().map((_, i) => {
                console.log(`i=${i}, i*number=${i*number}, (i+1)*number=${(i+1)*number}`)
                array.slice(i * number, (i + 1) * number)
            })
        },
        divideArrIntoPieces (arr,n){
            var arrList = [];
            var idx = 0;
            while(idx < arr.length){
                arrList.push(arr.splice(idx,idx+n));
            }
            return arrList;
        },
        changePage (pageNumber) {
            this.currentPage = pageNumber
            let items = this.divideArrIntoPieces(_.cloneDeep(this.items), 5)
            this.dispItems = items[pageNumber-1]
        },
        isFixed (item) {
            if (item.fixed) return true
            return false
        }
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
    }
    .selected_product_padding {
        padding-bottom: 80px;
    }

    .is_fixed {
        text-decoration: line-through;
        font-weight: 100;
        color: rgba(139, 139, 139, 0.5);
    }
</style>
