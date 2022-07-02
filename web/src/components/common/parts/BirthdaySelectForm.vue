<template>
    <span class="basic_select_wrap">
        <b-form-select
            v-model="localSelectedYear"
            :options=birthdayYearList
            value-field="value"
            text-field="text"
            class="basic_select"
        >
            <template #first>
                <b-form-select-option :value="null" disabled>年</b-form-select-option>
            </template>
        </b-form-select>
        <b-form-select
            v-model="localSelectedMonth"
            :options=birthdayMonthList
            value-field="value"
            text-field="text"
            class="basic_select"
        >
            <template #first>
                <b-form-select-option :value="null" disabled>月</b-form-select-option>
            </template>
        </b-form-select>
        <b-form-select
            v-model="localSelectedDay"
            :options=birthdayYearMonthDay
            value-field="value"
            text-field="text"
            class="basic_select"
        >
            <template #first>
                <b-form-select-option :value="null" disabled>日</b-form-select-option>
            </template>
        </b-form-select>
    </span>
</template>

<script>
import { Const } from '@/assets/js/const'
import _ from 'lodash'
const Con = new Const()
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)


export default {
    name: 'BirthdaySelectFormItem',
    props: {
        year: {
            type: Number,
            required: false,
            default: 0,
        },
        month: {
            type: Number,
            required: false,
            default: 0,
        },
        day: {
            type: Number,
            required: false,
            default: 0,
        },
    },
    created () {
    },
    data: () => ({
        birthdayMonthList: Con.MONTH,
    }),
    computed: {
        birthdayYearList () {
            let result = []
            const now = dayjs().year()
            let bottom = now - Con.BIRTHDAY_BOTTOM_LIMIT
            let top = now - Con.BIRTHDAY_TOP_LIMIT
            for (var i = bottom; i <= top; i++) {
                result.push({ 'value': i, text: i })
            }
            return result
        },
        birthdayYearMonthDay () {
            console.log(this.year, this.month)
            if (this.year != 0 && this.month != 0) {
                let day = Con.DAY
                if (this.year != null || this.month != null) {
                    console.log(this.year, this.month)
                    console.log(dayjs(this.year + '-' + this.month).endOf('month').format('DD') + 'まで')
                    day.length = dayjs(this.year + '-' + this.month).endOf('month').format('DD')
                    return day
                }
            }
            return Con.DAY
        },
        localSelectedYear: {
            get: function () {
                return this.year
            },
            set: function (value) {
                this.$emit('input', value)
            },
        },
        localSelectedMonth: {
            get: function () {
                return this.month
            },
            set: function (value) {
                this.$emit('input', value)
            },
        },
        localSelectedDay: {
            get: function () {
                return this.day
            },
            set: function (value) {
                this.$emit('input', value)
            },
        },
    },
    watch: {
    }
}

</script>
<style lang="scss" scoped>
    .small {
        width: 20px;
    }

    .basic_select_wrap {
        .basic_select {
            border-radius: 3px;
            border: 1px solid rgba(125, 125, 125, 0.6);
            padding: 3px 20px 3px 7px;
            font-size: 16px;
            font-weight: 200;
        }
    }

    .basic_select_wrap::after {
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 4.5px solid rgba(50, 50, 50, 1);
        content: "";
        position: relative;
        right: 12px;
        top: 13px;
        width: 0;
    }

</style>
