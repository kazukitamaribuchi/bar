<template>
    <div>
        <div class="account_order_history_wrap">
            <AccountPageTitleArea
                to="AccountOrderCheckSelect"
                title="注文確認"
            />

            <div v-if="!loading" style="padding-bottom: 120px;" class="pa-4">

                <v-card-text class="text-right pa-0">
                    <span style="font-size: 12px; color: rgba(70, 70, 70, 0.8);">
                        伝票No: {{ salesData.header_id }}
                    </span>
                </v-card-text>
                <v-divider class="mx-4"/>
                <v-card
                    flat
                    class="pa-1"
                >
                    <v-card-title class="pl-0">
                        伝票情報
                    </v-card-title>
                    <v-row>
                        <v-col cols="5" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>席</v-list-item-title>
                                    <v-list-item-subtitle>{{ salesData.disp_seat_name }}</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                        <v-col cols="7" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>来店時間</v-list-item-title>
                                    <v-list-item-subtitle>{{ salesData.visit_time }}</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                        <v-col cols="5" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>会員No</v-list-item-title>
                                    <v-list-item-subtitle v-if="salesData.customer != undefined">{{ salesData.customer.customer_no }}</v-list-item-subtitle>
                                    <v-list-item-subtitle v-else>-</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                        <v-col cols="7" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>来店人数</v-list-item-title>
                                    <v-list-item-subtitle>{{salesData.total_visitors}}人（男: {{salesData.male_visitors}}, 女: {{salesData.female_visitors}}）</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                        <v-col cols="5" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>ランク</v-list-item-title>
                                    <v-list-item-subtitle v-if="salesData.customer != undefined">{{ salesData.customer.rank_name }}</v-list-item-subtitle>
                                    <v-list-item-subtitle v-else>-</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                        <v-col cols="7" class="py-0">
                            <v-list-item two-line>
                                <v-list-item-content class="py-0">
                                    <v-list-item-title>顧客名</v-list-item-title>
                                    <v-list-item-subtitle v-if="salesData.customer != undefined">{{ salesData.customer.name }}</v-list-item-subtitle>
                                    <v-list-item-subtitle v-else>-</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                        </v-col>
                    </v-row>
                    <v-card-subtitle class="pb-0">
                        備考
                    </v-card-subtitle>
                    <v-card-text class="text--primary" v-if="salesData.remarks == ''">
                        無し
                    </v-card-text>
                    <v-card-text class="text--primary" v-else>
                        {{ salesData.remarks }}
                    </v-card-text>
                </v-card>
                <v-container fluid class="mt-3 px-1">
                    <v-row>
                        <v-col cols="5" class="py-0">
                            <div style="font-size: 13px;">
                                注文数
                            </div>
                        </v-col>
                        <v-col cols="7" class="text-right py-0">
                            <div style="font-size: 13px;">
                                {{ totalOrderCnt }} 点
                            </div>
                        </v-col>
                        <v-col cols="5" class="py-0">
                            <div style="font-size: 13px;">
                                注文料金
                            </div>
                        </v-col>
                        <v-col cols="7" class="text-right py-0">
                            <div style="font-size: 13px;">
                                <i class='bx bx-yen'></i>{{ detailPrice | priceLocaleString }}
                            </div>
                        </v-col>
                        <v-col cols="5" class="py-0">
                            <div style="font-size: 13px;">
                                サービス料金
                            </div>
                        </v-col>
                        <v-col cols="7" class="text-right py-0">
                            <div style="font-size: 13px;">
                                <i class='bx bx-yen'></i>{{ servicePrice | priceLocaleString }}
                            </div>
                        </v-col>
                        <v-col cols="5" class="pt-2 pb-0">
                            <div style="font-size: 15px;">
                                合計(税抜)
                            </div>
                        </v-col>
                        <v-col cols="7" class="text-right pt-2 pb-0">
                            <div style="font-size: 15px;">
                                <i class='bx bx-yen'></i>{{ totalPrice | priceLocaleString }}
                            </div>
                        </v-col>
                        <v-col cols="5" class="pt-1">
                            <div style="font-size: 17px; color: rgb(255, 87, 87); font-weight: bold;">
                                合計(税込)
                            </div>
                        </v-col>
                        <v-col cols="7" class="text-right pt-1">
                            <div style="font-size: 20px; color: rgb(255, 87, 87); font-weight: bold; font-style: italic;">
                                <i class='bx bx-yen'></i>{{ totalTaxPrice | priceLocaleString }}
                            </div>
                        </v-col>
                        <v-divider class="mx-2"/>
                    </v-row>

                    <v-row class="pt-4">
                        <v-card-title>
                            明細情報
                        </v-card-title>
                        <!-- <p style="font-size:13px; color:rgba(20, 20, 20, 1);">明細情報</p> -->
                        <v-card-subtitle class="text-right">
                            明細数 : {{ salesData.sales_detail.length }}
                        </v-card-subtitle>

                        <v-card
                            flat
                            v-if="salesData.sales_detail.length == 0"
                        >
                            <v-card-title>
                                明細がありません。
                            </v-card-title>

                            <v-divider />
                        </v-card>

                        <v-card
                            cols="12"
                            v-for="(item, i) in salesData.sales_detail"
                            :key="i"
                            flat
                            style="padding-left: 20px;"
                        >
                            <div class="px-2 sales_detail_no">
                                {{ i + 1 }}
                            </div>
                            <div class="text-right label-style">
                                注文時間 : {{ item.order_time }}
                            </div>
                            <div class="px-2">
                                <label class="label-style">
                                    商品名
                                </label>
                                <p class="product_name">
                                    {{ item.product.name }}
                                </p>
                            </div>
                            <v-row class="pa-2">
                                <v-col cols="7" class="py-0">
                                    <label class="label-style">
                                        実価格
                                    </label>
                                    <v-text-field
                                        v-model="item.fixed_price"
                                        placeholder="実価格"
                                        class="right-input mt-0 pt-0 mr-1"
                                        @change="updateSalesDetail(item, i)"
                                        :disabled="isEditMode"
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="5" class="py-0">
                                    <label class="label-style">
                                        数量
                                    </label>

                                    <v-card-subtitle class="text-right">
                                        {{ item.quantity }}
                                    </v-card-subtitle>
                                    <!-- <b-form-spinbutton
                                        class="mt-2"
                                        id="sb-inline"
                                        v-model="item.quantity"
                                        @change="updateSalesDetail(item, i)"
                                        :disabled="isEditMode"
                                        max="item.quantity"
                                    ></b-form-spinbutton> -->
                                </v-col>
                            </v-row>
                            <v-row class="pa-2">
                                <v-col cols="4" class="py-0">
                                    <div v-if="!isNotDrink(item)">
                                        <label class="label-style">
                                            ボトル登録
                                        </label>
                                        <v-switch
                                            v-model="item.bottle"
                                            class="mt-0"
                                            :disabled="isNotDrink(item)"
                                        ></v-switch>
                                    </div>
                                </v-col>
                                <v-col cols="3" class="py-0">
                                    <label class="label-style">
                                        非課税
                                    </label>
                                    <v-checkbox
                                        v-model="item.tax_free_flg"
                                        class="mt-0"
                                        @change="updateSalesDetail(item, i)"
                                        :disabled="isEditMode"
                                    ></v-checkbox>
                                </v-col>
                                <v-col cols="2" class="py-0">
                                    <div v-if="isNotDrink(item)">
                                        <label class="label-style">
                                            締め
                                        </label>
                                        <v-checkbox
                                            v-model="item.end_flg"
                                            disabled
                                            class="mt-0"
                                        ></v-checkbox>
                                    </div>
                                </v-col>
                                <v-col cols="3" class="py-0 text-center">
                                    <label class="label-style">
                                        削除
                                    </label>
                                    <vs-button
                                        circle
                                        icon
                                        danger
                                        animation-type="rotate"
                                        @click="deleteProductDetail(item)"
                                        :loading="checkLoading"
                                        style="margin: 0 auto;"
                                        :disabled="isEditMode"
                                    >
                                        <i class='bx bx-trash' ></i>
                                    </vs-button>
                                </v-col>
                            </v-row>
                            <v-divider/>
                        </v-card>

                        <div class="px-0">
                            <v-card-title>
                                ボトル情報
                            </v-card-title>
                            <v-card-subtitle class="text-right">
                                所有ボトル数 :
                                <span v-if="salesData.customer != undefined">{{ salesData.customer.bottle.length }}</span>
                                <span v-else>0</span>
                            </v-card-subtitle>

                            <div v-if="salesData.customer != undefined">
                                <div
                                    cols="12"
                                    v-for="(item, i) in salesData.customer.bottle"
                                    :key="i"
                                    flat
                                    style="padding-left: 20px;"
                                >
                                    <div class="px-2 sales_detail_no">
                                        {{ i + 1 }}
                                    </div>
                                    <div class="text-right label-style">
                                        開封日 : {{ item.open_date }}
                                    </div>
                                    <div class="px-2">
                                        <label class="label-style">
                                            商品名
                                        </label>
                                        <p class="product_name">
                                            {{ item.product.name }}
                                        </p>
                                    </div>

                                    <div>
                                        <label class="label-style">
                                            消込
                                        </label>
                                        <v-switch
                                        v-model="item.bottleDelete"
                                        class="mt-0"
                                        @change="updateBottleDelete(item)"
                                        ></v-switch>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <v-divider class="mx-3"/>

                        <v-card-title>
                            サービス料金
                        </v-card-title>
                        <v-row class="ml-5">


                            <v-col cols="4">
                                <div style="font-size: 14px;">
                                    滞在時間
                                </div>
                            </v-col>
                            <v-col cols="8" class="text-right">
                                <div style="font-size: 14px;">
                                    <CalcStayHour
                                        :visitTime=salesData.visit_time
                                        :leaveTime=leaveTime
                                        @calcStayHour="calcStayHour"
                                    />
                                </div>
                            </v-col>


                            <v-col cols="4">
                                <div style="font-size: 14px;">
                                    料金プラン
                                </div>
                            </v-col>
                            <v-col cols="8" class="text-right">
                                <div style="font-size: 14px;">
                                    {{ salesData.basic_plan_type.name }} / 1人
                                </div>
                            </v-col>


                            <CalcBasicPlanPrice
                                :salesData=salesData
                                :mode="mode == 1"
                                :leaveTime=leaveTime
                                @update="updateBasicPlanPrice"
                            />

                            <div style="font-size: 14px;">
                                TAX
                            </div>
                            <v-col cols="5" class="text-right py-0">
                                <div style="font-size: 14px;">
                                    サービス料
                                </div>
                            </v-col>
                            <v-col cols="7" class="text-right py-0">
                                <v-select
                                  :items="basicPlanServiceTaxList"
                                  item-text="name"
                                  item-value="val"
                                  dense
                                  outlined
                                  v-model="salesData.basic_plan_service_tax"
                                  :height=20
                                  :disabled="isEditMode"
                                ></v-select>
                            </v-col>
                            <v-col cols="5" class="text-right py-0">
                                <div style="font-size: 14px;">
                                    消費税
                                </div>
                            </v-col>
                            <v-col cols="7" class="text-right py-0">
                                <v-select
                                  :items="basicPlanServiceTaxList"
                                  item-text="name"
                                  item-value="val"
                                  dense
                                  outlined
                                  v-model="salesData.basic_plan_tax"
                                  :height=20
                                  :disabled="isEditMode"
                                ></v-select>
                            </v-col>
                            <v-col cols="5" class="text-right py-0">
                                <div style="font-size: 14px;">
                                    カード会計
                                </div>
                            </v-col>
                            <v-col cols="7" class="text-right py-0">
                                <v-select
                                  :items="basicPlanServiceTaxList"
                                  item-text="name"
                                  item-value="val"
                                  dense
                                  outlined
                                  v-model="salesData.basic_plan_card_tax"
                                  :height=20
                                ></v-select>
                            </v-col>

                            <div style="font-size: 14px;">
                                支払方法
                            </div>
                            <v-col cols="5" class="text-right py-0">
                                <div style="font-size: 14px;">
                                    カード払い
                                </div>
                            </v-col>
                            <v-col cols="7" class="text-right py-0">
                                <v-checkbox
                                    v-model="cardPayment"
                                    class="mt-0"
                                ></v-checkbox>
                            </v-col>
                        </v-row>
                    </v-row>

                    <!-- <DeleteSalesDetailDialog
                        ref="deleteSalesDetailDialog"
                        @deleteSalesDetail="deleteSalesDetail"
                    /> -->

                </v-container>

            </div>
            <div v-else style="text-align: center;">
                <v-progress-circular
                    indeterminate
                    color="primary"
                    style="text-align: center;"
                ></v-progress-circular>
            </div>

            <v-snackbar
                top
                v-model="snackbar"
                timeout="2000"
            >
                {{ snackbarText }}
                <template v-slot:action="{ attrs }">
                    <v-btn
                        color="pink"
                        text
                        v-bind="attrs"
                        @click="initSnackBar"
                    >Close</v-btn>
                </template>
            </v-snackbar>

            <v-dialog
                v-model="endAccountSuccessDialog"
                persistent
            >
                <v-card
                    flat
                >
                    <v-card-title>
                        伝票データの締め処理が成功しました。
                        ホームへ戻ります。
                    </v-card-title>
                    <v-card-actions>
                        <vs-button
                            primary
                            transparent
                            size="large"
                            @click="toHome"
                        >はい</vs-button>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>

        <EndSalesFooter
            :totalOrder="totalOrderCnt"
            :totalPrice="totalPrice"
            :totalTaxPrice="totalTaxPrice"
            :mode="mode"
            @changeMode="changeMode"
            @closeAccount="closeAccount"
        />
    </div>
