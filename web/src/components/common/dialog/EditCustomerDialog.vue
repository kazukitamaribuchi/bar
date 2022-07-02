<template>
    <b-modal
        v-model="dialog"
        size="lg"
        screenable
        title="顧客入力"
        header-bg-variant="primary"
        header-text-variant="light"
        ok-title="登録"
        cancel-title="閉じる"
        @ok="update"
        @cancel="close"
    >
    <!-- :ok-disabled=isDisabled -->
        <b-form class="create_customer_form">
            <b-container fluid>
                <b-row>
                    <b-col cols="4">
                        <b-form-group
                            label="会員No"
                        >
                            <b-input-group>
                                <b-form-input
                                    v-model="updateCustomerData.customer_no"
                                    type="text"
                                    placeholder="会員No"
                                    required
                                ></b-form-input>
                                <b-form-invalid-feedback :state="updateCustomerData.length == 0">
                                    <!-- {{ customerNoError }} -->
                                </b-form-invalid-feedback>
                            </b-input-group>
                        </b-form-group>
                    </b-col>
                    <b-col cols="4">
                    </b-col>
                    <b-col cols="4">
                        <!-- <b-form-group
                            label="来店日"
                        >
                            <b-form-datepicker
                                v-model="updateCustomerData.first_visit"
                                placeholder="来店日を選択してください"
                            ></b-form-datepicker>
                        </b-form-group> -->
                    </b-col>
                </b-row>
                <b-card class="mt-4" bg-variant="light">
                    <b-card-title>
                        顧客情報
                    </b-card-title>
                    <b-row class="mb-0 pb-0 mt-0 pt-0">
                        <b-col cols="12" class="mb-1 pb-0">
                            <b-form-group
                                label="名前"
                            >
                                <b-input-group>
                                    <b-form-input
                                        v-model="updateCustomerData.name"
                                        type="text"
                                        placeholder="名前"
                                        required
                                    ></b-form-input>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-row class="mt-0 pt-0">
                        <b-col cols="12" class="mt-0 pt-0">
                            <b-form-group>
                                <b-input-group>
                                    <b-form-input
                                        v-model="updateCustomerData.name_kana"
                                        type="text"
                                        placeholder="名前(カナ)"
                                    ></b-form-input>
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
                                label="年齢"
                            >
                                <b-input-group>
                                    <b-form-input
                                        v-model="updateCustomerData.age"
                                        type="number"
                                        placeholder="年齢"
                                    ></b-form-input>
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
                                        v-model="updateCustomerData.birthday_year"
                                        type="text"
                                        placeholder="YYYY"
                                    ></b-form-input>
                                    <b-form-input
                                        v-model="updateCustomerData.birthday_month"
                                        type="text"
                                        placeholder="MM"
                                    ></b-form-input>
                                    <b-form-input
                                        v-model="updateCustomerData.birthday_day"
                                        type="text"
                                        placeholder="DD"
                                    ></b-form-input>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col cols="5">
                            <b-form-group
                                label="電話番号"
                            >
                                <b-input-group>
                                    <b-form-input
                                        v-model="updateCustomerData.phone"
                                        type="tel"
                                        placeholder="電話番号"
                                    ></b-form-input>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col cols="8">
                            <b-form-group
                                label="メールアドレス"
                            >
                                <b-input-group>
                                    <b-form-input
                                        v-model="updateCustomerData.mail"
                                        type="text"
                                        placeholder="メールアドレス"
                                    ></b-form-input>
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
                                        v-model="updateCustomerData.job"
                                        type="text"
                                        placeholder="職業"
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
                                        v-model="updateCustomerData.company"
                                        type="text"
                                        placeholder="会社"
                                    ></b-form-input>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-form-group
                            label="要注意人物"
                        >
                            <b-form-checkbox
                                v-model="updateCustomerData.caution_flg"
                            ></b-form-checkbox>
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
                                    v-model="updateCustomerData.remarks"
                                ></b-form-textarea>
                            </b-form-group>
                        </b-col>
                    </b-row>
                </b-card>
            </b-container>
        </b-form>
    </b-modal>
    <!-- <v-dialog
        v-model="dialog"
        max-width="1000px"
    >
        <v-card>
            <v-card-title
                id="login-title"
            >
                顧客登録
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="6">
                        <v-card
                            flat
                        >
                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.customer_no"
                                        placeholder="会員No"
                                        label="会員No"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.name"
                                        placeholder="お名前"
                                        label="お名前"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.name_kana"
                                        placeholder="お名前（フリガナ）"
                                        label="お名前（フリガナ）"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_year"
                                        placeholder="年"
                                        label="誕生日"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_month"
                                        placeholder="月"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_day"
                                        placeholder="日"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="3">
                                    <vs-input
                                        v-model="updateCustomerData.age"
                                        placeholder="年齢"
                                        label="年齢"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.job"
                                        placeholder="職業"
                                        label="職業"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.company"
                                        placeholder="会社"
                                        label="会社"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                        </v-card>
                    </v-col>
                    <v-col cols="6">
                        <v-card
                            flat
                            class="edit-customer-dialog-right"
                        >
                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_year"
                                        placeholder="年"
                                        label="初回来店日"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_month"
                                        placeholder="月"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_day"
                                        placeholder="日"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.rank_id"
                                        label="ランク"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-spacer/>
                    <v-card-actions>
                        <vs-button
                            color="primary"
                            type="filled"
                            icon="done"
                            @click="update"
                        >更新</vs-button>
                        <vs-button
                            color="primary"
                            type="border"
                            icon="done"
                            @click="dialog = false"
                        >閉じる</vs-button>
                    </v-card-actions>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog> -->
