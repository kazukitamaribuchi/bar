<template>
    <div>
        <AccountPageTitleArea
            to="AccountHome"
            title="会員登録"
        />

        <v-card
            flat
        >
            <v-container>
                <v-row>
                    <v-col cols="12" class="category_top">
                        基本情報
                    </v-col>

                    <v-col cols="12">
                        <!-- <v-text-field
                            label="会員No"
                            v-model="customerInfo.customerNo"
                            :rules="[rules.required, rules.small]"
                        ></v-text-field> -->
                        <vs-input
                            class="my-3"
                            placeholder="会員No"
                            v-model="customerInfo.customerNo"
                            label="会員No(必須)"
                            @blur="checkCustomerNo"
                        >
                            <template
                                v-if="custonerNoSuccess"
                                #message-success
                            >
                                OK
                            </template>
                            <template
                                v-if="customerNoError"
                                #message-danger
                            >
                                {{ customerNoErrorText }}
                            </template>
                        </vs-input>

                    </v-col>

                    <v-col cols="12">
                        <!-- <v-text-field
                            label="顧客名"
                            v-model="customerInfo.name"
                            :rules="[rules.required]"
                        ></v-text-field> -->
                        <vs-input
                            class="my-3"
                            placeholder="名前"
                            v-model="customerInfo.name"
                            label="顧客名(必須)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12" class="pt-0">
                        <vs-input
                            class="my-3"
                            placeholder="名前(ふりがな)"
                            v-model="customerInfo.name_kana"
                            label="顧客名ふりがな(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="4" class="py-1">
                        <vs-input
                            class="my-3"
                            placeholder="年齢"
                            v-model="customerInfo.age"
                            label="年齢(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="8" class="py-1">
                        <!-- <label style="color: rgba(50, 50, 50, 0.8);">
                            誕生日
                        </label>
                        <b-input-group>
                            <b-form-input
                                v-model="customerInfo.birthday"
                                type="date"
                            ></b-form-input>
                        </b-input-group> -->
                        <vs-input
                            class="my-3"
                            type="date"
                            v-model="customerInfo.birthday"
                            label="誕生日(任意)"
                        />
                    </v-col>

                    <v-col cols="12" class="category_top mt-5">
                        詳細情報
                    </v-col>

                    <v-col cols="12" class="mt-4">
                        <vs-input
                            placeholder="電話番号"
                            v-model="customerInfo.phone"
                            label="電話番号(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12">
                        <vs-input
                            placeholder="メールアドレス"
                            v-model="customerInfo.mail"
                            label="メールアドレス(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12">
                        <vs-input
                            placeholder="住所"
                            v-model="customerInfo.address"
                            label="住所(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12" class="mt-5">
                        <vs-input
                            placeholder="職業"
                            v-model="customerInfo.job"
                            label="職業(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12">
                        <vs-input
                            placeholder="会社"
                            v-model="customerInfo.company"
                            label="会社(任意)"
                        >
                        </vs-input>
                    </v-col>

                    <v-col cols="12">
                        <!-- <v-checkbox
                            v-model="customerInfo.cautionFlg"
                            label="要注意人物"
                        ></v-checkbox> -->
                        <vs-checkbox v-model="customerInfo.cautionFlg">
                            要注意人物
                        </vs-checkbox>
                    </v-col>

                    <v-col cols="12">
                        <v-textarea
                            label="備考(任意)"
                            auto-grow
                            outlined
                            rows="2"
                            row-height="20"
                            v-model="customerInfo.remarks"
                        ></v-textarea>
                    </v-col>

                    <!-- <vs-button
                        block
                        success
                        size="large"
                        style="position: relative; left: -5px;"
                        @click="register"
                    >
                        <i class='bx bxs-send'></i> 会員情報作成
                    </vs-button> -->

                </v-row>
            </v-container>
            <!-- <v-col cols="12" class="mt-4">
                <v-card
                    id="new_visit_button_wrap"
                    style="background-color:rgba(37, 119, 224, 0.87); color:white; cursor:pointer;"
                    @click="register"
                >
                    <p class="text-center py-4 mb-0">会員情報作成</p>
                </v-card>
            </v-col> -->
            <v-col cols="12" class="py-0">
                <v-btn
                    block
                    depressed
                    color="primary"
                    @click="register"
                ><i class='bx bxs-send'></i> 会員情報作成</v-btn>
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
                    会員データの作成に成功しました。
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
    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'

    export default {
        name: 'AccountNewCustomerItem',
        components: {
            HomeButton,
            AccountPageTitleArea,
        },
        props: {
        },
        data: () => ({
            customerInfo: {
                customerNo: '',
                name: '',
                nameKana: '',
                age: '',
                birthday: '',
                phone: '',
                mail: '',
                address: '',
                company: '',
                cautionFlg: false,
                remarks: '',
            },
            rules: {
                required: val => !!val || '必須項目です。',
                small: val => !!Number(val) > 0 || '正しい数値を入力して下さい。',
            },
            snackbar: false,
            snackbarText: '会員データの作成に失敗しました。',
            date: nowD,
            time: nowT,
            menu: false,
            menu2: false,
            dialog: false,
            customerNoError: false,
            customerNoErrorText: '',
            custonerNoSuccess: false,
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
                    this.customerInfo.seatId = null
                })
            },
            register () {
                let birthday = ''
                if (this.customerInfo.birthday != '' && this.customerInfo.birthday != null) {
                    birthday = this.customerInfo.birthday.replaceAll('-', '/')
                }

                let data = {}
                data.customer_no = this.customerInfo.customerNo
                data.name = this.customerInfo.name
                data.name_kana = this.addData(this.customerInfo.name_kana)
                data.age = this.addData(this.customerInfo.age)
                data.birthday_str = this.addData(birthday)
                data.job = this.addData(this.customerInfo.job)
                data.mail = this.addData(this.customerInfo.mail)
                data.phone = this.addData(this.customerInfo.phone)
                data.company = this.addData(this.customerInfo.company)
                data.caution_flg = this.customerInfo.cautionFlg
                data.remarks = this.addData(this.customerInfo.remarks)
                data.rank_id = 1

                this.$axios({
                    method: 'POST',
                    url: '/api/customer/',
                    data: data
                })
                .then(res => {
                    console.log('register', res)
                    this.dialog = true
                })
                .catch(e => {
                    console.log(e)
                    this.snackbar = true
                })
            },
            addData (val) {
                if (val != '') {
                    return val
                }
                return null
            },
            init () {
                this.customerInfo = {
                    customerNo: '',
                    name: '',
                    nameKana: '',
                    age: '',
                    birthday: '',
                    phone: '',
                    mail: '',
                    address: '',
                    company: '',
                    cautionFlg: false,
                    remarks: '',
                }
                this.menu = false,
                this.menu2 = false
                this.date = this.nowDate
                this.time = this.nowTime
                this.customerNoError = false
                this.customerNoErrorText = ''
                this.custonerNoSuccess = false
            },
            toHome () {
                this.init()
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            checkCustomerNo () {
                const no = this.customerInfo.customerNo
                console.log(no)
                if (no != '') {
                    const reg = /^[0-9]+$/
                    if (no <= 0 || !reg.test(no)) {
                        this.showError('正しい会員Noを入力してください。')
                    } else {
                        this.$axios({
                            method: 'post',
                            url: '/api/customer/get_customer_no_duplicate/',
                            data: {
                                customer_no: no
                            }
                        })
                        .then(res => {
                            console.log(res.data.result == true)
                            if (res.data.result) {
                                this.hideError()
                                this.custonerNoSuccess = true
                            } else {
                                this.showError('既に他のユーザーと紐づいている会員Noです。')
                            }
                        })
                        .catch(e => {
                            console.log(e)
                            this.showError('会員No重複確認に失敗しました。')
                        })
                    }
                } else {
                    this.hideError()
                    this.custonerNoSuccess = false
                }
            },
            showError (text) {
                this.custonerNoSuccess = false
                this.customerNoError = true
                this.customerNoErrorText = text
            },
            hideError () {
                this.customerNoError = false
                this.customerNoErrorText = ''
            },
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