</template>
<script>
    import dayjs from 'dayjs'
    import _ from 'lodash'
    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
    import EndSalesFooter from '@/components/account/EndSalesFooter'
    import CalcStayHour from '@/components/account/parts/CalcStayHour'
    import CalcBasicPlanPrice from '@/components/account/parts/CalcBasicPlanPrice'
    import DeleteSalesDetailDialog from '@/components/account/dialog/DeleteSalesDetailDialog'
    import utilsMixin from '@/mixins/utils'

    export default {
        name: 'AccountOrderHistoryItem',
        components: {
            AccountPageTitleArea,
            EndSalesFooter,
            CalcStayHour,
            CalcBasicPlanPrice,
            DeleteSalesDetailDialog,
        },
        props: {
        },
        data: () => ({
            salesData: null,
            bottleDeleteList: [],
            basicPlanServiceTaxList: [
                { name: '10%', val: 10 },
                { name: '0%', val: 0 },
            ],
            cardPayment: false,
            snackbar: false,
            snackbarText: '',
            checkLoading: false,
            basicPlanPrice: {
                basicPlanNormalPrice1: 0,
                basicPlanNormalNum1: 0,
                basicPlanNormalPrice2: 0,
                basicPlanNormalNum2: 0,
                basicPlanExtentionPrice1: 0,
                basicPlanExtentionNum1: 0,
                basicPlanExtentionPrice2: 0,
                basicPlanExtentionNum2: 0,
            },
            totalPrice: 0,
            detailPrice: 0,
            servicePrice: 0,
            mode: 0,
            stayHour: null,
            taxRate: 0,
            endAccountSuccessDialog: false,
            loading: false,
        }),
        beforeCreate () {
        },
        created () {
            this.loading = true
            this.$axios({
                method: 'get',
                url: `/api/sales/${this.$route.params.id}/`,
            })
            .then(res => {
                console.log(res)
                this.loading = false
                this.salesData = _.cloneDeep(res.data)
            })
            .catch(e => {
                console.log(e)
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
        watch: {
            cardPayment: function (n, o) {
                if (n) {
                    this.salesData.basic_plan_card_tax = 10
                } else {
                    this.salesData.basic_plan_card_tax = 0
                }
            }
        },
        computed: {
            leaveTime () {
                return dayjs().format('YYYY/MM/DD HH:mm')
            },
            totalOrderCnt () {
                let cnt = 0
                if (this.salesData != null) {
                    for (const salesDetail of this.salesData.sales_detail) {
                        cnt += salesDetail.quantity
                    }
                }
                return cnt
            },
            totalTaxPrice () {
                let total = 0
                // 明細
                let detailPrice = 0
                let totalDetail = 0
                let totalTaxFreeDetail = 0
                if (this.salesData != null) {
                    for (const item of this.salesData.sales_detail) {
                        if (item.tax_free_flg) {
                            totalTaxFreeDetail += item.fixed_price * item.quantity
                        } else {
                            totalDetail += item.fixed_price * item.quantity
                        }
                    }
                }
                detailPrice = (totalDetail + totalTaxFreeDetail)

                let servicePrice = 0
                let totalTaxPrice = 0
                // サービス料金
                const normal1 = this.basicPlanPrice.basicPlanNormalPrice1 * this.basicPlanPrice.basicPlanNormalNum1
                const normal2 = this.basicPlanPrice.basicPlanNormalPrice2 * this.basicPlanPrice.basicPlanNormalNum2
                const extention1 = this.basicPlanPrice.basicPlanExtentionPrice1 * this.basicPlanPrice.basicPlanExtentionNum1
                const extention2 = this.basicPlanPrice.basicPlanExtentionPrice2 * this.basicPlanPrice.basicPlanExtentionNum2
                totalTaxPrice += (normal1 + normal2 + extention1 + extention2)
                servicePrice = (totalTaxPrice)
                totalTaxPrice += totalDetail


                let taxRate = 0
                if (this.salesData != null) {
                    taxRate += this.salesData.basic_plan_service_tax
                    taxRate += this.salesData.basic_plan_tax
                    taxRate += this.salesData.basic_plan_card_tax
                    total += this.roundDown2(totalTaxPrice + totalTaxPrice * (taxRate/100))
                    total += totalTaxFreeDetail

                    this.setTaxRate(taxRate)
                    this.setTotalPrice(totalTaxPrice + totalTaxFreeDetail)
                    this.setDetailPrice(detailPrice)
                    this.setSerivicePrice(servicePrice)
                }

                return total
            },
            isEditMode () {
                if (this.mode == 1) return true
                return false
            }
        },
        methods: {
            setTaxRate (val) {
                this.taxRate = val
            },
            setTotalPrice (val) {
                this.totalPrice = val
            },
            setDetailPrice (val) {
                this.detailPrice = val
            },
            setSerivicePrice (val) {
                this.servicePrice = val
            },
            isNotDrink (item) {
                // if (this.mode == 1) return true
                return item.product.category.large_category == 2
            },
            deleteProductDetail: _.debounce(function deleteProductDetail (item, i) {
                this.checkLoading = true
                item.header_id = this.salesData.id
                this.$axios({
                    method: 'delete',
                    url: '/api/sales/delete_sales_detail/',
                    data: item
                })
                .then(res => {
                    console.log(res)
                    this.salesData = res.data
                    this.checkLoading = false
                })
                .catch(e => {
                    console.log(e)
                    this.snackbarText = 'データの更新に失敗しました。'
                    this.snackbar = true
                    this.checkLoading = false
                })
                // this.$refs.deleteSalesDetailDialog.open(item)
            }, 0),
            updateSalesDetail: _.debounce(function updateSalesDetail(item, i) {
                item.header_id = this.salesData.id
                this.$axios({
                    method: 'put',
                    url: '/api/sales/update_sales_detail/',
                    data: item
                })
                .then(res => {
                    console.log(res)
                    this.salesData = res.data
                })
                .catch(e => {
                    console.log(e)
                    this.snackbarText = 'データの更新に失敗しました。'
                    this.snackbar = true
                })
            }, 500),
            deleteSalesDetail (item, idx) {
                console.log('deleteSalesDetail', item, idx)
            },
            initSnackBar () {
                this.snackbar = false
                this.snackbarText = ''
            },
            updateBasicPlanPrice (item) {
                this.basicPlanPrice = item
                console.log('this.basicPlanPrice', this.basicPlanPrice)
            },
            changeMode (mode) {
                // 0 => チェック、 1 => 締め
                this.mode = mode
            },
            closeAccount () {
                console.log('締め処理', this.salesData)
                let data = this.salesData
                let sales_service_detail = []
                if (this.basicPlanPrice.basicPlanNormalNum1 != 0) {
                    sales_service_detail.push({
                        service: this.salesData.basic_plan_type,
                        discount_flg: false,
                        quantity: this.basicPlanPrice.basicPlanNormalNum1,
                        fixed_price: this.basicPlanPrice.basicPlanNormalPrice1,
                        // とりあえず税の合算値
                        tax_rate: this.taxRate,
                    })
                }
                if (this.basicPlanPrice.basicPlanNormalNum2 != 0) {
                    sales_service_detail.push({
                        service: this.salesData.basic_plan_type,
                        discount_flg: true,
                        quantity: this.basicPlanPrice.basicPlanNormalNum2,
                        fixed_price: this.basicPlanPrice.basicPlanNormalPrice2,
                        // とりあえず税の合算値
                        tax_rate: this.taxRate,
                    })
                }
                if (this.basicPlanPrice.basicPlanExtentionNum1 != 0) {
                    sales_service_detail.push({
                        service: {
                            'large_category': 1,
                            'middle_category': (this.salesData.basic_plan_type.middle_category == 1) ? true: false,
                            'small_category': 0,
                        },
                        discount_flg: false,
                        quantity: this.basicPlanPrice.basicPlanExtentionNum1,
                        fixed_price: this.basicPlanPrice.basicPlanExtentionPrice1,
                        // とりあえず税の合算値
                        tax_rate: this.taxRate,
                    })
                }
                if (this.basicPlanPrice.basicPlanExtentionNum2 != 0) {
                    sales_service_detail.push({
                        service: {
                            'large_category': 1,
                            'middle_category': (this.salesData.basic_plan_type.middle_category == 1) ? true: false,
                            'small_category': 0,
                        },
                        discount_flg: true,
                        quantity: this.basicPlanPrice.basicPlanExtentionNum2,
                        fixed_price: this.basicPlanPrice.basicPlanExtentionPrice2,
                        // とりあえず税の合算値
                        tax_rate: this.taxRate,
                    })
                }
                data.sales_service_detail = sales_service_detail
                data.leave_time = this.leaveTime
                data.stay_hour = this.stayHour
                data.total_sales = this.totalPrice
                data.total_tax_sales = this.totalTaxPrice
                data.bottle_delete_list = this.bottleDeleteList
                this.$axios({
                    method: 'post',
                    url: '/api/sales/close_sales_header/',
                    data: data,
                })
                .then(res => {
                    console.log(res)
                    this.endAccountSuccessDialog = true
                })
                .catch(e => {
                    this.snackbarText = 'データの更新に失敗しました。'
                    this.snackbar = true
                    console.log(e)
                })
            },
            calcStayHour (val) {
                this.stayHour = val
            },
            toHome () {
                this.init()
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            init () {
                this.salesData = null
                this.cardPayment = false
                this.basicPlanPrice = {
                    basicPlanNormalPrice1: 0,
                    basicPlanNormalNum1: 0,
                    basicPlanNormalPrice2: 0,
                    basicPlanNormalNum2: 0,
                    basicPlanExtentionPrice1: 0,
                    basicPlanExtentionNum1: 0,
                    basicPlanExtentionPrice2: 0,
                    basicPlanExtentionNum2: 0,
                }
                this.totalPrice = 0
                this.detailPrice = 0
                this.servicePrice = 0
                this.mode = 0
                this.stayHour = null
                this.taxRate = 0
                this.bottleDeleteList = []
            },
            updateBottleDelete (item) {
                console.log('updateBottleDelete', item)
                if (item.bottleDelete) {
                    this.bottleDeleteList.push(item)
                } else {
                    this.bottleDeleteList = this.bottleDeleteList.filter(e => e.id !== item.id)
                }
                console.log('this.bottleDeleteList', this.bottleDeleteList)
            }
        },
        mixins: [
            utilsMixin,
        ],
    }
</script>
<style lang="scss" scoped>
    .label-style {
        font-size: 12px;
        color: rgba(70, 70, 70, 0.9);
    }

    .product_name {
        font-size: 15px;
    }

    .sales_detail_no {
        text-align: center;
        font-size: 13px;
        width: 25px;
        max-width: 50px;
        height: 25px;
        border: 1px solid rgba(50, 50, 50, 0.7);
        color: rgba(50, 50, 50, 0.7);
        line-height: 25px;
        border-radius: 4px;
        margin: 0 0 9px 4px;
        color: white;
        background-color: rgb(140, 140, 140);
    }

    .account_order_history_wrap {
        margin-bottom: 100px;
    }
</style>
