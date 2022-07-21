<template>
    <div style="padding-bottom: 120px;">
        <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            注文確認
        </p>
        <v-card-text class="text-right pa-0">
            <span style="font-size: 12px; color: rgba(70, 70, 70, 0.8);">
                伝票No: {{ salesData.header_id }}
            </span>
            <!-- <span style="font-size: 12px;">
                00000001
            </span> -->
        </v-card-text>
        <v-divider class="mx-4"/>
        <v-card
            flat
            class="pa-1"
        >
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
                            <v-list-item-title>来店日付</v-list-item-title>
                            <v-list-item-subtitle>{{ salesData.visit_time }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col cols="5" class="py-0">
                    <v-list-item two-line>
                        <v-list-item-content class="py-0">
                            <v-list-item-title>会員No</v-list-item-title>
                            <v-list-item-subtitle>{{ salesData.customer.customer_no }}</v-list-item-subtitle>
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
                            <v-list-item-subtitle>{{ salesData.customer.rank_name }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col cols="7" class="py-0">
                    <v-list-item two-line>
                        <v-list-item-content class="py-0">
                            <v-list-item-title>顧客名</v-list-item-title>
                            <v-list-item-subtitle>{{ salesData.customer.name }}</v-list-item-subtitle>
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
        <v-container fluid class="mt-3">
            <v-row>
                <v-col cols="5" class="py-0">
                    <div style="font-size: 17px;">
                        注文数
                    </div>
                </v-col>
                <v-col cols="7" class="text-right py-0">
                    <div style="font-size: 17px;">
                        {{ totalOrderCnt }} 点
                    </div>
                </v-col>
                <v-col cols="5">
                    <div style="font-size: 25px;">
                        合計(税込)
                    </div>
                </v-col>
                <v-col cols="7" class="text-right">
                    <div style="font-size: 25px;">
                        ￥1,999,999
                    </div>
                </v-col>
                <v-divider class="mx-2"/>
            </v-row>

            <v-row class="pt-4">
                <v-card-title>
                    明細情報
                </v-card-title>
                <!-- <p style="font-size:13px; color:rgba(20, 20, 20, 1);">明細情報</p> -->
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
                            ></v-text-field>
                        </v-col>
                        <v-col cols="5" class="py-0">
                            <label class="label-style">
                                数量
                            </label>
                            <b-form-spinbutton
                                class="mt-2"
                                id="sb-inline"
                                v-model="item.quantity"
                            ></b-form-spinbutton>
                        </v-col>
                    </v-row>
                    <v-row class="pa-2">
                        <v-col cols="4" class="py-0">
                            <label class="label-style">
                                ボトル登録
                            </label>
                            <v-switch
                                v-model="item.bottle"
                                class="mt-0"
                                :disabled="isNotDrink(item)"
                            ></v-switch>
                        </v-col>
                        <v-col cols="3" class="py-0">
                            <label class="label-style">
                                非課税
                            </label>
                            <v-checkbox
                                v-model="item.tax_free_flg"
                                class="mt-0"
                            ></v-checkbox>
                        </v-col>
                        <v-col cols="2" class="py-0">
                            <label class="label-style">
                                締め
                            </label>
                            <v-checkbox
                                v-model="item.end_flg"
                                disabled
                                class="mt-0"
                            ></v-checkbox>
                        </v-col>
                        <v-col cols="3" class="py-0 text-center">
                            <label class="label-style">
                                削除
                            </label>
                            <vs-button
                                circle
                                icon
                                danger
                                @click="deleteProductDetail(item)"
                                style="margin: 0 auto;"
                            >
                                <i class='bx bx-trash' ></i>
                            </vs-button>
                        </v-col>
                    </v-row>
                    <v-divider/>
                </v-card>

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
                            3時間30分
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
                    <div style="font-size: 14px;" class="mt-2">
                        基本料金
                    </div>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            ￥5,000
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            × 1
                        </div>
                    </v-col>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            ￥2,500
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            × 1
                        </div>
                    </v-col>
                    <div style="font-size: 14px;">
                        延長料金
                    </div>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            ￥5,000
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            × 2
                        </div>
                    </v-col>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            ￥2,500
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            × 2
                        </div>
                    </v-col>
                    <div style="font-size: 14px;">
                        TAX
                    </div>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            サービス料
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <!-- <div style="font-size: 14px;">
                            10%
                        </div> -->
                        <v-select
                          :items="basicPlanServiceTaxList"
                          item-text="name"
                          item-value="id"
                          dense
                          outlined
                          v-model="salesData.basic_plan_service_tax"
                        ></v-select>
                    </v-col>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            消費税
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            10%
                        </div>
                    </v-col>
                    <v-col cols="5" class="text-right py-0">
                        <div style="font-size: 14px;">
                            カード会計
                        </div>
                    </v-col>
                    <v-col cols="7" class="text-right py-0">
                        <div style="font-size: 14px;">
                            10%
                        </div>
                    </v-col>
                </v-row>
            </v-row>
        </v-container>

        <EndSalesFooter/>
    </div>
</template>
<script>
    import _ from 'lodash'
    import EndSalesFooter from '@/components/account/EndSalesFooter'

    export default {
        name: 'AccountOrderHistoryItem',
        components: {
            EndSalesFooter,
        },
        props: {
        },
        data: () => ({
            salesData: null,
            basicPlanServiceTaxList: [
                { name: '10%', id: 1 },
                { name: '0%', id: 2 },
            ]
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'get',
                url: `/api/sales/${this.$route.params.id}`,
            })
            .then(res => {
                console.log(res)
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
        },
        computed: {
            totalOrderCnt () {
                let cnt = 0
                for (const salesDetail of this.salesData.sales_detail) {
                    cnt += salesDetail.quantity
                }
                return cnt
            },
        },
        methods: {
            undo () {
                this.$router.push({
                    name: 'AccountOrderCheckSelect',
                })
            },
            isNotDrink (item) {
                return item.product.category.large_category == 2
            },
            deleteProductDetail (item) {

            },
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .undo-btn {
        font-size: 35px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }

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
        // color: white;
        color: rgba(50, 50, 50, 0.7);
        line-height: 25px;
        border-radius: 4px;
        margin: 0 0 9px 4px;
        // background-color: rgb(140, 140, 140);
    }
</style>
