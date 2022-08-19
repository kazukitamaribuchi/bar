<template>
    <v-dialog
        v-model="dialog"
        fullscreen
        persistent
    >
        <v-card
            flat
        >
            <v-toolbar
                dark
                color="primary"
            >
                <v-btn
                    icon
                    dark
                    @click="close"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>ボトル選択</v-toolbar-title>
                <!-- <v-spacer></v-spacer>
                <v-toolbar-items>
                    <v-btn
                        dark
                        text
                        @click="dialog = false"
                    >
                        Save
                    </v-btn>
                </v-toolbar-items> -->
            </v-toolbar>
            <!-- <div
                class="text-subtitle-1 text-center"
                style="height: 40px;"
            >
                ボトル選択
            </div> -->
            <!-- <v-subheader>
                ボトル選択
            </v-subheader> -->

            <v-subheader
                class="pt-5"
            >
                カテゴリ
            </v-subheader>

            <BottleCategoryFilter
                @bottleCategoryFilter="bottleCategoryFilter"
            />

            <v-subheader
                class="pt-5"
            >
                商品名
            </v-subheader>

            <KanaFilterBtn
                @kanaFilter="kanaFilter"
            />

            <v-divider
                class="mt-5"
            />

            <v-subheader
                style="height: 30px;"
            >
                商品一覧 <v-spacer/> {{ filterItems.length }}件
            </v-subheader>
            <v-subheader
                class="mt-3 ml-2"
                style="font-size: 12px;"
            >
                カテゴリ: {{ filterCategory }}<br>
                商品名: {{ filterProductName }}
            </v-subheader>

            <BottleProductList
                :items=filterItems
                :selectedBottle=item
                @selectBottle="selectBottle"
            />
        </v-card>
    </v-dialog>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters } from 'vuex'
import BottleCategoryFilter from '@/components/account/parts/BottleCategoryFilter'
import BottleProductList from '@/components/account/BottleProductList'
import KanaFilterBtn from '@/components/account/parts/KanaFilterBtn'
import _ from 'lodash'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'BottleSelectDialogItem',
    components: {
        BottleCategoryFilter,
        BottleProductList,
        KanaFilterBtn,
    },
    props: {
    },
    data: () => ({
        dialog: false,
        item: null,
        items: [],
        items0: [],
        items1: [],
        items2: [],
        items3: [],
        filterItems: [],
        displayKeyNo: null,
        displayProductKeyNo: 10,
        idx: null,
    }),
    created () {
    },
    computed: {
        ...mapGetters([
            'product',
            'popularProduct',
            'productByCategory',
        ]),
        filterCategory () {
            let res = 'All'
            switch (this.displayKeyNo) {
                case 0:
                    res = 'シャンパン'
                    break
                case 1:
                    res = 'ウイスキー'
                    break
                case 2:
                    res = '焼酎'
                    break
                case 3:
                    res = 'ワイン'
                    break
                default:
            }
            return res
        },
        filterProductName () {
            return Con.KANA_FILTER_VAL_ALL[this.displayProductKeyNo] + '行'
        }
    },
    methods: {
        init () {
            this.item = null
            this.items = []
            this.items0 = []
            this.items1 = []
            this.items2 = []
            this.items3 = []
            this.filterItems = []
            this.displayKeyNo = null
            this.displayProductKeyNo = 10
            this.idx = null
        },
        open (item, idx) {
            this.dialog = true
            this.item = item
            this.index = idx
            const items0 = this.productByCategory[1][0][0]
            const items1 = this.productByCategory[1][0][1]
            const items2 = this.productByCategory[1][0][2]
            const items3 = this.productByCategory[1][0][3]
            this.items = items0.concat(items1, items2, items3)
            this.items0 = items0
            this.items1 = items1
            this.items2 = items2
            this.items3 = items3
            this.filterItems = _.cloneDeep(this.items)
        },
        close () {
            this.init()
            this.dialog = false
        },
        deleteSalesDetail () {
            this.$emit('deleteSalesDetail', this.item, this.index)
            this.close()
        },
        bottleCategoryFilter (key) {
            let items
            switch (key) {
                case 0:
                    this.displayKeyNo = 0
                    items = this.items0
                    break
                case 1:
                    this.displayKeyNo = 1
                    items = this.items1
                    break
                case 2:
                    this.displayKeyNo = 2
                    items = this.items2
                    break
                case 3:
                    this.displayKeyNo = 3
                    items = this.items3
                    break
                default:
                    this.displayKeyNo = null
                    items = this.items
                    break
            }
            this.displayProductKeyNo = 10
            this.filterItems = items
        },
        kanaFilter (key) {
            this.displayProductKeyNo = key
            if (key == 10) {
                if (this.displayKeyNo == null) {
                    this.filterItems = this.items
                } else {
                    this.filterItems = eval('this.items' + this.displayKeyNo)
                }
            } else {
                if (this.displayKeyNo == null) {
                    this.filterItems = _.cloneDeep(this.items).filter(item => item.filter_key == key)
                } else {
                    let targetArray = eval('this.items' + this.displayKeyNo)
                    this.filterItems = _.cloneDeep(targetArray).filter(item => item.filter_key == key)
                }
            }
        },
        selectBottle (item) {
            this.$emit('selectBottle', item)
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
