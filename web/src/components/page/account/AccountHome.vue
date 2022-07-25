<template>
    <div class="pa-2">
        <v-card-title class="account_home_title">
            メニュー
        </v-card-title>
        <v-row class="mb-2 mx-1">
            <v-col
                v-for="(item, i) in items"
                :key="i"
                cols="6"
                class="pa-1"
            >
                <v-card
                    class="account-menu-card"
                    flat
                    @click="toPage(item.link)"
                    style="background-color: rgba(200, 200, 200, 0.1);"
                >
                    <v-img
                        v-if="item.src != ''"
                        :src="item.src"
                        height="100px"
                    ></v-img>
                    <div
                        v-else
                        class="account-menu-card-img-area"
                    >
                        <i
                            style="position: relative; top: 23px;"
                            :class="item.icon"
                        ></i>
                    </div>
                    <!-- <div class="account-menu-card-img-area">
                        <v-img
                            v-if="item.src != ''"
                            :src="item.src"
                            contain
                            height="80px"
                            class="account-menu-card-img"
                        ></v-img>
                        <i
                            v-else
                            style="position: relative; top: 23px;"
                            :class="item.icon"
                        ></i>
                    </div> -->
                    <div class="account-menu-card-text-area pa-2">
                        <v-card-text class="card-title text-center">
                            {{ item.title }}
                        </v-card-text>
                    </div>
                </v-card>
            </v-col>
        </v-row>
        <v-card
            flat
        >
            <v-card-title class="account_home_title">
                オーダー待ち状況
            </v-card-title>
            <v-row
                v-if="nonEndSalesDetail.length != 0"
                class="mb-1 mx-1"
            >
                <v-col
                    v-for="(item, i) in nonEndSalesDetail"
                    :key="i"
                    cols="12"
                    class="py-1 mx-0 px-0"
                >
                    <v-card
                        class="pt-4"
                    >
                        <v-row style="max-width: 100%; margin: 0 auto;">
                            <v-col cols="3" class="pa-0">
                                <v-img
                                    v-if="item.product.thumbnail != null"
                                    class="white--text align-end"
                                    height="120px"
                                    :src="item.product.thumbnail"
                                    contain
                                >
                                </v-img>
                                <v-img
                                    v-else
                                    class="white--text align-end"
                                    height="120px"
                                    src="http://localhost:8000/media/upload/酒6.png"
                                    contain
                                >
                                </v-img>
                            </v-col>
                            <v-col cols="9" class="pa-0">
                                <div
                                    class="pl-2"
                                    style="min-height: 65px;"
                                >
                                    <label class="label-style">
                                        商品名
                                    </label>
                                    <p
                                        style="font-size: 13px; line-height: 2;"
                                        class="mb-0"
                                    >
                                        {{ item.product.name | truncate(30) }}
                                    </p>
                                </div>
                                <div style="display: flex;" class="pl-2">
                                    <div style="margin-right: 30px;">
                                        <label class="label-style">
                                            伝票No
                                        </label>
                                        <p>
                                            {{ item.header_id }}
                                        </p>
                                    </div>
                                    <div>
                                        <label class="label-style">
                                            席
                                        </label>
                                        <p>
                                            {{ item.disp_seat_name }}
                                        </p>
                                    </div>
                                </div>
                                <div style="display: flex; height: 55px;" class="pl-2">
                                    <div style="margin-right: 30px;">
                                        <label class="label-style">
                                            注文数
                                        </label>
                                        <p>
                                            {{ item.quantity }}
                                        </p>
                                    </div>
                                    <div style="margin-right: 50px;">
                                        <label class="label-style">
                                            注文時刻
                                        </label>
                                        <p>
                                            {{ item.disp_order_time }}
                                        </p>
                                    </div>
                                    <vs-button
                                        icon
                                        relief
                                        success
                                        animation-type="rotate"
                                        @click="checkSalesDetail(item)"
                                        :loading="checkLoading"
                                        style="height: 34px; margin-top: 10px;"
                                    >
                                        <i class='bx bx-check'></i>
                                        <template #animate >
                                            <i class='bx bx-check'></i>
                                        </template>
                                    </vs-button>
                                </div>
                            </v-col>
                        </v-row>

                    </v-card>
                </v-col>
            </v-row>
            <v-card-text
                v-else
            >オーダー待ち無し</v-card-text>
        </v-card>
        <!-- <v-card
            flat
        >
            <v-card-title class="account_home_title">
                来店状況
            </v-card-title>
            <v-card-text>
                無し
            </v-card-text>
        </v-card> -->

        <v-snackbar
            v-model="snackbar"
            timeout="2000"
        >
            {{ snackbarText }}
            <template v-slot:action="{ attrs }">
                <v-btn
                    color="blue"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >Close</v-btn>
            </template>
        </v-snackbar>
    </div>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'
