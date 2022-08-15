<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            :title=createBottleDialogTitle
            header-bg-variant="primary"
            header-text-variant="light"
            ok-title="登録"
            cancel-title="閉じる"
            @ok="createOrUpdate"
            :ok-disabled=isDisabled
            @cancel="close"
        >
            <b-form class="create_bottle_form">
                <b-container fluid>

                    <b-card bg-variant="light">
                        <b-card-title>
                            顧客情報
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                            >
                                <b-icon
                                    id="create_bottle_customer_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="create_bottle_customer_info_icon"
                                title="ボトルと紐づける顧客情報を入力してください。"
                                ></b-tooltip>
                            </span>
                        </b-card-title>

                        <!-- <b-row>
                            <b-col cols="6">
                                <b-card-sub-title>会員タイプ</b-card-sub-title>
                                <b-form-group style="min-height: 40px;">
                                    <b-form-radio-group
                                        v-model="createBottleData.customerType"
                                        :options=customerTypeOptions
                                        button-variant="outline-primary"
                                        buttons
                                        style="min-height: 40px;"
                                    ></b-form-radio-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3">
                            </b-col>
                            <b-col cols="3">
                                <b-card-sub-title align="right">
                                    <span style="color: red;">*</span> : 必須項目
                                </b-card-sub-title>
                            </b-col>
                        </b-row> -->
                        <b-row v-if="createBottleData.customerType == 0">
                            <b-col cols="4">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': nonMemberNameInvalid}"
                                        class="form_required"
                                    >顧客名</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createBottleData.nonMemberName"
                                            type="text"
                                            placeholder="顧客名(必須)"
                                            required
                                            autofocus
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="nonMemberNameError.length == 0">
                                            {{ nonMemberNameError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row v-else>
                            <b-col cols="4">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerNoInvalid}"
                                        class="form_required"
                                    >会員No</label>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createBottleData.customerNo"
                                            type="text"
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
                            <b-col cols="4">
                            </b-col>
                            <b-col cols="4">
                            </b-col>
                        </b-row>
                        <b-row v-if="createBottleData.customerType == 1">
                            <b-col cols="12">
                                <b-card>
                                    <label>
                                        顧客情報
                                    </label>
                                    <b-container>
                                        <b-row>
                                            <b-col cols="5" class="mt-0 pt-0">
                                                <div style="display: flex;">
                                                    <div>
                                                        <img
                                                            src="@/assets/img/男性3.jpg"
                                                            class="create_bottle_customer_icon"
                                                        >
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-if="customerInfo != null">
                                                        <b-card-title style="font-size: 15px;">
                                                            {{ customerInfo.name}}
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            {{ customerInfo.name_kana }}
                                                        </b-card-sub-title>
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-else>
                                                        <b-card-title style="font-size: 15px;">
                                                            -
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            -
                                                        </b-card-sub-title>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    年齢
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ customerInfo.age }} 歳
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="3" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    誕生日
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ getStrInData(customerInfo.birthday) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    ランク
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ getStrInData(customerInfo.rank_name) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                        </b-row>
                                    </b-container>
                                </b-card>
                            </b-col>
                        </b-row>
                    </b-card>

                    <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            ボトル情報
                            <span
                                style="display: inline-block; margin-left: 0.4rem;"
                            >
                                <b-icon
                                    id="create_bottle_bottle_info_icon"
                                    icon="info-circle"
                                    variant="primary"
                                ></b-icon>
                                <b-tooltip
                                target="create_bottle_bottle_info_icon"
                                title="紐づけるボトルを選択してください。"
                                ></b-tooltip>
                            </span>
                        </b-card-title>
                        <b-row v-if="selectedBottle == null">
                            <b-col cols="4">
                                <b-button
                                    size="sm"
                                    @click="showAddBottleDialog"
                                    class="mzt-3"
                                    variant="primary"
                                >
                                    <b-icon
                                        icon="plus-circle"
                                        aria-hidden="true"
                                    ></b-icon> ボトルを選択
                                </b-button>
                            </b-col>
                            <b-col cols="5">
                            </b-col>
                            <b-col cols="3">
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-card-sub-title align="right">
                                <span style="color: red;">*</span> : 必須項目
                            </b-card-sub-title>
                            <b-col cols="12">
                                <b-card>
                                    <label
                                        class="form_required"
                                    >商品情報</label>
                                    <b-container>
                                        <b-row>
                                            <b-col cols="7">
                                                <div style="display: flex;">
                                                    <div>
                                                        <img
                                                            src="@/assets/img/酒9.png"
                                                            class="create_bottle_customer_icon"
                                                        >
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-if="selectedBottle != null">
                                                        <b-card-title style="font-size: 15px;">
                                                            {{ selectedBottle.name }}
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            {{ selectedBottle.price }}
                                                        </b-card-sub-title>
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-else>
                                                        <b-card-title style="font-size: 15px;">
                                                            -
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            -
                                                        </b-card-sub-title>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="3">
                                                <b-card-sub-title>
                                                    開封日
                                                </b-card-sub-title>
                                                <b-form-datepicker
                                                    v-if="selectedBottle != null"
                                                    v-model="createBottleData.openDate"
                                                    placeholder="開封日を選択してください"
                                                    class="mt-1"
                                                    style="font-size: 15px;"
                                                ></b-form-datepicker>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="2" style="margin-top: 20px;"  align-self="stretch" v-if="selectedBottle != null">
                                                <b-button
                                                    size="sm"
                                                    variant="outline-primary"
                                                    @click="showEditProductDialog()"
                                                >
                                                    <b-icon
                                                        icon="pencil"
                                                        aria-hidden="true"
                                                        variant="success"
                                                        class="edit_icon"
                                                    ></b-icon>
                                                </b-button>
                                                <!-- <b-button
                                                    size="sm"
                                                    style="position: relative; left: 10px;"
                                                    variant="outline-danger"
                                                    @click="deleteSelectedProduct()"
                                                >
                                                    <b-icon
                                                        icon="dash-square"
                                                        aria-hidden="true"
                                                        variant="danger"
                                                        class="trash_icon"
                                                    ></b-icon>
                                                </b-button> -->
                                                <b-button
                                                    size="sm"
                                                    style="position: relative; left: 10px;"
                                                    variant="outline-danger"
                                                    @click="deleteSelectedProduct"
                                                >
                                                    <b-icon
                                                        icon="trash"
                                                        aria-hidden="true"
                                                        variant="danger"
                                                        class="trash_icon"
                                                    ></b-icon>
                                                </b-button>
                                            </b-col>
                                        </b-row>
                                        <!-- <div
                                            v-if="selectedBottleList.length == 0"
                                        >
                                            <b-row>
                                                <b-col cols="7">
                                                    <div style="display: flex;">
                                                        <div>
                                                            <img
                                                                src="@/assets/img/酒9.png"
                                                                class="create_bottle_customer_icon"
                                                            >
                                                        </div>
                                                        <div class="mt-2" style="margin-left: 15px;">
                                                            <b-card-title style="font-size: 15px;">
                                                                -
                                                            </b-card-title>
                                                            <b-card-sub-title style="font-size: 12px;">
                                                                -
                                                            </b-card-sub-title>
                                                        </div>
                                                    </div>
                                                </b-col>
                                                <b-col cols="5">
                                                    <b-card-sub-title>
                                                        開封日
                                                    </b-card-sub-title>
                                                    <b-card-text>
                                                        -
                                                    </b-card-text>
                                                </b-col>
                                            </b-row>
                                        </div>
                                        <div
                                            v-else
                                        >
                                            <b-row
                                                v-for="(item, idx) in selectedBottleList"
                                                :key=item.id
                                            >
                                                <b-col cols="7">
                                                    <div style="display: flex;">
                                                        <div>
                                                            <img
                                                                src="@/assets/img/酒9.png"
                                                                class="create_bottle_customer_icon"
                                                            >
                                                        </div>
                                                        <div class="mt-2" style="margin-left: 15px;">
                                                            <b-card-title style="font-size: 15px;">
                                                                {{ item.name }}
                                                            </b-card-title>
                                                            <b-card-sub-title style="font-size: 12px;">
                                                                <b-icon icon="currency-yen"></b-icon> {{ item.price }}
                                                            </b-card-sub-title>
                                                        </div>
                                                    </div>
                                                </b-col>
                                                <b-col cols="3" class="mt-0 pt-0">
                                                    <b-card-sub-title>
                                                        開封日
                                                    </b-card-sub-title>
                                                    <b-form-datepicker
                                                        v-model="selectedBottleList[idx].openDate"
                                                        placeholder="開封日を選択してください"
                                                        class="mt-1"
                                                    ></b-form-datepicker>
                                                </b-col>
                                                <b-col cols="2" style="margin-top: 8px;"  align-self="stretch">
                                                    <b-button
                                                        size="sm"
                                                        variant="outline-primary"
                                                        @click="showEditProductDialog(item, idx)"
                                                    >
                                                        <b-icon
                                                            icon="pencil"
                                                            aria-hidden="true"
                                                            variant="success"
                                                            class="edit_icon"
                                                        ></b-icon>
                                                    </b-button>
                                                    <b-button
                                                        size="sm"
                                                        style="position: relative; left: 10px;"
                                                        variant="outline-danger"
                                                        @click="deleteSelectedProduct(item, idx)"
                                                    >
                                                        <b-icon
                                                            icon="dash-square"
                                                            aria-hidden="true"
                                                            variant="danger"
                                                            class="trash_icon"
                                                        ></b-icon>
                                                    </b-button>
                                                </b-col>
                                            </b-row>
                                        </div> -->
                                    </b-container>
                                </b-card>
                            </b-col>
                        </b-row>
                    </b-card>

                    <!-- <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            入力情報
                        </b-card-title>
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                    label="開封日"
                                >
                                    <b-form-datepicker
                                        v-model="createBottleData.openDate"
                                        placeholder="開封日を選択してください"
                                    ></b-form-datepicker>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3">
                            </b-col>
                            <b-col cols="2">
                                <b-form-group
                                    label="飲終"
                                >
                                    <b-form-checkbox-group
                                        v-model="createBottleData.end_flg"
                                        :options=endOptions
                                        buttons
                                        button-variant="outline-primary"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="2">
                                <b-form-group
                                    label="廃棄"
                                >
                                    <b-form-checkbox-group
                                        v-model="createBottleData.waste_flg"
                                        :options=wasteOptions
                                        buttons
                                        button-variant="outline-danger"
                                    ></b-form-checkbox-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="備考"
                                >
                                    <b-form-textarea
                                        rows="2"
                                        no-resize
                                        v-model="createBottleData.remarks"
                                    ></b-form-textarea>
                                </b-form-group>
                            </b-col>
                        </b-row>
                    </b-card> -->
                </b-container>
            </b-form>
        </b-modal>

        <AddBottleDialog
            ref="addBottleDialog"
            @update="selectedBottle = $event"
        />
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
import AddBottleDialog from '@/components/common/dialog/AddBottleDialog'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)
const now = dayjs().format('YYYY-MM-DD')
import utilsMixin from '@/mixins/utils'
import Vue from 'vue'

