<template>
    <div>
        <b-card-sub-title class="mb-4">
            商品を選択してください
        </b-card-sub-title>
        <b-card-title>
            {{ categoryTitle }}
        </b-card-title>
        <b-list-group horizontal>
            <b-list-group-item
                v-for="(item, id) in alcoholHeader"
                :key=id
                button
                variant="dark"
                class="header_menu"
                @click="filterBottleCategory(item)"
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
    name: 'AddBottleDialogHeaderItem',
    props: {
    },
    data: () => ({
        alcoholHeader: Con.INPUT_SALES_DETAIL_PRODUCT_ALCOHOL_HEADER,
        selected: 0,
    }),
    computed: {
        ...mapGetters([
            'productByCategory',
        ]),
        categoryTitle () {
            return this.alcoholHeader[this.selected].text
        },
    },
    methods: {
        filterBottleCategory (item) {
            this.selected = item.smallCategory
            // this.$eventHub.$emit('filterBottleCategory', item)
            const large = item.largeCategory
            const middle = item.middleCategory
            const small = item.smallCategory
            const res = this.productByCategory[large][middle][small]
            this.$emit('update', res)
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
