<template>
    <div>
        <i
            @click="undo"
            class='bx bx-undo undo-btn'
        ></i>
        <p class="text-center" style="font-size: 13px; height: 30px;">
            会員情報
        </p>

        <v-card
            flat
            class="pb-5"
        >
            <v-row
                style="padding: 0 3rem;"
            >
                <v-card-title>
                    会員No検索
                </v-card-title>
                <v-col cols="12">
                    <v-text-field
                        style="width: 80%; margin: 0 auto;"
                        label="会員No"
                        v-model="visitInfo.customerNo"
                        :rules="[rules.required, rules.small]"
                    ></v-text-field>
                </v-col>
                <v-btn
                    color="primary"
                    style="width: 75%; margin: 0 auto;"
                >
                    検索
                </v-btn>
            </v-row>
        </v-card>

        <v-divider class="mx-6 mt-8"/>

        <v-card
            flat
            class="pb-5"
        >
            <v-row
                style="padding: 0 3rem;"
            >
                <v-card-title>
                    顧客情報
                </v-card-title>
                <v-col cols="12">

                </v-col>
            </v-row>
        </v-card>

        <v-snackbar
            v-model="snackbar"
            timeout="2000"
        >
            {{ snackbarText }}
            <template v-slot:action="{ attrs }">
                <v-btn
                    color="pink"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >Close</v-btn>
            </template>
        </v-snackbar>

        <v-dialog
            v-model="dialog"
        >
            <v-card>
                <v-card-title>
                    入店データの作成に成功しました。
                </v-card-title>
                <v-card-actions>
                    <v-btn
                        color="green darken-1"
                        text
                        @click="toHome"
                    >
                        OK
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
<script>
    import dayjs from 'dayjs'
    import { mapGetters } from 'vuex'
    import HomeButton from '@/components/account/HomeButton'
    const nowD = dayjs().format('YYYY-MM-DD')
    const nowT = dayjs().format('hh:mm')

    export default {
        name: 'AccountNewVisitItem',
        components: {
            HomeButton,
        },
        props: {
        },
        data: () => ({
            visitInfo: {
                seatId: null,
                maleVisitors: 0,
                femaleVisitors: 0,
                customerNo: null,
                basicPlanType: null,
                visitTime: null,
                remarks: '',
            },
            basicPlanTypeList: [
                {
                    name: '通常料金(1時間)',
                    id: 1,
                },
                {
                    name: '通常料金(2時間)',
                    id: 2,
                },
                {
                    name: '通常料金(3時間)',
                    id: 3,
                },
                {
                    name: '貸切料金(1時間)',
                    id: 4,
                },
                {
                    name: '貸切料金(2時間)',
                    id: 5,
                },
                {
                    name: '貸切料金(3時間)',
                    id: 6,
                },
            ],
            rules: {
                required: val => !!val || '必須項目です。',
                small: val => !!Number(val) > 0 || '正しい数値を入力して下さい。',
            },
            snackbar: false,
            snackbarText: '入店データの作成に失敗しました。',
            visitTimeSwitch: true,
            date: nowD,
            time: nowT,
            menu: false,
            menu2: false,
            dialog: false,
        }),
        beforeCreate () {
        },
        created () {
            console.log('test', this.seat)
            console.log((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10))
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
            'visitInfo.customerNo': function (val) {
                // if (val != null) {
                // }
            }
        },
        computed: {
            ...mapGetters([
                'seat',
            ]),
            nowDate () {
                return dayjs().format('YYYY-MM-DD')
            },
            nowTime () {
                return dayjs().format('hh:mm')
            }
        },
        methods: {
            undo () {
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            toggle () {
                this.$nextTick(() => {
                    this.visitInfo.seatId = null
                })
            },
            createSalesHeader () {
                console.log('this.visitInfo', this.visitInfo)
                console.log('this.date', this.date)
                console.log('this.time', this.time)
                const data = this.visitInfo

                if (!this.visitTimeSwitch) {
                    data.visit_time = this.date + ' ' + this.time
                }
                this.$axios({
                    method: 'POST',
                    url: '/api/sales/create_sales_header/',
                    data: {
                        customer_no: data.customerNo,
                        male_visitors: data.maleVisitors,
                        female_visitors: data.femaleVisitors,
                        seat_id: data.seatId,
                        basic_plan_type: data.basicPlanType,
                        visit_time: data.visitTime,
                        remarks: data.remarks,
                    }
                })
                .then(res => {
                    console.log('createSalesHeader', res)
                    this.dialog = true
                })
                .catch(e => {
                    console.log(e)
                    this.snackbar = true
                })
            },
            init () {
                this.visitInfo = {
                    seatId: null,
                    maleVisitors: 0,
                    femaleVisitors: 0,
                    customerNo: null,
                    basicPlanType: null,
                    visitTime: null,
                    remarks: '',
                }
                this.visitTimeSwitch = true
                this.menu = false,
                this.menu2 = false
                this.date = this.nowDate
                this.time = this.nowTime
            },
            toHome () {
                this.init()
                this.$router.push({
                    name: 'AccountHome',
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .undo-btn {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
