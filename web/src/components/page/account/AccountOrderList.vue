<template>
    <div>
        <v-row v-if="!loading" style="margin: 0 1px;" class="pa-1">
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
                class="px-1"
                cols="12"
                @click="toPage(item)"
            >
                <v-card
                    class="sales-header"
                >
                    <v-card-title class="h6 my-0 pb-1 text-center">
                        伝票No : {{ item.id }}
                    </v-card-title>

                    <v-divider class="mx-5 my-1">
                    </v-divider>

                    <v-card-title class="subtitle-2 mt-0 pt-2 mb-0 pb-1">
                        席情報
                    </v-card-title>
                    <v-card-text class="my-0 py-1">
                        <div v-if="item.seat != null">
                            席： <span style="float: inline-end">{{ item.seat.seat_name }}</span>
                        </div>
                        <div v-else>
                            席： <span style="float: inline-end">指定無し</span>
                        </div>
                        <div>
                            基本料金: <span style="float: inline-end">{{ item.basic_plan_type.name }}</span>
                        </div>
                        <div>
                            来店時間: <span style="float: inline-end; font-size: 12px;">{{ item.visit_time }}</span>
                        </div>


                    </v-card-text>
                    <v-divider class="mx-5 my-1">
                    </v-divider>
                    <v-card-title class="subtitle-2 mt-0 pt-2 mb-0 pb-1">
                        顧客情報
                    </v-card-title>
                    <v-card-text class="my-0 py-1">
                        <div>
                            会員No： <span style="float: inline-end">{{ item.customer.customer_no }}</span>
                        </div>
                        <div>
                            会員名： <span style="float: inline-end">{{ item.customer.name }}</span>
                        </div>
                        <div>
                            ランク： <span style="float: inline-end">{{ item.customer.rank_name }}</span>
                        </div>
                        <div>
                            来店人数： <span style="float: inline-end">{{ item.total_visitors }} (男{{ item.male_visitors }},女{{ item.female_visitors }})</span>
                        </div>
                    </v-card-text>
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
                this.salesHeaderList = res.data
                this.loading = false
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
            toPage (item) {
                // console.log('item', item)
                // console.log('this.$route', this.$route)
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
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .sales-header {
        cursor: pointer;
        padding: 14px;
        background-color: rgba(224, 224, 224, 0.5);
    }
</style>
