<template>
    <div>
        <Header
            v-if="isAuth"
        />
        <v-container fluid class="px-1 py-0">
            <v-row class="mb-2 mx-1">
                <!-- <v-col
                    v-for="(item, i) in items"
                    :key="i"
                    cols="6"
                    sm="4"
                    md="3"
                    lg="2"
                    class="pb-3 px-1"
                >
                    <v-card
                        class="account-menu-card"
                        @click="toPage(item.link)"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <v-img
                            v-if="item.src != ''"
                            :src="item.src"
                            height="100px"
                        ></v-img>
                        <div class="account-menu-card-text-area pa-2">
                            {{ item.title }}
                        </div>
                    </v-card>
                </v-col> -->
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountOrderSelect')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/glass2-2.jpg" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">注文</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountOrderCheckSelect')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/account1-2.jpg" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">伝票確認</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountNewVisit')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/bar4.jpg" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">新規来店</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountBottle')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/酒4サムネ.png" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">ボトル情報照会</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountNewBottle')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/bar2.jpg" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">ボトル情報作成</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountCustomer')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <div>
                            <img src="@/static/img/data1.jpg" style="height: 100px; width: 100%;">
                        </div>
                        <div class="account-menu-card-text-area pa-2">顧客情報照会</div>
                    </v-card>
                </v-col>
                <v-col cols="6" sm="4" md="3" lg="2" class="pb-3 px-1">
                    <v-card
                        class="account-menu-card"
                        @click="toPage('AccountNewCustomer')"
                        style="background-color: rgba(200, 200, 200, 0.1);"
                    >
                        <img src="@/static/img/account3-2.jpg" style="height: 100px; width: 100%;">
                        <div class="account-menu-card-text-area pa-2">新規会員登録</div>
                    </v-card>
                </v-col>
            </v-row>


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
        </v-container>
    </div>
</template>

<script>
import Header from '@/components/account/Header'
import Sidebar from '@/components/common/Sidebar'
import Top from '@/components/page/Top'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountHomeItem',
    data: () => ({
        items: [
            {
                title: '注文',
                // src: 'http://localhost:8000/media/upload/glass2.jpg',
                src: '@/static/img/glass2.jpg',
                link: 'AccountOrderSelect',
                icon: 'bx bx-food-menu account-menu-card-icon',
            },
            {
                title: '伝票確認',
                // src: 'http://localhost:8000/media/upload/account1.jpg',
                src: '@/static/img/account1.jpg',
                link: 'AccountOrderCheckSelect',
                icon: 'bx bx-yen account-menu-card-icon',
            },
            {
                title: '新規来店',
                // src: 'http://localhost:8000/media/upload/bar4.jpg',
                src: '@/static/img/bar4.jpg',
                link: 'AccountNewVisit',
                icon: 'bx bxs-face account-menu-card-icon',
            },
            {
                title: 'ボトル情報照会',
                // src: 'http://localhost:8000/media/upload/酒2サムネ.png',
                src: '@/static/img/酒2サムネ.png',
                link: 'AccountBottle',
                icon: 'bx bxs-drink account-menu-card-icon',
            },
            {
                title: 'ボトル情報作成',
                // src: 'http://localhost:8000/media/upload/bar2.jpg',
                src: '@/static/img/bar2.jpg',
                link: 'AccountNewBottle',
                icon: 'bx bxs-drink account-menu-card-icon',
            },
            {
                title: '顧客情報照会',
                // src: 'http://localhost:8000/media/upload/data1.jpg',
                src: '@/static/img/data1.jpg',
                link: 'AccountCustomer',
                icon: 'bx bx-user account-menu-card-icon',
            },
            {
                title: '新規会員登録',
                // src: 'http://localhost:8000/media/upload/account3.jpg',
                src: '@/static/img/account3.jpg',
                link: 'AccountNewCustomer',
                icon: 'bx bx-user account-menu-card-icon',
            },
        ],
        // nonEndSalesDetail: [],
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

        // this.$axios({
        //     method: 'get',
        //     url: '/api/sales/get_non_end_sales_detail/',
        // })
        // .then(res => {
        //     console.log(res)
        //     this.nonEndSalesDetail = res.data
        // })
        // .catch(e => {
        //     console.log(e)
        // })
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
        // checkSalesDetail (item) {
        //     this.checkLoading = true
        //     this.$axios({
        //         method: 'post',
        //         url: '/api/sales/end_sales_detail/',
        //         data: {
        //             sales_detail_id: item.id
        //         }
        //     })
        //     .then(res => {
        //         console.log(res)
        //         this.nonEndSalesDetail = res.data
        //         this.checkLoading = false
        //         // this.snackbarText = 'データの更新に成功しました。'
        //         // this.snackbar = true
        //     })
        //     .catch(e => {
        //         console.log(e)
        //         this.checkLoading = false
        //         this.snackbarText = 'データの更新に失敗しました。'
        //         this.snackbar = true
        //     })
        // }
        imgSrc (item) {
            // const path = '@/static/img/glass2.jpg'
            const path = item.src
            // require([path], function (res) {
            //     return res
            // })

            let result = require("localhost:8080" + path)
            return result
            // return '@/static/img/glass2.jpg'
            // return require('@/static/img/glass2.jpg')
            // return require(item.src)
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
            font-size: 13px;
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