</template>

<script>
import _ from 'lodash'
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'EreateCustomerDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        customer: {},
        updateCustomerData: {},
    }),
    computed: {
        localEditCustomerDialog: {
            get: function () {
                return this.createCustomerDialog
            },
            set: function (value) {
                this.$emit('update', value)
            },
        },
    },
    methods: {
        ...mapMutations([
            'updateCustomerList',
        ]),
        open (customer) {
            this.customer = _.cloneDeep(customer)
            let updateCustomerData = _.cloneDeep(customer)
            const birthday_array = updateCustomerData.birthday.split('/')
            updateCustomerData.birthday_year = birthday_array[0]
            updateCustomerData.birthday_month = birthday_array[1]
            updateCustomerData.birthday_day = birthday_array[2]
            delete updateCustomerData.birthday
            // const first_visit_array = updateCustomerData.first_visit.split('-')
            // updateCustomerData.first_visit_year = first_visit_array[0]
            // updateCustomerData.first_visit_month = first_visit_array[1]
            // updateCustomerData.first_visit_day = first_visit_array[2]
            // delete updateCustomerData.first_visit
            this.updateCustomerData = updateCustomerData
            this.dialog = true
        },
        close () {
            this.customer = {}
            this.updateCustomerData = {}
            this.dialog = false
        },
        update () {
            const data = this.updateCustomerData
            // const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            console.log(data)
            let birthday = ''
            // 誕生日は後々セレクトに置き換える
            if (data.birthday_year != null && data.birthday_month != null && data.birthday_day != null) {
                birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            }

            this.$axios({
                url: `/api/customer/${this.$route.params['id']}/`,
                method: 'PUT',
                data: {
                    id: this.$route.params['id'],
                    name: data.name,
                    name_kana: data.name_kana,
                    age: data.age,
                    birthday_str: birthday,
                    job: data.job,
                    mail: data.mail,
                    phone: data.phone,
                    company: data.company,
                    customer_no: data.customer_no,
                    caution_flg: data.caution_flg,
                    remarks: data.remarks,
                    // first_visit: data.first_visit,
                    rank_id: 1,
                }
            })
            .then(res => {
                console.log(res)
                this.updateCustomerList(res.data)
                this.$emit('update', res.data)
                this.close()
            })
            .catch(e => {
                console.log(e)
            })

            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>

.create_customer_form {
    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }
}


// .container.form-wrap {
//   padding: 0px 40px;
// }

// .vs-component.vs-con-input-label.vs-input.vs-input-primary::v-deep {
//     width: 100%;
// }
// .vs-input-parent::v-deep {
//     width: 100%;
//     .vs-input {
//         width: 100%;
//     }
// }
//
// .edit-customer-dialog-right {
//     padding-top: 86px;
// }

</style>
