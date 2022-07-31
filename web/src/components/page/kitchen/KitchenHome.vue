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
                <!-- <v-toolbar-title>αPos</v-toolbar-title> -->

                <!-- <template v-slot:extension> -->
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
                <!-- </template> -->
            </v-toolbar>
        </v-card>

        <v-tabs-items
            v-model="tab"
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
                        <!-- style="border: 1px solid blue;" -->
                            <v-card
                                class="card_order_area"
                            >
                                <v-card-title>
                                    伝票No: {{ item }}
                                </v-card-title>
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
                            sm="6"
                            md="3"
                            lg="3"
                            class="px-1 py-1 col_order_area"
                        >
                            <v-card
                                class="card_order_area"
                            >
                                <v-card-title>
                                    伝票No: {{ item }}
                                </v-card-title>
                            </v-card>
                        </v-col>
                    </v-row>
                </div>
            </v-tab-item>
        </v-tabs-items>

        <!-- <v-tabs
            color="deep-purple accent-4"
            right
            fixed-tabs
        >
            <v-tab
                v-for="(item, i) in items"
                :key="i"
            >
                {{ item }}
            </v-tab>
            <v-tab-item
                v-for="n in 2"
                :key="n"
            >
                <v-container fluid>
                    <v-row>
                        <v-col
                            v-for="(s, i) in seat"
                            :key="i"
                            cols="4"
                        >
                            {{ s.seat_name }}
                        </v-col>
                    </v-row>
                </v-container>
            </v-tab-item>
        </v-tabs> -->

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

    import { mapGetters, mapActions, mapMutations } from 'vuex'

    export default {
        name: 'KitchenHomeItem',
        components: {
        },
        props: {
        },
        data: () => ({
            tab: null,
            menuItems: [
              '未調理', '調理済'
            ],
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            drawer: false,
            befItems: [{},{},{},{},{},{},{},{}],
            afItems: [{},{},{},{},{},{},{},{}],
        }),
        beforeCreate () {
        },
        created () {
            console.log('KitchenHome')
            this.$axios({
                method: 'get',
                url: '/api/sales/get_non_end_sales_detail/'
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
                url: '/api/sales/get_end_sales_detail/'
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
            ])
        },
        methods: {
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .home_wrap {
        min-height: 100%;

        .col_order_area {
            height: 320px;

            .card_order_area {
                height: 100%;
                overflow: auto;

            }
        }
    }
</style>
