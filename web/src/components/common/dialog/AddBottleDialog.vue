<template>
    <b-modal
        v-model="dialog"
        title="ボトル追加"
        header-bg-variant="primary"
        header-text-variant="light"
        size="xl"
    >
        <b-row>
            <b-col>
                <AddBottleDialogHeader
                    @update="updateProductByCategoryList"
                />
                <b-row>
                    <b-col
                        cols="2"
                        v-for="(item, i) in dispItems"
                        :key=i
                    >
                    <!-- @click="selectProduct(item)" -->
                        <b-card
                            class="productCard"
                            @click="addOrEdit(item)"
                            @dblclick="addOrEdit(item)"
                            body-class="product_body"
                        >
                            <!-- <b-card-img
                                :src="apiPath + item.thumbnail"
                                alt="productImage"
                                top
                                v-if="item.thumbnail != null"
                                height="80"
                                width="80"
                            ></b-card-img>
                            <b-card-img
                                :src="defaultIcon"
                                alt="productImage"
                                top
                                v-else
                                height="80"
                                width="80"
                            ></b-card-img> -->
                            <div class="add_bottle_img">
                                <img
                                    src="@/static/img/noimage8.png"
                                    class="add_bottle_default_icon"
                                >
                            </div>
                            <div class="add_bottle_info">
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
                            </div>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>

        <template #modal-footer>
            <b-container fluid>

                <b-pagination
                    v-model="currentPage"
                    :total-rows="rows"
                    :per-page="perPage"
                    aria-controls="my-table"
                    align="center"
                    @change="changePage"
                ></b-pagination>
                <!-- <b-row>
                    <b-col cols="6" class="add_bottle_footer_col">
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
                    <b-col cols="6" class="add_bottle_footer_col">
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
                        </b-row>
                    </b-col>
                </b-row> -->
                <b-row class="add_bottle_footer_bottom_area mt-5">
                    <b-col align="right" class="add_bottle_footer_col">
                        <b-button
                            variant="secondary"
                            @click="close"
                            class="btn_close add_bottle_footer_area4"
                        >
                            閉じる
                        </b-button>
                        <!-- <b-button
                            variant="primary"
                            @click="add"
                            class="add_bottle_footer_area4"
                            :disabled=isDisabled
                        >
                            追加
                        </b-button> -->
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
import AddBottleDialogHeader from '@/components/common/dialog/parts/AddBottleDialogHeader'
import SelectForm from '@/components/common/parts/SelectForm'
import Decimal from 'decimal.js'
import utilsMixin from '@/mixins/utils'


export default {
    name: 'AddBottleDialogItem',
    props: {
    },
    components: {
        AddBottleDialogHeader,
        SelectForm,
    },
    data: () => ({
        dialog: false,
        selected: {},
        selectedProductType: 0,
        defaultIcon: Con.DEFAULT_ALCOHOL_ICON,
        productByCategoryList: [],
        selectedProduct: null,
        selectedProductList: [],
        remarks: '',
        apiPath: Con.API_PATH,
        editIdx: 0,
        editMode: false,
        editOpenDate: '',

        currentPage: 1,
        dispItems: [],
        perPage: 12,
        rows: 1,
    }),
    computed: {
        ...mapGetters([
            // ↓人気商品、カテゴリ別の商品を取るようにする
            'product',
            'productByCategory',
            'popularProduct',
        ]),
        isDisabled () {
            if (this.selectedProductList.length > 0) return false
            return this.selectedProduct == null
        },
    },
    watch: {
    },
    created () {
        // this.$eventHub.$off('filterBottleCategory')
        // this.$eventHub.$on('filterBottleCategory', this.filterBottleCategory)
    },
    mounted () {
    },
    methods: {
        open (data, idx) {

            console.log('this.productByCategory', this.productByCategory)
            this.productByCategoryList = _.cloneDeep(this.productByCategory[1][0][0])

            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(this.productByCategoryList), 12)
            this.dispItems = slicedArray[0]
            this.rows = this.productByCategoryList.length

            this.dialog = true
            if (data) {
                this.editIdx = idx
                this.editOpenDate = data.openDate
                this.editMode = true
                console.log('ボトル変更モード')
            } else {
                this.editMode = false
                console.log('新規追加モード')
            }
        },
        updateProductByCategoryList (items) {
            let slicedArray = this.divideArrIntoPieces(_.cloneDeep(items), 12)
            this.rows = items.length
            this.dispItems = slicedArray[0]
            this.currentPage = 1
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
            let items = this.divideArrIntoPieces(_.cloneDeep(this.productByCategoryList), 12)
            this.dispItems = items[pageNumber-1]
        },
        close () {
            this.init()
            this.dialog = false
        },
        addOrEdit (data) {
            if (this.editMode) {
                this.update(data)
            } else {
                this.add(data)
            }
        },
        add (data) {
            console.log('add', data)
            this.$emit('update', data)
            // this.$eventHub.$emit('addBottle', data)
            this.close()
        },
        update (data) {
            console.log('update')
            const item = data
            item.openDate = this.editOpenDate
            console.log('item', item)
            this.$eventHub.$emit('editBottle', item, this.editIdx)
            this.close()
        },
        init () {
            this.selected = {}
            this.selectedProductType = null
            this.selectedProduct = null
            this.selectedProductList = []
            this.remarks = ''
            this.editIdx = 0
            this.editOpenDate = ''
        },
        selectProduct (item) {
            this.selectedProduct = item
        },
        // filterBottleCategory (data) {
        //     const large = data.largeCategory
        //     const middle = data.middleCategory
        //     const small = data.smallCategory
        //     const res = this.productByCategory[large][middle][small]
        //     this.productByCategoryList = _.cloneDeep(res)
        //     // this.$set(this.productByCategoryList)
        // },
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

.add_bottle_footer_col {
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


.add_bottle_footer_area4 {
    margin-top: 15px;
    margin-bottom: 13px;
}

.add_bottle_footer_bottom_area {
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

.add_bottle_img {
    margin: 0 auto;
    text-align: center;
    height: 85px;
    // margin-bottom: 10px;
    .add_bottle_default_icon {
        border-radius: 50%;
        width: 70px;
        height: 70px;
    }
}

.add_bottle_info {
    height: 55px;
}
</style>
