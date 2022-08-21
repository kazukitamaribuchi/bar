<template>
    <b-container fluid>
        <b-skeleton-img
            v-if="loading"
            style="position: relative; top: -6px;"
            height="180px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1">
                次ランクまで
            </b-card-text>
            <div class="text-right" style="font-family: 'Noto Sans JP'; font-size: 1.5rem;">
                <b-icon icon="currency-yen"></b-icon> {{ needForNextRank |priceLocaleString }}
            </div>
            <div class="text-right" style="color: #6c757d;">
                sales
            </div>
            <!-- <div style="display: flex; justify-content: space-between;">
                <span style="display: inline-block;">
                    現在売上
                </span>
                <span style="display: inline-block;">
                    50%
                </span>
            </div> -->

            <b-row>
                <b-col cols="12" class="mt-0 pt-0">
                    <VueApexCharts
                        height="100"
                        type="bar"
                        :options="totalSalesChartOptions"
                        :series="totalSalesSeries"
                    />
                </b-col>
                <!-- <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                    <b-card-title class="total_sales_content mt-2">
                        ￥{{ totalSalesStr }}
                    </b-card-title>
                    <b-card-sub-title>
                        sales
                    </b-card-sub-title>
                </b-col> -->
            </b-row>
        </div>
    </b-container>
</template>

<script>
    import dayjs from 'dayjs'
    import isBetween from 'dayjs/plugin/isBetween';
    import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
    import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
    dayjs.extend(isSameOrAfter)
    dayjs.extend(isSameOrBefore)
    dayjs.extend(isBetween)
    const now = dayjs().format('YYYY-MM-DD')

    export default {
        name: 'TotalByCustomerSalesAnalyticsItem',
        components: {
        },
        props: {
            rank: {
                type: Number,
                require: false,
                default: 1,
            },
            totalSalesData: {
                type: Number,
                require: false,
                default: null,
            }
        },
        data: () => ({
            totalSalesChartOptions: {
                chart: {
                    foreColor: '#fff',
                    height: 50,
                    type: 'bar',
                    stacked: true,
                    sparkline: {
                        enabled: true
                    }
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                        barHeight: '10%',
                        colors: {
                            backgroundBarColors: ['#40475D']
                        }
                    },
                },
                stroke: {
                    width: 0,
                },
                // title: {
                //     floating: true,
                //     offsetX: -10,
                //     offsetY: 5,
                //     text: '現在の売上'
                // },
                // subtitle: {
                //     floating: true,
                //     align: 'right',
                //     offsetY: 0,
                //     text: '44%',
                //     style: {
                //         fontSize: '20px',
                //     },
                // },
                tooltip: {
                    enabled: false
                },
                xaxis: {
                    categories: ['Process 1'],
                },
                yaxis: {
                    max: 100
                },
                fill: {
                    opacity: 1
                },
            },
            totalSales: 0,
            totalSalesStr: '0',
            loading: false,
            totalSalesSeries: [
                {
                    name: 'Next Rank',
                    data: [0]
                }
            ],
            rankSales: {
                1: 0,
                2: 3000000,
                3: 7000000,
                4: 10000000,
                5: 0,
            }
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
            let nextRank = this.rank + 1
            if (this.rank == 4) {
                this.totalSalesSeries[0].data = [0]
            } else {
                let res = this.totalSalesData / this.rankSales[nextRank] * 100
                this.totalSalesSeries[0].data = [res]
            }
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
            needForNextRank () {
                let nextRank = this.rank + 1
                if (this.rank == 4) {
                    return 0
                }
                return this.rankSales[nextRank] - this.totalSalesData
            },
        },
        methods: {
            // setTotalSalesData (item) {
            //     if (item.data.total_price == null) {
            //         this.totalSales = 0
            //         this.totalSalesStr = 0
            //     } else {
            //         this.totalSales = item.data.total_price / 10000
            //         this.totalSalesStr = item.data.total_price.toLocaleString()
            //     }
            //     this.loading = false
            // }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
