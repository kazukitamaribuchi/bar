<template>
    <b-modal
        v-model="dialog"
        title="明細追加"
        header-bg-variant="primary"
        header-text-variant="light"
        ok-title="追加"
        cancel-title="閉じる"
        size="xl"
    >
        <b-row class="add_sales_detail_product_area">
            <b-col cols="2">
                <b-list-group>
                    <b-list-group-item
                        button
                        @click="showTopPopularProduct"
                    >
                        TOP
                    </b-list-group-item>
                    <label
                        v-for="(head, id) in siderbaritems"
                        :key=id
                        button
                        class="mt-3"
                    >
                        {{ head.text }}
                        <b-list-group-item
                            v-for="(item, idx) in head.items"
                            :key=idx
                            button
                            @click="selectProductCategory(item)"
                        >
                            {{ item.text }}
                        </b-list-group-item>
                    </label>
                </b-list-group>
            </b-col>
            <b-col v-if="selectedProductType == null">
                <b-card-title>
                    人気商品
                </b-card-title>
                <b-row>
                    <b-col
                        cols="2"
                        v-for="item in popularProduct.popular"
                        :key=item.id
                    >
                        <b-card
                            class="productCard"
                            @click="selectProduct(item)"
                            @dblclick="directAddStack(item)"
                            body-class="productCardBody"
                        >
                            <img
                                v-if="item.thumbnail != null"
                                class="product_item_thumbnail"
                                :src="getImgLink(item.thumbnail)"
                            >
                            <img
                                v-else
                                class="product_item_thumbnail"
                                src="@/static/img/noimage8.png"
                            >
                            <div class="product_desc_area">
                                <div class="product_name_area">
                                    <b-card-text class="product_long_name" v-if="item.name.length > 20">
                                        {{ item.name }}
                                    </b-card-text>
                                    <b-card-text class="product_name" v-else>
                                        {{ item.name }}
                                    </b-card-text>
                                </div>
                                <div class="product_price_area">
                                    {{ item.price | priceLocaleString }} 円
                                </div>
                            </div>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
            <b-col v-else>
                <!-- <b-card-title>
                    カテゴリ毎
                </b-card-title> -->
                <InputSalesAddDetailDialogHeader
                    :productType=selectedProductType
                    @update="updateProductByCategoryList"
                />
                <!-- @update="productByCategoryList = $event" -->
                <b-row>
                    <b-col
                        cols="2"
                        v-for="item in dispItems"
                        :key=item.id
                    >
                        <b-card
                            class="productCard"
                            @click="selectProduct(item)"
                            @dblclick="directAddStack(item)"
                            body-class="productCardBody"
                        >
                            <img
                                v-if="item.thumbnail != null"
                                class="product_item_thumbnail"
                                :src="getImgLink(item.thumbnail)"
                            >
                            <img
                                v-else
                                class="product_item_thumbnail"
                                src="@/static/img/noimage8.png"
                            >
                            <div class="product_desc_area">
                                <div class="product_name_area">
                                    <b-card-text class="product_long_name" v-if="item.name.length > 20">
                                        {{ item.name }}
                                    </b-card-text>
                                    <b-card-text class="product_name" v-else>
                                        {{ item.name }}
                                    </b-card-text>
                                </div>
                                <div class="product_price_area">
                                    {{ item.price | priceLocaleString }} 円
                                </div>
                            </div>
                        </b-card>
                    </b-col>

                    <b-pagination
                        v-if="dispItems != undefined"
                        v-model="currentPage"
                        :total-rows="rows"
                        :per-page="perPage"
                        aria-controls="my-table"
                        align="center"
                        @change="changePage"
                    ></b-pagination>
                </b-row>
            </b-col>
        </b-row>
        <template #modal-footer>
            <b-container fluid>
                <b-row>
                    <b-col cols="4">
                        <b-card-title>選択商品</b-card-title>
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
                        <b-row>
                            <b-col cols="8" class="no_margin_no_padding">
                                <div>
                                    <b-card-sub-title>商品名</b-card-sub-title>
                                    <div v-if="selectedProduct != null" class="selected_product_area">
                                        {{ getStrInData(selectedProduct.name) }}
                                    </div>
                                    <div v-else class="selected_product_area">-</div>
                                </div>
                            </b-col>
                            <b-col cols="2" class="no_margin_no_padding">
                                <div>
                                    <b-card-sub-title>定価</b-card-sub-title>
                                    <div class="selected_product_area">
                                        <div v-if="selectedProduct != null">
                                            ￥{{ selectedProduct.price | priceLocaleString }}
                                        </div>
                                        <div v-else> - </div>
                                    </div>
                                </div>
                            </b-col>
                            <b-col cols="2" align="center" class="no_margin_no_padding">
                                <b-card-sub-title>商品を追加する</b-card-sub-title>
                                <b-icon
                                    icon="plus-square"
                                    font-scale="1.5"
                                    variant="success"
                                    class="mt-2 add_sales_detail_add_product_btn"
                                    @click="addStack"
                                ></b-icon>
                            </b-col>
                            <b-col cols="2" class="no_margin_no_padding">
                                <div>
                                    <b-card-sub-title>実価格</b-card-sub-title>
                                    <b-form-input
                                        v-model="actuallyPrice"
                                        type="number"
                                        placeholder="実価格"
                                        required
                                    ></b-form-input>
                                </div>
                            </b-col>
                            <b-col cols="2" align="center" class="no_margin_no_padding">
                                <b-card-sub-title>数量</b-card-sub-title>
                                <b-form-group>
                                    <b-form-group
                                        class="add_sales_detail_quantity_wrap"
                                    >
                                        <SelectForm
                                            :optionType=99
                                            v-model="quantity"
                                        />
                                    </b-form-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="2" align="center" class="no_margin_no_padding">
                                <!-- <b-card-sub-title>税率</b-card-sub-title>
                                <b-form-group>
                                    <b-form-group
                                        class="add_sales_detail_tax_wrap"
                                    >
                                        <SelectForm
                                            :optionType=3
                                            v-model="tax"
                                        />%
                                    </b-form-group>
                                </b-form-group> -->
                                <b-card-sub-title>課税</b-card-sub-title>
                                <b-form-group>
                                    <b-form-checkbox-group
                                        v-model="taxation"
                                        :options=taxationOptions
                                        buttons
                                        bg-variant="success"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="2" align="center" class="no_margin_no_padding">
                                <b-card-sub-title>ボトル登録</b-card-sub-title>
                                <b-button
                                    v-if="bottleCustomerInfo == null"
                                    variant="primary"
                                    @click="addBottleCustomerInfo(0)"
                                    :disabled=isBottleCustomerDisabled
                                >
                                    顧客選択
                                </b-button>
                                <b-button
                                    v-else
                                    variant="danger"
                                    @click="bottleCustomerInfo = null"
                                >
                                    選択解除
                                </b-button>
                            </b-col>
                            <b-col class="no_margin_no_padding">
                                <div>
                                    <b-card-sub-title>ボトル登録会員</b-card-sub-title>
                                    <div v-if="bottleCustomerInfo != null">{{ bottleCustomerInfo.name | truncate(15) }}</div>
                                    <div v-else>-</div>
                                </div>
                            </b-col>
                        </b-row>
                    </b-col>
                </b-row>
                <!-- <b-row class="pt-3">
                    <b-col cols="5" class="add_sales_detail_footer_col">
                        <b-card-sub-title>備考</b-card-sub-title>
                        <b-form-textarea
                            rows="2"
                            no-resize
                            v-model="remarks"
                        ></b-form-textarea>
                    </b-col>
                </b-row> -->
                <b-row class="mt-3">
                    <b-card v-if="selectedProductList.length > 0">
                        <b-container fluid>
                            <b-row>
                                <b-card-title class="mb-4">
                                    選択商品一覧
                                </b-card-title>
                                <table>
                                    <tr>
                                        <th>商品名</th>
                                        <th>実価格</th>
                                        <th>数量</th>
                                        <th>課税</th>
                                        <th>ボトル登録</th>
                                        <th>ボトル登録会員</th>
                                        <!-- <th>備考</th> -->
                                        <th></th>
                                    </tr>
                                    <tr
                                        v-for="(item, id) in selectedProductList"
                                        :key=id
                                    >
                                        <td>{{ item.name }}</td>
                                        <td>
                                            <!-- {{ item.actuallyPrice | priceLocaleString }} -->
                                            <b-form-input
                                                v-model="item.actuallyPrice"
                                                type="number"
                                                required
                                                style="width: 90%;"
                                            ></b-form-input>
                                        </td>
                                        <td>
                                            <!-- {{ item.quantity }} -->
                                            <b-form-spinbutton
                                                v-model="item.quantity"
                                                inline
                                                min=1
                                                size="sm"
                                            ></b-form-spinbutton>
                                        </td>
                                        <td>
                                            <!-- <span v-if="item.taxation">課税</span>
                                            <span v-else>非課税</span> -->
                                            <v-checkbox
                                                class="mt-3"
                                                v-model="item.taxation"
                                            ></v-checkbox>
                                        </td>
                                        <td>
                                            <!-- <v-checkbox
                                                class="mt-3"
                                                v-model="item.bottle"
                                            ></v-checkbox> -->
                                            <b-button
                                                v-if="item.customer == null"
                                                variant="primary"
                                                @click="addBottleCustomerInfo(1, id)"
                                                :disabled=isBottleCustomerDisabledRow(item)
                                            >
                                                顧客選択
                                            </b-button>
                                            <b-button
                                                v-else
                                                variant="danger"
                                                @click="deleteCustomerSelectedProductList(id)"
                                            >
                                                選択解除
                                            </b-button>
                                        </td>
                                        <td v-if="item.customer != null">{{ item.customer.name }}</td>
                                        <td v-else>-</td>
                                        <td>
                                            <b-icon
                                                icon="dash-square"
                                                font-scale="1.5"
                                                variant="danger"
                                                class="mt-2 add_sales_detail_delete_product_btn"
                                                @click="deleteProduct(id)"
                                            ></b-icon>
                                        </td>
                                    </tr>
                                </table>
                            </b-row>
                        </b-container>
                    </b-card>
                </b-row>
                <b-row class="add_cast_footer_bottom_area mt-5">
                    <b-col cols="3">
                        <b-card-sub-title>
                            総計(税抜)
                        </b-card-sub-title>
                        <b-card-title class="mb-0">
                            ￥ {{ totalPrice | priceLocaleString }}
                        </b-card-title>
                    </b-col>
                    <b-col cols="3">
                        <b-card-sub-title>
                            総計(税込)
                        </b-card-sub-title>
                        <b-card-title class="mb-0">
                            ￥ {{ totalTaxPrice | priceLocaleString }}
                        </b-card-title>
                    </b-col>
                    <b-col align="right" class="add_sales_detail_footer_col">
                        <b-button
                            variant="secondary"
                            @click="close"
                            class="btn_close add_sales_detail_footer_area4"
                        >
                            閉じる
                        </b-button>
                        <b-button
                            variant="primary"
                            @click="add"
                            class="add_sales_detail_footer_area4"
                            :disabled=isDisabled
                        >
                            確定する
                        </b-button>
                    </b-col>
                </b-row>
            </b-container>
        </template>

        <InputSalesSelectCustomerDialog
            ref="inputSalesSelectCustomerDialog"
            :customerList="customerList"
            @selectCustomer="selectCustomer"
            @selectCustomerProductList="selectCustomerProductList"
            msg="ボトル登録を行う会員を選択してください。"
            title="ボトル登録会員選択"
        />

    </b-modal>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import InputSalesAddDetailDialogHeader from '@/components/common/dialog/parts/InputSalesAddDetailDialogHeader'
