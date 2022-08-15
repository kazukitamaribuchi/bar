<template>
    <b-container fluid>
        <b-skeleton-img
            v-if="loading"
            style="position: relative; top: -6px;"
            height="180px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1">
                総売上
            </b-card-text>
            <b-row>
                <b-col cols="6" class="mt-0 pt-0">
                    <VueApexCharts
                        :width=width
                        :height=height
                        type="radialBar"
                        :options="totalSalesChartOptions"
                        :series="totalSalesSeries"
                    />
                </b-col>
                <b-col cols="6" align="right" class="pt-4 ml-0 pl-0">
                    <b-card-title class="total_sales_content mt-2">
                        ￥{{ totalSalesStr }}
                    </b-card-title>
                    <b-card-sub-title>
                        sales
                    </b-card-sub-title>
                </b-col>
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
        name: 'TotalSalesAnalyticsItem',
        components: {
        },
        props: {
            width: {
                type: Number,
                required: false,
                default: 165,
            },
            height: {
                type: Number,
                required: false,
                default: 165,
            },
            targetDate: {
                type: String,
                require: false,
                default: now,
            },
            range: {
                type: Number,
                require: false,
                default: 1,
            }
        },
        data: () => ({
            totalSalesChartOptions: {
                chart: {
                  height: 350,
                  type: 'radialBar',
                  toolbar: {
                    show: false
                  }
                },
                plotOptions: {
                  radialBar: {
                    startAngle: -135,
                    endAngle: 225,
                     hollow: {
                      margin: 0,
                      size: '80%',
                      background: '#fff',
                      image: undefined,
                      imageOffsetX: 0,
                      imageOffsetY: 0,
                      position: 'front',
                      dropShadow: {
                        enabled: true,
                        top: 3,
                        left: 0,
                        blur: 4,
                        opacity: 0.24
                      }
                    },
                    track: {
                      background: '#fff',
                      strokeWidth: '67%',
                      margin: 0, // margin is in pixels
                      dropShadow: {
                        enabled: true,
                        top: -3,
                        left: 0,
                        blur: 4,
                        opacity: 0.35
                      }
                    },

                    dataLabels: {
                      show: true,
                      name: {
                        offsetY: -10,
                        show: true,
                        color: '#888',
                        fontSize: '17px'
                      },
                      value: {
                        formatter: function(val) {
                          return parseInt(val);
                        },
                        color: '#111',
                        fontSize: '20px',
                        show: true,
                      }
                    }
                  }
                },
                fill: {
                  type: 'gradient',
                  gradient: {
                    shade: 'dark',
                    type: 'horizontal',
                    shadeIntensity: 0.5,
                    gradientToColors: ['#ABE5A1'],
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 100]
                  }
                },
                stroke: {
                  lineCap: 'round'
                },
                labels: ['total (万)'],
            },
            totalSales: 0,
            totalSalesStr: '0',
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            // console.log('target_date', this.targetDate)
            // console.log('range', this.range)

            // this.$axios({
            //     method: 'GET',
            //     url: '/api/sales/get_total_sales_analytics/',
            //     params: {
            //         target_date: this.targetDate,
            //         range: this.range,
            //     }
            // })
            // .then(res => {
            //     this.setTotalSalesData(res.data)
            //     console.log('setTotalSalesData', res)
            // })
            // .catch(e => {
            //     console.log(e)
            // })
        },
        beforeMount () {
            // console.log('before mount')
        },
        mounted () {
            // console.log('mount')
            // console.log('targetDate', this.targetDate)
            // console.log('range', this.range)
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_total_sales_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range,
                }
            })
            .then(res => {
                this.setTotalSalesData(res.data)
                // console.log('setTotalSalesData', res)
            })
            .catch(e => {
                console.log(e)
            })
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
            totalSalesSeries () {
                return [this.totalSales]
            }
        },
        methods: {
            setTotalSalesData (item) {
                if (item.data.total_price == null) {
                    this.totalSales = 0
                    this.totalSalesStr = 0
                } else {
                    this.totalSales = item.data.total_price / 10000
                    this.totalSalesStr = item.data.total_price.toLocaleString()
                }
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
