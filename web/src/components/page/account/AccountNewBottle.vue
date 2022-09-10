<template>
    <div>
        <AccountPageTitleArea
            to="AccountHome"
            title="ボトル情報作成"
        />

        <v-card
            flat
        >
            <v-container>
                <v-row>
                    <v-col cols="12" class="category_top">
                        顧客情報
                    </v-col>

                    <v-col cols="12">
                        <!-- <v-text-field
                            label="会員No"
                            v-model="customerInfo.customerNo"
                            :rules="[rules.required, rules.small]"
                        ></v-text-field> -->
                        <!-- <vs-input
                            class="mt-3 mb-0"
                            placeholder="会員No"
                            v-model="customerInfo.customerNo"
                            label="会員No(必須)"
                        >
                        </vs-input> -->
                        <SearchCustomerInfo
                            ref="searchCustomerInfo"
                            @updateCustomerInfo="updateCustomerInfo"
                        />

                    </v-col>

                    <v-col cols="12" class="category_top mt-5">
                        商品情報
                    </v-col>

                    <v-col cols="12">
                        <vs-button
                            @click="showBottleSelectDialog"
                        >
                            ボトル選択
                        </vs-button>
                    </v-col>

                    <v-col cols="12">
                        <div v-if="bottleInfo.selectedBottle == null">
                            <p class="bottle_product_name ma-0 pa-0">
                                対象のボトルは存在しません。
                            </p>
                        </div>
                        <v-row
                            v-else
                            align="center"
                            class="py-3"
                        >
                            <v-col
                                cols="2"
                                class="pa-0"
                            >
                                <v-avatar
                                    size="50px"
                                >
                                    <img
                                        v-if="bottleInfo.selectedBottle != null && bottleInfo.selectedBottle.thumbnail != null"
                                        :src="getImgLink(bottleInfo.selectedBottle.thumbnail)"
                                    >
                                    <img
                                        v-else
                                        src="@/static/img/noimage8.png"
                                    >
                                </v-avatar>
                            </v-col>
                            <v-col
                                cols="10"
                                class="pa-0"
                            >
                                <p class="bottle_product_name ma-0 pa-0">
                                    {{ bottleInfo.selectedBottle.name }}
                                </p>
                            </v-col>
                        </v-row>
                        <!-- <vs-button
                            v-if="bottleInfo.selectedBottle != null"
                            @click="bottleInfo.selectedBottle = null"
                            border
                            danger
                        >
                            クリア
                        </vs-button> -->
                    </v-col>

                    <!-- <v-col cols="12">
                        <vs-input
                            class="my-3"
                            type="date"
                            v-model="bottleInfo.openDate"
                            label="開封日(必須)"
                        />
                    </v-col> -->

                    <v-col cols="12">
                        <div>開封日</div>
                        <v-switch
                            v-model="todaySwitch"
                            label="本日"
                        ></v-switch>
                        <v-menu
                            v-if="!todaySwitch"
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
                                    v-model="bottleInfo.openDate"
                                    label="日付"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                ></v-text-field>
                            </template>
                            <v-date-picker
                                v-model="bottleInfo.openDate"
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
                    </v-col>


                    <v-col cols="12">
                        <v-textarea
                            label="備考(任意)"
                            auto-grow
                            outlined
                            rows="2"
                            row-height="20"
                            v-model="bottleInfo.remarks"
                        ></v-textarea>
                    </v-col>

                    <!-- <vs-button
                        block
                        success
                        size="large"
                        style="position: relative; left: -5px;"
                        @click="register"
                    >
                        <i class='bx bxs-send'></i> ボトル情報作成
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
                ><i class='bx bxs-send'></i> ボトル情報作成</v-btn>
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
                    ボトルデータの作成に成功しました。
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

        <BottleSelectDialog
            ref="bottleSelectDialog"
            @selectBottle="selectBottle"
        />
    </div>
</template>
<script>
    import dayjs from 'dayjs'
    import { mapGetters } from 'vuex'
    import HomeButton from '@/components/account/HomeButton'
    import SearchCustomerInfo from '@/components/account/SearchCustomerInfo'
    import BottleSelectDialog from '@/components/account/dialog/BottleSelectDialog'
    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
    const nowD = dayjs().format('YYYY-MM-DD')
    import utilsMixin from '@/mixins/utils'

    export default {
        name: 'AccountNewBottleItem',
        components: {
            HomeButton,
            SearchCustomerInfo,
            BottleSelectDialog,
            AccountPageTitleArea,
        },
        props: {
        },
        data: () => ({
            bottleInfo: {
                customerNo: '',
                selectedBottle: null,
                openDate: '',
                remarks: '',
            },
            snackbar: false,
            snackbarText: 'ボトルデータの作成に失敗しました。',
            menu: false,
            menu2: false,
            dialog: false,
            todaySwitch: true,
            date: nowD,
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
            ]),
        },
        methods: {
            undo () {
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            toggle () {
                this.$nextTick(() => {
                    this.bottleInfo.seatId = null
                })
            },
            register () {
                let data = {}
                data.customerType = 1
                data.customerNo = this.bottleInfo.customerNo
                data.selectedBottle = this.bottleInfo.selectedBottle
                data.remarks = this.bottleInfo.remarks

                let openDate = this.bottleInfo.openDate

                if (!this.todaySwitch) {
                    openDate = this.date
                }

                data.openDate = openDate

                this.$axios({
                    method: 'POST',
                    url: '/api/bottle/create_bottle_data/',
                    data: data,
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
                this.bottleInfo = {
                    customerNo: '',
                    selectedBottle: null,
                    openDate: '',
                    remarks: '',
                }
                this.menu = false
                this.menu2 = false
                this.todaySwitch = true
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
                    this.bottleInfo.customerNo = ''
                } else {
                    this.bottleInfo.customerNo = val.customer_no
                }
            },
            selectBottle (item) {
                console.log('selectBottle', item)
                this.bottleInfo.selectedBottle = item
            },
            showBottleSelectDialog () {
                this.$refs.bottleSelectDialog.open(this.bottleInfo.selectedBottle)
            }
        },
        mixins: [
            utilsMixin
        ],
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

    .bottle_product_name {
        font-size: 13px;
        color: rgba(100, 100, 100, 0.8);
    }
</style>
