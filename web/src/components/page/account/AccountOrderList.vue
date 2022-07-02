<template>
    <div>
        <v-row>
            <v-col
                v-for="(item, i) in testData"
                :key="i"
                cols="6"
                @click="toPage(item)"
            >
                <v-card
                    style="cursor: pointer;"
                >
                    <v-card-title class="h6 my-0 pb-1 text-center">
                        伝票No : {{ item.sales_no }}
                    </v-card-title>

                    <v-divider class="mx-5 my-1">
                    </v-divider>

                    <v-card-title class="subtitle-2 mt-0 pt-2 mb-0 pb-1">
                        席情報
                    </v-card-title>
                    <v-card-text class="my-0 py-1">
                        <div>
                            席： <span style="float: inline-end">{{ item.seat_name }}</span>
                        </div>
                        <div>
                            貸切: <span style="float: inline-end">{{ item.is_charter }}</span>
                        </div>
                        <div>
                            基本料金: <span style="float: inline-end">{{ item.basic_plan_name }}</span>
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
                            来店人数： <span style="float: inline-end">{{ item.total_visitors }} (男{{ item.visitor_male }},女{{ item.visitor_female }})</span>
                        </div>
                    </v-card-text>
                    <!-- <v-divider class="mx-5 my-1">
                    </v-divider>
                    <v-card-title class="subtitle-2 mt-0 pt-2 mb-0 pb-1">
                        注文情報
                    </v-card-title>
                    <v-card-text class="my-0 py-1">
                        <div>
                            会員No： {{ item.customer.customer_no }}
                        </div>
                        <div>
                            会員名： {{ item.customer.name }}
                        </div>
                        <div>
                            ランク： {{ item.customer.rank_name }}
                        </div>
                        <div>
                            来店人数： {{ item.total_visitors }} (男{{ item.visitor_male }},女{{ item.visitor_female }})
                        </div>
                    </v-card-text> -->
                    <!-- <v-row>
                        <v-col cols="4">
                            <v-img
                                style="width: 85px; height: 85px; margin: 25px 0 0 17px;"
                                src="http://localhost:8000/media/upload/伝票1.jpg"
                            ></v-img>
                        </v-col>
                        <v-col cols="12">

                            <p class="mb-0">伝票No. {{ item.sales_no }}</p>
                            <p class="mb-0">席 {{ item.seat_name }}</p>
                            <p class="mb-0">会員No {{ item.customer.customer_no }}</p>
                            <p class="mb-0">会員名 {{ item.customer.name }}</p>
                            <p class="mb-0">来店時間 {{ item.visit_time }}</p>
                            <p class="mb-0">来店人数 {{ item.total_visitors }}</p>
                        </v-col>
                    </v-row> -->
                </v-card>
            </v-col>
            <v-col cols="12" class="my-0 py-2">
                <NewVisitButton/>
            </v-col>
            <v-col cols="12" class="my-0 py-1">
                <HomeButton/>
            </v-col>
        </v-row>
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
            ]
        }),
        beforeCreate () {
        },
        created () {
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
                    'id': item.sales_no,
                }
                if (route == 'AccountOrderSelect') {
                    this.$router.push({
                        name: 'AccountOrder',
                        params: params
                    })
                } else if (route == 'AccountOrderCheckSelect') {
                    this.$router.push({
                        name: 'AccountOrderCheck',
                        params: params
                    })
                }
            },
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
