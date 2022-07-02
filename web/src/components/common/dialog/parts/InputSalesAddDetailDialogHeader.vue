<template>
    <div>
        <b-card-title>
            {{ categoryTitle }}
        </b-card-title>
        <b-list-group horizontal>
            <b-list-group-item
                v-for="(item, id) in categoryList"
                :key=id
                button
                variant="dark"
                class="header_menu"
                @click="filterProductCategory(item)"
            >
                {{ item.text }}
            </b-list-group-item>
        </b-list-group>
    </div>
</template>

<script>
import { Const } from '@/assets/js/const'
import _ from 'lodash'
const Con = new Const()
import { mapGetters } from 'vuex'

export default {
    name: 'ListViewItem',
    props: {
        productType: {
            type: Number,
            required: true,
            default: 0,
        },
    },
    data: () => ({
        alcoholHeader: Con.INPUT_SALES_DETAIL_PRODUCT_ALCOHOL_HEADER,
        nonAlcoholHeader: Con.INPUT_SALES_DETAIL_PRODUCT_NON_ALCOHOL_HEADER,
        softDrinkHeader: Con.INPUT_SALES_DETAIL_PRODUCT_SOFTDRINK_HEADER,

        mainHeader: Con.INPUT_SALES_DETAIL_PRODUCT_MAIN_HEADER,
        saradaHeader: Con.INPUT_SALES_DETAIL_PRODUCT_SARADA_HEADER,
        zensaiHeader: Con.INPUT_SALES_DETAIL_PRODUCT_ZENSAI_HEADER,
        agemonoHeader: Con.INPUT_SALES_DETAIL_PRODUCT_AGEMONO_HEADER,
        suimonoHeader: Con.INPUT_SALES_DETAIL_PRODUCT_SUIMONO_HEADER,

        categoryTitleList: Con.INPUT_SALES_DETAIL_PRODUCT_CATEGORY_LIST,
    }),
    computed: {
        ...mapGetters([
            'productByCategory',
        ]),
        categoryTitle () {
            return this.categoryTitleList[this.productType]
        },
        categoryList () {
            switch (this.productType) {
                case 0:
                    return this.alcoholHeader
                case 1:
                    return this.nonAlcoholHeader
                case 2:
                    return this.softDrinkHeader
                case 3:
                    return this.mainHeader
                case 4:
                    return this.saradaHeader
                case 5:
                    return this.zensaiHeader
                case 6:
                    return this.agemonoHeader
                case 7:
                    return this.suimonoHeader
                default:
                    return []
            }
        }
    },
    methods: {
        filterProductCategory (item) {
            // this.$eventHub.$emit('filterProductCategory', item)
            const large = item.largeCategory
            const middle = item.middleCategory
            const small = item.smallCategory
            const res = this.productByCategory[large][middle][small]
            // this.productByCategoryList = _.cloneDeep(res)
            this.$emit('update', _.cloneDeep(res))
        }
    }
}

</script>

<style lang="scss" scoped>
    .header_menu {
        color: white;
        background-color: rgba(70, 70, 70, 0.7);
        text-align: center;
        border: 1px solid white;

        // ぼこっと出す？
        // border: 1px solid #838383;
        // box-shadow: 1px 1px 1px rgba(101, 101, 101, 0.7);
    }
</style>
