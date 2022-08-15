<template>
    <v-container
        fluid
        :class="{'selected_product_padding': isShowSelectedProductFooter}"
    >
        <KanaFilterBtn
            @kanaFilter="kanaFilter"
        />
        <v-row>
            <v-col v-if="dispItems == undefined || dispItems == null || dispItems.length == 0">
                <v-card-subtitle>
                    対象の商品は存在しません。
                </v-card-subtitle>
            </v-col>
            <v-col
                cols="12"
                v-for="(item, i) in dispItems"
                :key="i"
                class="py-1 px-0"
            >
                <v-card
                    class="pt-4"
                    outlined
                    style="cursor: pointer;"
                    @click="toProductDetail(item)"
                >
                    <v-row style="max-width: 100%; margin: 0 auto;">
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
                                            style="font-size: 16px;"
                                        >
                                            <i class='bx bx-yen'></i> <span
                                                style="font-weight: 200;"
                                            >{{ item.price | priceLocaleString }}</span>
                                        </p>
                                    </div>
                                    <div class="mt-1 mb-2">
                                        <b-form-spinbutton
                                            id="sb-inline"
                                            v-model="item.quantity"
                                            size="sm"
                                            min="0"
                                            @change="changeQuantity(item)"
                                        ></b-form-spinbutton>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;" class="mt-5 mb-2">
                                        <vs-button
                                            style="width: 160px; border-radius: 13px;"
                                            @click.stop="addCart(item, i)"
                                        >
                                            追加
                                        </vs-button>
                                        <!-- <b-form-spinbutton
                                            id="sb-inline"
                                            v-model="items[i].quantity"
                                            inline
                                            size="sm"
                                            style="height: 20px; margin: auto;"
                                            min="0"
                                            @change="changeQuantity(item)"
                                        ></b-form-spinbutton> -->
                                        <vs-button
                                            circle
                                            icon
                                            border
                                            success
                                            @click="openAddOption(item, i)"
                                            :disabled="isDisabled(item)"
                                        >
                                            <i class='bx bx-plus' ></i>
                                        </vs-button>
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
                    </v-row>
                </v-card>
            </v-col>

            <v-col
                cols="12"
                class="pt-4 pb-9 mb-5"
            >
                <vs-pagination
                    v-model="currentPage"
                    :length="pageNum"
                    @input="changePage"
                />
            </v-col>

            <!-- <v-col cols="12"

            >

            </v-col> -->

            <AccountAddOption
                ref="accountAddOption"
                @addSelectedProductOpt="addOpt"
            />
        </v-row>
    </v-container>
</template>

<script>

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
        test: 1,
        items: [],
        // large: 1,
        // middle: 0,
        // small: 0,
        currentPage: 1,
        pageNum: 0,
        dispItems: [],
    }),
    components: {
        SpinButton,
        AccountAddOption,
        KanaFilterBtn,
    },
    beforeCreate () {
    },
    created () {
        // const large = this.$route.params.large
        // const middle = this.$route.params.middle
        // const small = this.$route.params.small

        const selectedProductList = _.cloneDeep(this.selectedProduct)
        const customerBottleList = _.cloneDeep(this.headerInfo.customer.bottle)
        console.log('customerBottleList', customerBottleList)
        const copyItems = _.cloneDeep(this.productByCategory[this.large][this.middle][this.small])
        // let slicedArray = this.divideArrIntoPieces(copyItems, 5)
        // this.items = copyItems


        console.log('selectedProductList', selectedProductList)
        console.log('customerBottleList', customerBottleList)
        console.log('copyItems', copyItems)


        let items = copyItems.map(function(ele) {
            const selectedIdx = selectedProductList.findIndex(e => e.id == ele.id)
            const bottleIdx = customerBottleList.findIndex(e => e.product.id == ele.id)
            if (selectedIdx != -1) {
                ele.quantity = selectedProductList[selectedIdx].quantity
            } else {
                ele.quantity = 0
            }

            if (bottleIdx != -1) {
                ele.isBottle = true
            } else {
                ele.isBottle = false
            }

            ele.fixedPrice = ele.price
            ele.taxFree = false
            return ele
        })
        this.items = items
        console.log('this.items', this.items)
        let slicedArray = this.divideArrIntoPieces(_.cloneDeep(items), 5)
        this.dispItems = slicedArray[0]
        this.pageNum = slicedArray.length
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
        changeQuantity (item) {
            this.updateSelectedProductQuantity(item)
        },
        addOpt (item, index) {
            console.log('item', item, index)
            this.items[index].quantity = item.quantity
        },
        isDisabled (item) {
            if (item.quantity != 0) {
                return true
            }
            return false
        },
        kanaFilter (key) {
            // const large = this.$route.params.large
            // const middle = this.$route.params.middle
            // const small = this.$route.params.small
            const selectedProductList = _.cloneDeep(this.selectedProduct)
            const customerBottleList = _.cloneDeep(this.headerInfo.customer.bottle)
            let copyItems = _.cloneDeep(this.productByCategory[this.large][this.middle][this.small])

            if (key != 10) {
                copyItems = copyItems.filter(item => item.filter_key == key)
            }

            console.log('selectedProductList', selectedProductList)
            console.log('customerBottleList', customerBottleList)
            console.log('copyItems', copyItems)

            let items = copyItems.map(function(ele) {
                const selectedIdx = selectedProductList.findIndex(e => e.id == ele.id)
                const bottleIdx = customerBottleList.findIndex(e => e.product.id == ele.id)
                if (selectedIdx != -1) {
                    ele.quantity = selectedProductList[selectedIdx].quantity
                } else {
                    ele.quantity = 0
                }

                if (bottleIdx != -1) {
                    ele.isBottle = true
                } else {
                    ele.isBottle = false
                }

                ele.fixedPrice = ele.price
                ele.taxFree = false
                return ele
            })

            this.items = items
            this.currentPage = 1
            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(items), 5)
            this.dispItems = slicedArray[0]
            this.pageNum = slicedArray.length
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
        // setCategory (large, middle, small) {
        //
        //     const selectedProductList = _.cloneDeep(this.selectedProduct)
        //     const copyItems = _.cloneDeep(this.productByCategory[large][middle][small])
        //     console.log('copyItems', copyItems, this.large, this.middle, this.small)
        //     this.items = copyItems.map(function(ele) {
        //         const idx = selectedProductList.findIndex(e => e.id == ele.id)
        //         if (idx != -1) {
        //             ele.quantity = selectedProductList[idx].quantity
        //         } else {
        //             ele.quantity = 0
        //         }
        //         ele.fixedPrice = ele.price
        //         ele.taxFree = false
        //         return ele
        //     })
        // }
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
</style>