import InputSalesSelectCustomerDialog from '@/components/common/dialog/InputSalesSelectCustomerDialog'
import SelectForm from '@/components/common/parts/SelectForm'
import Decimal from 'decimal.js'
import utilsMixin from '@/mixins/utils'

export default {
    name: 'InputSalesAddDetailDialogItem',
    props: {
        customerList: {
            type: Array,
            required: true,
            default: () => ([]),
        },
    },
    components: {
        InputSalesAddDetailDialogHeader,
        InputSalesSelectCustomerDialog,
        SelectForm,
    },
    data: () => ({
        dialog: false,
        selected: {},

        // ボトル登録する会員 2022/10/23
        bottleCustomerInfo: null,

        quantity: 1,
        actuallyPrice: 0,
        bottleOptions: [
            { text: '登録', value: 1 }
        ],
        taxationOptions: [
            { text: '課税', value: 1 }
        ],
        appointOptions: [
            { text: '指名', value: 0 },
            { text: '本指名', value: 1 },
            { text: '場内指名', value: 2 },
        ],
        quantityOptions: Con.OPTIONS_QUANTITIES,
        taxOptions: Con.OPTIONS_TAX,
        siderbaritems: Con.INPUT_SALES_DETAIL_PRODUCT_CATEGORY_SIDEBAR,
        selectedProductType: null,
        productByCategoryList: [],
        selectedProduct: null,
        selectedProductList: [],
        // remarks: '',
        tax: 10,
        taxation: [1],
        currentPage: 1,
        rows: 1,
        perPage: 12,
        dispItems: [],
    }),
    computed: {
        ...mapGetters([
            'cast',
            // ↓人気商品、カテゴリ別の商品を取るようにする
            'product',
            'productByCategory',
            'popularProduct',
        ]),
        isBottleCustomerDisabled () {
            if (this.customerList.length == 0 ||
                !this.isDrink) {
                return true
            }
            return false
        },
        isDisabled () {
            if (this.selectedProductList.length > 0) return false
            return this.selectedProduct == null
        },
        isDrink () {
            if (this.selectedProduct == null) return false
            if (this.selectedProduct.category.large_category == 1
                && this.selectedProduct.category.middle_category == 0)
            {
                if (this.selectedProduct.category.small_category != 4) {
                    return true
                } else {
                    return false
                }
            }
            return false
        },
        totalPrice () {
            let total = 0
            for (const i in this.selectedProductList) {
                total += this.calcQuantityPrice(
                    this.selectedProductList[i].quantity,
                    Number(this.selectedProductList[i].actuallyPrice),
                )
            }
            return total
            // if (this.selectedProduct == null) return total
            // total += this.calcQuantityPrice(Number(this.actuallyPrice), this.quantity)
            // return total
        },
        totalTaxPrice () {
            let totalTaxFree = 0
            let totalTax = 0
            // 商品毎にtaxが設定されている場合も考慮
            for (const i in this.selectedProductList) {
                // let q = new Decimal(this.selectedProductList[i].quantity)
                let q = this.selectedProductList[i].quantity
                if (!this.selectedProductList[i].taxation) {
                    // TAX無しの場合
                    totalTaxFree += Math.ceil(q * Number(this.selectedProductList[i].actuallyPrice))
                    // total += Math.ceil(q.times(this.selectedProductList[i].actuallyPrice).toNumber())
                } else {
                    // TAX有の場合
                    totalTax += this.calcAddTaxPrice(
                        Math.ceil(q * Number(this.selectedProductList[i].actuallyPrice)),
                        Con.SALES_TAX,
                    )
                }
            }
            const total = totalTaxFree + totalTax
            return total

            // if (this.selectedProduct == null) return total
            // if (this.taxation.length == 0) {
            //     total += this.calcQuantityPrice(
            //         Number(this.actuallyPrice),
            //         this.quantity
            //     )
            // } else {
            //     total += this.calcAddTaxPrice(
            //         this.calcQuantityPrice(
            //             Number(this.actuallyPrice),
            //             this.quantity
            //         ),
            //         Con.SALES_TAX,
            //     )
            // }
            // return total
        },
    },
    watch: {
    },
    created () {
        // this.$eventHub.$off('filterProductCategory')
        // this.$eventHub.$on('filterProductCategory', this.filterProductCategory)
    },
    mounted () {
    },
    methods: {
        open () {
            this.dialog = true
            this.productByCategoryList = _.cloneDeep(this.productByCategory)
        },
        close () {
            this.dialog = false
            this.init()
        },
        directAdd (item) {
            this.selectedProduct = item
            this.add()
        },
        add () {
            if (this.selectedProductList.length > 0) {
                // console.log('this.selectedProductList.length > 0 => addSalesDetailList')
                // console.log('this.selectedProductList', this.selectedProductList)
                this.$emit('addSalesDetailList', this.selectedProductList)
                this.close()
                return
            }

            let actuallyTaxPrice = 0

            if (this.taxation.length != 0) {
                actuallyTaxPrice = this.calcAddTaxPrice(Number(this.actuallyPrice), this.tax)
            } else {
                actuallyTaxPrice = Number(this.actuallyPrice)
            }

            const product = this.selectedProduct
            const data = {
                name: product.name,
                price: product.price,
                actuallyPrice: Number(this.actuallyPrice),
                actuallyTaxPrice: actuallyTaxPrice,
                taxRate: this.tax,
                taxation: this.taxation.length != 0,
                quantity: this.quantity,
                totalPrice: this.totalPrice,
                totalTaxPrice: this.totalTaxPrice,
                thumbnail: product.thumbnail,
                category: product.category,
                // remarks: this.remarks,
                product: product,
                bottle: this.bottleCustomerInfo != null,
                customer: this.bottleCustomerInfo,
            }
            this.init()
            this.$emit('addSalesDetail', data)
            this.close()
        },
        init () {
            this.selected = {}
            this.selectedProductType = null
            this.selectedProduct = null
            this.selectedProductList = []
            // this.remarks = ''
            this.quantity = 1
            this.taxation = [1]
            this.actuallyPrice = 0

            this.bottleCustomerInfo = null
        },
        select (item) {
            if (this.isAppointed(item)) return
            this.selected = item
        },
        getIsAppointedStr (cast) {
            if (this.isAppointed(cast)) return '選択済み'
            return ''
        },
        isEmptyObject (obj) {
            return !Object.keys(obj).length
        },
        selectProductCategory (item) {
            // console.log('this.popularProduct.top', this.popularProduct.top)
            // console.log('this.productByCategory', this.productByCategory)
            // console.log('item.productType', item.productType)
            // console.log('item', item)

            // this.productByCategoryList = this.popularProduct.top[item.productType]

            const large = item.largeCategory
            const middle = item.middleCategory
            const small = item.smallCategory
            this.productByCategoryList = this.productByCategory[large][middle][small]

            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(this.productByCategoryList), 12)
            this.dispItems = slicedArray[0]

            this.rows = this.productByCategoryList.length

            this.selectedProductType = item.productType
        },
        selectProduct (item) {
            // console.log('selectProduct', item)
            this.selectedProduct = item
            this.actuallyPrice = item.price
        },

        // filterProductCategory (data) {
        //     console.log('filterProductCategory', data)
        //     const large = data.largeCategory
        //     const middle = data.middleCategory
        //     const small = data.smallCategory
        //     const res = this.productByCategory[large][middle][small]
        //     this.productByCategoryList = _.cloneDeep(res)
        //     // this.productByCategoryList = res
        // },
        showTopPopularProduct () {
            this.selectedProductType = null
        },
        directAddStack (item) {
            this.selectProduct(item)
            this.addStack()
        },
        addStack () {
            const product = this.selectedProduct

            if (product == null) return

            let actuallyTaxPrice = 0

            if (this.taxation.length != 0) {
                actuallyTaxPrice = this.calcAddTaxPrice(Number(this.actuallyPrice), this.tax)
            } else {
                actuallyTaxPrice = Number(this.actuallyPrice)
            }

            // console.log('product', product)

            const data = {
                name: product.name,
                price: product.price,
                actuallyPrice: Number(this.actuallyPrice),
                actuallyTaxPrice: actuallyTaxPrice,
                taxRate: this.tax,
                taxation: this.taxation.length != 0,
                quantity: this.quantity,
                totalPrice: this.totalPrice,
                totalTaxPrice: this.totalTaxPrice,
                thumbnail: product.thumbnail,
                category: product.category,
                // remarks: this.remarks,
                product: product,
                bottle: this.bottleCustomerInfo != null,
                customer: this.bottleCustomerInfo,
            }
            this.selectedProductList.push(data)
            this.selectedProduct = null
            // this.remarks = ''
            this.quantity = 1
            this.tax = Con.SALES_TAX
            this.taxation = [1]
            this.actuallyPrice = 0
            this.bottleCustomerInfo = null
        },
        deleteProduct (id) {
            // console.log('deleteProduct', id, this.selectedProductList)
            this.selectedProductList.splice(id, 1)
        },
        changePage (pageNumber) {
            this.currentPage = pageNumber
            let items = this.divideArrIntoPieces(_.cloneDeep(this.productByCategoryList), 12)
            this.dispItems = items[pageNumber-1]
        },
        updateProductByCategoryList (arr) {
            this.productByCategoryList = arr
            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(this.productByCategoryList), 12)
            this.dispItems = slicedArray[0]
            this.rows = this.productByCategoryList.length
            this.currentPage = 1
        },
        addBottleCustomerInfo (val, updateIdx) {
            this.$refs.inputSalesSelectCustomerDialog.open(val, updateIdx)
        },
        selectCustomer (idx) {
            this.bottleCustomerInfo = this.customerList[idx]
        },
        selectCustomerProductList (idx, updateIdx) {
            this.selectedProductList[updateIdx].customer = this.customerList[idx]
        },
        deleteCustomerSelectedProductList (idx) {
            // console.log('this.selectedProductList', this.selectedProductList)
            this.selectedProductList[idx].customer = null
        },
        isBottleCustomerDisabledRow (item) {
            // console.log('isBottleCustomerDisabledRow', item)
            if (item.product.category.large_category == 1 &&
                item.product.category.middle_category == 0)
            {
                if (item.product.category.small_category != 4) {
                    return false
                } else {
                    return true
                }
            }
            return true
        },
    },
    mixins: [
        utilsMixin
    ]
}

