<template>
    <div>
        <b-modal
            v-model="dialog"
            size="lg"
            screenable
            title="顧客入力"
            header-bg-variant="primary"
            header-text-variant="light"
        >
        <!-- ok-title="登録"
        cancel-title="閉じる"
        @ok="createOrUpdate"
        :ok-disabled=isDisabled
        @cancel="close" -->
            <b-form class="create_customer_form">
                <b-container fluid>
                    <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            顧客情報
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                                v-if="mode == 0"
                            >
                                <b-icon
                                    id="create_customer_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="create_customer_info_icon"
                                title="新規で顧客情報を作成します。"
                                ></b-tooltip>
                            </span>
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                                v-else
                            >
                                <b-icon
                                    id="edit_customer_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="edit_customer_info_icon"
                                title="顧客情報を更新します。"
                                ></b-tooltip>
                            </span>
                        </b-card-title>
                        <b-row>
                            <b-card-sub-title align="right">
                                <span style="color: red;">*</span> : 必須項目
                            </b-card-sub-title>
                            <b-col cols="4">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerNoInvalid}"
                                        class="form_required"
                                    >会員No</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.customerNo"
                                            type="number"
                                            placeholder="会員No(必須)"
                                            required
                                            autofocus
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNoError.length == 0">
                                            {{ customerNoError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="5">
                            </b-col>
                            <b-col cols="3">
                                <!-- <b-form-group
                                    label="来店日"
                                >
                                    <b-form-datepicker
                                        v-model="createCustomerData.first_visit"
                                        placeholder="来店日を選択してください"
                                    ></b-form-datepicker>
                                </b-form-group> -->
                            </b-col>
                        </b-row>
                        <b-row class="mb-0 pb-0 mt-0 pt-0">
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerNameInvalid}"
                                        class="form_required"
                                    >名前</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.name"
                                            type="text"
                                            placeholder="名前(必須)"
                                            required
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNameError.length == 0">
                                            {{ customerNameError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row class="mt-0 pt-0">
                            <b-col cols="12" class="mt-0 pt-0">
                                <b-form-group>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.name_kana"
                                            type="text"
                                            placeholder="カナ(任意)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNameKanaError.length == 0">
                                            {{ customerNameKanaError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <!-- <b-col>
                                <b-form-group
                                    label="誕生日"
                                >
                                    <BirthdaySelectForm
                                        :year=createCustomerData.birthday_year
                                        :month=createCustomerData.birthday_month
                                        :day=createCustomerData.birthday_day
                                    />
                                </b-form-group>
                            </b-col> -->
                            <b-col cols="4">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerAgeInvalid}"
                                    >年齢</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.age"
                                            type="number"
                                            placeholder="年齢(任意)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerAgeError.length == 0">
                                            {{ customerAgeError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="誕生日"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.birthday"
                                            type="date"
                                        ></b-form-input>
                                        <!-- <b-form-input
                                            v-model="createCustomerData.birthday_year"
                                            type="text"
                                            placeholder="YYYY"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCustomerData.birthday_month"
                                            type="text"
                                            placeholder="MM"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCustomerData.birthday_day"
                                            type="text"
                                            placeholder="DD"
                                        ></b-form-input> -->
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerPhoneInvalid}"
                                    >電話番号</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.phone"
                                            type="tel"
                                            placeholder="電話番号(ハイフン無し,任意)"
                                            @blur="checkPhoneNumber"
                                        ></b-form-input>
                                        <!-- @change="testt"
                                        @input="testtt"
                                        @update="testttt"
                                        @focus="testtttt"
                                        @blur.native="testin" -->
                                        <b-form-invalid-feedback :state="customerPhoneError.length == 0">
                                            {{ customerPhoneError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="8">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerMailInvalid}"
                                    >メールアドレス</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.mail"
                                            type="text"
                                            placeholder="メールアドレス(任意)"
                                            @blur="checkMailAddress"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerMailError.length == 0">
                                            {{ customerMailError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                    label="職業"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.job"
                                            type="text"
                                            placeholder="職業(任意)"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="会社"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.company"
                                            type="text"
                                            placeholder="会社(任意)"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row class="mb-2 mt-3 pt-2">
                            <!-- <b-form-group
                                label="要注意人物"
                            >
                                <b-form-checkbox
                                    v-model="createCustomerData.caution_flg"
                                ></b-form-checkbox>
                            </b-form-group> -->
                            <!-- <b-card-sub-title>要注意人物</b-card-sub-title> -->
                            <b-form-group
                                label="要注意人物"
                            >
                                <b-form-checkbox-group
                                    v-model="createCustomerData.cautionFlg"
                                    :options=cautionOptions
                                    buttons
                                    button-variant="outline-secondary"
                                ></b-form-checkbox-group>
                            </b-form-group>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="備考"
                                >
                                    <b-form-textarea
                                        rows="2"
                                        no-resize
                                        v-model="createCustomerData.remarks"
                                    ></b-form-textarea>
                                </b-form-group>
                            </b-col>
                            <!-- <b-col cols="3">
                                <b-button
                                    style="margin-top: 25px;"
                                    @click="init"
                                    variant="outline-secondary"
                                >フォーム初期化</b-button>
                            </b-col> -->
                        </b-row>
                    </b-card>

                    <b-button
                        style="margin-top: 25px;"
                        @click="init"
                        variant="outline-secondary"
                    >フォーム初期化</b-button>
                </b-container>
            </b-form>
            <template #modal-footer>
                <b-container fluid>
                    <b-row>
                        <b-col align="right" class="add_sales_detail_footer_col">
                            <b-button
                                variant="secondary"
                                @click="close"
                                class="btn_close"
                            >
                                閉じる
                            </b-button>
                            <b-button
                                variant="primary"
                                :disabled=isDisabled
                                @click="createOrUpdate"
                            >
                                登録
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>

        <b-modal
            v-model="registerSuccessDialog"
            hide-header
        >
            <div>
                顧客データの作成に成功しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="initClose"
                        >
                            OK
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="registerFailureDialog"
            hide-header
        >
            <div>
                顧客データの作成に失敗しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="registerFailureDialog = false"
                        >
                            閉じる
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="updateSuccessDialog"
            hide-header
        >
            <div>
                顧客データの更新に成功しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="initClose"
                        >
                            OK
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="updateFailureDialog"
            hide-header
        >
            <div>
                顧客データの更新に失敗しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="updateFailureDialog = false"
                        >
                            閉じる
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
    </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import moment from 'moment'
import SelectForm from '@/components/common/parts/SelectForm'
import BirthdaySelectForm from '@/components/common/parts/BirthdaySelectForm'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
import utilsMixin from '@/mixins/utils'
import validateMixin from '@/mixins/validate'
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)

export default {
    name: 'CreateCustomerDialogItem',
    props: {
    },
    components: {
        SelectForm,
        BirthdaySelectForm,
    },
    data: () => ({
        createCustomerData: {
            birthday: null,
            // birthday_year: null,
            // birthday_month: null,
            // birthday_day: null,
            customerNo: '',
            name: '',
            name_kana: '',
            age: '',
            phone: '',
            mail: '',
            job: '',
            company: '',
            remarks: '',
            cautionFlg: []
        },
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
        customerNoError: '',
        customerNameError: '',
        customerNameKanaError: '',
        customerAgeError: '',
        customerPhoneError: '',
        customerMailError: '',
        customerJobError: '',
        customerCompanyError: '',
        mode: 0,
        cautionOptions: [
            { text: '要注意', value: 1 }
        ],

        registerSuccessDialog: false,
        registerFailureDialog: false,
        updateSuccessDialog: false,
        updateFailureDialog: false,

        waitServerResponse: false,
    }),
    computed: {
        ...mapGetters([
            'customer',
        ]),
        isDisabled () {
            if (this.errorCheck() || this.requiredCheck()) {
                return true
            } else {
                return false
            }
        },
        today () {
            return dayjs().format("YYYY-MM-DD")
        },
        customerNoInvalid () {
            if (this.customerNoError != '') {
                return true
            }
            return false
        },
        customerNameInvalid () {
            if (this.customerNameError != ''
                || this.customerNameKanaError != '') {
                return true
            }
            return false
        },
        customerAgeInvalid () {
            if (this.customerAgeError != '') {
                return true
            }
            return false
        },
        customerPhoneInvalid () {
            if (this.customerPhoneError != '') {
                return true
            }
            return false
        },
        customerMailInvalid () {
            if (this.customerMailError != '') {
                return true
            }
            return false
        },
    },
    watch: {
        "createCustomerData.customerNo": function (val) {
            let reg = /^[0-9]+$/
            if (val == null) {
                this.customerNoError = ''
                return
            }
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.customerNoError = '正しい値を入力してください'
                } else {
                    this.checkCustomerNoDuplicate(val)
                }
            } else {
                this.customerNoError= '会員Noを入力してください'
            }
        },
        "createCustomerData.name": function (val) {
            this.customerNameError = this.validateName(val, true)
        },
        "createCustomerData.name_kana": function (val) {
            this.customerNameKanaError = this.validateNameKana(val)
        },
        "createCustomerData.age": function (val) {
            this.customerAgeError = this.validateAge(val)
        },
        // "createCustomerData.birthday": function (val) {
        //     this.customerBirthdayError = this.validateBirthday(val)
        // },
    },
    created () {
        // this.createCustomerData.first_visit = this.today
    },
    methods: {
        ...mapMutations([
            'addCustomerList',
            'updateCustomerList',
            'addCustomerListTop',
        ]),
        createOrUpdate () {
            if (this.waitServerResponse) {
                console.log('サーバー応答待ち')
                return
            }

            if (this.mode == 0) {
                this.register()
            } else if (this.mode == 1) {
                this.update()
            }
        },
        register () {
            console.log('register', this.createCustomerData)

            let birthday = ''
            if (this.createCustomerData.birthday != '' && this.createCustomerData.birthday != null) {
                birthday = this.createCustomerData.birthday.replaceAll('-', '/')
            }

            // let birthday = ''
            // // 誕生日は後々セレクトに置き換える?
            // if (data.birthday_year != null && data.birthday_month != null && data.birthday_day != null) {
            //     birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // }

            const cautionFlg = (this.createCustomerData.cautionFlg.length != 0) ? true : false

            let data = {
                name: this.createCustomerData.name,
                birthday_str: birthday,
                caution_flg: cautionFlg,
                rank_id: 1,
            }
            if (this.createCustomerData.name_kana != '') data.name_kana = this.createCustomerData.name_kana
            if (this.createCustomerData.age != '') data.age = this.createCustomerData.age
            if (this.createCustomerData.job != '') data.job = this.createCustomerData.job
            if (this.createCustomerData.mail != '') data.mail = this.createCustomerData.mail
            if (this.createCustomerData.phone != '') data.phone = this.createCustomerData.phone
            if (this.createCustomerData.company != '') data.company = this.createCustomerData.company
            if (this.createCustomerData.customerNo != '') data.customer_no = this.createCustomerData.customerNo
            if (this.createCustomerData.remarks != '') data.remarks = this.createCustomerData.remarks

            console.log('data', data)

            this.waitServerResponse = true

            this.$axios({
                method: 'POST',
                url: '/api/customer/',
                data: data
                // {
                //     name: data.name,
                //     name_kana: data.name_kana,
                //     age: data.age,
                //     birthday_str: birthday,
                //     job: data.job,
                //     mail: data.mail,
                //     phone: data.phone,
                //     company: data.company,
                //     customer_no: data.customerNo,
                //     caution_flg: cautionFlg,
                //     remarks: data.remarks,
                //     // ランクは最初から上位で作る事も許容させるか? => マスタでやらせる。
                //     rank_id: 1,
                // }
            })
            .then(res => {
                console.log(res)
                this.addCustomerListTop(res.data)

                // this.registerSuccessDialog = true
                this.initClose()
            })
            .catch(e => {
                console.log(e)

                this.registerFailureDialog = true
                this.waitServerResponse = false
            })
        },
        update () {
            const data = this.createCustomerData
            // const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // let birthday = ''
            // // 誕生日は後々セレクトに置き換える
            // if (data.birthday_year != null && data.birthday_month != null && data.birthday_day != null) {
            //     birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // }
            console.log('data.birthday', data.birthday)
            console.log(data.birthday == '-')
            let birthday = ''
            if (data.birthday != '' && data.birthday != null) {
                birthday = data.birthday.replaceAll('-', '/')
            }

            if (data.birthday == '-') {
                birthday = ''
            }

            const cautionFlg = (this.createCustomerData.cautionFlg.length != 0) ? true : false

            console.log(birthday, data)

            this.waitServerResponse = true

            this.$axios({
                // url: `/api/customer/${data.id}/`,
                url: '/api/customer/update_customer_data/',
                method: 'PUT',
                data: {
                    id: data.id,
                    name: data.name,
                    name_kana: data.name_kana,
                    age: data.age,
                    birthday_str: birthday,
                    job: data.job,
                    mail: data.mail,
                    phone: data.phone,
                    company: data.company,
                    customer_no: Number(data.customerNo),
                    caution_flg: cautionFlg,
                    remarks: data.remarks,
                    // first_visit: data.first_visit,
                    // rank_id: 1,
                }
            })
            .then(res => {
                console.log(res)
                this.updateCustomerList(res.data)
                this.$emit('update', res.data)

                // this.updateSuccessDialog = true
                this.initClose()
            })
            .catch(e => {
                console.log(e)
                this.updateFailureDialog = true
                this.waitServerResponse = false
            })

            // this.close()
        },
        init () {
            this.createCustomerData = {
                birthday: null,
                // birthday_year: null,
                // birthday_month: null,
                // birthday_day: null,
                customerNo: '',
                name: '',
                name_kana: '',
                age: '',
                phone: '',
                mail: '',
                job: '',
                company: '',
                remarks: '',
                cautionFlg: []
            }
            this.customerNoError = ''
            this.customerNameError = ''
            this.customerNameKanaError = ''
            this.customerAgeError = ''
            this.customerPhoneError = ''
            this.customerMailError = ''
            this.customerJobError = ''
            this.customerCompanyError = ''

            this.registerSuccessDialog = false
            this.registerFailureDialog = false
            this.updateSuccessDialog = false
            this.updateFailureDialog = false

            // this.dialog = false
            this.waitServerResponse = false
        },
        close () {
            // this.init()
            this.dialog = false
        },
        initClose () {
            this.init()
            this.dialog = false
        },
        open (data) {
            this.dialog = true
            if (data) {
                this.convertData(data)
                this.mode = 1
            } else {
                this.init()
                this.mode = 0
            }
        },
        convertData (data) {
            console.log('convert',data)
            let copyData = _.cloneDeep(data)
            let cautionFlg = []
            if (copyData.caution_flg) {
                cautionFlg.push(1)
            }

            // let birthday_year = ''
            // let birthday_month = ''
            // let birthday_day = ''
            // if (copyData.birthday != null || copyData.birthday == '') {
            //     let birthday_split = copyData.birthday.split('/')
            //     birthday_year = birthday_split[0]
            //     birthday_month = birthday_split[1]
            //     birthday_day = birthday_split[2]
            // }

            if (copyData.birthday != '') {
                copyData.birthday = copyData.birthday.replaceAll('/', '-')
            }

            copyData.customerNo = String(copyData.customer_no)
            copyData.cautionFlg = cautionFlg
            // copyData.birthday_year = birthday_year
            // copyData.birthday_month = birthday_month
            // copyData.birthday_day = birthday_day
            this.createCustomerData = copyData
        },
        checkCustomerNoDuplicate (customerNo) {
            const id = this.$route.params.id
            // const me = this.customer.find(c => c.id == id)
            const selfCustomerNo = this.createCustomerData.customer_no

            if (this.$route.name == 'CustomerDetail'
                && this.mode == 1
                && selfCustomerNo == Number(customerNo)) {
                this.customerNoError = ''
            } else {
                this.$axios({
                    method: 'post',
                    url: '/api/customer/get_customer_no_duplicate/',
                    data: {
                        customer_no: customerNo
                    }
                })
                .then(res => {
                    if (res.data.result) {
                        this.customerNoError = ''
                    } else {
                        this.customerNoError = '既に他のユーザーと紐づいています。'
                    }
                })
                .catch(e => {
                    console.log(e)
                    this.customerNoError = '会員No重複確認に失敗しました。'
                })
            }

            // this.$axios({
            //     method: 'POST',
            //     url: '/api/customer/get_customer_no_duplicate/',
            //     data: { customer_no: customerNo }
            // })
            // .then(res => {
            //     console.log(res.data.result)
            //     if (res.data.result) {
            //         this.customerNoError = ''
            //     } else {
            //         this.customerNoError = res.data.msg
            //     }
            // })
            // .catch(e => {
            //     console.log(e)
            // })
        },
        checkPhoneNumber () {
            this.customerPhoneError = this.validatePhone(this.createCustomerData.phone)
        },
        checkMailAddress () {
            this.customerMailError = this.validateMail(this.createCustomerData.mail)
        },
        errorCheck () {
            if (this.customerNoError != ''
                || this.customerNameError != ''
                || this.customerNameKanaError != ''
                || this.customerAgeError != ''
                || this.customerPhoneError != ''
                || this.customerMailError != ''
                || this.customerJobError != ''
                || this.customerCompanyError != '') {
                return true
            } else {
                return false
            }
        },
        requiredCheck () {
            if (this.createCustomerData.customerNo == ''
                || this.createCustomerData.name == '') {
                return true
            } else {
                return false
            }
        },

    },
    mixins: [
        utilsMixin,
        validateMixin
    ]
}

</script>

<style lang="scss" scoped>
    .create_customer_form {
        .input-group-text {
            height: 100%;
            border-radius: 5px 0 0 5px !important;
        }
    }

    .invalid {
        color: red;
    }

    .form_required:after{
        content: '*';
        color: red;
    }
</style>
