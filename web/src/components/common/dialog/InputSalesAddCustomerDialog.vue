<template>
    <div>
        <b-modal
            v-model="dialog"
            size="lg"
            screenable
            title="会員追加"
            header-bg-variant="primary"
            header-text-variant="light"
        >
        <!-- ok-title="登録"
        cancel-title="閉じる"
        @ok="createOrUpdate"
        :ok-disabled=isDisabled
        @cancel="close" -->
            <b-form class="create_bottle_form">
                <b-container fluid>
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
                                title="会員Noを入力してください。"
                            ></b-tooltip>
                        </span>
                    </b-card-title>
                    <b-row>
                        <b-col cols="4">
                            <b-form-group
                            >
                                <label
                                    :class="{'invalid': customerNoInvalid}"
                                    class="form_required"
                                >会員No</label>
                                <b-input-group>
                                    <b-form-input
                                        v-model="customerNo"
                                        type="number"
                                        placeholder="会員No(必須)"
                                        required
                                        :autofocus="mode == 0"
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
                    <b-row>
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
                                                        src="@/static/img/男性3.jpg"
                                                        class="create_bottle_customer_icon"
                                                    >
                                                </div>
                                                <div class="mt-0" style="margin-left: 30px;" v-if="customerInfo != null">
                                                    <b-card-sub-title>
                                                        名前
                                                    </b-card-sub-title>
                                                    <b-card-text style="font-size: 15px;">
                                                        {{ customerInfo.name}}
                                                    </b-card-text>
                                                    <!-- <b-card-sub-title style="font-size: 12px;">
                                                        {{ customerInfo.name_kana }}
                                                    </b-card-sub-title> -->
                                                </div>
                                                <div class="mt-0" style="margin-left: 30px;" v-else>
                                                    <b-card-sub-title>
                                                        名前
                                                    </b-card-sub-title>
                                                    <b-card-text style="font-size: 15px;">
                                                        -
                                                    </b-card-text>
                                                    <!-- <b-card-sub-title style="font-size: 12px;">
                                                        -
                                                    </b-card-sub-title> -->
                                                </div>
                                            </div>
                                        </b-col>
                                        <b-col cols="2" class="mt-0 pt-0">
                                            <b-card-sub-title>
                                                年齢
                                            </b-card-sub-title>
                                            <b-card-text v-if="customerInfo != null">
                                                {{ getStrInData(customerInfo.age) }} 歳
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
                                @click="addOrUpdate"
                            >
                                {{ btnStr }}
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>
    </div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import SelectForm from '@/components/common/parts/SelectForm'
import BirthdaySelectForm from '@/components/common/parts/BirthdaySelectForm'
import utilsMixin from '@/mixins/utils'
import customerMixin from '@/mixins/customer'
import Vue from 'vue'

export default {
    name: 'InputSalesAddCustomerDialogItem',
    props: {
        customerList: {
            type: Array,
            required: false,
            default: () => ([])
        },
        // customerListSub: {
        //     type: Array,
        //     required: true,
        //     default: () => ([])
        // },
    },
    components: {
        SelectForm,
        BirthdaySelectForm,
    },
    data: () => ({
        customerNo: '',
        customerInfo: null,

        dialog: false,
        customerNoError: '',
        mode: 0,
        updateIndex: 0,
    }),
    computed: {
        ...mapGetters([
            'customer',
        ]),
        isDisabled () {
            if (this.customerNo == ''
                || this.customerNoError.length > 0
                || this.customerInfo == null) {
                return true
            }
            return false
        },
        customerNoInvalid () {
            if (this.customerNoError.length != 0) {
                return true
            }
            return false
        },
        btnStr () {
            if (this.mode == 0) return '追加'
            return '更新'
        }
    },
    watch: {
        "customerNo": function (val) {
            let reg = /^[0-9]+$/
            if (val == null) return
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.customerNoError = '正しい値を入力してください'
                    this.customerInfo = null
                } else {
                    this.searchCustomerNo(val)
                    .then(res => {
                        console.log(res)
                        if (res.data.status == 'success') {
                            this.customerNoError = ''
                            this.customerInfo = res.data.data
                            this.customerDuplicate(res.data.data)
                        } else {
                            this.customerNoError = '存在しない会員Noです。'
                            this.customerInfo = null
                        }
                    })
                    .catch(e => {
                        console.log(e)
                        this.customerNoError = '顧客データの取得に失敗しました。'
                        this.customerInfo = null
                    })
                }
            } else {
                this.customerNoError= '会員Noを入力してください'
                this.customerInfo = null
            }
        },
    },
    created () {
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
        ]),
        init () {
            this.customerNo = ''
            this.customerInfo = null
            this.customerNoError = ''
            this.mode = 0
            this.updateIndex = 0
        },
        close () {
            this.dialog = false
        },
        initClose () {
            this.init()
            this.dialog = false
        },
        open (data, index) {
            this.dialog = true
            if (data) {
                this.init()
                this.convertData(data, index)
                this.mode = 1
            } else {
                this.init()
                this.mode = 0
            }
        },
        convertData (data, index) {
            this.customerNo = String(data.customer_no)
            this.updateIndex = index
            // this.customerInfo = data
            // console.log('this.customerInfo', this.customerInfo)
        },
        addOrUpdate () {
            if (this.mode == 0) {
                this.addCustomer()
            } else {
                this.updateCustomer()
            }
        },
        addCustomer () {
            this.customerInfo.amountPaid = 0
            this.customerInfo.cardPayment = false
            this.customerInfo.basicPlanCardTax = 0

            this.$emit('addCustomer', this.customerInfo)
            this.initClose()
        },
        updateCustomer () {
            this.customerInfo.amountPaid = 0
            this.customerInfo.cardPayment = false
            this.customerInfo.basicPlanCardTax = 0

            this.$emit('updateCustomer', this.customerInfo, this.updateIndex)
            this.initClose()
        },
        customerDuplicate (data) {
            for (const item of this.customerList) {
                console.log('customerDuplicate', item, data)
                if (item.customer_no == data.customer_no) {
                    this.customerNoError = '既に追加されている会員情報です。'
                    break
                } else {
                    this.customerNoError = ''
                }
            }
        },
    },
    mixins: [
        utilsMixin,
        customerMixin,
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
