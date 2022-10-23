<template>
    <span class="basic_select_wrap" :class="{'small': size === 'sm'}">
        <b-form-select
            v-model="localSelected"
            :options=options
            value-field="value"
            text-field="text"
            class="basic_select"
            :class="{'full_size': fullSize}"
            :disabled="formDisabled"
        >
            <template #first v-if="initValue != ''">
                <b-form-select-option :value="firstValue" :disabled="disabled">{{ initValue }}</b-form-select-option>
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
    name: 'SelectFormItem',
    props: {
        optionType: {
            type: Number,
            required: false,
            default: 0,
        },
        value: {
            type: Number,
            required: false,
            default: 0,
        },
        initVal: {
            type: String,
            required: false,
            default: '',
        },
        size: {
            type: String,
            required: false,
            default: 'md',
        },
        year: {
            type: Number,
            required: false,
            default: null,
        },
        month: {
            type: Number,
            required: false,
            default: null,
        },
        fullSize: {
            type: Boolean,
            required: false,
            default: false,
        },
        dispOptions: {
            type: Array,
            required: false,
            default: null,
        },
        disabled: {
            type: Boolean,
            required: false,
            default: true,
        },
        formDisabled: {
            type: Boolean,
            required: false,
            default: false,
        },
        firstValue: {
            type: Number,
            required: false,
            default: null,
        }
    },
    created () {
    },
    data: () => ({
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
            if (this.year != null && this.month != null) {
                let day = Con.DAY
                console.log(dayjs(this.year + '-' + this.month).endOf('month').format('DD') + 'まで')
                day.length = dayjs(this.year + '-' + this.month).endOf('month').format('DD')
                return day
            }
            return Con.DAY
        },
        options () {
            if (this.dispOptions != null) return this.dispOptions
            const OPT = [
                Con.OPTIONS_HOUR, // 0
                Con.OPTIONS_HOUR_ALL, // 1
                Con.OPTIONS_MINUTE, // 2
                Con.OPTIONS_TAX, // 3
                Con.OPTIONS_BASIC_SERVICE, // 4
                Con.OPTIONS_HOUR_OPEN_CLOSE, // 5
                Con.OPTIONS_MINUTE_HALF, // 6
                Con.OPTIONS_QUANTITIES, // 7
                Con.OPTIONS_ZERO_OR_ONE, // 8
                this.birthdayYearList, // 9(誕生年) 現在年月から100歳以下18歳以上をセレクト
                Con.MONTH, // 10
                this.birthdayYearMonthDay, // 11
                Con.OPTIONS_BASIC_PLAN_TYPE_LIST2, // 12
            ]
            if (this.optionType != 99) return OPT[this.optionType]

            return Con.OPTIONS_NUM
        },
        localSelected: {
            get: function () {
                return this.value
            },
            set: function (value) {
                this.$emit('input', value)
            },
        },
        initValue () {
            if (this.initVal != '') return this.initVal

            if (this.dispOptions != null) return ''
            const val = [
                '時',
                '時',
                '分',
                '',
                '',
                '時',
                '分',
                '',
                '',
                '年',
                '月',
                '日',
                '',
            ]

            if (this.optionType != 99) return val[this.optionType]

            return ''
        },
    }
}

</script>
<style lang="scss" scoped>
    .small {
        width: 20px;
    }

    .basic_select_wrap {
        .basic_select {
            background: white;
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

    .full_size {
        width: 95%;
    }

</style>
