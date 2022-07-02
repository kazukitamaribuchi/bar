<template>
    <div>
        <b-skeleton-img
            v-if="loading"
            height="290px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1">
                指名比率
            </b-card-text>
            <VueApexCharts
                style="position: relative; top: 50px;"
                :width="width"
                type="pie"
                :options="appointChartOptions"
                :series="appointRatioSeries"
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
        name: 'AppointRatioAnalyticsItem',
        components: {
        },
        props: {
            width: {
                type: Number,
                required: false,
                default: 280,
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
            appointChartOptions: {
                chart: {
                  type: 'pie',
                },
                labels: ['フリー', '指名'],
                // ↓これ意味あるのか？
                // responsive: [{
                //   breakpoint: 480,
                //   options: {
                //     chart: {
                //       width: 200
                //     },
                //     legend: {
                //       position: 'bottom'
                //     }
                //   }
                // }]
            },
            ratio: [50, 50],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_appoint_ratio_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range,
                }
            })
            .then(res => {
                this.setAppointRatioData(res.data)
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
            appointRatioSeries () {
                return this.ratio
            }
        },
        methods: {
            setAppointRatioData (item) {
                if (item.data.length == 0) {
                    this.ratio = [100, 0]
                } else if (item.data.length == 1) {
                    if (!item.data[0].appoint) {
                        this.ratio = [item.data[0].total, 0]
                    } else {
                        this.ratio = [0, item.data[0].total]
                    }
                } else {
                    if (!item.data[0].appoint) {
                        this.ratio = [item.data[0].total, item.data[1].total]
                    } else {
                        this.ratio = [item.data[1].total, item.data[0].total]
                    }
                }
                this.loading = false
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
