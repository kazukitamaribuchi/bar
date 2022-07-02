<template>
    <div>
        <b-skeleton-img
            v-if="loading"
            height="290px"
        ></b-skeleton-img>
        <div v-else>
            <b-card-text class="mb-1">
                基本プラン比率
            </b-card-text>
            <VueApexCharts
                style="position: relative; top: 50px;"
                :width="width"
                type="pie"
                :options="basicPlanTypeChartOptions"
                :series="basicPlanTypeRatioSeries"
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
        name: 'BasicPlanTypeRatioAnalyticsItem',
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
            basicPlanTypeChartOptions: {
                chart: {
                  type: 'pie',
                },
                labels: ['Normal', 'VIP'],
            },
            ratio: [50, 50],
            loading: true,
        }),
        beforeCreate () {
        },
        created () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_basic_plan_type_ratio_analytics/',
                params: {
                    target_date: this.targetDate,
                    range: this.range,
                }
            })
            .then(res => {
                this.setBasicPlanTypeRatioData(res.data)
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
            basicPlanTypeRatioSeries () {
                return this.ratio
            }
        },
        methods: {
            setBasicPlanTypeRatioData (item) {
                if (item.data.length == 0) {
                    this.ratio = [100, 0]
                } else if (item.data.length == 1) {
                    if (item.data[0].basic_plan_type == 0) {
                        this.ratio = [item.data[0].total, 0]
                    } else {
                        this.ratio = [0, item.data[0].total]
                    }
                } else {
                    if (item.data[0].basic_plan_type == 0) {
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
