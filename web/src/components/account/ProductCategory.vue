<template>
    <v-container fluid>
        <v-row>
            <!-- <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
                v-for="(item, i) in items"
                :key="i"
            >
                <v-card
                    class="pt-4 product_category_card"
                    @click="toProductDetail(item)"
                >
                    <img
                        class="white--text align-end"
                        :src="item.src"
                        style="height: 80px; display: block; margin: 0 auto; width: 120px;"
                    >
                    <v-card-text
                        class="text-center pa-2"
                        style="font-size: 12px;"
                    >
                        {{ item.title }}
                    </v-card-text>
                </v-card>
            </v-col> -->
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(0)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/酒4サムネ.png"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        シャンパン
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(1)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/ウイスキー1-1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        ウイスキー
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(2)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/焼酎2-1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        焼酎
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(3)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/ワイン1-1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        ワイン
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(4)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/ショットドリンク2.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        ドリンク
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(5)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/寿司1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        メイン
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(6)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/サラダ1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        サラダ
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(7)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/枝豆2-1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        一品物
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(8)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/天ぷら1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        揚げ物
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col
                class="px-1 py-1"
                xs="6"
                cols="6"
                sm="3"
                md="2"
            >
                <v-card
                    class="pt-2 product_category_card"
                    @click="toProductDetail(9)"
                >
                    <img
                        class="white--text align-end"
                        src="@/static/img/お茶漬け1.jpg"
                        style="height: 100px; display: block; margin: 0 auto; width: 100%;"
                    >
                    <v-card-text class="text-center px-2 py-1" style="font-size: 12px;">
                        吸い物、御飯物
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <AccountProductDetail
            ref="accountProductDetail"
            :headerInfo="headerInfo"
        />
    </v-container>
</template>

<script>


import AccountProductDetail from '@/components/page/account/AccountProductDetail'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'ProductCategoryItem',
    props: {
        headerInfo: {
            type: Object,
            required: false,
        }
    },
    data: () => ({
        items: [
            {
                title: 'シャンパン',
                // src: 'http://localhost:8000/media/upload/酒2.png',
                src: '@/static/img/酒2.png',
                large_category: 1,
                middle_category: 0,
                small_category: 0,
            },
            // {
            //     title: 'シャンパン2',
            //     src: 'http://localhost:8000/media/upload/酒2.png',
            //     large_category: 1,
            //     middle_category: 0,
            //     small_category: 1,
            // },
            {
                title: 'ウイスキー',
                // src: 'http://localhost:8000/media/upload/ウイスキー1.jpg',
                src: '@/static/img/ウイスキー1.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 1,
            },
            {
                title: '焼酎',
                // src: 'http://localhost:8000/media/upload/焼酎2.jpg',
                src: '@/static/img/焼酎2.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 2,
            },
            {
                title: 'ワイン',
                // src: 'http://localhost:8000/media/upload/ワイン1.jpg',
                src: '@/static/img/ワイン1.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 3,
            },
            {
                title: 'ドリンク',
                // src: 'http://localhost:8000/media/upload/ショットドリンク2.jpg',
                src: '@/static/img/ショットドリンク2.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 4,
            },
            // {
            //     title: 'ノンアルコール',
            //     src: 'http://localhost:8000/media/upload/ノンアルコール1.jpg',
            //     large_category: 1,
            //     middle_category: 1,
            //     small_category: 0,
            // },
            // {
            //     title: 'ソフトドリンク',
            //     src: 'http://localhost:8000/media/upload/ドリンク1.jpg',
            //     large_category: 1,
            //     middle_category: 2,
            //     small_category: 0,
            // },
            {
                title: 'メイン',
                // src: 'http://localhost:8000/media/upload/寿司1.jpg',
                src: '@/static/img/寿司1.jpg',
                large_category: 2,
                middle_category: 0,
                small_category: 0,
            },
            {
                title: 'サラダ',
                // src: 'http://localhost:8000/media/upload/サラダ1.jpg',
                src: '@/static/img/サラダ1.jpg',
                large_category: 2,
                middle_category: 1,
                small_category: 0,
            },
            {
                title: '一品物',
                // src: 'http://localhost:8000/media/upload/枝豆2.jpg',
                src: '@/static/img/枝豆2.jpg',
                large_category: 2,
                middle_category: 2,
                small_category: 0,
            },
            {
                title: '揚げ物',
                // src: 'http://localhost:8000/media/upload/天ぷら1.jpg',
                src: '@/static/img/天ぷら1.jpg',
                large_category: 2,
                middle_category: 3,
                small_category: 0,
            },
            {
                title: '吸い物、御飯物',
                // src: 'http://localhost:8000/media/upload/お茶漬け1.jpg',
                src: '@/static/img/お茶漬け1.jpg',
                large_category: 2,
                middle_category: 4,
                small_category: 0,
            },
        ]
    }),
    components: {
        AccountProductDetail
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
    },
    created () {
    },
    methods: {
        ...mapMutations([
            'initSelectedProduct',
        ]),
        ...mapActions([
        ]),
        toNewVisit () {
            this.$router.push({
                name: 'AccountNewVisit'
            })
        },
        toProductDetail (idx) {
            const item = this.items[idx]
            console.log('toProductDetail', item)
            this.$refs.accountProductDetail.open(item)



            // console.log('toProductDetail', item)
            // this.$refs.accountProductDetail.open(item)

            // this.$router.push({
            //     name: 'AccountProductDetail',
            //     params: {
            //         large: item.large_category,
            //         middle: item.middle_category,
            //         small: item.small_category,
            //     }
            // })
        },
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
    }

    .product_category_card {
        cursor: pointer;

    }
</style>
