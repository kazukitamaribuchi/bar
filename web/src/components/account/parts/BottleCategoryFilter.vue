<template>
    <v-container fluid :class="{'pa-0': paddingOff}">
        <v-row class="bottle_category_filter_btn_wrap">

            <v-col
                cols="4"
                sm="4"
                md="2"
                v-for="(item, i) in items"
                :key="i"
                class="bottle_category_filter_btn_area"
            >
                <div
                    class="bottle_category_filter_btn"
                    @click="filter(item)"
                >
                    {{ item.name }}
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
    name: 'BottleCategoryFilterItem',
    props: {
        paddingOff: {
            type: Boolean,
            required: false,
            default: false,
        }
    },
    data: () => ({
        items: [
            { name: 'シャンパン', key: 0 },
            { name: 'ウイスキー', key: 1 },
            { name: '焼酎', key: 2 },
            { name: 'ワイン', key: 3 },
            { name: 'All', key: null },
        ]
    }),
    computed: {
        ...mapGetters([
        ]),
    },
    methods: {
        filter (item) {
            this.$emit('bottleCategoryFilter', item.key)
        }
    }
}

</script>

<style lang="scss" scoped>
    .bottle_category_filter_btn_wrap {

        .bottle_category_filter_btn_area {
            height: 57px;
            padding: 0px;

            .bottle_category_filter_btn {
                cursor: pointer;
                width: 90%;
                height: 90%;
                margin: auto;
                border: 1px solid rgba(96, 96, 96, 0.5);
                border-collapse: collapse;
                // border-radius: 4px;
                box-shadow: 2px 2px 3px rgba(136, 136, 136, 0.4);
                border-radius: 20px;
                line-height: 50px;
                text-align: center;
                color: rgba(100, 100, 100, 0.9);
                font-size: 11px;
            }
        }

    }
</style>
