<template>
    <!-- background-color: rgba(244, 243, 243, 0.5); -->
    <v-row
        style="height: 70px; margin-bottom: 6px;"
    >
        <v-col
            cols="3"
            class="pa-0 menu-area"
            style="border-right: 1px solid rgba(200, 200, 200, 0.5);"
            @click="toHome"
        >
            <p class="text-center menu-text">
                ホーム
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            style="border-right: 1px solid rgba(200, 200, 200, 0.5);"
            @click="showCustomerDetail"
        >
            <p class="text-center menu-text">
                顧客情報
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            style="border-right: 1px solid rgba(200, 200, 200, 0.5);"
            @click="toAccountOrderCheck"
        >
            <p class="text-center menu-text">
                注文情報
            </p>
        </v-col>
        <v-col
            cols="3"
            class="pa-0 menu-area"
            @click="toEditSalesHeader"
        >
            <p class="text-center menu-text">
                席情報
            </p>
        </v-col>
    </v-row>
</template>

<script>

import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'ProductCategoryItem',
    data: () => ({
        headerInfo: null,
    }),
    components: {
    },
    created () {
        this.$axios({
            method: 'get',
            url: `/api/sales/${this.$route.params.id}/`
        })
        .then(res => {
            console.log(res)
            this.headerInfo = res.data
        })
        .catch(e => {
            console.log(e)
        })
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
        toHome () {
            this.$router.push({
                name: 'AccountHome'
            })
        },
        showCustomerDetail () {
        },
        toAccountOrderCheck () {
        },
        toEditSalesHeader () {
        }
    }
}
</script>

<style lang="scss" scoped>
    .menu-text {
        font-size: 12px;
        padding-top: 25px;
    }

    .menu-area {
        cursor: pointer;
    }
</style>