import Top from '@/components/page/Top'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountHomeItem',
    data: () => ({
        items: [
            {
                title: 'オーダー',
                src: 'http://localhost:8000/media/upload/glass2.jpg',
                // src: '',
                link: 'AccountOrderSelect',
                icon: 'bx bx-food-menu account-menu-card-icon',
            },
            {
                title: '注文確認',
                src: 'http://localhost:8000/media/upload/account1.jpg',
                // src: '',
                link: 'AccountOrderCheckSelect',
                icon: 'bx bx-yen account-menu-card-icon',
            },
            {
                title: '新規入店',
                src: 'http://localhost:8000/media/upload/bar4.jpg',
                // src: '',
                link: 'AccountNewVisit',
                icon: 'bx bxs-face account-menu-card-icon',
            },
            {
                title: 'ボトル',
                src: 'http://localhost:8000/media/upload/酒2サムネ.png',
                // src: '',
                link: 'AccountBottle',
                icon: 'bx bxs-drink account-menu-card-icon',
            },
            {
                title: '顧客情報',
                src: 'http://localhost:8000/media/upload/data1.jpg',
                // src: '',
                link: 'AccountCustomer',
                icon: 'bx bx-user account-menu-card-icon',
            },
            {
                title: '新規会員登録',
                src: 'http://localhost:8000/media/upload/account3.jpg',
                // src: '',
                link: 'AccountNewCustomer',
                icon: 'bx bx-user account-menu-card-icon',
            },
        ],
        nonEndSalesDetail: [],
        checkLoading: false,
        snackbar: false,
        snackbarText: '',
    }),
    components: {
        Header,
        Sidebar,
        Top,
    },
    created () {
        if (!this.isAuth) {
            this.$router.push({ name: 'AccountHome' })
        }

        if (!this.initStatus) {
            this.appInitAction()
            .then(res => {
                this.setInitStatus(true)
            })
            .catch(e => {
                console.log(e)
            })
        }

        this.$axios({
            method: 'get',
            url: '/api/sales/get_non_end_sales_detail/',
        })
        .then(res => {
            console.log(res)
            this.nonEndSalesDetail = res.data
        })
        .catch(e => {
            console.log(e)
        })
    },
    computed: {
        ...mapGetters([
            'isAuth',
            'initStatus',
        ])
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
            'setInitStatus',
        ]),
        ...mapActions([
            'appInitAction',
        ]),
        toPage (link) {
            this.$router.push({
                name: link,
            })
        },
        checkSalesDetail (item) {
            this.checkLoading = true
            this.$axios({
                method: 'post',
                url: '/api/sales/end_sales_detail/',
                data: {
                    sales_detail_id: item.id
                }
            })
            .then(res => {
                console.log(res)
                this.nonEndSalesDetail = res.data
                this.checkLoading = false
                // this.snackbarText = 'データの更新に成功しました。'
                // this.snackbar = true
            })
            .catch(e => {
                console.log(e)
                this.checkLoading = false
                this.snackbarText = 'データの更新に失敗しました。'
                this.snackbar = true
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    .account-menu-card {
        // height: 120px;
        cursor: pointer;

        text-align: center;

        .account-menu-card-img-area {
            height: 80px;
            // text-align: center;
            // padding-top: 20px;
            // .account-menu-card-img {
            //     border-radius: 50%;
            //     margin: 0 auto;
            //     height: 40px;
            //     width: 40px;
            // }
            .account-menu-card-icon {
                font-size: 40px;

            }
        }

        .account-menu-card-text-area {
            text-align: center;
            // height: 30px;
            .card-title {
                font-size: 12px;
                margin-top: 0;
                padding-top: 0;
                margin-bottom: 0;
                padding-bottom: 5px;
            }
            .card-sub-title {
                font-size: 10px;
                margin-bottom: 0;
                padding-bottom: 0;
            }

        }
    }

    .account_home_title {
        font-size: 1rem;
        // font-weight: bold;
    }

    .label-style {
        font-size: 12px;
        color: rgba(70, 70, 70, 0.5);
    }
</style>
