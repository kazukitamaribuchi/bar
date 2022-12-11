<template>
    <div id="sales_detail_wrap">
        <div v-if="loading" class="loading">
            <div class="loading_icon">
                <b-spinner
                    style="width: 6rem; height: 6rem; display: block; margin: 0 auto;"
                    label="Large Spinner"
                    variant="light"
                ></b-spinner>
            </div>
        </div>
        <b-row v-else>
            <b-tabs pill>
                <b-tab
                    title="売上詳細"
                >
                    <b-card
                        class="sales_detail_area"
                    >
                        <b-container fluid>
                            <b-row>
                                <div style="display: flex; justify-content: space-between;">
                                    <b-card-title>
                                        伝票情報
                                    </b-card-title>
                                    <div style="height: 55px;">
                                        <b-button
                                            size="sm"
                                            @click="showEditSalesDialog"
                                        >
                                            <b-icon
                                                icon="pencil"
                                                aria-hidden="true"
                                            ></b-icon> 編集
                                        </b-button>
                                        <b-button
                                            size="sm"
                                            style="position: relative; left: 10px;"
                                            @click="showDeleteSalesDetailDialog"
                                        >
                                            <b-icon
                                                icon="trash"
                                                aria-hidden="true"
                                            ></b-icon> 削除
                                        </b-button>
                                    </div>
                                </div>

                                <b-col cols="2">
                                    <b-card-sub-title>
                                        伝票No
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.id }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        来店人数
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.total_visitors }} 人 (男:{{ salesData.male_visitors }} 女:{{ salesData.female_visitors }})
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        来店時間
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.visit_time }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        退店時間
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.leave_time }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        座席
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.disp_seat_name }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        料金プラン
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.basic_plan_type.name }}
                                    </b-card-text>
                                </b-col>
                            </b-row>
                            <b-row class="sales_detail_top_total_sales">
                                <b-card-title>
                                    来店会員
                                </b-card-title>
                                <b-table
                                    dark

                                    striped
                                    :items="salesData.customer_list"
                                    :fields="salesCustomerDetailFields"
                                    class="mb-0 pb-0"
                                >
                                    <template #cell(age)="data">
                                        <div>{{ getStrInData(data.value) }}</div>
                                    </template>
                                </b-table>
                            </b-row>
                            <b-row class="sales_detail_top_total_sales">
                                <b-card-title>
                                    支払情報
                                </b-card-title>
                                <b-table
                                    dark
                                    striped
                                    :items="salesData.sales_payment"
                                    :fields="salesPaymentDetailFields"
                                    class="mb-0 pb-0"
                                >
                                    <template #cell(amount_paid)="data">
                                        <div>
                                            {{ data.value | priceLocaleString }}
                                        </div>
                                    </template>
                                    <template #cell(amount_card_paid)="data">
                                        <div>
                                            {{ data.value | priceLocaleString }}
                                        </div>
                                    </template>
                                    <template #cell(basic_plan_card_tax)="data">
                                        <div>{{ dispBasicPlanCardTax(data) }}%</div>
                                        <!-- <div v-else>{{ dispBasicPlanCardTax }}</div> -->
                                    </template>
                                </b-table>
                            </b-row>
                            <b-row class="sales_detail_top_total_sales">
                                <b-card-title>
                                    総計
                                </b-card-title>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        消費税
                                    </b-card-sub-title>
                                    <b-card-title>
                                        {{ salesData.basic_plan_tax }}%
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        サービス税
                                    </b-card-sub-title>
                                    <b-card-title>
                                        {{ salesData.basic_plan_service_tax }}%
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        総計（税抜）
                                    </b-card-sub-title>
                                    <b-card-title>
                                        <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.total_sales) | priceLocaleString }}
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        総計（税込）
                                    </b-card-sub-title>
                                    <b-card-title>
                                        <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.total_tax_sales) | priceLocaleString }}
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        支払価格
                                    </b-card-sub-title>
                                    <b-card-title>
                                        <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.fixed_total_tax_sales) | priceLocaleString }}
                                    </b-card-title>
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-card>
                    <b-card class="sales_detail_area mt-3">
                        <b-container fluid>
                            <b-row>
                                <b-card-title>
                                    基本料金
                                </b-card-title>
                                <b-table
                                    dark
                                    striped
                                    :items="salesData.sales_service_detail"
                                    :fields="salesServiceDetailFields"
                                    class="mb-0 pb-0"
                                >
                                    <!-- <template #cell(discount_flg)="data">
                                        <div v-if="data.value">割引</div>
                                    </template> -->

                                    <template #cell(fixed_price)="data">
                                        <div>{{ data.value | priceLocaleString }}</div>
                                    </template>

                                    <template #cell(quantity)="data">
                                        <div>{{ data.value | priceLocaleString }}</div>
                                    </template>

                                    <template #cell(total_price)="data">
                                        <div align="right">{{ data.value | priceLocaleString }}</div>
                                    </template>

                                </b-table>
                                <b-col cols="7" class="mt-0 pt-0">
                                </b-col>
                                <b-col cols="2" class="mt-2 pt-2">
                                    小計（税抜）
                                </b-col>
                                <b-col cols="3" class="mt-2 pt-2" align="right">
                                    <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.sales_service_detail_total_price) | priceLocaleString }}
                                </b-col>
                                <!-- <b-col cols="7" class="mt-0 pt-0">
                                </b-col>
                                <b-col cols="2" class="mt-2 pt-2">
                                    総計（税込）
                                </b-col>
                                <b-col cols="3" class="mt-2 pt-2" align="right">
                                    <b-icon icon="currency-yen"></b-icon> {{ salesData.sales_service_detail_total_tax_price }}
                                </b-col> -->
                            </b-row>
                            <b-row class="mt-3 pt-3 sales_detail_separate">
                                <b-card-title>
                                    明細情報
                                </b-card-title>
                                <b-table
                                    dark

                                    striped
                                    :items="salesData.sales_detail"
                                    :fields="salesDetailFields"
                                    class="mb-0 pb-0"
                                    show-empty
                                    empty-text="明細情報は0件です"
                                >
                                    <template #empty="scope">
                                        <h6>{{ scope.emptyText }}</h6>
                                    </template>
                                    <!-- <template #cell(cast)="data">
                                        <span v-if="data.value.icon == null">
                                            <img
                                                src="@/static/img/女性11.jpg"
                                                class="sales_detail_cast"
                                            >
                                        </span>
                                        <span v-else>
                                            <img
                                                :src="data.value.icon"
                                                class="sales_detail_cast"
                                            >
                                        </span>
                                        <span style="position: relative; left: 20px;">{{ data.value.name }}</span>
                                    </template> -->

                                    <!-- <template #cell(bottle_register)="data">
                                        <div v-if="data.value">有</div>
                                        <div v-else>-</div>
                                    </template> -->

                                    <template #cell(fixed_price)="data">
                                        <div>{{ data.value | priceLocaleString }}</div>
                                    </template>

                                    <template #cell(quantity)="data">
                                        <div>{{ data.value | priceLocaleString }}</div>
                                    </template>

                                    <template #cell(total_price)="data">
                                        <div align="right">{{ data.value | priceLocaleString }}</div>
                                    </template>


                                </b-table>
                                <b-col cols="7" class="mt-0 pt-0">
                                </b-col>
                                <b-col cols="2" class="mt-2 pt-2">
                                    小計（税抜）
                                </b-col>
                                <b-col cols="3" class="mt-2 pt-2" align="right">
                                    <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.sales_detail_total_price) | priceLocaleString }}
                                </b-col>
                            </b-row>
                            <b-row class="mt-3 pt-3 sales_detail_separate">
                                <b-card-title>
                                    備考
                                </b-card-title>
                                <b-col cols="12" class="mt-0 pt-0">
                                    <b-card-text v-if="salesData.remarks != null && salesData.remarks.length > 0" style="font-size: 20px; white-space: pre-line;">
                                        {{ salesData.remarks }}
                                    </b-card-text>
                                    <b-card-text v-else>
                                        なし
                                    </b-card-text>
                                    <!-- <b-form-textarea
                                        rows="2"
                                        no-resize
                                        disabled
                                        v-model="salesData.remarks"
                                    ></b-form-textarea> -->
                                </b-col>
                            </b-row>
                        </b-container>
                    </b-card>
                </b-tab>
            </b-tabs>
        </b-row>

        <InputSalesDialog
            ref="inputSalesDialog"
            @update="salesData = $event"

        />

        <DeleteSalesDetailDialog
            ref="deleteSalesDetailDialog"
        />
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'
import utilsMixin from '@/mixins/utils'
import DeleteSalesDetailDialog from '@/components/common/dialog/DeleteSalesDetailDialog'
import InputSalesDialog from '@/components/common/dialog/InputSalesDialog'

