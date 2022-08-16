<template>
    <div id="customer_day_stay_hour_analytics">
        <b-skeleton-img
            v-if="loading"
            height="290px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1">
                顧客別滞在時間
            </b-card-text>
            <VueApexCharts
                :height=height
                type="rangeBar"
                :options="customerDayStayHourChartOptions"
                :series="customerDayStayHourSeries"
            />
        </div>
    </div>
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
        name: 'CustomerDayStayHourAnalyticsItem',
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
            }
        },
        data: () => ({
            customerDayStayHourChartOptions: {
                chart: {
                    type: 'rangeBar',
                    toolbar: {
                        show: false,
                    },
                    zoom: {
                        enabled: false,
                    }
                },
                plotOptions: {
                    bar: {
                        horizontal: true
                    }
                },
                grid: {
                    // xaxis: {
                    //     lines: {
                    //         show: true
                    //     }
                    // },
                },
                xaxis: {
                    type: 'datetime',
                    position: 'top',
                    labels: {
                        datetimeUTC: false,
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        }
                    },
                    axisBorder: {
                        show: false
                    },
                    // title: {
                    //     text: '滞在時間'
                    // },
                },
                yaxis: {
                    labels: {
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        }
                    }
                },
                tooltip: {
                    theme: 'dark',
                    // fillSeriesColor: true,
                    // カーソルに合わせて動く
                    // followCursor: true,
                    // intersect: true,
                    inverseOrder: true,
                    x: {
                        show: true,
                        format: 'dd MMM',
                        formatter: function (val) {
                            return dayjs(val).format('YYYY年MM月DD日 HH時mm分')
                        },
                    },
                    y: {
                        title: {
                            formatter: function (a, b) {
                                if (b.w == undefined) {
                                    return
                                }
                                if (b.w.globals == undefined) {
                                    return
                                }
                                if (b.w.globals.seriesX == undefined) {
                                    return
                                }
                                if (b.w.globals.seriesX.length == 0) {
                                    return
                                }
                                return b.w.globals.seriesX[0][b.dataPointIndex]
                            },
                        },
                        formatter: function (val) {
                            return ''
                        },
                    },
                }
            },
            customerDayStayHourSeries: [
                {
                    data: []
                }
            ],
            loading: true,
            categories: [],
        }),
        beforeCreate () {
        },
        created () {
            // this.$axios({
            //     method: 'GET',
            //     url: '/api/sales/get_customer_day_stay_hour_analytics/',
            //     params: {
            //         target_date: this.targetDate,
            //     }
            // })
            // .then(res => {
            //     this.setCustomerDayStayHourData(res.data)
            // })
            // .catch(e => {
            //     console.log(e)
            // })
        },
        beforeMount () {
            // console.log('before mount')
        },
        mounted () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_customer_day_stay_hour_analytics/',
                params: {
                    target_date: this.targetDate,
                }
            })
            .then(res => {
                // console.log('get_customer_day_stay_hour_analytics', res)
                this.setCustomerDayStayHourData(res.data)
            })
            .catch(e => {
                console.log(e)
            })
            // console.log('mount')
        },
        beforeUpdate () {
            // console.log('before update')
        },
        update () {
            // console.log('update')
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
            setCustomerDayStayHourData (item) {
                const colors = [
                    '#008FFB',
                    '#3399FF',
                    '#008FFB',
                    '#3399FF',
                ]
                let c = 0
                const data = item.data
                let categories = []
                let series = []
                for (const i in data) {
                    categories.push(data[i].customer.name)
                    let visitTime = dayjs(data[i].visit_time).valueOf()
                    let leaveTime = dayjs(data[i].leave_time).valueOf()
                    if (visitTime == leaveTime) {
                        leaveTime += 60000
                    }
                    series.push({
                        x: data[i].customer.name,
                        y: [
                            visitTime,
                            leaveTime,
                        ],
                        fillColor: colors[c]
                    })
                    if (c < 3) {
                        c++
                    } else {
                        c = 0
                    }
                }
                this.categories = categories
                this.customerDayStayHourSeries[0].data = series
                this.loading = false
                // console.log('this.customerDayStayHourSeries', this.customerDayStayHourSeries)
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #customer_day_stay_hour_analytics {
        max-height: 100%;
    //     .customer_day_sales_analytics_area {
    //         max-height: 100%;
    //         background-color: $theme-color;
    //         color: white;
    //     }
    }

</style>
