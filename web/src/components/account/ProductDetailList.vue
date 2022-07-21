<template>
    <v-row>
        <v-col
            cols="12"
            v-for="(item, i) in items"
            :key="i"
            class="py-1"
        >
            <v-card
                class="pt-4"
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
                                <div style="display: flex;" class="mt-2">
                                    <vs-button
                                        style="width: 100px; border-radius: 13px;"
                                        @click.stop="addCart(item, i)"
                                    >
                                        追加
                                    </vs-button>
                                    <b-form-spinbutton
                                        id="sb-inline"
                                        v-model="items[i].quantity"
                                        inline
                                        size="sm"
                                        style="height: 20px; margin: auto;"
                                        min="0"
                                        @change="changeQuantity(item)"
                                    ></b-form-spinbutton>
                                    <!-- <SpinButton
                                    /> -->
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

        <AccountAddOption
            ref="accountAddOption"
            @addSelectedProductOpt="addOpt"
        />
    </v-row>
</template>

<script>

import AccountAddOption from '@/components/account/dialog/AccountAddOption'
import SpinButton from '@/components/account/SpinButton'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'

export default {
    name: 'ProductDetailListItem',
    data: () => ({
        test: 1,
        items: [],
    }),
    components: {
        SpinButton,
        AccountAddOption,
    },
    beforeCreate () {
    },
    created () {
        const large = this.$route.params.large
        const middle = this.$route.params.middle
        const small = this.$route.params.small
        const selectedProductList = _.cloneDeep(this.selectedProduct)
        const copyItems = _.cloneDeep(this.productByCategory[large][middle][small])
        this.items = copyItems.map(function(ele) {
            const idx = selectedProductList.findIndex(e => e.id == ele.id)
            if (idx != -1) {
                ele.quantity = selectedProductList[idx].quantity
            } else {
                ele.quantity = 0
            }
            ele.fixedPrice = ele.price
            ele.taxFree = false
            return ele
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
            this.items[idx].quantity += 1
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
        }
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
    }
    .undo-btn {
        font-size: 35px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
