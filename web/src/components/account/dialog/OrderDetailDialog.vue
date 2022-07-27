<template>
    <vs-dialog
        v-model="dialog"
    >
        <v-card
            class="pt-3"
            flat
        >
            <!-- <v-toolbar dark>
                <v-btn
                    icon
                    @click="dialog = false"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-toolbar>

            <v-divider/> -->

            <v-card-title>
                注文情報
            </v-card-title>

            <v-card-text class="text-right pb-0">
                <span style="font-size: 13px; color: rgba(40, 40, 40, 0.8);">
                    伝票No: {{ salesData.header_id }}
                </span>
            </v-card-text>

            <v-card-text>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>来店日付</v-list-item-title>
                        <v-list-item-subtitle>{{ salesData.visit_time }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>滞在時間</v-list-item-title>
                        <v-list-item-subtitle>{{ stayHour }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>来店人数</v-list-item-title>
                        <v-list-item-subtitle>{{salesData.total_visitors}}人（男: {{salesData.male_visitors}}, 女: {{salesData.female_visitors}}）</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>注文数</v-list-item-title>
                        <v-list-item-subtitle>{{ salesData.sales_detail.length }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-card-text>

            <v-divider class="mx-5"/>

            <v-card-subtitle class="pb-0">
                オーダー待ち: {{ waitOrder.length }}件
            </v-card-subtitle>

            <v-card
                v-for="(item, i) in waitOrder"
                :key="i"
                class="mx-5 my-2"
                outlined
            >
                <v-card-text>
                    <label style="font-size: 12px;">商品名</label>
                    <p>{{ item.product.name }}</p>
                    <label style="font-size: 12px;">数量</label>
                    <p>{{ item.quantity }}</p>
                    <label style="font-size: 12px;">注文時間</label>
                    <p>{{ item.order_time }}</p>
                </v-card-text>
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
    </vs-dialog>
</template>

<script>
    import dayjs from 'dayjs'

    export default {
        name: 'OrderDetailDialogItem',
        props: {
        },
        data: () => ({
            dialog: false,
            salesData: null,
            // info: null,
            loading: false,
            waitOrder: [],
        }),
        computed: {
            stayHour () {
                const now = dayjs()
                const diff = now.diff(dayjs(this.salesData.visit_time), 'minute')
                const hour = Math.floor(diff / 60)
                const min = diff - (hour * 60)
                return hour + '時間' + min + '分'
            },
        },
        methods: {
            open (salesData) {
                this.waitOrder = []
                this.salesData = null
                this.loading = true
                this.salesData = salesData
                for (const item of salesData.sales_detail) {
                    if (!item.end_flg) {
                        this.waitOrder.push(item)
                    }
                }
                // this.$axios({
                //     method: 'get',
                //     url: `/api/sales/${salesData.id}/`
                // })
                // .then(res => {
                //     console.log(res)
                //     this.order = res.data
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
                this.salesData = null
                // this.info = null
                this.waitOrder = []
            },
        }
    }

</script>

<style lang="scss" scoped>
</style>
