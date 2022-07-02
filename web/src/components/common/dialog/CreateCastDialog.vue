<template>
    <div>
        <b-modal
            v-model="dialog"
            size="lg"
            screenable
            title="キャスト入力"
            header-bg-variant="primary"
            header-text-variant="light"
            ok-title="登録"
            cancel-title="閉じる"
            @ok="createOrUpdate"
            :ok-disabled=isDisabled
            @cancel="close"
        >
            <b-form class="create_cast_form">
                <b-container fluid>
                    <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            キャスト情報
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                                v-if="mode == 0"
                            >
                                <b-icon
                                    id="create_cast_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="create_cast_info_icon"
                                title="新規でキャスト情報を作成します。"
                                ></b-tooltip>
                            </span>
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                                v-else
                            >
                                <b-icon
                                    id="edit_cast_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="edit_cast_info_icon"
                                title="キャスト情報を更新します。"
                                ></b-tooltip>
                            </span>
                        </b-card-title>

                        <b-row class="mb-0 pb-0 mt-0 pt-0">
                            <b-card-sub-title align="right">
                                <span style="color: red;">*</span> : 必須項目
                            </b-card-sub-title>
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': castNameInvalid}"
                                        class="form_required"
                                    >源氏名</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.name"
                                            type="text"
                                            placeholder="源氏名(必須)"
                                            required
                                            autofocus
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castNameError.length == 0">
                                            {{ castNameError }}
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
                                            v-model="createCastData.name_kana"
                                            type="text"
                                            placeholder="カナ(任意)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castNameKanaError.length == 0">
                                            {{ castNameKanaError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>

                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': castAgeInvalid}"
                                    >年齢</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.age"
                                            placeholder="年齢(任意)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castAgeError.length == 0">
                                            {{ castAgeError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>

                        <b-row class="mb-0 pb-0">
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': castRealNameInvalid}"
                                    >本名</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.real_name"
                                            type="text"
                                            placeholder="本名"
                                            required
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castRealNameError.length == 0">
                                            {{ castRealNameError }}
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
                                            v-model="createCastData.real_name_kana"
                                            type="text"
                                            placeholder="本名(カナ)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castRealNameKanaError.length == 0">
                                            {{ castRealNameKanaError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                    label="実年齢"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.real_age"
                                            placeholder="実年齢"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                    label="勤務開始日"
                                >
                                    <b-form-datepicker
                                        v-model="createCastData.start_working_date"
                                        placeholder="勤務開始日を選択してください"
                                    ></b-form-datepicker>
                                </b-form-group>
                            </b-col>
                            <b-col cols="2">
                                <b-button
                                    style="margin-top: 31px;"
                                    @click="createCastData.start_working_date = null"
                                    variant="outline-secondary"
                                >Clear</b-button>
                            </b-col>
                        </b-row>
                        <b-row class="mb-2 mt-3 pt-2">
                            <b-form-group
                                label="経験有無"
                            >
                                <b-form-checkbox-group
                                    v-model="createCastData.experienced"
                                    :options=experiencedOptions
                                    buttons
                                    button-variant="outline-primary"
                                ></b-form-checkbox-group>
                            </b-form-group>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="誕生日"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.birthday"
                                            type="date"
                                        ></b-form-input>
                                        <!-- <b-form-input
                                            v-model="createCastData.birthday_year"
                                            type="text"
                                            placeholder="YYYY"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCastData.birthday_month"
                                            type="text"
                                            placeholder="MM"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCastData.birthday_day"
                                            type="text"
                                            placeholder="DD"
                                        ></b-form-input> -->
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <!-- <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="顔写真"
                                >
                                    <b-form-file
                                        id="file-small"
                                        v-model="createCastData.icon"
                                        browse-text="Browse"
                                        placeholder=""
                                        drop-placeholder=""
                                        no-drop-placeholder=""
                                        ref='input'
                                        @change='inputFile'
                                    ></b-form-file>
                                </b-form-group>
                            </b-col>
                        </b-row> -->
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': castPhoneInvalid}"
                                    >電話番号</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.phone"
                                            type="tel"
                                            placeholder="電話番号"
                                            @blur="checkPhoneNumber"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castPhoneError.length == 0">
                                            {{ castPhoneError }}
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
                                        :class="{'invalid': castMailInvalid}"
                                    >メールアドレス</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.mail"
                                            type="text"
                                            placeholder="メールアドレス"
                                            @blur="checkMailAddress"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="castMailError.length == 0">
                                            {{ castMailError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="住所"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.address"
                                            type="text"
                                            placeholder="住所"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row class="mb-2 mt-3 pt-2">
                            <b-col cols="2">
                                <b-form-group
                                    label="退職済"
                                >
                                    <b-form-checkbox-group
                                        v-model="createCastData.resign_flg"
                                        :options=resignOptions
                                        buttons
                                        button-variant="outline-secondary"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="5">
                                <b-form-group
                                    label="退職日"
                                >
                                    <b-form-datepicker
                                        v-model="createCastData.resign_date"
                                        placeholder="退職日を選択してください"
                                    ></b-form-datepicker>
                                </b-form-group>
                            </b-col>
                            <b-col cols="2">
                                <b-button
                                    style="margin-top: 31px;"
                                    @click="createCastData.resign_date = null"
                                    variant="outline-secondary"
                                >Clear</b-button>
                            </b-col>
                        </b-row>
                        <!-- <b-row>
                            <b-col>
                                <b-form-group
                                    label="Q&A1"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_one"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_one"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Q&A2"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_two"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_two"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Q&A3"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_three"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_three"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row> -->
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="備考"
                                >
                                    <b-form-textarea
                                        rows="2"
                                        no-resize
                                        v-model="createCastData.remarks"
                                    ></b-form-textarea>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3">
                                <b-button
                                    style="margin-top: 25px;"
                                    @click="init"
                                    variant="outline-secondary"
                                >フォーム初期化</b-button>
                            </b-col>
                        </b-row>
                    </b-card>
                </b-container>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import utilsMixin from '@/mixins/utils'
import validateMixin from '@/mixins/validate'

const reader = new FileReader()

export default {
    name: 'CreateCastDialogItem',
    props: {
    },
    data: () => ({
        // createCastData: {
        //     question_one: null,
        //     question_two: null,
        //     question_three: null,
        //     resign_flg: []
        // },
        // createCastData: {
        //     name: 'おっぱいまん',
        //     name_kana: 'おっぱいまん',
        //     real_name: 'おっぱいまん',
        //     real_name_kana: 'おっぱいまん',
        //     age: 3,
        //     real_age: 100,
        //     experienced: [1],
        //     resign_flg: [],
        //     resign_date: null,
        //     mail: null,
        //     address: null,
        //     phone: null,
        //     remarks: null,
        //     start_working_date: null
        // },
        createCastData: {
            name: '',
            name_kana: '',
            real_name: '',
            real_name_kana: '',
            age: null,
            real_age: null,
            experienced: [],
            resign_flg: [],
            resign_date: null,
            mail: null,
            address: '',
            phone: null,
            remarks: null,
            start_working_date: null,
            birthday: null,
        },
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
        mode: 0,
        experiencedOptions: [
            { text: '有', value: 1 }
        ],
        resignOptions: [
            { text: '済', value: 1 }
        ],
        showImage: false,
        file: null,
        previewSrc: '',
        castNameError: '',
        castNameKanaError: '',
        castAgeError: '',
        castRealNameError: '',
        castRealNameKanaError: '',
        castRealAgeError: '',
        castPhoneError: '',
        castMailError: '',
    }),
    computed: {
        ...mapGetters([
            'question',
        ]),
        isDisabled () {
            if (this.errorCheck() || this.requiredCheck()) {
                return true
            } else {
                return false
            }
        },
        // 質問内容の絞り込み（後で
        qanda () {
            return this.question
        },
        castNameInvalid () {
            if (this.castNameError != ''
                || this.castNameKanaError != '') {
                return true
            }
            return false
        },
        castAgeInvalid () {
            if (this.castAgeError != '') {
                return true
            }
            return false
        },
        castRealNameInvalid () {
            if (this.castRealNameError != ''
                || this.castRealNameKanaError != '') {
                return true
            }
            return false
        },
        castRealAgeInvalid () {
            if (this.castRealAgeError != '') {
                return true
            }
            return false
        },
        castPhoneInvalid () {
            if (this.castPhoneError != '') {
                return true
            }
            return false
        },
        castMailInvalid () {
            if (this.castMailError != '') {
                return true
            }
            return false
        },
    },
    watch: {
        "createCastData.name": function (val) {
            this.castNameError = this.validateName(val, true)
        },
        "createCastData.name_kana": function (val) {
            this.castNameKanaError = this.validateNameKana(val)
        },
        "createCastData.age": function (val) {
            this.castAgeError = this.validateAge(val)
        },
        "createCastData.real_name": function (val) {
            this.castRealNameError = this.validateRealName(val, this.createCastData.real_name_kana)
            if (this.castRealNameError == ''
                && this.castRealNameKanaError == Con.ERROR_MSG.RealNameKana.Illegal) {
                this.castRealNameKanaError = ''
            }
        },
        "createCastData.real_name_kana": function (val) {
            this.castRealNameKanaError = this.validateRealNameKana(val, this.createCastData.real_name)
            if (this.castRealNameKanaError == ''
                && this.castRealNameError == Con.ERROR_MSG.RealName.Illegal) {
                this.castRealNameError = ''
            }
        },
        "createCastData.real_age": function (val) {
            this.castRealAgeError = this.validateAge(val)
        },
    },
    created () {
    },
    methods: {
        ...mapMutations([
            'addCastList',
            'updateCastList',
        ]),
        createOrUpdate () {
            if (this.mode == 0) {
                this.register()
            } else if (this.mode == 1) {
                this.update()
            }
        },
        register () {
            // console.log('register', this.createCastData)
            const data = this.createCastData

            console.log('register', data)

            let birthday = ''
            let start_working_date_str = ''
            let resign_date_str = ''

            // 誕生日は後々セレクトに置き換える
            // if (data.birthday_year != null && data.birthday_month != null && data.birthday_day != null) {
            //     birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // }
            if (data.birthday != '' && data.birthday != null) {
                birthday = data.birthday.replaceAll('-', '/')
            }

            if (data.start_working_date != null) {
                start_working_date_str = data.start_working_date.replaceAll('-', '/')
            }

            if (data.resign_date != null) {
                resign_date_str = data.resign_date.replaceAll('-', '/')
            }

            let experienced = (this.createCastData.experienced.length != 0) ? true : false
            let resign_flg  = (this.createCastData.resign_flg.length != 0) ? true : false

            let postData

            // if (this.file !== null) {
            //     postData = new FormData()
            //     postData.append('name', data.name)
            //     postData.append('name_kana', data.name_kana)
            //     postData.append('real_name', data.real_name)
            //     postData.append('real_name_kana', data.real_name_kana)
            //     postData.append('age', data.age)
            //     postData.append('real_age', data.real_age)
            //     postData.append('birthday_str', data.birthday)
            //     postData.append('start_working_date', data.start_working_date)
            //     postData.append('experienced', experienced)
            //     postData.append('mail', data.mail)
            //     postData.append('phone', data.phone)
            //     postData.append('address', data.address)
            //     postData.append('remarks', data.remarks)
            //     postData.append('icon', this.file)
            //     postData.append('resign_flg', data.resign_flg)
            //     postData.append('resign_date', data.resign_date)
            // } else {
                postData = {
                    name: data.name,
                    name_kana: data.name_kana,
                    real_name: data.real_name,
                    real_name_kana: data.real_name_kana,
                    age: data.age,
                    real_age: data.real_age,
                    birthday_str: birthday,
                    // icon: data.icon,
                    start_working_date_str: start_working_date_str,
                    resign_date_str: resign_date_str,
                    experienced: experienced,
                    mail: data.mail,
                    phone: data.phone,
                    address: data.address,
                    remarks: data.remarks,
                    resign_flg: resign_flg,
                    resign_date: data.resign_date,
                }
            // }

            console.log('this.postData', postData)

            this.$axios({
                method: 'POST',
                url: '/api/cast/',
                data: postData
            })
            .then(res => {
                console.log(res)
                this.addCastList(res)
                this.close()
            })
            .catch(e => {
                console.log(e)
            })

        },
        update () {
            const data = this.createCastData
            // const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            let birthday = ''
            let start_working_date_str = ''
            let resign_date_str = ''

            console.log('update', data)


            // 誕生日は後々セレクトに置き換える
            // if (data.birthday_year != null && data.birthday_month != null && data.birthday_day != null) {
            //     birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // }

            if (data.birthday != '' && data.birthday != null) {
                birthday = data.birthday.replaceAll('-', '/')
            }

            if (data.start_working_date != null) {
                start_working_date_str = data.start_working_date.replaceAll('-', '/')
            }

            if (data.resign_date != null) {
                resign_date_str = data.resign_date.replaceAll('-', '/')
            }

            let experienced = (this.createCastData.experienced.length != 0) ? true : false
            let resign_flg  = (this.createCastData.resign_flg.length != 0) ? true : false

            let postData

            postData = {
                id: this.$route.params['id'],
                name: data.name,
                name_kana: data.name_kana,
                real_name: data.real_name,
                real_name_kana: data.real_name_kana,
                age: data.age,
                real_age: data.real_age,
                birthday_str: birthday,
                // icon: data.icon,
                start_working_date_str: start_working_date_str,
                resign_date_str: resign_date_str,
                experienced: experienced,
                mail: data.mail,
                phone: data.phone,
                address: data.address,
                remarks: data.remarks,
                resign_flg: resign_flg,
                resign_date: data.resign_date,
            }

            console.log('this.postData', postData)

            this.$axios({
                url: `/api/cast/${this.$route.params['id']}/`,
                method: 'PUT',
                data: postData
            })
            .then(res => {
                console.log(res)
                this.updateCastList(res.data)
                this.$emit('update', res.data)
                this.close()
            })
            .catch(e => {
                console.log(e)
            })

        },
        init () {
            this.createCastData = {
                name: null,
                name_kana: '',
                real_name: '',
                real_name_kana: '',
                age: null,
                real_age: null,
                experienced: [],
                resign_flg: [],
                resign_date: null,
                mail: null,
                address: '',
                phone: null,
                remarks: null,
                start_working_date: null,
                birthday: null,
            }
        },
        close () {
            this.dialog = false
            this.init()
        },
        open (data) {
            this.dialog = true
            if (data) {
                this.convertData(data)
                this.mode = 1
            } else {
                this.mode = 0
            }
        },
        convertData (data) {
            let copyData = _.cloneDeep(data)
            let resign_flg = []
            if (copyData.resign_flg) {
                resign_flg.push(1)
            }
            let experienced = []
            if (copyData.experienced) {
                experienced.push(1)
            }

            let resign_date = ''
            if (copyData.resign_date != null) {
                resign_date = copyData.resign_date.replaceAll('/', '-')
            }

            let start_working_date = ''
            if (copyData.start_working_date != null) {
                start_working_date = copyData.start_working_date.replaceAll('/', '-')
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

            // copyData.birthday_year = birthday_year
            // copyData.birthday_month = birthday_month
            // copyData.birthday_day = birthday_day

            copyData.resign_flg = resign_flg
            copyData.experienced = experienced
            copyData.resign_date = resign_date
            copyData.start_working_date = start_working_date
            this.createCastData = copyData
        },
        checkPhoneNumber () {
            this.castPhoneError = this.validatePhone(this.createCastData.phone)
        },
        checkMailAddress () {
            this.castMailError = this.validateMail(this.createCastData.mail)
        },
        errorCheck () {
            if (this.castNameError != ''
                || this.castNameKanaError != ''
                || this.castAgeError != ''
                || this.castRealNameError != ''
                || this.castRealNameKanaError != ''
                || this.castRealAgeError != ''
                || this.castPhoneError != ''
                || this.castMailError != '') {
                return true
            } else {
                return false
            }
        },
        requiredCheck () {
            if (this.createCastData.name == '') {
                return true
            } else {
                return false
            }
        }
        // inputFile (e) {
        //     reader.onload = e => {
        //         this.previewSrc = e.target.result
        //     }
        //     reader.readAsDataURL(e)
        //     this.file = e
        //     this.showImage = true
        // },
        //
        // delete_image () {
        //     this.file = null
        //     this.previewSrc = ''
        //     this.$refs.input.lazyValue = ''
        //     this.showImage = false
        // },
    },
    mixins: [
        utilsMixin,
        validateMixin
    ]
}

</script>

<style lang="scss" scoped>
    .basic_select_wrap {
        width: 100%;
        display: grid;
        .basic_select {
            background: white;
            border-radius: 4px;
            border: 1px solid rgba(125, 125, 125, 0.4);
            padding: 6px 20px 6px 7px;
            font-size: 16px;
            font-weight: 200;
            width: 100%;
        }
    }

    .basic_select_wrap::after {
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 4.5px solid rgba(50, 50, 50, 1);
        content: "";
        position: relative;
        // right: 12px;
        // top: 13px;
        right: -315px;
        top: -18px;
        width: 0;
    }

    .invalid {
        color: red;
    }

    .form_required:after{
        content: '*';
        color: red;
    }

    // きかない・・・
    // #file-small {
    //     border: 1px solid rgba(182, 182, 182, 0.5) !important;
    //     border-radius: 6px !important;
    //     padding: 5px !important;
    //     background: white !important;
    // }
    //
    // .custom-file-label {
    //     display: none !important;
    // }
</style>
