<template>
    <div>
        <AccountPageTitleArea
            to="AccountHome"
            title="会員情報"
        />

        <v-container>

            <v-card-title class="py-0">
                検索条件
            </v-card-title>

            <div>
                <div class="px-5">
                    <vs-input
                        class="my-3"
                        placeholder="会員No"
                        v-model="searchInfo.customerNo"
                    >
                        <template #icon>
                            <i class='bx bx-credit-card' ></i>
                        </template>
                    </vs-input>
                    <vs-input
                        class="my-3"
                        placeholder="名前"
                        v-model="searchInfo.customerName"
                    >
                        <template #icon>
                            <i class='bx bx-user'></i>
                        </template>
                    </vs-input>

                </div>

                <vs-button
                    class="mt-4"
                    block
                    :loading="searchLoading"
                    @click="search"
                >
                    <i class='bx bx-search-alt'></i> Search
                </vs-button>
            </div>

        </v-container>

        <v-divider class="mx-6 mt-8"/>

        <v-container class="px-3">
            <v-card-title>
                検索結果: {{ searchResult.count }} 件
            </v-card-title>
            <v-card-text v-if="searchResult.results == null">
                検索条件を入力してください。
            </v-card-text>
            <v-card-text v-else-if="searchResult.results.length == 0">
                検索結果は0件です。
            </v-card-text>
            <v-card-text v-else>
                <v-row class="mb-3">
                    <v-col
                        v-for="(item, i) in searchResult.results"
                        :key="i"
                        class="my-0 py-0"
                        cols="12"
                    >
                        <v-card
                            class="mt-1 px-1 py-3"
                            style="cursor: pointer;"
                            @click="showCustomerDetail(item)"
                        >
                            <v-row
                                align="center"
                                class="spacer"
                                no-gutters
                            >
                                <v-col
                                    cols="3"
                                    sm="1"
                                    md="1"
                                    class="pl-2"
                                >
                                    <v-avatar
                                        size="36px"
                                    >
                                        <img
                                            alt="Avatar"
                                            src="@/static/img/男性1.jpg"
                                        >
                                        <!-- src="http://localhost:8000/media/upload/男性1.jpg" -->
                                    </v-avatar>
                                    <!-- {{ item.customer_no }} -->
                                </v-col>
                                <!-- class="hidden-xs-only" -->
                                <v-col
                                    sm="4"
                                    md="4"
                                >
                                    <div style="font-size:10px;" class="text-grey">名前</div>
                                    <div>{{ item.name | truncate(10) }}</div>
                                </v-col>
                                <v-col
                                    cols="3"
                                    sm="2"
                                    md="2"
                                >
                                    <!-- <div style="font-size:10px;" class="text-grey">会員No</div>
                                    <div>{{ item.customer_no }}</div> -->
                                    <div style="font-size:10px;" class="text-grey">年齢</div>
                                    <div>{{ getStrInData(item.age) }}歳</div>
                                </v-col>
                                <v-col
                                    cols="1"
                                    sm="1"
                                    md="1"
                                    class="hidden-lg-only"
                                >
                                    <div class="text-right">
                                        <i style="color:rgba(100,100,100,0.5);" class='bx bx-chevron-right'></i>
                                    </div>
                                </v-col>
                            </v-row>
                        </v-card>
                        <!-- <vs-card type="3">
                            <template #title>
                                <h3>Pot with a plant</h3>
                            </template>
                            <template #img>
                                <img src="http://localhost:8000/media/upload/男性99.jpg" alt="">
                            </template>
                            <template #text>
                                <p>
                                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                                    </p>
                                </template>
                            <template #interactions>
                                <vs-button danger icon>
                                    <i class='bx bx-heart'></i>
                                </vs-button>
                                <vs-button class="btn-chat" shadow primary>
                                    <i class='bx bx-chat' ></i>
                                    <span class="span">
                                        54
                                    </span>
                                </vs-button>
                            </template>
                        </vs-card> -->
                    </v-col>
                </v-row>
                <v-pagination
                    v-model="currentPage"
                    :length=pageNum
                    circle
                    @input="getPageNumber"
                />
            </v-card-text>
        </v-container>


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

        <!-- <v-dialog
            v-model="dialog"
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
        </v-dialog> -->

        <CustomerDetailDialog
            ref="customerDetailDialog"
        />
    </div>
</template>
<script>
    import CustomerDetailDialog from '@/components/account/dialog/CustomerDetailDialog'
    import dayjs from 'dayjs'
    import { mapGetters } from 'vuex'
    import HomeButton from '@/components/account/HomeButton'
    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
    import utilsMixin from '@/mixins/utils'

    export default {
        name: 'AccountCustomerItem',
        components: {
            CustomerDetailDialog,
            HomeButton,
            AccountPageTitleArea,
        },
        props: {
        },
        data: () => ({
            rules: {
                required: val => !!val || '必須項目です。',
                small: val => !!Number(val) > 0 || '正しい数値を入力して下さい。',
            },
            snackbar: false,
            snackbarText: '顧客情報の取得に失敗しました。',
            searchInfo: {
                customerNo: '',
                customerName: '',
            },
            searchedInfo: {
                customerNo: '',
                customerName: '',
            },
            searchLoading: false,
            searchResult: {
                results: null,
                count: 0,
                next: '',
                previous: '',
            },
            currentPage: 1,
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
            pageNum () {
                return Math.ceil(this.searchResult.count / 10)
            }
        },
        methods: {
            undo () {
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            init () {
                this.snackbar = false
                this.snackbarText = '顧客情報の取得に失敗しました。'
                this.searchInfo = {
                    customerNo: '',
                    customerName: '',
                }
                this.searchLoading = false
            },
            toHome () {
                this.init()
                this.$router.push({
                    name: 'AccountHome',
                })
            },
            search () {
                let params = {}
                if (this.searchInfo.customerName != '') {
                    params.name = this.searchInfo.customerName
                }
                if (this.searchInfo.customerNo != '') {
                    params.customer_no = this.searchInfo.customerNo
                }

                params.delete_flg = false

                this.searchLoading = true
                this.$axios({
                    method: 'get',
                    url: '/api/customer/search/',
                    params: params
                })
                .then(res => {
                    this.searchedInfo.customerNo = this.searchInfo.customerNo
                    this.searchedInfo.customerName = this.searchInfo.customerName
                    this.searchLoading = false
                    this.searchResult = res.data
                    console.log(res)
                })
                .catch(e => {
                    this.searchLoading = false
                    this.snackbar = true
                    console.log(e)
                })
            },
            getPageNumber (pageNumber) {
                let params = {}
                // const page = '?page=' + pageNumber
                // let url = '/api/customer/search/' + page
                // if (this.searchedInfo.customerNo != '') {
                //     url += '&customerNo=' + this.searchedInfo.customerNo
                // }
                // if (this.searchedInfo.customerName != '') {
                //     url += '&customerName=' + this.searchedInfo.customerName
                // }
                params.page = pageNumber
                params.customerNo = this.searchedInfo.customerNo
                params.customerName = this.searchedInfo.customerName

                this.searchLoading = true
                this.$axios({
                    method: 'get',
                    url: '/api/customer/search/',
                    params: params
                })
                .then(res => {
                    this.searchLoading = false
                    this.searchResult = res.data
                    console.log(res)
                })
                .catch(e => {
                    this.searchLoading = false
                    this.snackbar = true
                    console.log(e)
                })
            },
            showCustomerDetail (item) {
                this.$refs.customerDetailDialog.open(item)
            }
        },
        mixins: [
            utilsMixin,
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
</style>
