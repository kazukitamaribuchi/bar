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
        <!-- <b-row>
            <b-col cols="6">
                <b-input-group>
                    <b-input-group-prepend is-text>
                        <b-icon icon="search"></b-icon>
                    </b-input-group-prepend>
                    <b-form-input
                        v-model="searchWord"
                        type="text"
                        placeholder="キャスト名で検索"
                    ></b-form-input>
                </b-input-group>
            </b-col>
            <b-col cols="6" align="right">
                <b-button
                    variant="outline-primary"
                >
                    <b-icon
                        icon="filter"
                    ></b-icon>
                </b-button>
            </b-col>
        </b-row> -->
        <b-row>
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
                            @dblclick="addStack(item)"
                            body-class="product_body"
                        >
                            <!-- <div align="center">
                                <b-img
                                    :src="defaultIcon"
                                    height=110
                                    width=110
                                    class="product_img"
                                ></b-img>
                            </div>
                            <b-card-text class="product_name">
                                {{ item.name }}
                            </b-card-text> -->
                            <b-card-img
                                :src="apiPath + item.thumbnail"
                                alt="productImage"
                                top
                                v-if="item.thumbnail != null"
                            ></b-card-img>
                            <b-card-img
                                :src="defaultIcon"
                                alt="productImage"
                                top
                                v-else
                            ></b-card-img>
                            <div class="product_name_area">
                                <b-card-text class="product_long_name" v-if="item.name.length > 20">
                                    {{ item.name }}
                                </b-card-text>
                                <b-card-text class="product_name" v-else>
                                    {{ item.name }}
                                </b-card-text>
                            </div>
                            <div class="product_price_area">
                                {{ item.price }} 円
                            </div>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
            <b-col v-if="selectedProductType != null">
                <!-- <b-card-title>
                    カテゴリ毎
                </b-card-title> -->
                <InputSalesAddDetailDialogHeader
                    :productType=selectedProductType
                    @update="productByCategoryList = $event"
                />
                <b-row>
                    <b-col
                        cols="2"
                        v-for="item in productByCategoryList"
                        :key=item.id
                    >
                        <b-card
                            class="productCard"
                            @click="selectProduct(item)"
                            @dblclick="addStack(item)"
                            body-class="product_body"
                        >
                            <b-card-img
                                :src="apiPath + item.thumbnail"
                                alt="productImage"
                                top
                                v-if="item.thumbnail != null"
                            ></b-card-img>
                            <b-card-img
                                :src="defaultIcon"
                                alt="productImage"
                                top
                                v-else
                            ></b-card-img>
                            <div class="product_name_area">
                                <b-card-text class="product_long_name" v-if="item.name.length > 20">
                                    {{ item.name }}
                                </b-card-text>
                                <b-card-text class="product_name" v-else>
                                    {{ item.name }}
                                </b-card-text>
                            </div>
                            <div class="product_price_area">
                                {{ item.price }} 円
                            </div>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
        <template #modal-footer>
            <b-container fluid>
                <b-row>
                    <b-col cols="4" class="add_sales_detail_footer_col">
                        <b-card-sub-title>選択商品</b-card-sub-title>
                        <div class="selected_product_area">
                            <b v-if="selectedProduct != null">
                                <b-img
                                    v-if="selectedProduct.thumbnail != null"
                                    :src="apiPath + selectedProduct.thumbnail"
                                    alt="Selected Product"
                                    rounded
                                    height="50"
                                    width="50"
                                ></b-img>
                                <b-img
                                    v-else
                                    :src="defaultIcon"
                                    alt="Selected Product"
                                    rounded
                                    height="50"
                                    width="50"
                                ></b-img>
                            </b>
                            <span v-if="selectedProduct != null">{{ selectedProduct.name }}</span>
                            <span v-else> - </span>
                        </div>
                    </b-col>
                    <b-col cols="8" class="add_sales_detail_footer_col">
                        <b-row>
                            <b-col cols="2" class="add_sales_detail_footer_col">
                                <b-card-sub-title>定価</b-card-sub-title>
                                <div class="selected_product_area">
                                    <div v-if="selectedProduct != null">
                                        ￥{{ selectedProduct.price }}
                                    </div>
                                    <div v-else> - </div>
                                </div>
                            </b-col>
                            <b-col class="add_sales_detail_footer_col">
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
                            <b-col cols="2" class="add_sales_detail_footer_col">
                                <b-card-sub-title>実価格</b-card-sub-title>
                                <b-form-input
                                    v-model="actuallyPrice"
                                    type="number"
                                    placeholder="実価格"
                                    required
                                ></b-form-input>
                            </b-col>
                            <b-col align="center" class="add_sales_detail_footer_col">
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
                                <b-card-sub-title>税区分</b-card-sub-title>
                                <b-form-group>
                                    <b-form-checkbox-group
                                        v-model="taxation"
                                        :options=taxationOptions
                                        buttons
                                        bg-variant="success"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                            <b-col align="center" class="add_sales_detail_footer_col">
                                <b-card-sub-title>ボトル登録</b-card-sub-title>
                                <b-form-group>
                                    <b-form-checkbox-group
                                        v-model="isBottle"
                                        :options=bottleOptions
                                        buttons
                                        :disabled=!isDrink
                                        bg-variant="success"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                            <b-col align="center" class="add_sales_detail_footer_col">
                                <b-card-sub-title>まとめて追加</b-card-sub-title>
                                <b-icon
                                    icon="plus-square"
                                    font-scale="1.5"
                                    variant="success"
                                    class="mt-2 add_sales_detail_add_product_btn"
                                    @click="addStack"
                                ></b-icon>
                            </b-col>
                        </b-row>
                    </b-col>
                </b-row>
                <b-row class="pt-3">
                    <b-col cols="5" class="add_sales_detail_footer_col">
                        <b-card-sub-title>備考</b-card-sub-title>
                        <b-form-textarea
                            rows="2"
                            no-resize
                            v-model="remarks"
                        ></b-form-textarea>
                    </b-col>
                </b-row>
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
                                        <th>定価</th>
                                        <th>数量</th>
                                        <th>実価格</th>
                                        <th>課税対象</th>
                                        <th>ボトル</th>
                                        <th>備考</th>
                                        <th></th>
                                    </tr>
                                    <tr
                                        v-for="(item, id) in selectedProductList"
                                        :key=id
                                    >
                                        <td>
                                            <b-img
                                                v-if="item.thumbnail != null"
                                                :src="apiPath + item.thumbnail"
                                                alt="Selected Product"
                                                rounded
                                                height="50"
                                                width="50"
                                            ></b-img>
                                            <b-img
                                                v-else
                                                :src="defaultIcon"
                                                alt="Selected Product"
                                                rounded
                                                height="50"
                                                width="50"
                                            ></b-img>
                                            <span>{{ item.name }}</span>
                                        </td>
                                        <td>{{ item.price }}</td>
                                        <td>{{ item.quantity }}</td>
                                        <td>{{ item.actuallyPrice }}</td>
                                        <td>{{ item.taxation }}</td>
                                        <td>{{ item.bottle }}</td>
                                        <td>{{ item.remarks }}</td>
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
                    <b-col cols="2">
                        <b-card-sub-title>
                            総計(税抜)
                        </b-card-sub-title>
                        <b-card-title class="mb-0">
                            ￥ {{ totalPrice }}
                        </b-card-title>
                    </b-col>
                    <b-col cols="2">
                        <b-card-sub-title>
                            総計(税込)
                        </b-card-sub-title>
                        <b-card-title class="mb-0">
                            ￥ {{ totalTaxPrice }}
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
                            追加
                        </b-button>
                    </b-col>
                </b-row>
            </b-container>
        </template>
    </b-modal>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import InputSalesAddDetailDialogHeader from '@/components/common/dialog/parts/InputSalesAddDetailDialogHeader'
