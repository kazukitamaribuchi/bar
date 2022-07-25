<template>
    <p>
        {{ stayHour }}
    </p>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters } from 'vuex'

export default {
    name: 'CalcStayHourItem',
    props: {
        visitTime: {
            type: String,
            required: true,
            default: '',
        },
        leaveTime: {
            type: String,
            required: true,
        }
    },
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'selectedProduct'
        ]),
        stayHour () {
            console.log('this.visitTime', this.visitTime)
            console.log('this.leaveTime', this.leaveTime)
            const diff = dayjs(this.leaveTime).diff(dayjs(this.visitTime), 'minute')
            console.log('diff', diff)
            const hour = Math.floor(diff / 60)
            const min = diff - (hour * 60)
            // console.log(hour + '時間' + min + '分', diff)
            this.$emit('calcStayHour', diff)
            return hour + '時間' + min + '分'
        }
    },
    methods: {
    }
}

</script>

<style lang="scss" scoped>
</style>
