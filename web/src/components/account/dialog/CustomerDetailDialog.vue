<template>
    <v-dialog
        v-model="dialog"
        fullscreen
        persistent
    >
        <v-card
            class="pt-3"
            flat
            v-if="customer != null"
        >

            <v-toolbar
                dark
                color="primary"
            >
                <v-btn
                    dark
                    icon
                    @click="dialog = false"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>顧客情報</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>

            <!-- <v-divider/> -->

            <!-- <v-card-title>
                顧客情報
            </v-card-title> -->

            <!-- <v-divider/> -->

            <v-card-text class="text-right pb-0">
                <span style="font-size: 13px; color: rgba(40, 40, 40, 0.8);">
                    会員No: {{ customer.customer_no }}
                </span>
            </v-card-text>

            <v-card-text>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>顧客名</v-list-item-subtitle>
                        <v-list-item-title>{{ customer.name }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>年齢</v-list-item-subtitle>
                        <v-list-item-title>{{ customer.age }}歳</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-content>
                        <v-list-item-subtitle>誕生日</v-list-item-subtitle>
                        <v-list-item-title>{{ customer.birthday }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>ランク</v-list-item-subtitle>
                        <v-list-item-title>{{ customer.rank_name }}</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-content>
                        <v-list-item-subtitle>初来店日</v-list-item-subtitle>
                        <v-list-item-title>{{ customer.first_visit }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>総売上</v-list-item-subtitle>
                        <v-list-item-title><i class='bx bx-yen'></i>{{ customer.total_sales | priceLocaleString }}</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-content>
                        <v-list-item-subtitle>要注意人物</v-list-item-subtitle>
                        <v-list-item-title v-if="customer.caution_flg">要注意</v-list-item-title>
                        <v-list-item-title v-else>-</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-card-text>

            <v-divider class="mx-5 my-2"/>

            <div class="text-caption text-right pr-4">
                所有ボトル {{ customer.bottle.length }}件
            </div>

            <v-card
                v-for="(b, i) in customer.bottle"
                :key="i"
                flat
                class="pa-2"
            >
                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-subtitle>商品名</v-list-item-subtitle>
                        <v-list-item-title class="sales_header_info_content pl-1">{{ b.product.name }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item two-line>
                    <v-list-item-content>
                        <v-list-item-subtitle>開封日</v-list-item-subtitle>
                        <v-list-item-title class="sales_header_info_content pl-1">{{ b.open_date }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-divider class="mx-5 my-2"/>

            </v-card>

            <v-card-actions>
                <v-btn
                    block
                    depressed
                    outlined
                    color="indigo"
                    @click="dialog = false"
                >閉じる</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>

    export default {
        name: 'CustomerDetailDialogItem',
        props: {
        },
        data: () => ({
            dialog: false,
            customer: null,
            // info: null,
            loading: false,
        }),
        computed: {
        },
        methods: {
            open (customer) {
                // this.loading = true
                this.customer = customer
                // this.$axios({
                //     method: 'get',
                //     url: `/api/customer/${customer.id}/`
                // })
                // .then(res => {
                //     console.log(res)
                //     this.info = res.data
                //     this.loading = false
                // })
                // .catch(e => {
                //     console.log(e)
                //     this.loading = false
                // })
                this.dialog = true
            },
            close () {
                this.dialog = false
                this.customer = null
                // this.info = null
            },
        }
    }

</script>

<style lang="scss" scoped>
</style>
