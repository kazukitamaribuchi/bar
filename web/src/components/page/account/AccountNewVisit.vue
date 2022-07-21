<template>
    <v-row>
        <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            入店情報入力
        </p>
        <v-card
            flat
        >
            <v-row
                style="padding: 0 3rem;"
            >
                <v-col cols="12">
                    <v-text-field
                        label="会員No"
                        v-model="visitInfo.customerNo"
                        :rules="[rules.required, rules.small]"
                    ></v-text-field>
                </v-col>
                <v-col cols="12" class="pb-0">
                    <v-select
                      :items="seat"
                      item-text="seat_name"
                      item-value="id"
                      label="座席"
                      dense
                      outlined
                      v-model="visitInfo.seatId"
                    >
                        <template v-slot:prepend-item>
                            <v-list-item ripple @click="toggle">
                                <v-list-item-content>
                                    <v-list-item-title>
                                        指定無し
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </template>
                    </v-select>
                </v-col>
                <v-col cols="12" class="pb-0">
                    <v-select
                      :items="basicPlanTypeList"
                      item-text="name"
                      item-value="id"
                      label="基本料金"
                      dense
                      outlined
                      v-model="visitInfo.basicPlanType"
                    ></v-select>
                </v-col>
                <v-col cols="6" class="pt-0">
                    <label style="font-size:12px;">男性客数</label>
                    <b-form-spinbutton
                        v-model="visitInfo.maleVisitors"
                        min="0"
                        size="lg"
                    ></b-form-spinbutton>
                <!-- @change="updateQuantity(item)" -->
                </v-col>
                <v-col cols="6" class="pt-0">
                    <label style="font-size:12px;">女性客数</label>
                    <b-form-spinbutton
                        v-model="visitInfo.femaleVisitors"
                        min="0"
                        size="lg"
                    ></b-form-spinbutton>
                </v-col>
                <v-col cols="12">
                    <div>来店時間</div>
                    <v-switch
                        v-model="visitTimeSwitch"
                        label="現在時刻"
                    ></v-switch>
                    <v-menu
                        v-if="!visitTimeSwitch"
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :return-value.sync="date"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="date"
                                label="日付"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker
                            v-model="date"
                            no-title
                            scrollable
                        >
                            <v-spacer></v-spacer>
                            <v-btn
                                text
                                color="primary"
                                @click="menu = false"
                            >Cancel</v-btn>
                            <v-btn
                                text
                                color="primary"
                                @click="$refs.menu.save(date)"
                            >OK</v-btn>
                        </v-date-picker>
                    </v-menu>
                    <v-menu
                        v-if="!visitTimeSwitch"
                        ref="menu2"
                        v-model="menu2"
                        :close-on-content-click="false"
                        :return-value.sync="time"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="time"
                                label="時刻"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                        </template>
                        <v-time-picker
                            v-model="time"
                        >
                            <v-spacer></v-spacer>
                            <v-btn
                                text
                                color="primary"
                                @click="menu2 = false"
                            >Cancel</v-btn>
                            <v-btn
                                text
                                color="primary"
                                @click="$refs.menu2.save(time)"
                            >OK</v-btn>
                        </v-time-picker>
                    </v-menu>
                </v-col>
                <v-col cols="12">
                    <v-textarea
                        label="備考"
                        auto-grow
                        outlined
                        rows="2"
                        row-height="20"
                        v-model="visitInfo.remarks"
                    ></v-textarea>
                </v-col>
            </v-row>
            <v-col cols="12" class="mt-4">
                <v-card
                    id="new_visit_button_wrap"
                    style="background-color:rgba(37, 119, 224, 0.87); color:white; cursor:pointer;"
                    @click="createSalesHeader"
                >
                    <p class="text-center py-4 mb-0">入店情報作成</p>
                </v-card>
            </v-col>
            <v-col cols="12">
                <HomeButton/>
            </v-col>
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
    </v-row>
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
