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
            :key=n+100
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
import { Const } from '@/assets/js/const'
const Con = new Const()

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
        // 通常60 large=0, middle=0, small=0,
        // 通常120 large=0, middle=0, small=1,
        // 通常180 large=0, middle=0, small=2,
        // 貸切60 large=0, middle=1, small=0
        // 貸切180 large=0, middle=1, small=1
        // 貸切120 large=0, middle=1, small=2

        // 通常(0) or 貸切(1)
        const middle = this.salesData.basic_plan_type.middle_category

        // 1時間(0) or 2時間(1) or 3時間(2)
        const small = this.salesData.basic_plan_type.small_category

        let isDouhan = true
        let isCharted = middle == 1

        const maleVisitors = this.salesData.male_visitors
        const femaleVisitors = this.salesData.female_visitors
        if ((maleVisitors > 0 && femaleVisitors == 0) ||
            (maleVisitors == 0 && femaleVisitors > 0)) {
            isDouhan = false
        }

        // 男のみ☞全て通常
        // 女のみ☞全て通常
        // 同伴☞女は通常の場合、基本料金と延長が半額、貸切の場合全て通常

        let basicPlanNormalNum1 = 0
        let basicPlanNormalNum2 = 0

        if (isDouhan && !isCharted) {
            // 同伴で通常プランの場合 => 女性は半額

            // 基本料金の数量 = 男性客数分
            basicPlanNormalNum1 = maleVisitors

            // 基本料金(割引)の数量 = 女性客数分
            basicPlanNormalNum2 = femaleVisitors

        } else {
            // それ以外は割引無
            basicPlanNormalNum1 += (maleVisitors + femaleVisitors)
        }

        // 基本料金の値段をプランによって設定
        const basicPlanNormalPrice1 = Con.BASIC_PLAN_PRICE[middle][small]
        this.basicPlanNormalPrice1 = basicPlanNormalPrice1
        this.basicPlanNormalPrice2 = basicPlanNormalPrice1 / 2
        this.basicPlanNormalNum1 = basicPlanNormalNum1
        this.basicPlanNormalNum2 = basicPlanNormalNum2

        const basicPlanExtentionPrice1 = (isCharted) ? Con.EXTENTION_PRICE[1] : Con.EXTENTION_PRICE[0]
        this.basicPlanExtentionPrice1 = basicPlanExtentionPrice1
        this.basicPlanExtentionPrice2 = basicPlanExtentionPrice1 / 2

        // あと延長の数
        // 基本料金によって区切りが違う(最初ののみ。後は1時間区切り)
        // 退店時刻(画面開いた時間)を取得を取得
        const now = dayjs(this.leaveTime)
        // 来店時刻との差分を分で取得
        const diff = now.diff(dayjs(this.salesData.visit_time), 'minute')

        // 全体の分数から基本プランの分数引いた数を取得
        const diffMinute = diff - Con.BASIC_PLAN_SEP_MINUTE[small]

        // 延長の時間を切り上げで取得
        let extentionNum = 0
        if (diffMinute > 0) {
            extentionNum = Math.ceil(diffMinute / 60)
        }

        if (isDouhan && !isCharted) {
            this.basicPlanExtentionNum1 = maleVisitors * extentionNum
            this.basicPlanExtentionNum2 = femaleVisitors * extentionNum
        } else {
            this.basicPlanExtentionNum1 = (maleVisitors + femaleVisitors) * extentionNum
            this.basicPlanExtentionNum2 = 0
        }

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
                return '割引料金'
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