export default {
    name: 'SalesDetailItem',
    props: {
    },
    components: {
        DeleteSalesDetailDialog,
        InputSalesDialog,
    },
    data: () => ({
        loading: false,
        salesData: {},
        editSalesData: {},
        salesCustomerDetailFields: [
            {
                key: 'customer_no',
                label: '会員No',
            },
            {
                key: 'name',
                label: '会員名',
            },
            {
                key: 'age',
                label: '年齢',
            },
            {
                key: 'birthday',
                label: '誕生日',
            },
            {
                key: 'rank_name',
                label: 'ランク',
            },
        ],
        salesPaymentDetailFields: [
            {
                key: 'customer.customer_no',
                label: '会員No',
            },
            {
                key: 'customer.name',
                label: '会員名',
            },
            {
                key: 'disp_payment',
                label: '支払方法',
            },
            {
                key: 'amount_paid',
                label: '現金支払金額',
            },
            {
                key: 'amount_card_paid',
                label: 'カード支払金額',
            },
            {
                key: 'basic_plan_card_tax',
                label: 'カード手数料',
            },
        ],
        salesServiceDetailFields: [
            {
                key: 'service.name',
                label: '名称'
            },
            {
                key: 'fixed_price',
                label: '料金'
            },
            {
                key: 'quantity',
                label: '数量'
            },
            {
                key: 'total_price',
                label: '合計'
            },
        ],
        salesDetailFields: [
            {
                key: 'product.name',
                label: '商品名'
            },
            {
                key: 'product.category.large_category_label',
                label: '大カテゴリ'
            },
            {
                key: 'product.category.middle_category_label',
                label: '中カテゴリ'
            },
            {
                key: 'product.category.small_category_label',
                label: '小カテゴリ'
            },
            // {
            //     key: 'bottle_register',
            //     label: 'ボトル登録'
            // },
            {
                key: 'fixed_price',
                label: '料金'
            },
            {
                key: 'quantity',
                label: '数量'
            },
            {
                key: 'total_price',
                label: '合計'
            },
        ],
    }),
    computed: {
        ...mapGetters([
            'sales',
        ]),
        // dispBasicPlanCardTax () {
        //     if (this.salesData != null) {
        //         if (this.salesData.sales_payment.length > 1) {
        //             return '-'
        //         } else if (this.salesData.sales_payment.length == 1) {
        //             return this.salesData.sales_payment[0].basic_plan_card_tax
        //         }
        //     }
        //     return '-'
        // },
    },
    created () {
        // 検索から詳細きてうまくいかせるやり方わかったら、↓の様にstoreから取得する方法に切り替え
        // this.salesData = this.sales.find(s => s.id == this.$route.params['id'])
        this.loading = true

        this.$axios({
            method: 'GET',
            url: `/api/sales/${this.$route.params['id']}/`
        })
        .then(res => {
            console.log(res)
            this.salesData = _.cloneDeep(res.data)
            this.loading = false
        })
        .catch(e => {
            console.log(e)
            this.loading = false
        })

        this.$eventHub.$off('updateSalesDetail')
        this.$eventHub.$on('updateSalesDetail', this.updateSalesDetail)
        console.log('this.salesData', this.salesData)
    },
    mounted () {
    },
    methods: {
        showEditSalesDialog () {
            this.$refs.inputSalesDialog.open(this.salesData)
        },
        showDeleteSalesDetailDialog () {
            this.$refs.deleteSalesDetailDialog.open(this.salesData)
        },
        updateSalesDetail (data) {
            this.salesData = data
        },
        toCustomerDetail () {
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: this.salesData.customer.customer_no
                }
            })
        },
        dispBasicPlanCardTax (data) {
            // console.log('dispBasicPlanCardTax', data)
            if (this.salesData != null) {
                let salesPayment = this.salesData.sales_payment
                if (salesPayment.length > 1) {
                    let i = data.index
                    if (salesPayment[i].amount_card_paid > 0) {
                        return '10'
                    }
                    return '-'
                } else if (salesPayment.length == 1) {
                    return salesPayment[0].basic_plan_card_tax
                }
            }
            return '-'
        }
    },
    mixins: [
        utilsMixin
    ]
}
</script>

<style lang="scss" scoped>
    #sales_detail_wrap {
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        color: white;
        padding: 20px;

        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
        }

        .sales_detail_area {
            background-color: $theme-color;
            padding: 0;
            margin: 0;


            .sales_detail_customer {
                border-radius: 50%;
                width: 80px;
                height: 80px;
            }

            .sales_detail_cast {
                border-radius: 50%;
                width: 50px;
                height: 50px;
                position: relative;
                left: 6px;
            }

            .sales_detail_customer_birthday {
                border-radius: 50%;
                width: 30px;
                height: 30px;
                position: relative;
                left: 7px;
            }

            .sales_detail_top_total_sales {
                margin-top: 25px;
                padding-top: 10px;
                border-top: 0.5px solid rgba(200, 200, 200, 0.1);
            }
        }

        .sales_detail_separate {
            border-top: 1px solid rgba(100, 100, 100, 0.5);
        }
    }

    .loading {
        height: 100%;
        width: 100%;
        .loading_icon {
            display: block;
            margin: 0 auto;
            padding-top: 20%;
        }
    }
</style>
