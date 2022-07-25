<template>
    <v-row class="pa-2">
        <!-- <div>
            <i
                @click="undo"
                class='bx bx-undo undo-btn'
            ></i>
        </div>
        <p class="text-center" style="font-size: 13px;">
            商品カテゴリ
        </p> -->
        <v-col
            cols="4"
            class="px-1"
            v-for="(item, i) in items"
            :key="i"
        >
            <v-card
                class="pt-4"
                style="cursor: pointer;"
                @click="toProductDetail(item)"
            >
                <v-img
                    class="white--text align-end"
                    height="80px"
                    :src="item.src"
                    contain
                >
                <!-- src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" -->
                </v-img>
                <v-card-text
                    class="text-center pa-2"
                    style="font-size: 12px;"
                >
                    {{ item.title }}
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>

import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'ProductCategoryItem',
    data: () => ({
        items: [
            {
                title: 'シャンパン1',
                src: 'http://localhost:8000/media/upload/シャンパン1.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 0,
            },
            {
                title: 'シャンパン2',
                src: 'http://localhost:8000/media/upload/酒2.png',
                large_category: 1,
                middle_category: 0,
                small_category: 1,
            },
            {
                title: 'ウイスキー',
                src: 'http://localhost:8000/media/upload/ウイスキー1.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 2,
            },
            {
                title: '焼酎',
                src: 'http://localhost:8000/media/upload/焼酎2.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 3,
            },
            {
                title: 'ワイン',
                src: 'http://localhost:8000/media/upload/ワイン1.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 4,
            },
            {
                title: 'ドリンク',
                src: 'http://localhost:8000/media/upload/ショットドリンク2.jpg',
                large_category: 1,
                middle_category: 0,
                small_category: 5,
            },
            {
                title: 'ノンアルコール',
                src: 'http://localhost:8000/media/upload/ノンアルコール1.jpg',
                large_category: 1,
                middle_category: 1,
                small_category: 0,
            },
            {
                title: 'ソフトドリンク',
                src: 'http://localhost:8000/media/upload/ドリンク1.jpg',
                large_category: 1,
                middle_category: 2,
                small_category: 0,
            },
            {
                title: 'メイン',
                src: 'http://localhost:8000/media/upload/寿司1.jpg',
                large_category: 2,
                middle_category: 0,
                small_category: 0,
            },
            {
                title: 'サラダ',
                src: 'http://localhost:8000/media/upload/サラダ1.jpg',
                large_category: 2,
                middle_category: 1,
                small_category: 0,
            },
            {
                title: '前菜',
                src: 'http://localhost:8000/media/upload/枝豆2.jpg',
                large_category: 2,
                middle_category: 2,
                small_category: 0,
            },
            {
                title: '揚げ物',
                src: 'http://localhost:8000/media/upload/天ぷら1.jpg',
                large_category: 2,
                middle_category: 3,
                small_category: 0,
            },
            {
                title: '吸い物、御飯物',
                src: 'http://localhost:8000/media/upload/お茶漬け1.jpg',
                large_category: 2,
                middle_category: 4,
                small_category: 0,
            },
        ]
    }),
    components: {
    },
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
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
        undo () {
            // カートに商品があったら確認メッセージ
            if (this.selectedProduct.length != 0) {
                console.log('カートの中身破棄するか確認する')
                this.initSelectedProduct()
                this.$router.push({
                    name: 'AccountOrderSelect'
                })
            } else {
                this.$router.push({
                    name: 'AccountOrderSelect'
                })
            }
        },
        toProductDetail (item) {
            this.$router.push({
                name: 'AccountProductDetail',
                params: {
                    large: item.large_category,
                    middle: item.middle_category,
                    small: item.small_category,
                }
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
    }
    .undo-btn {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
