<template>
    <v-dialog
        v-model="dialog"
    >
        <v-card class="pt-3">
            <v-toolbar dark>
                <v-btn
                    icon
                    @click="dialog = false"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-toolbar>

            <v-divider/>

            <v-card-title>
                席情報
            </v-card-title>

            <v-card-text>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>来店時間</v-list-item-title>
                        <v-list-item-subtitle>{{ salesData.visit_time }}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-content>
                        <v-list-item-title>滞在時間</v-list-item-title>
                        <v-list-item-subtitle>{{ stayHour }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item class="mt-3">
                    <v-select
                      :items="seat"
                      item-text="seat_name"
                      item-value="id"
                      label="座席"
                      dense
                      outlined
                      v-model="seatId"
                    >
                        <template v-slot:prepend-item>
                            <v-list-item ripple @click="toggle">
                                <v-list-item-content>
                                    <v-list-item-title>
                                        指定無し
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </template>
                    </v-select>
                </v-list-item>

                <v-list-item class="mt-3">
                    <v-select
                      :items="basicPlanTypeList"
                      item-text="name"
                      item-value="id"
                      label="基本料金"
                      dense
                      outlined
                      v-model="basicPlanType"
                    ></v-select>
                </v-list-item>

                <v-list-item>
                    <v-row>
                        <v-col cols="6" class="pt-0">
                            <label style="font-size:12px;">男性客数</label>
                            <b-form-spinbutton
                                inline
                                v-model="salesData.male_visitors"
                                min="0"
                                size="lg"
                            ></b-form-spinbutton>
                        </v-col>
                        <v-col cols="6" class="pt-0">
                            <label style="font-size:12px;">女性客数</label>
                            <b-form-spinbutton
                                inline
                                v-model="salesData.female_visitors"
                                min="0"
                                size="lg"
                            ></b-form-spinbutton>
                        </v-col>
                    </v-row>
                </v-list-item>

                <v-list-item style="margin-top: 30px;">
                    <v-textarea
                        label="備考"
                        auto-grow
                        outlined
                        rows="2"
                        row-height="20"
                        v-model="salesData.remarks"
                    ></v-textarea>
                </v-list-item>

            </v-card-text>
            <v-card-actions>
                <v-row class="ma-0">
                    <v-col class="ma-0">
                        <v-btn
                            block
                            color="blue-grey"
                            @click="dialog = false"
                            dark
                        >
                            閉じる
                        </v-btn>
                    </v-col>
                    <v-col class="ma-0">
                        <v-btn
                            block
                            color="primary"
                            depressed
                            @click="update"
                            :loading="updateLoading"
                        >更新</v-btn>
                    </v-col>
                </v-row>
            </v-card-actions>
        </v-card>

        <v-snackbar
            v-model="snackbar"
            timeout="2000"
        >
            データの更新に失敗しました。
            <template v-slot:action="{ attrs }">
                <v-btn
                    color="pink"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >Close</v-btn>
            </template>
        </v-snackbar>

        <v-dialog
            v-model="successDialog"
        >
            <v-card>
                <v-card-title>
                    データの更新に成功しました。
                </v-card-title>
                <v-card-actions>
                    <v-btn
                        color="green darken-1"
                        text
                        @click="init"
                    >
                        OK
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-dialog>
</template>

<script>
    import dayjs from 'dayjs'
    import { mapGetters } from 'vuex'

    export default {
        name: 'SeatDetailDialogItem',
        props: {
        },
        data: () => ({
            dialog: false,
            salesData: null,
            // info: null,
            loading: false,
            basicPlanTypeList: [
                {
                    name: '通常料金(1時間)',
                    id: 1,
                },
                {
                    name: '通常料金(2時間)',
                    id: 2,
                },
                {
                    name: '通常料金(3時間)',
                    id: 3,
                },
                {
                    name: '貸切料金(1時間)',
                    id: 4,
                },
                {
                    name: '貸切料金(2時間)',
                    id: 5,
                },
                {
                    name: '貸切料金(3時間)',
                    id: 6,
                },
            ],
            basicPlanType: 0,
            updateLoading: false,
            seatId: null,
            snackbar: false,
            successDialog: false,
        }),
        computed: {
            ...mapGetters([
                'seat'
            ]),
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
                this.loading = true
                this.salesData = salesData
                this.basicPlanType = salesData.basic_plan_type.id
                this.seatId = salesData.seat.id
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
            },
            update () {
                this.updateLoading = true
                const data = this.salesData
                data.basic_plan_type_id = this.basicPlanType
                data.seat_id = this.seatId
                console.log('data', data)
                this.$axios({
                    method: 'put',
                    url: '/api/sales/update_sales_header/',
                    data: data
                })
                .then(res => {
                    console.log(res)
                    this.salesData = res.data
                    this.$emit('updateSalesData', res.data)
                    this.successDialog = true
                    this.updateLoading = false
                    // this.init()
                })
                .catch(e => {
                    this.updateLoading = false
                    this.snackbar = true
                    console.log(e)
                })
            },
            init () {
                this.basicPlanType = 0
                this.seatId = null
                this.dialog = false
                this.snackbar = false
                this.successDialog = false
            },
            toggle () {
                this.$nextTick(() => {
                    this.seatId = null
                })
            },
        }
    }

</script>

<style lang="scss" scoped>
</style>