export default {
    name: 'CreateBottleDialogItem',
    props: {
    },
    components: {
        SelectForm,
        BirthdaySelectForm,
        AddBottleDialog,
    },
    data: () => ({
        createBottleData: {
            customerNo: '',
            customerType: 1,
            nonMemberName: '',
            openDate: now,
            remarks: '',
        },
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
        customerNoError: '',
        nonMemberNameError: '',
        mode: 0,
        editId: null,
        customerInfo: null,
        // endOptions: [
        //     { text: '飲終', value: 1 }
        // ],
        // wasteOptions: [
        //     { text: '廃棄', value: 1 },
        // ],
        customerTypeOptions: [
            { text: '非会員', value: 0 },
            { text: '会員', value: 1 },
        ],
        // selectedBottleList: [],
        selectedBottle: null,
    }),
    computed: {
        ...mapGetters([
            'customer',
            // 'bottle',
            // 'product',
        ]),
        isDisabled () {
            // if (this.selectedBottleList.length == 0) {
            //     return true
            // }
            if (this.selectedBottle == null
                || this.createBottleData.openDate == '') {
                return true
            }

            if (this.createBottleData.customerType == 0) {
                if (this.createBottleData.nonMemberName == '' || this.nonMemberNameError != '') {
                    return true
                } else {
                    return false
                }
            } else {
                if (this.createBottleData.customerNo == '' || this.customerNoError != '') {
                    return true
                } else {
                    return false
                }
            }
        },
        today () {
            return dayjs().format("YYYY-MM-DD")
        },
        customerNoInvalid () {
            if (this.customerNoError.length != 0
                || this.createBottleData.customerNo == null) {
                return true
            }
            return false
        },
        nonMemberNameInvalid () {
            if (this.nonMemberNameError.length != 0
                || this.createBottleData.nonMemberName == null) {
                return true
            }
            return false
        },
        createBottleDialogTitle () {
            if (this.mode == 0) {
                 return 'ボトル入力'
            } else {
                return 'ボトル入力(編集)'
            }
        }
    },
    watch: {
        "createBottleData.customerNo": function (val) {
            let reg = /^[0-9]+$/
            if (val == null) return
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.customerNoError = '正しい値を入力してください'
                    this.customerInfo = null
                } else {
                    this.customerInfo = _.cloneDeep(this.customer.find(c => c.customer_no == val))
                    if (this.customerInfo == undefined) {
                        this.customerNoError = '存在しない会員Noです。'
                    } else {
                        this.customerNoError = ''
                    }
                }
            } else {
                this.customerNoError= '会員Noを入力してください'
                this.customerInfo = null
            }
        },
        "createBottleData.nonMemberName": function (val) {
            let reg = /^[\w\sぁ-んーァ-ヶーｱ-ﾝﾞﾟ一-龠]+$/
            if (val == null) return
            if (val.length > 0) {
                if (!reg.test(val)) {
                    this.nonMemberNameError = '正しい値を入力してください'
                } else {
                    this.nonMemberNameError = ''
                }
            } else {
                this.nonMemberNameError= '顧客名を入力してください'
            }
        },
    },
    created () {
        // this.createCustomerData.first_visit = this.today
        // this.$eventHub.$off('addBottle')
        // this.$eventHub.$on('addBottle', this.addBottle)
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
            'addBottleList',
            'updateBottleList',
        ]),
        createOrUpdate () {
            if (this.mode == 0) {
                this.register()
            } else if (this.mode == 1) {
                this.update()
            }
        },
        register () {
            const data = this.createBottleData
            // data.selectedBottleList = this.selectedBottleList
            data.selectedBottle = this.selectedBottle

            console.log('register', data)

            this.$axios({
                method: 'POST',
                url: '/api/bottle/create_bottle_data/',
                data: data
            })
            .then(res => {
                console.log(res)
                this.addBottleList(res.data.data)
                this.init()
            })
            .catch(e => {
                console.log(e)
            })
            this.close()
        },
        update () {
            const data = this.createBottleData
            // data.selectedBottleList = this.selectedBottleList
            data.selectedBottle = this.selectedBottle
            data.id = this.editId
            console.log('update', data)

            this.$axios({
                url: '/api/bottle/update_bottle_data/',
                method: 'PUT',
                data: data
            })
            .then(res => {
                console.log(res)
                this.updateBottleList(res.data.data)
                this.$emit('update', res.data)

                this.$emit('updateCustomerBottleDetail', res.data.data)
                this.close()
            })
            .catch(e => {
                console.log(e)
            })

            this.close()
        },
        init () {
            this.createBottleData = {
                customerNo: '',
                nonMemberName: '',
                customerType: 1,
                remarks: '',
            }
            this.customerNoError = ''
            this.nonMemberNameError = ''
            // this.selectedBottleList = []
            this.selectedBottle = null
            this.editId = null
            this.mode = 0
        },
        close () {
            this.init()
            this.dialog = false
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
            const customerType = copyData.customer_type
            let product = copyData.product
            this.createBottleData.openDate = copyData.open_date.replace('年', '-').replace('月', '-').replace('日', '')
            this.editId = copyData.id

            if (customerType == 0) {
                this.createBottleData.nonMemberName = copyData.customer_name
                this.createBottleData.customer = null
                this.createBottleData.customerType = 0
            } else {
                this.createBottleData.nonMemberName = null
                this.createBottleData.customerNo = String(copyData.customer.customer_no)
                this.createBottleData.customerType = 1
            }

            this.selectedBottle = product
        },
        showAddBottleDialog () {
            this.$refs.addBottleDialog.open()
            // this.$refs.createBottleAddProductDialog.open()
        },
        addBottle (data) {
            const item = data
            item.openDate = now
            // this.selectedBottleList.push(item)
        },
        editBottle (data, idx) {
            // this.selectedBottleList[idx] = data
            // ↓でリアクティブに変わった
            // Vue.set(this.selectedBottleList, idx, data)
        },
        // showEditProductDialog (data, idx) {
        showEditProductDialog () {
            // this.$refs.addBottleDialog.open(data, idx)
            this.$refs.addBottleDialog.open()
        },
        // deleteSelectedProduct (data, idx) {
        deleteSelectedProduct () {
            // this.selectedBottleList.splice(idx, 1)
            this.selectedBottle = null
        }
    },
    mixins: [
        utilsMixin
    ]
}

</script>

<style lang="scss" scoped>
    .create_bottle_form {
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

    .create_bottle_customer_icon {
        border-radius: 50%;
        width: 50px;
        height: 50px;
    }
</style>
