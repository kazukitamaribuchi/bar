<template>
    <div id="customer_day_total_sales_analytics">
        <!-- <b-card class="customer_day_sales_analytics_area"> -->
            <b-skeleton-img
                v-if="loading"
                height="290px"
            ></b-skeleton-img>
            <div v-else>
                <b-card-text class="mb-1 mt-1">
                    顧客別売上総計
                </b-card-text>
                <VueApexCharts
                    :height=height
                    type="bar"
                    :options="customerDayTotalSalesChartOptions"
                    :series="customerDayTotalSalesSeries"
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
        name: 'CustomerDayTotalSalesAnalyticsItem',
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
            customerDayTotalSalesChartOptions: {
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
                  type: 'bar',
                  stacked: true,
                  toolbar: {
                      show: false,
                  },
                  // zoom: {
                  //   enabled: true
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
                plotOptions: {
                    bar: {
                        horizontal: false,
                        borderRadius: 10,
                        dataLabels: {
                            position: 'bottom', // top, center, bottom
                        },
                    },
                },
                xaxis: {
                    categories: ['斎藤一', '斎藤一1', '斎藤一2', '斎藤一3', '斎藤一4', '斎藤一5'],
                    // title: {
                    //     text: '顧客名'
                    // },
                    position: 'top',
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
                    // tooltip: {
                    //     enabled: true,
                    // }
                    labels: {
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        }
                    }
                },
                yaxis: {
                    labels: {
                        style: {
                            fontSize: '12px',
                            colors: ["#ffffff"]
                        }
                    }
                },
                dataLabels: {
                    enabled: true,
                    formatter: function (val) {
                        return val.toLocaleString() + "円";
                    },
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#ffffff"]
                    }
                },
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
                    // fillSeriesColor: true,
                }
                // colors: ['#546E7A']
            },
            customerDayTotalSalesSeries: [
                {
                    name: '売上',
                    data: [44, 55, 41, 67, 22, 43]
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            // this.$axios({
            //     method: 'GET',
            //     url: '/api/sales/get_customer_day_sales_analytics/',
            //     params: {
            //         target_date: this.targetDate,
            //         range: this.range,
            //     }
            // })
            // .then(res => {
            //     this.setCustomerDayTotalSalesData(res.data)
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
                url: '/api/sales/get_customer_day_sales_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range,
                }
            })
            .then(res => {
                // console.log('res', res)
                this.setCustomerDayTotalSalesData(res.data)
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
            setCustomerDayTotalSalesData (item) {
                const data = item.data
                let series = []
                let categories = []
                let colors = []
                for (const i in data) {
                    series.push(data[i].total)
                    categories.push(data[i].customer.name)
                    colors.push('#ffffff')
                }
                this.customerDayTotalSalesSeries[0].data = series
                this.customerDayTotalSalesChartOptions.xaxis.categories = categories
                this.customerDayTotalSalesChartOptions.xaxis.labels.style.colors = colors
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
