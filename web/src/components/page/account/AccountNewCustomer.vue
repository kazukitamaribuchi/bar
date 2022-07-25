<template>
    <div>
        <i
            @click="undo"
            class='bx bx-undo undo-btn'
        ></i>
        <p class="text-center" style="font-size: 13px;">
            入店情報入力
        </p>
        <v-card
            flat
        >
            <v-row
                style="padding: 0 3rem;"
            >
                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="会員No"
                        v-model="customerInfo.customerNo"
                        :rules="[rules.required, rules.small]"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="顧客名"
                        v-model="customerInfo.name"
                        :rules="[rules.required]"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="顧客名(カナ)"
                        v-model="customerInfo.nameKana"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="年齢"
                        v-model="customerInfo.age"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-1">
                    <label style="color: rgba(50, 50, 50, 0.8);">
                        誕生日
                    </label>
                    <b-input-group>
                        <b-form-input
                            v-model="customerInfo.birthday"
                            type="date"
                        ></b-form-input>
                    </b-input-group>
                </v-col>


                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="電話番号"
                        v-model="customerInfo.phone"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="メール"
                        v-model="customerInfo.mail"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="住所"
                        v-model="customerInfo.address"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="職業"
                        v-model="customerInfo.job"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-text-field
                        label="会社"
                        v-model="customerInfo.company"
                    ></v-text-field>
                </v-col>

                <v-col cols="12" class="py-0">
                    <v-checkbox
                        v-model="customerInfo.cautionFlg"
                        label="要注意人物"
                    ></v-checkbox>
                </v-col>

                <v-col cols="12">
                    <v-textarea
                        label="備考"
                        auto-grow
                        outlined
                        rows="2"
                        row-height="20"
                        v-model="customerInfo.remarks"
                    ></v-textarea>
                </v-col>
            </v-row>
            <v-col cols="12" class="mt-4">
                <v-card
                    id="new_visit_button_wrap"
                    style="background-color:rgba(37, 119, 224, 0.87); color:white; cursor:pointer;"
                    @click="register"
                >
                    <p class="text-center py-4 mb-0">会員情報作成</p>
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

    export default {
        name: 'AccountNewCustomerItem',
        components: {
            HomeButton,
        },
        props: {
        },
        data: () => ({
            customerInfo: {
                customerNo: null,
                name: '',
                nameKana: null,
                age: null,
                birthday: null,
                phone: null,
                mail: null,
                address: null,
                company: null,
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
            'customerInfo.customerNo': function (val) {
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
                    this.customerInfo.seatId = null
                })
            },
            register () {
                const data = this.customerInfo
                let birthday = ''
                if (data.birthday != '' && data.birthday != null) {
                    birthday = data.birthday.replaceAll('-', '/')
                }

                this.$axios({
                    method: 'POST',
                    url: '/api/customer/',
                    data: {
                        name: data.name,
                        name_kana: data.nameKana,
                        age: data.age,
                        birthday_str: birthday,
                        job: data.job,
                        mail: data.mail,
                        phone: data.phone,
                        company: data.company,
                        customer_no: data.customerNo,
                        caution_flg: data.cautionFlg,
                        remarks: data.remarks,
                        // ランクは最初から上位で作る事も許容させるか? => マスタでやらせる。
                        rank_id: 1,
                    }
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
            init () {
                this.customerInfo = {
                    customerNo: null,
                    name: '',
                    nameKana: null,
                    age: null,
                    birthday: null,
                    phone: null,
                    mail: null,
                    address: null,
                    company: null,
                    cautionFlg: false,
                    remarks: '',
                }
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
