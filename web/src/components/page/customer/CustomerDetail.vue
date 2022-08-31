<template>
    <div id="customer_detail_wrap">
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
                    title="顧客詳細"
                >
                    <b-card
                        class="customer_detail_area"
                    >
                        <b-container fluid>
                            <b-row>
                                <b-col cols="6" class="pb-0 mb-0">
                                    <b-card-title>
                                        顧客詳細
                                    </b-card-title>
                                </b-col>
                                <b-col cols="4" class="pb-0 mb-0"/>
                                <b-col cols="2" align-self="end" class="pb-0 mb-0">
                                    <b-button
                                        size="sm"
                                        @click="showEditCustomerDialog"
                                    >
                                        <b-icon
                                            icon="pencil"
                                            aria-hidden="true"
                                        ></b-icon> 編集
                                    </b-button>
                                    <b-button
                                        size="sm"
                                        style="position: relative; left: 10px;"
                                        @click="showDeleteCustomerDetailDialog"
                                    >
                                        <b-icon
                                            icon="trash"
                                            aria-hidden="true"
                                        ></b-icon> 削除
                                    </b-button>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="5" class="pt-0 mt-0">
                                    <!-- <b-card-title>
                                        顧客詳細
                                    </b-card-title> -->
                                    <div style="display: flex; margin-left: 30px; margin-top: 30px;">
                                        <div>
                                            <img
                                                src="@/static/img/男性3.jpg"
                                                class="customer_detail_customer_icon"
                                                style="position: relative; top: -13px; left: -7px;"
                                            >
                                        </div>
                                        <div class="mt-3" style="margin-left: 15px;">
                                            <b style="font-size: 20px;">
                                                {{ customerData.name }}
                                            </b>
                                            <b-card-sub-title>
                                                {{ getStrInData(customerData.name_kana) }}
                                            </b-card-sub-title>
                                        </div>
                                    </div>
                                </b-col>
                                <b-col cols="2" class="pt-8">
                                    <b-card-sub-title>
                                        会員No
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;">
                                        {{ getStrInData(customerData.customer_no) }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2" class="pt-8">
                                    <b-card-sub-title>
                                        年齢
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;">
                                        {{ getStrInData(customerData.age) }} 歳
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2" class="pt-8">
                                    <b-card-sub-title>
                                        ランク
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;">
                                        {{ customerData.rank_name }}
                                    </b-card-text>
                                </b-col>
                                <!-- <b-col cols="2" align-self="stretch">
                                    <b-button
                                        size="sm"
                                        @click="showEditCustomerDialog"
                                    >
                                        <b-icon
                                            icon="pencil"
                                            aria-hidden="true"
                                        ></b-icon> 編集
                                    </b-button>
                                    <b-button
                                        size="sm"
                                        style="position: relative; left: 10px;"
                                        @click="showDeleteCustomerDetailDialog"
                                    >
                                        <b-icon
                                            icon="trash"
                                            aria-hidden="true"
                                        ></b-icon> 削除
                                    </b-button>
                                </b-col> -->
                            </b-row>
                            <b-row>
                                <b-tabs pill card fill>
                                    <b-tab
                                        title="詳細情報"
                                    >
                                        <b-card-title
                                            style="border-bottom: 1px solid rgba(200, 200, 200, 0.1); margin-top: 20px; padding-bottom: 14px;"
                                        >
                                            顧客情報
                                        </b-card-title>

                                        <b-row>
                                            <b-col cols="7">
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    住所
                                                </b-card-sub-title>
                                                <b-card-text style="font-size: 20px; white-space: pre-line;">
                                                    {{ strAddress }}
                                                </b-card-text>
                                                <b-card-sub-title class="mt-3" style="font-size: 15px;">
                                                    会社
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(customerData.company) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    職業
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(customerData.job) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    要注意人物
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ strCaution }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    備考
                                                </b-card-sub-title>
                                                <b-card-text style="font-size: 20px; white-space: pre-line;">
                                                    {{ strRemarks }}
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="5">
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    誕生日
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(customerData.birthday) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    電話番号
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(customerData.phone) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    メールアドレス
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(customerData.mail) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    初来店日
                                                </b-card-sub-title>
                                                <b-card-title  style="font-size: 20px;">
                                                    {{ getStrInData(customerData.first_visit) }}
                                                </b-card-title>
                                            </b-col>
                                        </b-row>
                                        <b-card-title
                                            style="border-bottom: 1px solid rgba(200, 200, 200, 0.1); margin-top: 20px; padding-bottom: 14px;"
                                        >
                                            ボトル情報
                                        </b-card-title>
                                        <b-row>
                                            <b-col cols="12" style="min-height: 100px;">
                                                <b-card-sub-title>
                                                    現在保持中
                                                </b-card-sub-title>
                                                <b-row style="min-height: 100px;" v-if="customerOwnBottleList.length != 0">
                                                    <b-col
                                                        v-for="item in customerOwnBottleList"
                                                        :key=item.id
                                                        cols="6"
                                                    >
                                                        <b-card
                                                            bg-variant="dark"
                                                            text-variant="white"
                                                            style="min-height: 180px;"
                                                            class="bottle_card"
                                                        >
                                                        <div text-align="right" align="right">
                                                            <b-button
                                                                size="sm"
                                                                style="position: relative; left: -10px;"
                                                                @click="showEndBottleDialog(item)"
                                                            >
                                                                <b-icon
                                                                    icon="check-circle"
                                                                    aria-hidden="true"
                                                                ></b-icon> 消込
                                                            </b-button>
                                                            <b-button
                                                                size="sm"
                                                                @click="showEditBottleDialog(item)"
                                                            >
                                                                <b-icon
                                                                    icon="pencil"
                                                                    aria-hidden="true"
                                                                ></b-icon> 編集
                                                            </b-button>
                                                            <b-button
                                                                size="sm"
                                                                style="position: relative; left: 10px;"
                                                                @click="showDeleteBottleDetailDialog(item)"
                                                            >
                                                                <b-icon
                                                                    icon="trash"
                                                                    aria-hidden="true"
                                                                ></b-icon> 削除
                                                            </b-button>
                                                        </div>

                                                            <b-container fluid class="mt-0 pt-0">
                                                                <b-row>
                                                                    <b-col cols="3">
                                                                        <img
                                                                            src="@/static/img/酒2.png"
                                                                            class="customer_detail_customer_icon"
                                                                        >
                                                                    </b-col>
                                                                    <b-col cols="9">
                                                                        <b-card-sub-title style="width: 60px;">
                                                                            商品名
                                                                        </b-card-sub-title>
                                                                        <b-card-text>
                                                                            {{ item.product.name }}
                                                                        </b-card-text>
                                                                        <b-card-sub-title>
                                                                            開封日
                                                                        </b-card-sub-title>
                                                                        <b-card-text>
                                                                            {{ item.open_date }}
                                                                        </b-card-text>
                                                                    </b-col>
                                                                </b-row>
                                                            </b-container>
                                                        </b-card>
                                                    </b-col>
                                                </b-row>
                                                <b-row style="min-height: 100px;" v-else>
                                                    <b-col cols="4">
                                                        <b-card-text>
                                                            無し
                                                        </b-card-text>
                                                    </b-col>
                                                </b-row>
                                            </b-col>
                                        </b-row>
                                        <!-- <b-row>
                                            <b-col cols="12" style="min-height: 100px;">
                                                <b-card-sub-title>
                                                    過去データ
                                                </b-card-sub-title>
                                                <b-row style="min-height: 100px;" v-if="customerBottleHistoryList.length != 0">
                                                    <b-col
                                                        v-for="item in customerBottleHistoryList"
                                                        :key=item.id
                                                        cols="6"
                                                    >
                                                        <b-card
                                                            bg-variant="dark"
                                                            text-variant="white"
                                                            style="min-height: 180px;"
                                                            class="bottle_card"
                                                            @click="showBottleDetail(item)"
                                                        >
                                                        <div text-align="right" align="right">
                                                            <b-button
                                                                size="sm"
                                                                style="position: relative; left: -10px;"
                                                                @click="showEditCustomerDialog"
                                                            >
                                                                <b-icon
                                                                    icon="check-circle"
                                                                    aria-hidden="true"
                                                                ></b-icon> 飲終
                                                            </b-button>
                                                            <b-button
                                                                size="sm"
                                                                @click="showDeleteCustomerDetailDialog"
                                                            >
                                                                <b-icon
                                                                    icon="pencil"
                                                                    aria-hidden="true"
                                                                ></b-icon> 編集
                                                            </b-button>
                                                            <b-button
                                                                size="sm"
                                                                style="position: relative; left: 10px;"
                                                                @click="showDeleteCustomerDetailDialog"
                                                            >
                                                                <b-icon
                                                                    icon="trash"
                                                                    aria-hidden="true"
                                                                ></b-icon> 削除
                                                            </b-button>
                                                        </div>

                                                            <b-container fluid class="mt-0 pt-0">
                                                                <b-row>
                                                                    <b-col cols="3">
                                                                        <img
                                                                            src="@/assets/img/酒2.png"
                                                                            class="customer_detail_customer_icon"
                                                                        >
                                                                    </b-col>
                                                                    <b-col cols="9">
                                                                        <b-card-sub-title style="width: 60px;">
                                                                            商品名
                                                                        </b-card-sub-title>
                                                                        <b-card-text>
                                                                            {{ item.product.name }}
                                                                        </b-card-text>
                                                                        <b-card-sub-title>
                                                                            開封日
                                                                        </b-card-sub-title>
                                                                        <b-card-text>
                                                                            {{ item.open_date }}
                                                                        </b-card-text>
                                                                    </b-col>
                                                                </b-row>
                                                            </b-container>
                                                        </b-card>
                                                    </b-col>
                                                </b-row>
                                                <b-row style="min-height: 100px;" v-else>
                                                    <b-col cols="4">
                                                        <b-card-text>
                                                            無し
                                                        </b-card-text>
                                                    </b-col>
                                                </b-row>
                                            </b-col>

                                        </b-row> -->
                                    </b-tab>
                                    <b-tab
                                        title="売上データ"
                                    >
                                        <b-card-title
                                            style="border-bottom: 1px solid rgba(200, 200, 200, 0.1); margin-top: 20px; padding-bottom: 14px;"
                                        >
                                            売上情報
                                        </b-card-title>

                                        <b-row>
                                            <b-col cols="4">
                                                <TotalByCustomerSalesAnalytics
                                                    :customerNo="customerData.customer_no"
                                                    :totalSalesData="customerData.total_sales"
                                                />
                                            </b-col>
                                            <b-col cols="4">
                                                <TotalByCustomerVisitAnalytics
                                                    :customerNo="customerData.customer_no"
                                                    :totalVisitData="customerData.total_visit"
                                                />
                                            </b-col>
                                            <b-col cols="4">
                                                <NextRankByCustomerAnalytics
                                                    :rank="customerData.rank_id"
                                                    :totalSalesData="customerData.total_sales"
                                                />
                                            </b-col>
                                        </b-row>
                                        <b-row>
                                            <b-col cols="12">
                                                <AllSalesEveryDayByCustomerAnalytics
                                                    :customerNo="customerData.customer_no"
                                                />
                                            </b-col>
                                        </b-row>
                                    </b-tab>
                                </b-tabs>
                            </b-row>
                        </b-container>
                    </b-card>
                </b-tab>
            </b-tabs>
        </b-row>

        <!-- <b-card
            class="customer_detail"
            text-variant="white"
        >
            <b-card-title
                :title="customerData.name"
            >
            </b-card-title>
            <b-card-sub-title
                :sub-title=customerData.name_kana
            >
            </b-card-sub-title>

            <b-row>
                <b-col cols="4">
                    <b-card
                        header="顧客ランク"
                        class="mb-2"
                        header-text-variant="white"
                        :header-bg-variant=backColorHeaderRank
                        border-variant="secondary"
                        :text-variant=textColorRank
                        :bg-variant=backColorRank
                    >
                        <b-card-body class="customer_detail_card_body">
                            <div>
                                <label for="rating-inline">
                                    <b-icon
                                        :icon=cardType
                                        :style=cardColor
                                    ></b-icon>
                                    {{ customerData.rank_name }}
                                </label>
                                <b-form-rating
                                    id="rating-inline"
                                    inline no-border
                                    :value=customerData.rank_id
                                    readonly
                                ></b-form-rating>
                            </div>
                            <small class="customer_detail_rank_detail">
                                【初回来店日】  2022年6月15日
                            </small>
                            <small class="customer_detail_rank_detail">
                                【総来店数】  110 回
                            </small>
                            <small class="customer_detail_rank_detail">
                                【総売上】  ￥100,000,000
                            </small>
                        </b-card-body>
                    </b-card>
                    <b-card
                        header="基本情報"
                        :text-variant=textColorBasis
                        :bg-variant=backColorBasis
                        header-text-variant="white"
                        border-variant="secondary"
                        :header-bg-variant=backColorHeaderBasis
                    >
                        <b-card-body class="customer_detail_card_body">
                            <b-card-text>
                                <b-form-group
                                    label="年齢"
                                    class="customer_detail_age"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.age"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="誕生日"
                                    class="customer_detail_birthday"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.birthday"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="職業"
                                    class="customer_detail_job"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.job"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="会社"
                                    class="customer_detail_company"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.company"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                            </b-card-text>
                        </b-card-body>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card
                        title="予約状況、ボトルとか"
                        text-variant="black"
                    >

                    </b-card>
                </b-col>
                <b-col>
                    <b-card
                        title="グラフとかテーブルで指名、売上の傾向とか"
                        text-variant="black"
                    >
                    </b-card>
                </b-col>
            </b-row>
        </b-card> -->

        <CreateCustomerDialog
            ref="createCustomer"
            @update="customerData = $event"
        />

        <DeleteCustomerDetailDialog
            ref="deleteCustomerDetailDialog"
        />

        <EndBottleDetailDialog
            ref="endBottleDetailDialog"
            @deleteCustomerBottleDetail="deleteCustomerBottleDetail"
        />

        <CreateBottleDialog
            ref="editBottleDialog"
            @updateCustomerBottleDetail="updateCustomerBottleDetail"
        />

        <DeleteBottleDetailDialog
            ref="deleteBottleDetailDialog"
            @deleteCustomerBottleDetail="deleteCustomerBottleDetail"
        />
    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'
