<template>
    <div>
    <b-modal
        v-model="dialog"
        title="会員No検索"
        @ok="search"
        centered
        ok-title="検索"
        cancel-title="閉じる"
    >
        <b-form
            class="mt-3"
            @submit.prevent
        >
            <b-form-group
                class="search_customer_no"
            >
                <b-input-group>
                    <b-input-group-prepend is-text>
                        <b-icon icon="person-fill"></b-icon>
                    </b-input-group-prepend>
                    <b-form-input
                        v-model="customerNo"
                        type="number"
                        placeholder="会員No"
                        autofocus
                        required
                        @keyup.enter="enterSearch"
                        @keypress="setSearch"
                        ref="focusInput"
                    ></b-form-input>
                    <b-form-invalid-feedback :state="customerNoError.length == 0">
                        {{ customerNoError }}
                    </b-form-invalid-feedback>
                </b-input-group>
            </b-form-group>

            <!-- <b-button
                block
                variant="primary"
                class="search_btn"
                @click="search"
            >検索</b-button> -->
        </b-form>
    </b-modal>
    <!-- <v-dialog
        v-model="dialog"
        max-width="400px"
    >
        <v-card>
            <v-card-title
            >
                会員No検索
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="customer_no"
                            placeholder="会員No"
                            label="会員No"
                        ></vs-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-spacer/>
                    <v-card-actions>
                        <vs-button
                            color="primary"
                            type="filled"
                            icon="done"
                            @click="search"
                        >検索</vs-button>
                        <vs-button
                            color="primary"
                            type="border"
                            icon="done"
                            @click="close"
                        >閉じる</vs-button>
                    </v-card-actions>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog> -->

    <b-modal
        v-model="dialog2"
        title="Error"
        ok-only
        centered
    >
        存在しない会員Noです。
        正しい会員Noかチェックしてください。
    </b-modal>

</div>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'SearchCustomerNoDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        dialog2: false,
        customerNo: '',
        searchCustomerNoValue: false,
        customerNoError: '',
    }),
    computed: {
        ...mapGetters([
            'customer',
        ]),
    },
    watch: {
        customerNo: function (val) {
            const reg = /^[0-9]+$/
            if (val == null) {
                this.customerNoError = ''
                return
            }
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.customerNoError = '正しい値を入力してください'
                } else {
                    this.customerNoError = ''
                }
            } else {
                this.customerNoError= ''
            }
        }
    },
    beforeRouteUpdate (to, from, next) {
        next();
    },
    mounted () {
    },
    methods: {
        setSearch () {
            this.searchCustomerNoValue = true
        },
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
            this.customer_no = ''
        },
        enterSearch () {
            if (!this.searchCustomerNoValue ||
                this.customerNoError.length != 0)
            {
                return
            }
            this.search()
            this.searchCustomerNoValue = false
        },
        search () {
            let usernameRegex = /^\d+$/
            if (usernameRegex.test(this.customerNo)) {
                // if (this.customer.find(c => c.customer_no == this.customerNo) == undefined) {
                //     this.dialog2 = true
                //     this.customerNo = ''
                //     return
                // }
                this.$router.push({
                    name: 'CustomerDetail',
                    params: {
                        id: this.customerNo
                    }
                })
                this.customerNo = ''
                // this.$router.go({
                //     path: this.$router.currentRoute.path,
                //     force: true
                // })

                this.close()
            }
        },
        // checkCustomerNo () {
        //     const val = this.customerNo
        //
        //     const reg = /^[0-9]+$/
        //     if (val == null) {
        //         this.customerNoError = ''
        //         return
        //     }
        //     if (val.length > 0) {
        //         if (val <= 0 || !reg.test(val)) {
        //             this.customerNoError = '正しい値を入力してください'
        //         } else {
        //             this.customerNoError = ''
        //         }
        //     } else {
        //         this.customerNoError= ''
        //     }
        // },
    }
}

</script>

<style lang="scss" scoped>

.input-group-text {
    height: 100%;
    border-radius: 5px 0 0 5px !important;
}



// .container.form-wrap {
//   padding: 0px 40px;
// }
//
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
