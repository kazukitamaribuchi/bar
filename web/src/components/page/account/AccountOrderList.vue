<template>
    <div>
        <v-row v-if="!loading" style="margin: 0 1px;">
            <v-col
                v-if="salesHeaderList.length == 0"
                cols="12"
            >
                <v-card-text>伝票情報が存在しません。</v-card-text>
            </v-col>
            <v-col
                v-else
                v-for="(item, i) in salesHeaderList"
                :key="i"
                cols="12"
                xs="6"
                sm="6"
                md="3"

                @click="toPage(item)"
            >
                <v-card
                    class="sales_header_card"
                >
                    <div class="sales_header_title text-subtitle-2">
                        <span>Sales No. {{ item.id }}</span><span class="sales_header_seat_name">席:{{ dispSeat(item.seat) }}</span>
                    </div>

                    <v-list-item two-line>
                        <v-list-item-content>
                            <v-list-item-subtitle>基本料金</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.basic_plan_type.name }}</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                            <v-list-item-subtitle>来店時間</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.visit_time }}</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <v-divider class="mx-2 my-1"/>

                    <v-container fluid class="ma-0 px-4 pt-1">
                        <v-row>
                            <v-col
                                cols="2"
                            >
                                <v-avatar
                                    size="36px"
                                >
                                    <img
                                        alt="Avatar"
                                        src="@/static/img/男性1.jpg"
                                    >
                                    <!-- src="http://localhost:8000/media/upload/男性1.jpg" -->
                                </v-avatar>
                            </v-col>
                            <v-col
                                cols="10"
                                class="pt-1"
                            >
                                <div class="text-subtitle-1 py-0 my-0">
                                    {{ item.customer.name }}
                                </div>
                                <div class="text-caption py-0 my-0">
                                    {{ item.customer.age }} 歳 (誕生日 {{ item.customer.birthday }})
                                </div>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-list-item two-line>
                        <v-list-item-content>
                            <v-list-item-subtitle>会員No</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.customer.customer_no }}</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                            <v-list-item-subtitle>ランク</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.customer.rank_name }}</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                            <v-list-item-subtitle>来店人数</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.total_visitors }} (男{{ item.male_visitors }},女{{ item.female_visitors }})</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <v-list-item two-line>
                        <v-list-item-content>
                            <v-list-item-subtitle>要注意人物</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content" v-if="item.customer.caution_flg">要注意</v-list-item-title>
                            <v-list-item-title class="sales_header_info_content" v-else>-</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                            <v-list-item-subtitle>来店数</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.customer.total_visit }}</v-list-item-title>
                        </v-list-item-content>
                        <v-list-item-content>
                            <v-list-item-subtitle>売上総額</v-list-item-subtitle>
                            <v-list-item-title class="sales_header_info_content">{{ item.customer.total_sales }}円</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <v-divider class="mx-5 my-2"/>

                    <div class="text-caption text-right pr-4">
                        所有ボトル {{ item.customer.bottle.length }}件
                    </div>

                    <v-card
                        v-for="(b, i) in item.customer.bottle"
                        :key="i"
                        flat
                        class="pa-2 sales_header_bottle_info"
                    >
                        <v-list-item two-line>
                            <v-list-item-content>
                                <v-list-item-subtitle>商品名</v-list-item-subtitle>
                                <v-list-item-title class="sales_header_info_content pl-1">{{ b.product.name }}</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        <v-list-item two-line>
                            <v-list-item-content>
                                <v-list-item-subtitle>開封日</v-list-item-subtitle>
                                <v-list-item-title class="sales_header_info_content pl-1">{{ b.open_date }}</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>

                        <v-divider class="mx-5 my-2"/>

                    </v-card>
                </v-card>
            </v-col>
            <v-col cols="12" class="my-0 py-2">
                <NewVisitButton/>
            </v-col>
            <v-col cols="12" class="my-0 py-1">
                <HomeButton/>
            </v-col>
        </v-row>
        <div v-else style="text-align: center;">
            <v-progress-circular
                indeterminate
                color="primary"
                style="text-align: center;"
            ></v-progress-circular>
        </div>
    </div>
</template>
<script>
    import NewVisitButton from '@/components/account/NewVisitButton'
    import HomeButton from '@/components/account/HomeButton'
    import { mapMutations } from 'vuex'

    export default {
        name: 'AccountOrderListItem',
        components: {
            NewVisitButton,
            HomeButton,
        },
        props: {
        },
        data: () => ({
            testData: [
                {
                    sales_no: 1,
                    customer: {
                        name: '吉田修一',
                        customer_no: 1,
                        rank_name: 'ブラック',
                    },
                    visit_time: '2022/06/22 01:32',
                    total_visitors: 1,
                    seat_name: 'C1',
                    is_charter: true,
                    visitor_male: 1,
                    visitor_female: 0,
                    basic_plan_name: '1時間',
                },
                {
                    sales_no: 3,
                    customer: {
                        name: '田中洋平',
                        customer_no: 2,
                        rank_name: 'ブラック',
                    },
                    visit_time: '2022/06/22 02:12',
                    total_visitors: 2,
                    seat_name: 'C2, C3',
                    is_charter: false,
                    visitor_male: 1,
                    visitor_female: 1,
                    basic_plan_name: '2時間',
                },
            ],
            salesHeaderList: [],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_non_close_sales_header/',
            })
            .then(res => {
                console.log(res)
                // this.salesHeaderList = res.data
                this.setSalesHeaderList(res.data)
                // this.loading = false
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
        },
        methods: {
            ...mapMutations([
                'initSelectedProduct',
            ]),
            toPage (item) {
                // console.log('item', item)
                // console.log('this.$route', this.$route)
                this.initSelectedProduct()

                const route = this.$route.name
                const params = {
                    'id': item.id,
                }
                if (route == 'AccountOrderSelect') {
                    this.$router.push({
                        name: 'AccountOrder',
                        params: params
                    })
                } else if (route == 'AccountOrderCheckSelect') {
                    this.$router.push({
                        name: 'AccountOrderHistory',
                        params: params
                    })
                }
            },
            dispSeat (seat) {
                if (seat == null) return '指定無し'
                return seat.seat_name
            },
            setSalesHeaderList (salesHeaderList) {
                let items = salesHeaderList

                this.salesHeaderList = items
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .sales_header_card {
        cursor: pointer;
        // padding: 14px;
        background-color: rgba(224, 224, 224, 0.5);

        .sales_header_title {
            height: 37px;
            line-height: 37px;
            // text-align: right;
            background-color: rgb(52, 52, 52);
            color: white;
            padding: 0 20px;
            .sales_header_seat_name {
                font-size: 12px;
                float: inline-end;
            }
        }
        .sales_header_info_content {
            font-size: 14px !important;
        }
    }

    .sales_header_bottle_info {
        background-color: rgba(224, 224, 224, 0.5);
    }
</style>