</script>

<style lang="scss" scoped>

    .add_sales_detail_product_area {
        height: 563px;
    }

    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }

    .add_sales_detail_footer_col {
        margin: 0;
        padding: 0;
    }


    .btn_close {
        display: inline-block;
        margin-right: 8px;
    }

    .productCard {
        cursor: pointer;
        padding: 10px;
        height: 185px;
        .product_desc_area {
            height: calc(100% - 80px);
            .product_name_area {
                height: calc(100% - 20px);

                .product_name {
                    font-size: 12px;
                }
                .product_long_name {
                    font-size: 10px;
                }
            }
        }


        .product_price_area {
            height: 20px;
            line-height: 20px;
            font-size: 13px;
            text-align: right;
        }
    }

    .productCard:hover {
        box-shadow: 1px 1px 2px 1px rgba(150, 150, 150, 0.5);
        transition: 0.5s;
    }

    .productCardBody {
        padding: 0;
    }

    .selected_product_area {
        margin-top: 2px;
        min-height: 50px;
    }

    .add_cast_footer_area3 {
        display: inline-block;
    }

    .add_sales_detail_quantity, .add_sales_detail_tax {
        height: 38px;
        padding: 4px 9px;
        border-radius: 3px;
        border: 1px solid rgba(125, 125, 125, 0.6);
    }


    .add_sales_detail_footer_area4 {
        margin-top: 15px;
        margin-bottom: 13px;
    }

    .add_cast_footer_bottom_area {
        margin-top: 20px;
        border-top: 1px solid rgba(155, 155, 155, 0.5);
    }

    .isAppointed {
        background-color: rgba(255, 255, 255, 1);
        filter: opacity(30%);
    }

    .add_sales_detail_add_product_btn,
    .add_sales_detail_delete_product_btn {
        cursor: pointer;
    }

    .product_item_thumbnail {
        height: 80px;
        width: 80px;
        margin: 0 auto;
        display: block;
    }

    .no_margin_no_padding {
        margin: 0;
        padding: 0;
    }
</style>