import SelectForm from '@/components/common/parts/SelectForm'
import Decimal from 'decimal.js'
import utilsMixin from '@/mixins/utils'


export default {
    name: 'InputSalesAddDetailDialogItem',
    props: {
    },
    components: {
        InputSalesAddDetailDialogHeader,
        SelectForm,
    },
    data: () => ({
        dialog: false,
        selected: {},
        filterdCast: [],
        searchWord: '',
        appointedCastId: new Set(),
        isBottle: [],
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
        defaultIcon: Con.DEFAULT_ALCOHOL_ICON,
        productByCategoryList: [],
        selectedProduct: null,
        selectedProductList: [],
        remarks: '',
        tax: 35,
        taxation: [1],
        apiPath: Con.API_PATH,
    }),
    computed: {
        ...mapGetters([
            'cast',
            // ↓人気商品、カテゴリ別の商品を取るようにする
            'product',
            'productByCategory',
            'popularProduct',
        ]),
        isDisabled () {
            if (this.selectedProductList.length > 0) return false
            return this.selectedProduct == null
        },
        isDrink () {
            if (this.selectedProduct == null) return false
            if (this.selectedProduct.category.large_category == 1
                && this.selectedProduct.category.middle_category == 0) {
                return true
            }
            return false
        },
        actuallyTaxPrice () {
            return this.calcAddTaxPrice(this.actuallyPrice, this.tax)
        },
        totalPrice () {
            let total = 0

            for (const i in this.selectedProductList) {
                total += this.calcQuantityPrice(
                    this.selectedProductList[i].quantity,
                    this.selectedProductList[i].actuallyPrice,
                )
            }

            if (this.selectedProduct == null) return total

            total += this.calcQuantityPrice(this.actuallyPrice, this.quantity)
            return total
        },
        totalTaxPrice () {
            let total = 0

            // 商品毎にtaxが設定されている場合も考慮
            for (const i in this.selectedProductList) {
                // let q = new Decimal(this.selectedProductList[i].quantity)
                let q = this.selectedProductList[i].quantity
                if (!this.selectedProductList[i].taxation) {
                    // TAX無しの場合
                    total += Math.ceil(q * this.selectedProductList[i].actuallyPrice)
                    // total += Math.ceil(q.times(this.selectedProductList[i].actuallyPrice).toNumber())
                } else {
                    // TAX有の場合
                    total += this.calcAddTaxPrice(
                        this.selectedProductList[i].actuallyPrice,
                        Con.TAX_DEFAULT,
                    )
                }
            }

            if (this.selectedProduct == null) return total
            if (this.taxation.length == 0) {
                total += this.calcQuantityPrice(
                    this.actuallyPrice,
                    this.quantity
                )
            } else {
                total += this.calcAddTaxPrice(
                    this.calcQuantityPrice(
                        this.actuallyPrice,
                        this.quantity
                    ),
                    Con.TAX_DEFAULT,
                )
            }
            return total
        },
    },
    watch: {
        searchWord: function (val) {
            if (val.length > 0) {
                this.search(val)
            } else {
                // このメソッドは重くないか?
                this.filterdCast = _.cloneDeep(this.cast)
            }
        }
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
            this.filterdCast = _.cloneDeep(this.cast)
            this.appointedCastId = new Set()
            for (const i in this.appointed) {
                const item = this.appointed[i]
                this.appointedCastId.add(item.cast.id)
            }
            this.productByCategoryList = _.cloneDeep(this.productByCategory)
        },
        close () {
            this.dialog = false
            this.init()
        },
        add () {

            if (this.selectedProductList.length > 0) {
                this.$eventHub.$emit('addSalesDetailList', this.selectedProductList)
                this.close()
                return
            }

            const product = this.selectedProduct

            const data = {
                name: product.name,
                price: product.price,
                actuallyPrice: this.actuallyPrice,
                actuallyTaxPrice: this.actuallyTaxPrice,
                taxRate: this.tax,
                taxation: this.taxation.length != 0,
                quantity: this.quantity,
                totalPrice: this.totalPrice,
                totalTaxPrice: this.totalTaxPrice,
                bottle: this.isBottle.length != 0,
                thumbnail: product.thumbnail,
                category: product.category,
                remarks: this.remarks,
                product: product,
            }
            this.init()
            this.$eventHub.$emit('addSalesDetail', data)
            console.log('★', data)
            this.close()
        },
        init () {
            this.selected = {}
            this.filterdCast = {}
            this.searchWord = ''
            this.appointedCastId = new Set()
            this.selectedProductType = null
            this.selectedProduct = null
            this.selectedProductList = []
            this.remarks = ''
            this.actuallyPrice = 0
            this.isBottle = []
            this.quantity = 1
            this.taxation = [1]
        },
        select (item) {
            if (this.isAppointed(item)) return
            this.selected = item
        },
        search: _.debounce(function search (searchText) {
            const targetCastList = _.cloneDeep(this.cast)
            const reg = new RegExp("^" + searchText)
            const res = targetCastList.filter(target => {
                // 検索に本名は含める？・・・
                if (target.name.match(reg) || target.real_name.match(reg)) {
                    return true
                }
            }, 4000)
            this.filterdCast = res
        }),
        getIsAppointedStr (cast) {
            if (this.isAppointed(cast)) return '選択済み'
            return ''
        },
        isAppointed (cast) {
            if(this.appointedCastId.has(cast.id)) return true
            return false
        },
        isEmptyObject (obj) {
            return !Object.keys(obj).length
        },
        selectProductCategory (item) {
            this.productByCategoryList = this.popularProduct.top[item.productType]
            this.selectedProductType = item.productType
        },
        selectProduct (item) {
            this.selectedProduct = item
            this.actuallyPrice = item.price
            if (!this.isDrink) {
                this.isBottle = []
            }
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
        addStack () {
            const product = this.selectedProduct

            const data = {
                name: product.name,
                price: product.price,
                actuallyPrice: this.actuallyPrice,
                actuallyTaxPrice: this.actuallyTaxPrice,
                product: product,
                taxRate: this.tax,
                taxation: this.taxation.length != 0,
                quantity: this.quantity,
                totalPrice: this.totalPrice,
                totalTaxPrice: this.totalTaxPrice,
                bottle: this.isBottle.length != 0,
                thumbnail: product.thumbnail,
                category: product.category,
                remarks: this.remarks,
            }
            this.selectedProductList.push(data)
            this.selectedProduct = null
            this.remarks = ''
            this.quantity = 1
            this.tax = 35
            this.isBottle = []
            this.taxation = [1]
        },
        deleteProduct (id) {
            this.selectedProductList.splice(id, 1)
        }
    },
    mixins: [
        utilsMixin
    ]
}

</script>

<style lang="scss" scoped>

.input-group-text {
    height: 100%;
    border-radius: 5px 0 0 5px !important;
}

.productCard {
    cursor: pointer;
    height: 170px;
}

.productCard:hover {
    box-shadow: 1px 1px 2px 1px rgba(150, 150, 150, 0.5);
    transition: 0.5s;
}

.add_sales_detail_footer_col {
    margin: 0;
    padding: 0;
}


.btn_close {
    display: inline-block;
    margin-right: 8px;
}

.product_name_area {
    min-height: 35px;
    max-height: 35px;
}

.product_price_area {
    height: 25px;
    font-size: 13px;
    text-align: right;
}

.product_name {
    font-size: 12px;
}

.product_long_name {
    font-size: 10px;
}

.product_body {
    margin-top: 10px;
    padding-top: 0;
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
</style>
