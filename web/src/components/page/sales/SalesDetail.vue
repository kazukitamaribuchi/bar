<template>
    <div id="sales_detail_wrap">
        <b-row>
            <b-tabs pill>
                <b-tab
                    title="売上詳細"
                >
                    <b-card
                        class="sales_detail_area"
                    >
                        <b-container fluid>
                            <b-row>
                                <b-col cols="4">
                                    <b-card-title>
                                        売上詳細
                                    </b-card-title>
                                    <b-card-sub-title>
                                        伝票No{{ salesData.id }}
                                    </b-card-sub-title>
                                    <div style="display: flex; margin-left: 30px; margin-top: 20px;">
                                        <div>
                                            <img
                                                src="@/assets/img/男性3.jpg"
                                                class="sales_detail_customer"
                                            >
                                        </div>
                                        <div class="mt-3" style="margin-left: 15px;">
                                            <b>
                                                {{ salesData.customer.name }}
                                            </b>
                                            <b-card-sub-title>
                                                {{ getStrInData(salesData.customer.name_kana) }}
                                            </b-card-sub-title>
                                        </div>
                                    </div>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        年齢
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.age) }} 歳
                                    </b-card-text>
                                    <b-card-sub-title>
                                        誕生日
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.birthday) }}
                                        <span
                                            v-if="salesData.customer.birthday == salesData.account_date"
                                        >
                                            <img
                                                src="@/assets/img/ケーキ.png"
                                                class="sales_detail_customer_birthday">
                                        </span>
                                    </b-card-text>
                                    <b-card-sub-title>
                                        ランク
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.customer.rank_name }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        会社
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.company) | truncate(20) }}
                                    </b-card-text>
                                    <b-card-sub-title>
                                        職業
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.job) | truncate(20) }}
                                    </b-card-text>
                                    <b-card-sub-title>
                                        電話番号
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.phone) | truncate(20) }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        メールアドレス
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ getStrInData(salesData.customer.mail) | truncate(20) }}
                                    </b-card-text>
                                    <b-card-sub-title>
                                        来店時間
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.visit_time }}
                                    </b-card-text>
                                    <b-card-sub-title>
                                        退店時間
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.leave_time }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <div style="height: 55px;">
                                        <!-- <b-button
                                            size="sm"
                                            @click="showEditSalesDialog"
                                        >
                                            <b-icon
                                                icon="pencil"
                                                aria-hidden="true"
                                            ></b-icon> 編集
                                        </b-button> -->
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
                                </b-col>
                            </b-row>
                            <b-row class="sales_detail_top_total_sales">
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        総計（税込）
                                    </b-card-sub-title>
                                    <b-card-title>
                                        <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.total_tax_sales) }}
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        総計（税抜）
                                    </b-card-sub-title>
                                    <b-card-title>
                                        <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.total_sales) }}
                                    </b-card-title>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        料金プラン
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.basic_plan_type.name }}
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
                                <b-col cols="1">
                                    <b-card-sub-title>
                                        座席名
                                    </b-card-sub-title>
                                    <b-card-text v-if="salesData.seat != null">
                                        {{ salesData.seat.seat_name }}
                                    </b-card-text>
                                    <b-card-text v-else>
                                        -
                                    </b-card-text>
                                </b-col>
                                <b-col cols="1">
                                    <b-card-sub-title>
                                        支払い方法
                                    </b-card-sub-title>
                                    <b-card-text v-if="salesData.payment == 0">
                                        現金
                                    </b-card-text>
                                    <b-card-text v-else>
                                        カード
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2">
                                    <b-card-sub-title>
                                        会計日
                                    </b-card-sub-title>
                                    <b-card-text>
                                        {{ salesData.account_date }}
                                    </b-card-text>
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
                                    borderless
                                    striped
                                    :items="salesData.sales_service_detail"
                                    :fields="salesServiceDetailFields"
                                    class="mb-0 pb-0"
                                >
                                    <template #cell(discount_flg)="data">
                                        <div v-if="data.value">割引</div>
                                    </template>

                                    <template #cell(total_price)="data">
                                        <div align="right">{{ data.value }}</div>
                                    </template>

                                </b-table>
                                <b-col cols="7" class="mt-0 pt-0">
                                </b-col>
                                <b-col cols="2" class="mt-2 pt-2">
                                    総計（税抜）
                                </b-col>
                                <b-col cols="3" class="mt-2 pt-2" align="right">
                                    <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.sales_service_detail_total_price) }}
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
                                    borderless
                                    striped
                                    :items="salesData.sales_detail"
                                    :fields="salesDetailFields"
                                    class="mb-0 pb-0"
                                >
                                    <template #cell(cast)="data">
                                        <span v-if="data.value.icon == null">
                                            <img
                                                src="@/assets/img/女性11.jpg"
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
                                    </template>

                                    <template #cell(bottle_register)="data">
                                        <div v-if="data.value">有</div>
                                    </template>

                                    <template #cell(total_price)="data">
                                        <div align="right">{{ data.value }}</div>
                                    </template>


                                </b-table>
                                <b-col cols="7" class="mt-0 pt-0">
                                </b-col>
                                <b-col cols="2" class="mt-2 pt-2">
                                    総計（税抜）
                                </b-col>
                                <b-col cols="3" class="mt-2 pt-2" align="right">
                                    <b-icon icon="currency-yen"></b-icon> {{ getNumInData(salesData.sales_detail_total_price) }}
                                </b-col>
                            </b-row>
                            <b-row class="mt-3 pt-3 sales_detail_separate">
                                <b-card-text>
                                    備考
                                </b-card-text>
                                <b-col cols="12" class="mt-0 pt-0">
                                    <b-card-text style="font-size: 20px; white-space: pre-line;">
                                        {{ salesData.remarks }}
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
        salesData: {},
        editSalesData: {},
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
                key: 'discount_flg',
                label: '割引料金'
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
        salesAppointDetailFields: [
            {
                key: 'cast',
                label: 'キャスト'
            },
            {
                key: 'service.name',
                label: '名称'
            },
            {
                key: 'service.basic_plan_type',
                label: '料金プラン'
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
            {
                key: 'bottle_register',
                label: 'ボトル登録'
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
    }),
    computed: {
        ...mapGetters([
            'sales',
        ]),
    },
    created () {
        // 検索から詳細きてうまくいかせるやり方わかったら、↓の様にstoreから取得する方法に切り替え
        this.salesData = this.sales.find(s => s.id == this.$route.params['id'])
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
</style>