import { mapGetters } from 'vuex'
import _ from 'lodash'
import utilsMixin from '@/mixins/utils'
import DeleteCustomerDetailDialog from '@/components/common/dialog/DeleteCustomerDetailDialog'
import EndBottleDetailDialog from '@/components/common/dialog/EndBottleDetailDialog'
import CreateBottleDialog from '@/components/common/dialog/CreateBottleDialog'
import DeleteBottleDetailDialog from '@/components/common/dialog/DeleteBottleDetailDialog'
import TotalByCustomerSalesAnalytics from '@/components/common/analytics/TotalByCustomerSalesAnalytics'
import TotalByCustomerVisitAnalytics from '@/components/common/analytics/TotalByCustomerVisitAnalytics'
import NextRankByCustomerAnalytics from '@/components/common/analytics/NextRankByCustomerAnalytics'
import AllSalesEveryDayByCustomerAnalytics from '@/components/common/analytics/AllSalesEveryDayByCustomerAnalytics'

export default {
    name: 'CustomerDetailItem',
    data: () => ({
        customerId: '',
        customerData: {},
        editCustomerData: {},
        colorx: 'rgb(16, 16, 179)',
        editCustomerDialog: false,
        isDanger: false,
        // 現在のボトルデータ
        customerOwnBottleList: [],
        // 過去のボトルデータ
        customerBottleHistoryList: [],
        loading: false,
    }),
    props: {
    },
    components: {
        CreateCustomerDialog,
        DeleteCustomerDetailDialog,
        EndBottleDetailDialog,
        CreateBottleDialog,
        DeleteBottleDetailDialog,
        TotalByCustomerSalesAnalytics,
        TotalByCustomerVisitAnalytics,
        NextRankByCustomerAnalytics,
        AllSalesEveryDayByCustomerAnalytics,
    },
    computed: {
        ...mapGetters([
            'customer',
            'bottle',
        ]),
        cardColor () {
            let cardColor = 'rgb(116, 116, 116)'
            switch (this.customerData.rank_id) {
                case 1:
                    cardColor = 'rgb(116, 116, 116)'
                    break;
                case 2:
                    cardColor = 'rgb(192, 192, 192)'
                    break;
                case 3:
                    cardColor = 'rgb(185, 199, 19)'
                    break;
                case 4:
                    cardColor = 'rgb(98, 98, 98)'
                    break;
                case 5:
                    cardColor ='rgb(0, 0, 0)'
                    break;
            }
            return `color: ${cardColor};`
        },
        cardType () {
            if (this.customerData.rank_id == 1) return 'credit-card2-front'
            return 'credit-card2-front-fill'
        },
        backColorBasis () {
            if (this.isDanger) return 'danger'
            return 'light'
        },
        textColorBasis () {
            if (this.isDanger) return 'white'
            return 'black'
        },
        backColorHeaderBasis () {
            if (this.isDanger) return 'danger'
            return 'dark'
        },
        backColorHeaderRank () {
            if (this.isDanger) return 'danger'
            return 'dark'
        },
        backColorRank () {
            if (this.isDanger) return 'danger'
            return 'light'
        },
        textColorRank () {
            if (this.isDanger) return 'white'
            return 'black'
        },
        strCaution () {
            if (this.customerData != null
                && this.customerData.caution_flg) {
                    return '要注意'
                }
            return '-'
        },
        strRemarks () {
            if (this.customerData != null
                && this.customerData.remarks != ''
                && this.customerData.remarks != null) {
                    return this.customerData.remarks
                }
            return '-'
        },
        strAddress () {
            if (this.customerData != null
                && this.customerData.address != null
                && this.customerData.address != '') {
                    return this.customerData.address
                }
            return '-'
        },
    },
    created () {
        this.loading = true
        this.$axios({
            method: 'GET',
            url: `/api/customer/${this.$route.params['id']}/`,
        })
        .then(res => {
            console.log(res)
            this.customerData = _.cloneDeep(res.data)
            this.customerOwnBottleList = _.cloneDeep(res.data.bottle)
            this.loading = false
        })
        .catch(e => {
            console.log(e)
            this.customerData = {}
            this.loading = false
        })

        // 検索から詳細きてうまくいかせるやり方わかったら、↓の様にstoreから取得する方法に切り替え
        // const customer_no = this.$route.params['id']
        // const id = this.$route.params['id']
        //
        // if (this.customer.find(c => c.id == id) == undefined) {
        //     this.customerData = {}
        // }  else {
        //     this.customerData = _.cloneDeep(this.customer.find(c => c.id == id))
        //     const customerNo = this.customerData.customer_no
        //
        //     const customerOwnBottleList = this.bottle.filter(function(b) {
        //         if (b.customer != null
        //             && b.customer.customer_no == customerNo
        //             && (!b.end_flg && !b.waste_flg && !b.delete_flg)) {
        //             return true
        //         }
        //     })
        //
        //     // const customerBottleHistoryList = this.bottle.filter(function(b) {
        //     //     if (b.customer != null
        //     //         && b.customer.customer_no == customer_no
        //     //         && (b.end_flg || b.waste_flg || b.delete_flg)) {
        //     //         return true
        //     //     }
        //     // })
        //
        //     this.customerOwnBottleList = customerOwnBottleList
        //     // this.customerBottleHistoryList = customerBottleHistoryList
        // }

        // console.log('customerData', this.customerData)
    },
    beforeRouteUpdate (to, from, next) {
        if (from.name == 'CustomerDetail') {
            // this.$axios({
            //     method: 'GET',
            //     url: `/api/customer/${this.$route.params['id']}`,
            // })
            // .then(res => {
            //     console.log(res)
            //     this.customerData = _.cloneDeep(res.data)
            //     this.isDanger = this.customerData.caution_flg
            // })
            // .catch(e => {
            //     console.log(e)
            // })
            // console.log('this.customer.find(c => c.customer_no == to.params.id)', this.customer.find(c => c.customer_no == to.params.id))
            this.customerData = _.cloneDeep(this.customer.find(c => c.id == to.params.id))
            // console.log('this.customerData', this.customerData)
        }
        // console.log('CustomerDetail => beforeRouteUpdate')
        // console.log(to)
        // console.log(from)
        // console.log(next)
        next();
    },
    mounted () {
        // console.log(this.$router.referrer)
        // console.log(this.$router.toPage)
    },
    // beforeRouteUpdate (to, from, next) {
    //     this.cusotmerId = to.query.id
    //     this.customerData = _.cloneDeep(this.customer.find(c => c.id === this.customerId))
    //     console.log(this.customer)
    //     console.log(this.customerId)
    //     console.log(this.customerData)
    //     next()
    // },
    methods: {
        showEditCustomerDialog () {
            this.$refs.createCustomer.open(this.customerData)
        },
        showDeleteCustomerDetailDialog () {
            this.$refs.deleteCustomerDetailDialog.open(this.customerData)
        },
        showBottleDetail (item) {
            console.log('bottleDetail', item)
        },
        showEditBottleDialog (item) {
            console.log('item', item)
            if (item.delete_flg || item.end_flg) return
            this.$refs.editBottleDialog.open(item)
        },
        showDeleteBottleDetailDialog (item) {
            console.log('item', item)
            this.$refs.deleteBottleDetailDialog.open(item)
        },
        showEndBottleDialog (item) {
            console.log('item', item)
            this.$refs.endBottleDetailDialog.open(item)
        },
        deleteCustomerBottleDetail (item) {
            this.customerData.bottle = this.customerData.bottle.filter(b => b.id != item.id)
            this.customerOwnBottleList = this.customerOwnBottleList.filter(b => b.id != item.id)
        },
        updateCustomerBottleDetail (item) {
            console.log('updateCustomerBottleDetail', item)
            this.customerData.bottle = item.customer.botttle
            const customerNo = this.customerData.customer_no

            const customerOwnBottleList = this.bottle.filter(function(b) {
                if (b.customer != null
                    && b.customer.customer_no == customerNo
                    && (!b.end_flg && !b.waste_flg && !b.delete_flg)) {
                    return true
                }
            })

            this.customerOwnBottleList = customerOwnBottleList
        }
    },
    mixins: [
        utilsMixin
    ]
}
</script>

<style lang="scss" scoped>
    #customer_detail_wrap {
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

        .customer_detail_area {
            background-color: $theme-color;
            padding: 0;
            margin: 0;

            .customer_detail_customer_icon {
                border-radius: 50%;
                width: 100px;
                height: 100px;
            }
        }

        // .bottle_card {
        //     cursor: pointer;
        // }

        // .customer_detail {
        //     background-color: $theme-color;
        //     height: 100%;
        //
        //     .customer_detail_card_body {
        //         padding: 0 1.5rem;
        //
        //
        //         .input-group-text {
        //             height: 100%;
        //             border-radius: 5px 0 0 5px !important;
        //         }
        //
        //         .customer_detail_age {
        //             width: 6rem;
        //         }
        //
        //         .customer_detail_birthday {
        //             width: 8rem;
        //         }
        //
        //         .customer_detail_job {
        //             width: 12rem;
        //         }
        //
        //         .customer_detail_rank_detail {
        //             display: block;
        //         }
        //
        //     }
        //
        // }

    }

// .con-slot-tabs {
//     margin-bottom: 4px;
//     background: white !important;
// }

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
