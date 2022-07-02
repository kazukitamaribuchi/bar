<template>
    <div>
        <v-card-title>
            メニュー
        </v-card-title>
        <v-row>
            <v-col
                v-for="(item, i) in items"
                :key="i"
                cols="3"
                class="pa-1"
            >
                <v-card
                    class="account-menu-card"
                    @click="toPage(item.link)"
                    flat
                >
                    <div class="account-menu-card-img-area">
                        <i
                            :class="item.icon"
                        ></i>
                        <!-- <v-img
                            :src="item.src"
                            class="account-menu-card-img"
                        ></v-img> -->
                    </div>
                    <div class="account-menu-card-text-area">
                        <v-card-title class="card-title">
                            {{ item.title }}
                        </v-card-title>
                    </div>
                </v-card>
            </v-col>
        </v-row>
        <v-card
            flat
        >
            <v-card-title>
                オーダー待ち状況
            </v-card-title>
            <v-card-text>
                オーダー待ち無し
            </v-card-text>
        </v-card>
        <v-card
            flat
        >
            <v-card-title>
                来店状況
            </v-card-title>
            <v-card-text>
                無し
            </v-card-text>
        </v-card>
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
                src: 'http://localhost:8000/media/upload/オーダー2.jpg',
                link: 'AccountOrderSelect',
                icon: 'bx bx-food-menu account-menu-card-icon',
            },
            {
                title: '注文確認',
                src: 'http://localhost:8000/media/upload/伝票1.jpg',
                link: 'AccountOrderCheckSelect',
                icon: 'bx bx-yen account-menu-card-icon',
            },
            {
                title: '新規入店',
                src: 'http://localhost:8000/media/upload/男性2.jpg',
                link: 'AccountNewVisit',
                icon: 'bx bxs-face account-menu-card-icon',
            },
            {
                title: 'ボトル',
                src: 'http://localhost:8000/media/upload/酒9.png',
                link: 'AccountBottle',
                icon: 'bx bxs-drink account-menu-card-icon',
            },
            {
                title: '顧客情報',
                src: 'http://localhost:8000/media/upload/男性3.jpg',
                link: 'AccountCustomer',
                icon: 'bx bx-user account-menu-card-icon',
            },
        ]
    }),
    components: {
        Header,
        Sidebar,
        Top
    },
    created () {
    },
    computed: {
        ...mapGetters([
        ])
    },
    methods: {
        ...mapMutations([
        ]),
        ...mapActions([
        ]),
        toPage (link) {
            this.$router.push({
                name: link,
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    .account-menu-card {
        height: 120px;
        cursor: pointer;

        text-align: center;

        .account-menu-card-img-area {
            height: 60px;
            // text-align: center;
            padding-top: 20px;
            .account-menu-card-img {
                border-radius: 50%;
                margin: 0 auto;
                height: 40px;
                width: 40px;
            }
            .account-menu-card-icon {
                font-size: 40px;

            }
        }

        .account-menu-card-text-area {
            text-align: center;
            height: 30px;
            .card-title {
                font-size: 14px;
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
</style>
