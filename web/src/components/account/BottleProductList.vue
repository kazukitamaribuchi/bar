<template>
    <v-container fluid>
        <v-row class="bottle_product_list_wrap">
            <v-col cols="12" v-if="items.length == 0">
                <p class="bottle_product_name ma-0 pa-0">
                    対象のボトルは存在しません。
                </p>
            </v-col>
            <v-col
                cols="12"
                md="6"
                v-for="(item, i) in items"
                :key="i"
                class="bottle_product_area"
            >
                <!-- <div
                    class="bottle_product"
                >
                    {{ item.name }}
                </div> -->
                <v-row
                    align="center"
                    class="py-3"
                    :class="{'selected': isSelectedBottle(item)}"
                >
                    <v-col
                        cols="2"
                        class="pa-0"
                    >
                        <v-badge
                            bordered
                            color="success"
                            icon="mdi-check"
                            overlap
                            :value=isSelectedBottle(item)
                        >
                            <v-avatar
                                size="50px"
                            >
                                <!-- <img
                                    alt="Avatar"
                                    src="http://localhost:8000/media/upload/酒6.png"
                                > -->
                                <img
                                    v-if="item.thumbnail != null"
                                    :src="getImgLink(item.thumbnail)"
                                >
                                <img
                                    v-else
                                    src="@/static/img/noimage8.png"
                                >
                            </v-avatar>
                        </v-badge>
                    </v-col>
                    <v-col
                        cols="8"
                        class="pa-0"
                    >
                        <p class="bottle_product_name ma-0 pa-0">
                            {{ item.name }}
                        </p>
                    </v-col>
                    <v-col
                        cols="2"
                        class="pa-0"
                    >
                        <vs-button
                            icon
                            relief
                            success
                            animation-type="rotate"
                            style="height: 30px;"
                            @click="selectBottle(item)"
                        >
                            <i class='bx bx-check'></i>
                            <template #animate >
                                <i class='bx bx-check'></i>
                            </template>
                        </vs-button>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

import { mapGetters } from 'vuex'
import utilsMixin from '@/mixins/utils'

export default {
    name: 'BottleProductListItem',
    props: {
        items: {
            type: Array,
            required: true,
        },
        selectedBottle: {
            type: Object,
            required: false,
            default: null,
        }
    },
    data: () => ({
    }),
    created () {
        console.log('this.items', this.items)
    },
    computed: {
        ...mapGetters([
        ]),
    },
    methods: {
        selectBottle (item) {
            this.$emit('selectBottle', item)
        },
        isSelectedBottle (item) {
            if (this.selectedBottle == null) {
                return false
            }
            if (item.id == this.selectedBottle.id) {
                return true
            }
            return false
        }
    },
    mixins: [
        utilsMixin,
    ]
}

</script>

<style lang="scss" scoped>
    .bottle_product_name {
        font-size: 13px;
        color: rgba(100, 100, 100, 0.8);
    }

    .selected {
        box-shadow: 2px 3px 3px 2px rgba(166,166,166,0.5);
    }
</style>
