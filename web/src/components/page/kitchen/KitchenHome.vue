<template>
    <div class="home_wrap">
        <v-card>
            <v-toolbar
                color="blue-grey darken-3"
                dark
                flat
            >
                <v-app-bar-nav-icon
                    @click.stop="drawer = !drawer"
                ></v-app-bar-nav-icon>
                    <v-tabs
                        v-model="tab"
                        centered
                    >
                        <v-tabs-slider color="yellow"></v-tabs-slider>
                        <v-tab
                            v-for="menuItem in menuItems"
                            :key="menuItem"
                        >
                            {{ menuItem }}
                        </v-tab>
                    </v-tabs>
            </v-toolbar>
        </v-card>
        <v-tabs-items
            v-model="tab"
            class="order_area_wrap"
        >
            <v-tab-item
                v-for="i in 2"
                :key="i"
            >
                <div
                    v-if="i == 1"
                    class="mx-3"
                >
                    <v-row
                    >
                        <v-col
                            v-for="(item, i) in befItems"
                            :key="i"
                            xs="12"
                            sm="12"
                            md="12"
                            lg="12"
                            class="px-1 py-1 col_order_area"
                        >
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
                        </v-col>
                    </v-row>
                </div>


                <div
                    v-else
                    class="mx-3"
                >
                    <v-row
                    >
                        <v-col
                            v-for="(item, i) in afItems"
                            :key="i"
                            xs="12"
                            sm="12"
                            md="12"
                            lg="12"
                            class="px-1 py-1 col_order_area"
                        >
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
                                        締め時間
                                    </v-subheader>
                                    <v-card-subtitle>
                                        {{ item.end_time }}
                                    </v-card-subtitle>
                                </v-col>
                                <v-col cols="1" class="ma-0 pa-0">
                                    <div
                                        class="card_order_ok_btn"
                                        @click="orderNotDone(item)"
                                    >
                                        戻す
                                    </div>
                                </v-col>
                            </v-row>
                        </v-card>
                        </v-col>
                    </v-row>
                </div>
            </v-tab-item>
        </v-tabs-items>

        <v-navigation-drawer
            v-model="drawer"
            absolute
            temporary
        >
            <v-list
                nav
                dense
            >
                <v-list-item-group
                    v-model="group"
                    active-class="deep-purple--text text--accent-4"
                >
                    <v-list-item>
                        <v-list-item-title>Foo</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-title>Bar</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-title>Fizz</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-title>Buzz</v-list-item-title>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>
<script>
    import dayjs from 'dayjs'
    import { mapGetters, mapActions, mapMutations } from 'vuex'

    export default {
        name: 'KitchenHomeItem',
        components: {
        },
        props: {
        },
        data: () => ({
            now: null,
            tab: null,
            menuItems: [
              '未調理', '調理済'
            ],
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            drawer: false,
            // befItems: [{},{},{},{},{},{},{},{}],
            // afItems: [{},{},{},{},{},{},{},{}],
            befItems: [],
            afItems: [],
        }),
        beforeCreate () {
        },
        created () {
            this.$eventHub.$off('addNewOrder')
            this.$eventHub.$on('addNewOrder', this.addNewOrder)
            this.$eventHub.$off('closeSalesHeader')
            this.$eventHub.$on('closeSalesHeader', this.closeSalesHeader)

            console.log('KitchenHome')
            this.$axios({
                method: 'get',
                url: '/api/sales/get_non_end_sales_food_detail/'
            })
            .then(res => {
                console.log(res)
                if (res.data.length <= 7) {
                    let idx = 0
                    for (const d of res.data) {
                        this.$set(this.befItems, idx, d)
                        idx++
                    }
                } else {
                    this.befItems = res.data
                }
            })
            .catch(e => {
                console.log(e)
            })

            this.$axios({
                method: 'get',
                url: '/api/sales/get_end_sales_food_detail/'
            })
            .then(res => {
                console.log(res)
                if (res.data.length <= 7) {
                    let idx = 0
                    for (const d of res.data) {
                        this.$set(this.afItems, idx, d)
                        idx++
                    }
                } else {
                    this.afItems = res.data
                }
            })
            .catch(e => {
                console.log(e)
            })

            setInterval(function() {
                this.now = dayjs()
            }.bind(this), 1000)
        },
        beforeMount () {
        },
        mounted () {
        },
        beforeUpdate () {
        },
        update () {
        },
        beforeDestroy () {
        },
        destoryd () {
        },
        watch: {
        },
        computed: {
            ...mapGetters([
                'seat',
            ]),
        },
        methods: {
            addNewOrder (item) {
                console.log('addNewOrder', item)
                this.befItems.push(item)
                const nt = this.$vs.notification({
                    duration: 10000,
                    progress: 'auto',
                    color: '',
                    position: '', // position
                    width: '50%',
                    title: '新規オーダー追加',
                    text: `
                        商品名: ${item.product.name}<br>
                        数量: ${item.quantity}<br>
                        注文時間: ${item.order_time}<br>
                        席: ${item.disp_seat_name}
                    `
                })
            },
            getWaitTime (orderTime) {
                let diff = this.now.diff(dayjs(orderTime), 'minute')
                const hour = Math.floor(diff / 60)
                const min = diff - (hour * 60)
                let res = min + '分'
                if (hour != 0) {
                    res = hour + '時間' + res
                }
                return res + '待ち'
            },
            orderDone (item) {
                this.$axios({
                    method: 'POST',
                    url: '/api/sales/end_sales_detail/',
                    data: {
                        sales_detail_id: item.id
                    }
                })
                .then(res => {
                    console.log(res)
                    this.befItems = this.befItems.filter(item => item.id !== res.data.id)
                    this.afItems.push(res.data)
                })
                .catch(e => {
                    console.log(e)
                    // エラー
                })
            },
            orderNotDone (item) {
                this.$axios({
                    method: 'POST',
                    url: '/api/sales/not_end_sales_detail/',
                    data: {
                        sales_detail_id: item.id
                    }
                })
                .then(res => {
                    console.log(res)
                    this.afItems = this.afItems.filter(item => item.id !== res.data.id)
                    this.befItems.push(res.data)
                })
                .catch(e => {
                    console.log(e)
                    // エラー
                })
            },
            closeSalesHeader (header) {
                this.befItems = this.befItems.filter(item => item.header.id != header.id)
                this.afItems = this.afItems.filter(item => item.header.id != header.id)
                const nt = this.$vs.notification({
                    duration: 10000,
                    progress: 'auto',
                    color: '',
                    position: '', // position
                    width: '50%',
                    title: '会計を締めました。',
                    text: `
                        伝票No: ${header.header_id}<br>
                        席: ${header.disp_seat_name}
                    `
                })
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .home_wrap {
        min-height: 100%;

        .order_area_wrap {
            height: 100%;
            background-color: rgba(229, 229, 229, 0.5);
        }

        .col_order_area {
            height: 142px;

            .card_order_area {
                height: 100%;
                overflow: auto;
            }
            .card_order_ok_btn {
                border-left: 1px solid rgba(255,255,255,1);
                // height: 140px;
                line-height: 135px;
                text-align: center;
                // background-color: rgba(71, 71, 71, 0.5);
                cursor: pointer;
            }
            .card_order_ok_btn:hover {
                // background-color: rgba(121, 121, 121, 0.6);
            }
        }
    }
</style>
