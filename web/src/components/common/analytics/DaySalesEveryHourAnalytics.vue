<template>
    <div id="day_sales_every_hour_analytics">
        <!-- <b-card class="customer_day_sales_analytics_area"> -->
            <b-skeleton-img
                v-if="loading"
                height="290px"
            ></b-skeleton-img>
            <div v-else>
                <b-card-text class="mb-1 mt-1">
                    時間別売上
                </b-card-text>
                <VueApexCharts
                    :height=height
                    type="line"
                    :options="daySalesEveryHourChartOptions"
                    :series="daySalesEveryHourSeries"
                />
            </div>
        <!-- </b-card> -->
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
        name: 'DaySalesEveryHourAnalyticsItem',
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
            }
        },
        data: () => ({
            daySalesEveryHourChartOptions: {
                // title: {
                //     text: '顧客別売上',
                //     align: 'left',
                //     style: {
                //         fontSize:  '14px',
                //         fontWeight:  'bold',
                //         fontFamily:  undefined,
                //         color:  '#ffffff'
                //     },
                // },
                chart: {
                  type: 'line',
                  height: 270,
                  // toolbar: {
                  //     show: false,
                  // },
                  // zoom: {
                  //   enabled: false
                  // }
                },
                // responsive: [{
                //   breakpoint: 480,
                //   options: {
                //     legend: {
                //       position: 'bottom',
                //       offsetX: -10,
                //       offsetY: 0
                //     }
                //   }
                // }],
                // plotOptions: {
                //     bar: {
                //         horizontal: false,
                //         borderRadius: 10,
                //         dataLabels: {
                //             position: 'bottom', // top, center, bottom
                //         },
                //     },
                // },
                xaxis: {
                    type: 'category',
                    // position: 'top',
                    // axisBorder: {
                    //     show: false
                    // },
                    // axisTicks: {
                    //     show: false
                    // },
                    // crosshairs: {
                    //     fill: {
                    //         type: 'gradient',
                    //         gradient: {
                    //             colorFrom: '#D8E3F0',
                    //             colorTo: '#BED1E6',
                    //             stops: [0, 100],
                    //             opacityFrom: 0.4,
                    //             opacityTo: 0.5,
                    //         }
                    //     }
                    // },
                    // tooltip: {
                    //     enabled: true,
                    // },
                    // labels: {
                    //     style: {
                    //         fontSize: '12px',
                    //         colors: ["#ffffff"]
                    //     },
                    //     datetimeFormatter: {
                    //         year: 'yyyy年',
                    //         month: "M月",
                    //         day: 'M月dd日',
                    //         hour: 'HH:mm',
                    //     },
                    //     datetimeUTC: false,
                    // }
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
                // dataLabels: {
                //     enabled: true,
                //     enabledOnSeries: [1]
                //     // enabled: false,
                //     // formatter: function (val) {
                //     //     return val.toLocaleString() + "円";
                //     // },
                //     // offsetY: -20,
                //     // style: {
                //     //     fontSize: '12px',
                //     //     colors: ["#ffffff"]
                //     // }
                // },
                stroke: {
                    curve: 'straight',
                    // width: [0, 5]
                },
                labels: [
                    '00:00 ~ 00:59',
                    '01:00 ~ 01:59',
                    '02:00 ~ 02:59',
                    '03:00 ~ 03:59',
                    '04:00 ~ 04:59',
                    '05:00 ~ 05:59',
                    '06:00 ~ 06:59',
                    '07:00 ~ 07:59',
                    '08:00 ~ 08:59',
                    '09:00 ~ 09:59',
                    '10:00 ~ 10:59',
                    '11:00 ~ 11:59',
                    '12:00 ~ 12:59',
                    '13:00 ~ 13:59',
                    '14:00 ~ 14:59',
                    '15:00 ~ 15:59',
                    '16:00 ~ 16:59',
                    '17:00 ~ 17:59',
                    '18:00 ~ 18:59',
                    '19:00 ~ 19:59',
                    '20:00 ~ 20:59',
                    '21:00 ~ 21:59',
                    '22:00 ~ 22:59',
                    '23:00 ~ 23:59',
                ],

                legend: {
                    position: 'right',
                    offsetX: 0,
                    offsetY: 50
                },
                fill: {
                    opacity: 0.9
                },
                // fill: {
                //     type: 'gradient',
                //     gradient: {
                //         shade: 'dark',
                //         gradientToColors: [ '#FDD835'],
                //         shadeIntensity: 1,
                //         type: 'horizontal',
                //         opacityFrom: 1,
                //         opacityTo: 1,
                //         stops: [0, 100, 100, 100]
                //     },
                // },
                tooltip: {
                    theme: 'dark',
                    followCursor: true
                    // fillSeriesColor: true,
                },
                // colors: ['#546E7A']
            },
            daySalesEveryHourSeries: [
                {
                    name: '売上',
                    type: 'column',
                    data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
                },
                {
                    name: '来店数',
                    type: 'line',
                    data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            // console.log('★get_sales_by_every_time_analytics')
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_sales_by_every_time_analytics/',
                params: {
                    target_date: this.targetDate,
                    // target_date: '2022-08-14',
                }
            })
            .then(res => {
                // console.log('res',res)
                this.setDaySalesEveryHourData(res.data)
            })
            .catch(e => {
                console.log(e)
            })
        },
        beforeMount () {
            // console.log('before mount')
        },
        mounted () {
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
            setDaySalesEveryHourData (item) {
                // console.log('setDaySalesEveryHourData', item)
                let cnt = 0
                const data = item
                let sales = []
                let visit = []
                let colors = []
                for (const i in data) {
                    // console.log('data[i]', data[i][cnt])
                    sales.push(data[i][cnt].total)
                    visit.push(data[i][cnt].total_visit)
                    colors.push('#ffffff')
                    cnt++
                    // if (cnt >= 8) break
                }
                // console.log('sales', sales)
                // console.log('visit', visit)
                // console.log('this.daySalesEveryHourSeries', this.daySalesEveryHourSeries)
                this.daySalesEveryHourSeries[0].data = sales
                this.daySalesEveryHourSeries[1].data = visit
                // this.daySalesEveryHourChartOptions.labels = labels
                // this.daySalesEveryHourChartOptions.xaxis.labels.style.colors = colors
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #day_sales_every_hour_analytics {
        max-height: 100%;
    //     .customer_day_sales_analytics_area {
    //         max-height: 100%;
    //         background-color: $theme-color;
    //         color: white;
    //     }
    }

</style>
