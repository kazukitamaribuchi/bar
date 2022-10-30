<template>
    <div id="all_sales_every_day_by_customer_analytics">
        <b-skeleton-img
            v-if="loading"
            height="290px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1 mt-1">
                売上遷移
            </b-card-text>
            <VueApexCharts
                :height=height
                type="line"
                :options="allSalesEveryDayByCustomerChartOptions"
                :series="allSalesEveryDayByCustomerSeries"
            />
        </div>
    </div>
</template>

<script>
    import dayjs from 'dayjs'
    import isBetween from 'dayjs/plugin/isBetween';
    import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
    import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
    import _ from 'lodash'
    dayjs.extend(isSameOrAfter)
    dayjs.extend(isSameOrBefore)
    dayjs.extend(isBetween)
    const now = dayjs().format('YYYY-MM-DD')

    export default {
        name: 'AllSalesEveryDayByCustomerAnalyticsItem',
        components: {
        },
        props: {
            height: {
                type: Number,
                required: false,
                default: 270,
            },
            targetDate: {
                type: String,
                require: false,
                default: now,
            },
            range: {
                type: Number,
                require: false,
                default: 1
            },
            customerNo: {
                type: Number,
                require: true,
            },
        },
        data: () => ({
            allSalesEveryDayByCustomerChartOptions: {
                chart: {
                  type: 'line',
                  height: 270,
                },
                xaxis: {
                    type: 'category',
                },
                yaxis: [
                    {
                        title: {
                            text: '売上',
                        },
                    },
                    {
                        opposite: true,
                        title: {
                            text: '来店数'
                        }
                    }
                ],
                stroke: {
                    curve: 'straight',
                },
                labels: [
                ],
                legend: {
                    position: 'right',
                    offsetX: 0,
                    offsetY: 50
                },
                fill: {
                    opacity: 0.9
                },
                tooltip: {
                    theme: 'dark',
                    followCursor: true
                },
            },
            allSalesEveryDayByCustomerSeries: [
                {
                    name: '売上',
                    type: 'column',
                    data: []
                },
                {
                    name: '来店数',
                    type: 'line',
                    data: []
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {

            // データ取得の基準日/開始日（オープンの9/1以降にする
            const open = dayjs('2022-09-01')

            const now = dayjs()

            // テスト
            // const now = dayjs('2022-10-07')

            const diff = now.diff(open, 'month')
            let labels = []
            let val = 1

            for (let i = 0; i <= diff; i++) {
                labels.push(open.add(i, 'M').format('YYYY-MM'))
            }

            this.allSalesEveryDayByCustomerChartOptions.labels = labels

            let initArray = [...Array(labels.length)].map(() => 0)
            this.allSalesEveryDayByCustomerSeries[0].data = initArray
            this.allSalesEveryDayByCustomerSeries[1].data = initArray

            console.log('this.customerNo', this.customerNo)

            this.$axios({
                method: 'GET',
                url: '/api/sales/get_month_sales_analytics/',
                params: {
                    customer_no: this.customerNo,
                }
            })
            .then(res => {
                console.log('res', res)
                this.setAllSalesEveryDayByCustomerData(res.data.data)
            })
            .catch(e => {
                console.log(e)
                this.loading = false
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
            setAllSalesEveryDayByCustomerData (item) {
                // console.log('setDaySalesEveryHourData', item)
                const data = item

                let length = this.allSalesEveryDayByCustomerChartOptions.labels.length

                let initArray = [...Array(length)].map(() => 0)
                let sales = _.cloneDeep(initArray)
                let visit = _.cloneDeep(initArray)

                for (const i in data) {
                    const target_month = data[i].month.slice(0, 7)
                    const index = this.allSalesEveryDayByCustomerChartOptions.labels.findIndex(l => l == target_month)
                    if (index != -1) {
                        sales[index] = data[i].total
                        visit[index] = data[i].total_visit
                    }
                }

                this.allSalesEveryDayByCustomerSeries[0].data = sales
                this.allSalesEveryDayByCustomerSeries[1].data = visit
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #all_sales_every_day_by_customer_analytics {
        max-height: 100%;
    //     .customer_day_sales_analytics_area {
    //         max-height: 100%;
    //         background-color: $theme-color;
    //         color: white;
    //     }
    }

</style>
