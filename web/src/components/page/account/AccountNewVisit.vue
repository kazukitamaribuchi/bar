<template>
    <div>

        <v-card
            flat
        >
            <AccountPageTitleArea
                to="AccountHome"
                title="入店情報入力"
            />

            <v-container fluid>
                <v-row>
                    <v-col cols="12" class="category_top">
                        来店情報
                    </v-col>

                    <v-col cols="12">
                        <!-- <vs-input
                            class="my-3"
                            placeholder="会員No"
                            v-model="visitInfo.customerNo"
                            label="会員No(必須)"
                        >
                        </vs-input> -->

                        <SearchCustomerInfo
                            ref="searchCustomerInfo"
                            @updateCustomerInfo="updateCustomerInfo"
                        />

                    </v-col>
                    <v-col cols="12">
                        <!-- <v-select
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
                        </v-select> -->
                        <vs-select
                            placeholder='座席を選択してください'
                            label="座席(任意)"
                            v-model="visitInfo.seatId"
                            chips
                        >
                            <vs-option
                                v-for='(label, i) in seat'
                                :key='i'
                                :label='label.seat_name'
                                :value='label.id'
                            >{{ label.seat_name }}
                            </vs-option>
                        </vs-select>

                    </v-col>
                    <v-col cols="12">
                        <!-- <v-select
                          :items="basicPlanTypeList"
                          item-text="name"
                          item-value="id"
                          label="基本料金"
                          dense
                          outlined
                          v-model="visitInfo.basicPlanType"
                        ></v-select> -->

                        <vs-select
                            placeholder='座席を選択してください'
                            label="基本料金(必須)"
                            v-model="visitInfo.basicPlanType"
                            chips
                            @change="selectBasicPlan"
                        >
                            <vs-option
                                v-for='(label, i) in basicPlanTypeList'
                                :key='i'
                                :label='label.name'
                                :value='label.id'
                            >{{ label.name }}
                            </vs-option>

                            <template
                                v-if="basicPlanError"
                                #message-danger
                            >
                                基本料金を選択してください。
                            </template>
                        </vs-select>
                    </v-col>
                    <v-col cols="6" class="py-0">
                        <div style="font-size:12px;">男性客数</div>
                        <b-form-spinbutton
                            inline
                            v-model="visitInfo.maleVisitors"
                            @change="changeVisitors"
                            min="0"
                            size="lg"
                        ></b-form-spinbutton>
                    <!-- @change="updateQuantity(item)" -->
                    </v-col>
                    <v-col cols="6" class="py-0">
                        <div style="font-size:12px;">女性客数</div>
                        <b-form-spinbutton
                            inline
                            @change="changeVisitors"
                            v-model="visitInfo.femaleVisitors"
                            min="0"
                            size="lg"
                        ></b-form-spinbutton>
                    </v-col>
                    <v-col cols="pa-0 ma-0">
                        <p
                            v-if="visitorsError"
                            class="pa-0 ma-0"
                            style="color: red; font-size: 12px;"
                        >
                            来店人数を入力してください。
                        </p>
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
                            label="備考(任意)"
                            auto-grow
                            outlined
                            rows="2"
                            row-height="20"
                            v-model="visitInfo.remarks"
                        ></v-textarea>
                    </v-col>

                    <!-- <vs-button
                        block
                        success
                        size="large"
                        style="position: relative; left: -5px;"
                        @click="createSalesHeader"
                    >
                        <i class='bx bxs-send'></i> 入店情報作成
                    </vs-button> -->
                </v-row>
            </v-container>
            <!-- <v-col cols="12" class="mt-4">
                <v-card
                    id="new_visit_button_wrap"
                    style="background-color:rgba(37, 119, 224, 0.87); color:white; cursor:pointer;"
                    @click="createSalesHeader"
                >
                    <p class="text-center py-4 mb-0">入店情報作成</p>
                </v-card>
            </v-col> -->
            <v-col cols="12" class="py-0">
                <v-btn
                    block
                    depressed
                    color="primary"
                    @click="createSalesHeader"
                ><i class='bx bxs-send'></i> 入店情報作成</v-btn>
            </v-col>
            <v-col cols="12" class="pb-0">
                <v-btn
                    block
                    depressed
                    color="success"
                    @click="init"
                ><i class='bx bx-trash'></i> クリア</v-btn>
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
            persistent
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
    import SearchCustomerInfo from '@/components/account/SearchCustomerInfo'
    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
    import { Const } from '@/assets/js/const'
    const nowD = dayjs().format('YYYY-MM-DD')
    const nowT = dayjs().format('hh:mm')
    const Con = new Const()

    export default {
        name: 'AccountNewVisitItem',
        components: {
            HomeButton,
            SearchCustomerInfo,
            AccountPageTitleArea,
        },
        props: {
        },
        data: () => ({
            visitInfo: {
                seatId: '',
                maleVisitors: 0,
                femaleVisitors: 0,
                customerNo: '',
                basicPlanType: '',
                visitTime: '',
                remarks: '',
            },
            basicPlanTypeList: Con.OPTIONS_BASIC_PLAN_TYPE_LIST,
            // basicPlanTypeList: [
            //     {
            //         name: '通常料金(1時間)',
            //         id: 1,
            //     },
            //     {
            //         name: '通常料金(2時間)',
            //         id: 2,
            //     },
            //     {
            //         name: '通常料金(3時間)',
            //         id: 3,
            //     },
            //     {
            //         name: '貸切料金(1時間)',
            //         id: 4,
            //     },
            //     {
            //         name: '貸切料金(2時間)',
            //         id: 5,
            //     },
            //     {
            //         name: '貸切料金(3時間)',
            //         id: 6,
            //     },
            // ],
            rules: {
                required: val => !!val || '必須項目です。',
                small: val => !!Number(val) > 0 || '正しい数値を入力して下さい。',
            },
            snackbar: false,
            snackbarText: '',
            visitTimeSwitch: true,
            date: nowD,
            time: nowT,
            menu: false,
            menu2: false,
            dialog: false,
            basicPlanError: false,
            customerNoError: false,
            visitorsError: false,
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
            selectBasicPlan () {
                console.log('selectBasicPlan')
                this.basicPlanError = false
            },
            createSalesHeader () {
                console.log('this.visitInfo', this.visitInfo)
                console.log('this.date', this.date)
                console.log('this.time', this.time)
                const data = this.visitInfo

                this.customerNoError = false
                this.visitorsError = false

                if (this.visitInfo.customerNo == '') {
                    this.customerNoError = true
                    this.$refs.searchCustomerInfo.showError('会員Noを入力してください。')
                }

                if (this.visitInfo.basicPlanType == '') {
                    this.basicPlanError = true
                }

                if (this.visitInfo.maleVisitors == 0
                    && this.visitInfo.femaleVisitors == 0) {
                    this.visitorsError = true
                }

                if (this.customerNoError
                    || this.basicPlanError
                    || this.visitorsError) {
                        return
                }

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
                    if (e.response.data != '') {
                        this.snackbarText = e.response.data.msg
                    } else {
                        this.snackbarText = '入店データの作成に失敗しました。'
                    }
                    this.snackbar = true
                })
            },
            init () {
                this.visitInfo = {
                    seatId: '',
                    maleVisitors: 0,
                    femaleVisitors: 0,
                    customerNo: '',
                    basicPlanType: '',
                    visitTime: '',
                    remarks: '',
                }
                this.snackbar = false
                this.snackbarText = false
                this.basicPlanError = false
                this.customerNoError = false
                this.visitorsError = false
                this.visitTimeSwitch = true
                this.menu = false
                this.menu2 = false
                this.date = this.nowDate
                this.time = this.nowTime
                this.$refs.searchCustomerInfo.init()
            },
            toHome () {
                this.init()
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            updateCustomerInfo (val) {
                if (val == null) {
                    this.visitInfo.customerNo = ''
                } else {
                    this.visitInfo.customerNo = val.customer_no
                }
            },
            changeVisitors () {
                this.visitorsError = false
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

    .vs-input-parent::v-deep {
        width: 100%;
        .vs-input {
            width: 100%;
        }
    }

    .category_top {
        // border-bottom: 1px solid rgba(151, 151, 151, 0.9);
        border-bottom: 1px solid rgba(213, 213, 213, 0.9);
        padding-bottom: 0px;
        margin-bottom: 10px;
    }
</style>
