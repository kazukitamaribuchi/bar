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
                  toolbar: {
                      show: false,
                  },
                  zoom: {
                    enabled: false
                  }
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
                    type: 'datetime',
                    // position: 'top',
                    axisBorder: {
                        show: false
                    },
                    axisTicks: {
                        show: false
                    },
                    crosshairs: {
                        fill: {
                            type: 'gradient',
                            gradient: {
                                colorFrom: '#D8E3F0',
                                colorTo: '#BED1E6',
                                stops: [0, 100],
                                opacityFrom: 0.4,
                                opacityTo: 0.5,
                            }
                        }
                    },
                    tooltip: {
                        enabled: true,
                    },
                    labels: {
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        },
                        datetimeFormatter: {
                            year: 'yyyy年',
                            month: "M月",
                            day: 'M月dd日',
                            hour: 'HH:mm',
                        },
                        datetimeUTC: false,
                    }
                },
                yaxis: {
                    labels: {
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        }
                    },
                    title: {
                        text: "来店数",
                        style: {
                            color: '#008FFB',
                        }
                    },
                },
                dataLabels: {
                    enabled: false,
                    formatter: function (val) {
                        return val.toLocaleString() + "円";
                    },
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#ffffff"]
                    }
                },
                stroke: {
                    curve: 'straight',
                },
                labels: ['01 Jan 2001', '02 Jan 2001', '03 Jan 2001', '04 Jan 2001', '05 Jan 2001', '06 Jan 2001', '07 Jan 2001', '08 Jan 2001', '09 Jan 2001', '10 Jan 2001', '11 Jan 2001', '12 Jan 2001'],
                
                // title: {
                //     text: 'Fundamental Analysis of Stocks',
                //     align: 'left'
                // },
                // subtitle: {
                //     text: 'Price Movements',
                //     align: 'left'
                // },

                // legend: {
                //     position: 'right',
                //     offsetX: 0,
                //     offsetY: 50
                // },
                // fill: {
                //     opacity: 0.9
                // },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shade: 'dark',
                        gradientToColors: [ '#FDD835'],
                        shadeIntensity: 1,
                        type: 'horizontal',
                        opacityFrom: 1,
                        opacityTo: 1,
                        stops: [0, 100, 100, 100]
                    },
                },
                tooltip: {
                    theme: 'dark',
                    followCursor: true
                    // fillSeriesColor: true,
                },
                // colors: ['#546E7A']
            },
            daySalesEveryHourSeries: [
                {
                    name: 'Blog',
                    type: 'column',
                    data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
                },
            {
                    name: '',
                    type: 'line',
                    data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_sales_by_every_time_analytics/',
                params: {
                    // target_date: this.targetDate,
                    target_date: '2022-08-14',
                }
            })
            .then(res => {
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
                const data = item.data
                let series = []
                let labels = []
                let colors = []
                for (const i in data) {
                    labels.push(data[i].date)
                    series.push(data[i].total)
                    colors.push('#ffffff')
                }
                this.daySalesEveryHourSeries[0].data = series
                this.daySalesEveryHourChartOptions.labels = labels
                this.daySalesEveryHourChartOptions.xaxis.labels.style.colors = colors
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
