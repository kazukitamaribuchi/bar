<template>
    <div id="auto-input-leave-time-wrap">
        <b-form-group>
            <b-card-sub-title
                style="display: inline-block;"
            >退店時間自動入力</b-card-sub-title>
            <span
                style="display: inline-block; margin-left: 0.4rem;"
            >
                <b-icon
                    id="auto-input-leave-time-info-icon"
                    icon="info-circle"
                    variant="primary"
                ></b-icon>
            </span>
            <b-tooltip
                target="auto-input-leave-time-info-icon"
                title="退店時間を入店時間から指定時間後に設定します。入店時間の入力が必須です。"
            ></b-tooltip>
            <b-button-group
                style="display: block;"
            >
                <b-button
                    v-for="(item, i) in btnType"
                    :key="i"
                    variant="outline-primary"
                    @click="inputLeaveTime(item.value)"
                >{{ item.text }}</b-button>
            </b-button-group>
        </b-form-group>
    </div>
</template>
<script>
    import dayjs from 'dayjs'

    export default {
        name: 'AutoInputLeaveTimeItem',
        components: {
        },
        props: {
            inputSalesData: {
                type: Object,
                required: true,
            },
            visitTime: {
                type: String,
                required: false,
                default: null,
            },
        },
        data: () => ({
            btnType: [
                { text: '1h', value: 1 },
                { text: '2h', value: 2 },
                { text: '3h', value: 3 },
                { text: '4h', value: 4 },
                { text: '5h', value: 5 },
            ]
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
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
        },
        methods: {
            inputLeaveTime (value) {
                if (this.visitTime != null) {
                    let leaveTime = dayjs(this.visitTime).add(value, 'hour')
                    const leaveTime1 = leaveTime.format('YYYY-MM-DD')
                    const leaveTime2 = leaveTime.format('HH:mm')
                    this.$emit('update', {...this.inputSalesData, leaveTime1: leaveTime1, leaveTime2: leaveTime2})
                }
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
