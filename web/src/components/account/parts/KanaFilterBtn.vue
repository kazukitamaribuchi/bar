<template>
    <v-container fluid :class="{'pa-0': paddingOff}">
        <vs-button
            circle
            icon
            @click="showFilter != showFilter"
        >
            <i class='bx bx-filter'></i>
        </vs-button>
        <v-row v-if="showFilter" class="kana_filter_btn_wrap">
            <v-col
                cols="2"
                sm="2"
                md="1"
                v-for="(item, i) in items"
                :key="i"
                class="kana_filter_btn_area"
            >
                <div
                    class="kana_filter_btn"
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
    name: 'KanaFilterBtnItem',
    props: {
        paddingOff: {
            type: Boolean,
            required: false,
            default: false,
        }
    },
    data: () => ({
        items: [
            { name: 'ア', key: 0 },
            { name: 'カ', key: 1 },
            { name: 'サ', key: 2 },
            { name: 'タ', key: 3 },
            { name: 'ナ', key: 4 },
            { name: 'ハ', key: 5 },
            { name: 'マ', key: 6 },
            { name: 'ヤ', key: 7 },
            { name: 'ラ', key: 8 },
            { name: 'ワ', key: 9 },
            { name: 'All', key: 10 },
        ],
        showFilter: false,
    }),
    computed: {
        ...mapGetters([
        ]),
    },
    methods: {
        filter (item) {
            this.$emit('kanaFilter', item.key)
        }
    }
}

</script>

<style lang="scss" scoped>
    .kana_filter_btn_wrap {

        .kana_filter_btn_area {
            height: 60px;
            // width: 50px;
            padding: 0px;
            // border: 1px solid blue;

            .kana_filter_btn {
                cursor: pointer;
                width: 90%;
                height: 90%;
                margin: auto;
                border: 1px solid rgba(96, 96, 96, 0.5);
                border-radius: 4px;
                box-shadow: 2px 1px 2px rgba(236, 236, 236, 0.4);
                line-height: 50px;
                text-align: center;
                color: rgba(100, 100, 100, 0.9);
                font-size: 13px;
            }
        }

    }

    .paddingOff {
        padding: 0;
    }
</style>
