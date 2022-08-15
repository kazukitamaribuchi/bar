<template>
    <div id="day_sales_analytics">
        <!-- <b-card class="customer_day_sales_analytics_area"> -->
            <b-skeleton-img
                v-if="loading"
                height="380px"
            ></b-skeleton-img>
            <div v-else>
                <b-card-text class="mb-1 mt-1">
                    売上遷移
                </b-card-text>
                <VueApexCharts
                    :height=height
                    type="area"
                    :options="daySalesChartOptions"
                    :series="daySalesSeries"
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
        name: 'DaySalesAnalyticsItem',
        components: {
        },
        props: {
            height: {
                type: Number,
                required: false,
                default: 330,
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
            daySalesChartOptions: {
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
                  type: 'area',
                  height: 350,
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
                        text: "売上",
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
                labels: [
                    "13 Nov 2017",
                    "14 Nov 2017",
                    "15 Nov 2017",
                    "16 Nov 2017",
                    "17 Nov 2017",
                    "20 Nov 2017",
                    "21 Nov 2017",
                    "22 Nov 2017",
                    "23 Nov 2017",
                    "24 Nov 2017",
                    "27 Nov 2017",
                    "28 Nov 2017",
                    "29 Nov 2017",
                    "30 Nov 2017",
                    "01 Dec 2017",
                    "04 Dec 2017",
                    "05 Dec 2017",
                    "06 Dec 2017",
                    "07 Dec 2017",
                    "08 Dec 2017"
                ],
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
                tooltip: {
                    theme: 'dark',
                    followCursor: true
                    // fillSeriesColor: true,
                },
                // colors: ['#546E7A']
            },
            daySalesSeries: [
                {
                    name: '売上',
                    data:  [
                        8107.85,
                        8128.0,
                        8122.9,
                        8165.5,
                        8340.7,
                        8423.7,
                        8423.5,
                        8514.3,
                        8481.85,
                        8487.7,
                        8506.9,
                        8626.2,
                        8668.95,
                        8602.3,
                        8607.55,
                        8512.9,
                        8496.25,
                        8600.65,
                        8881.1,
                        9340.85
                    ],
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            // this.$axios({
            //     method: 'GET',
            //     url: '/api/sales/get_day_sales_analytics/',
            //     params: {
            //         target_date: this.targetDate,
            //         range: this.range,
            //     }
            // })
            // .then(res => {
            //     this.setDaySalesData(res.data)
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
                url: '/api/sales/get_day_sales_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range,
                }
            })
            .then(res => {
                this.setDaySalesData(res.data)
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
            setDaySalesData (item) {
                const data = item.data
                let series = []
                let labels = []
                let colors = []
                for (const i in data) {
                    labels.push(data[i].date)
                    series.push(data[i].total)
                    colors.push('#ffffff')
                }
                this.daySalesSeries[0].data = series
                this.daySalesChartOptions.labels = labels
                this.daySalesChartOptions.xaxis.labels.style.colors = colors
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    #customer_day_sales_analytics {
        max-height: 100%;
    //     .customer_day_sales_analytics_area {
    //         max-height: 100%;
    //         background-color: $theme-color;
    //         color: white;
    //     }
    }

</style>
