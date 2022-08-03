<template>
    <v-card
        dark
        color="#385F73"
    >
        <v-row>
            <v-col
                cols="5"
            >
                <v-subheader>
                    商品名
                </v-subheader>
                <v-card-title>
                    {{ item.product.name }}
                </v-card-title>
            </v-col>
            <v-col cols="2">
                <v-subheader>
                    数量
                </v-subheader>
                <v-card-title>
                    {{ item.quantity }}
                </v-card-title>
            </v-col>
            <v-col cols="2">
                <v-subheader>
                    席
                </v-subheader>
                <v-card-title>
                    {{ item.disp_seat_name }}
                </v-card-title>
            </v-col>
            <v-col cols="2">
                <v-subheader>
                    待ち時間
                </v-subheader>
                <v-card-subtitle>
                    {{ getWaitTime(item.order_time) }}
                </v-card-subtitle>
            </v-col>
            <v-col cols="1" class="ma-0 pa-0">
                <div
                    class="card_order_ok_btn"
                    @click="orderDone(item)"
                >
                    OK
                </div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters } from 'vuex'

export default {
    name: 'CalcStayHourItem',
    props: {
        item: {
            type: Object,
            required: true,
        },
    },
    data: () => ({
    }),
    computed: {
    },
    methods: {
    }
}

</script>

<style lang="scss" scoped>
</style>
