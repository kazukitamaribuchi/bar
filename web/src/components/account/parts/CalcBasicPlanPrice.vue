<template>
    <div>
        <div style="font-size: 14px;" class="mt-2">
            基本料金
        </div>

        <v-row
            v-for="n of 2"
            :key=n
            class="mt-3"
        >
            <v-col cols="1"></v-col>
            <v-col cols="6" class="text-right py-0">
                <v-text-field
                    v-model="$data['basicPlanNormalPrice' + n]"
                    :label=basicPlanLabel(n)
                    class="right-input mt-0 pt-0 mr-1"
                    @change="updateBasicPlanPrice"
                    :disabled="mode"
                ></v-text-field>
            </v-col>
            <v-col cols="5" class="text-right py-0">
                <b-form-spinbutton
                    v-model="$data['basicPlanNormalNum' + n]"
                    inline
                    size="sm"
                    min="0"
                    @change="updateBasicPlanPrice"
                    :disabled="mode"
                ></b-form-spinbutton>
            </v-col>
        </v-row>

        <div style="font-size: 14px;" class="mt-2">
            延長料金
        </div>

        <v-row
            v-for="n of 2"
            :key=n
            class="mt-3"
        >
            <v-col cols="1"></v-col>
            <v-col cols="6" class="text-right py-0">
                <v-text-field
                    v-model="$data['basicPlanExtentionPrice' + n]"
                    :label=basicPlanLabel(n)
                    class="right-input mt-0 pt-0 mr-1"
                    @change="updateBasicPlanPrice"
                    :disabled="mode"
                ></v-text-field>
            </v-col>
            <v-col cols="5" class="text-right py-0">
                <b-form-spinbutton
                    v-model="$data['basicPlanExtentionNum' + n]"
                    inline
                    size="sm"
                    min="0"
                    @change="updateBasicPlanPrice"
                    :disabled="mode"
                ></b-form-spinbutton>
            </v-col>
        </v-row>
    </div>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters } from 'vuex'

export default {
    name: 'CalcBasicPlanPriceItem',
    props: {
        salesData: {
            type: Object,
            required: true,
        },
        mode: {
            type: Boolean,
            required: true,
        },
        leaveTime: {
            type: String,
            required: true,
        }
    },
    data: () => ({
        basicPlanNormalPrice1: 0,
        basicPlanNormalNum1: 0,
        basicPlanNormalPrice2: 0,
        basicPlanNormalNum2: 0,
        basicPlanExtentionPrice1: 0,
        basicPlanExtentionNum1: 0,
        basicPlanExtentionPrice2: 0,
        basicPlanExtentionNum2: 0,
    }),
    computed: {
        ...mapGetters([
            'selectedProduct'
        ]),
    },
    created () {
        const BASIC_PLAN_PRICE = [
            [
                5000, 9000, 12000
            ],
            [
                10000, 18000, 24000
            ]
        ]
        const BASIC_PLAN_SEP_MINUTE = [
            60, 120, 180
        ]
        const EXTENTION_PRICE = [
            5000, 10000
        ]
        // const large = this.salesData.basic_plan_type.large_category
        const middle = this.salesData.basic_plan_type.middle_category
        const small = this.salesData.basic_plan_type.small_category
        let basicPlanNormalNum1 = this.salesData.male_visitors
        let basicPlanNormalNum2 = 0
        let isCharted = middle == 1
        const maleVisitors = this.salesData.male_visitors
        const femaleVisitors = this.salesData.female_visitors
        if (this.salesData.basic_plan_type.middle_category == 1) {
            basicPlanNormalNum1 += femaleVisitors
        } else {
            basicPlanNormalNum2 = femaleVisitors
        }
        const basicPlanNormalPrice1 = BASIC_PLAN_PRICE[middle][small]
        this.basicPlanNormalPrice1 = basicPlanNormalPrice1
        this.basicPlanNormalPrice2 = basicPlanNormalPrice1 / 2
        this.basicPlanNormalNum1 = basicPlanNormalNum1
        this.basicPlanNormalNum2 = basicPlanNormalNum2

        const basicPlanExtentionPrice1 = (isCharted) ? EXTENTION_PRICE[1] : EXTENTION_PRICE[0]
        this.basicPlanExtentionPrice1 = basicPlanExtentionPrice1
        this.basicPlanExtentionPrice2 = basicPlanExtentionPrice1 / 2

        // あと延長の数
        // 基本料金によって区切りが違う(最初ののみ。後は1時間区切り)
        const now = this.leaveTime
        const diff = now.diff(dayjs(this.salesData.visit_time), 'minute')

        const diffMinute = diff - BASIC_PLAN_SEP_MINUTE[small]
        console.log('diffMinute', diffMinute, BASIC_PLAN_SEP_MINUTE[small])
        let extentionNum = 0
        if (diffMinute > 0) {
            extentionNum = Math.ceil(diffMinute / 60)
        }

        // console.log('diff', diff)
        // console.log('diffMinute', diffMinute)
        // console.log('extentionNum', extentionNum)
        this.basicPlanExtentionNum1 = maleVisitors * extentionNum
        this.basicPlanExtentionNum2 = femaleVisitors * extentionNum

        const data = {
            basicPlanNormalPrice1: this.basicPlanNormalPrice1,
            basicPlanNormalNum1: this.basicPlanNormalNum1,
            basicPlanNormalPrice2: this.basicPlanNormalPrice2,
            basicPlanNormalNum2: this.basicPlanNormalNum2,
            basicPlanExtentionPrice1: this.basicPlanExtentionPrice1,
            basicPlanExtentionNum1: this.basicPlanExtentionNum1,
            basicPlanExtentionPrice2: this.basicPlanExtentionPrice2,
            basicPlanExtentionNum2: this.basicPlanExtentionNum2,
        }
        this.$emit('update', data)
    },
    methods: {
        basicPlanLabel (i) {
            if (i == 1) {
                return '一般料金'
            } else {
                return '女性割'
            }
        },
        updateBasicPlanPrice (item) {
            const data = {
                basicPlanNormalPrice1: this.basicPlanNormalPrice1,
                basicPlanNormalNum1: this.basicPlanNormalNum1,
                basicPlanNormalPrice2: this.basicPlanNormalPrice2,
                basicPlanNormalNum2: this.basicPlanNormalNum2,
                basicPlanExtentionPrice1: this.basicPlanExtentionPrice1,
                basicPlanExtentionNum1: this.basicPlanExtentionNum1,
                basicPlanExtentionPrice2: this.basicPlanExtentionPrice2,
                basicPlanExtentionNum2: this.basicPlanExtentionNum2,
            }
            this.$emit('update', data)
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
