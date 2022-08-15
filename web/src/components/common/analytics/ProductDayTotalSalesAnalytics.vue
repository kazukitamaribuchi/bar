<template>
    <div id="product_day_sales_analytics">
        <!-- <b-card class="customer_day_sales_analytics_area"> -->
            <b-skeleton-img
                v-if="loading"
                height="380px"
            ></b-skeleton-img>
            <div v-else>
                <b-card-text class="mb-1 mt-1">
                    商品別売上総計
                </b-card-text>
                <VueApexCharts
                    :height=height
                    type="bar"
                    :options="productDayTotalSalesChartOptions"
                    :series="productDayTotalSalesSeries"
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
        name: 'ProductDayTotalSalesAnalyticsItem',
        components: {
        },
        props: {
            height: {
                type: Number,
                required: false,
                default: 300,
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
            productDayTotalSalesChartOptions: {
                chart: {
                  type: 'bar',
                  height: 350,
                  // stacked: true,
                  // zoom: {
                  //   enabled: true
                  // }
                  toolbar: {
                      show: false,
                  },
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
                        columnWidth: '55%',
                        // endingShape: 'rounded',
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
                yaxis: [
                    {
                        seriesName: '総計',
                        // opposite: true,
                        axisTicks: {
                            show: true,
                        },
                        axisBorder: {
                            show: true,
                            color: '#008FFB'
                        },
                        labels: {
                            style: {
                                fontSize: '12px',
                                colors: ["#ffffff"]
                            }
                        },
                        title: {
                            text: "総計",
                            style: {
                                color: '#008FFB',
                            }
                        },
                    },
                    {
                        seriesName: '売上数',
                        opposite: true,
                        axisTicks: {
                            show: true,
                        },
                        axisBorder: {
                            show: true,
                            color: '#00E396'
                        },
                        labels: {
                            style: {
                                fontSize: '12px',
                                colors: ["#ffffff"]
                            }
                        },
                        title: {
                            text: "売上数",
                            style: {
                                color: '#00E396',
                            }
                        },
                    },
                ],
                dataLabels: {
                    enabled: true,
                    formatter: function (a, b) {
                        if (b.seriesIndex == 0) {
                            return a.toLocaleString() + "円"
                        } else if (b.seriesIndex == 1) {
                            return a.toLocaleString()
                        }
                    },
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#ffffff"]
                    }
                },
                legend: {
                    position: 'right',
                    // offsetX: 0,
                    // offsetY: 100,
                    // horizontalAlign: 'left',
                    // offsetX: 40
                    labels: {
                        colors: ['#ffffff', '#ffffff']
                    }
                },
                fill: {
                    opacity: 0.9
                },
                tooltip: {
                    theme: 'dark',
                    followCursor: true
                    // fillSeriesColor: true,
                    // fixed: {
                    //     enabled: true,
                    //     position: 'topLeft', // topRight, topLeft, bottomRight, bottomLeft
                    //     offsetY: 30,
                    //     offsetX: 60
                    // },
                },
                stroke: {
                    show: true,
                    width: 2,
                    colors: ['transparent']
                },
                // colors: ['#546E7A']
            },
            productDayTotalSalesSeries: [
                {
                    name: '総計',
                    data: [44, 55, 41, 67, 22, 43]
                },
                {
                    name: '売上数',
                    data: [2, 5, 3, 1, 1, 9]
                }
            ],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_product_day_sales_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range
                }
            })
            .then(res => {
                console.log(res)
                this.setProductDayTotalSalesData(res.data)
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
            setProductDayTotalSalesData (item) {
                const data = item.data
                let total_sales_price_series = []
                let total_sales_cnt_series = []
                let categories = []
                let colors = []
                for (const i in data) {
                    total_sales_price_series.push(data[i].total)
                    total_sales_cnt_series.push(data[i].total_cnt)
                    categories.push(data[i].sales_detail.name)
                    colors.push('#ffffff')
                }
                this.productDayTotalSalesSeries[0].data = total_sales_price_series
                this.productDayTotalSalesSeries[1].data = total_sales_cnt_series
                this.productDayTotalSalesChartOptions.xaxis.categories = categories
                this.productDayTotalSalesChartOptions.xaxis.labels.style.colors = colors
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
