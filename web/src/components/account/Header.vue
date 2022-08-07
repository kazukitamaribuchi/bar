<template>
    <div id="header_wrap">
        <!-- color="blue-grey darken-3"
        dark -->
        <v-toolbar
            flat
            height="45"
        >
            <v-toolbar-title>
                Menu
            </v-toolbar-title>
            <v-spacer/>
            <v-app-bar-nav-icon
                @click.stop="drawer = !drawer"
            ></v-app-bar-nav-icon>

                <!-- <v-tabs
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
                </v-tabs> -->
        </v-toolbar>

        <!-- <div>
            <i
                class='bx header-hum'
                :class="{trans: menu, 'trans2': !menu, 'bx-menu': !menu, 'bx-x': menu}"
            ></i>
            @click="menu = !menu"
        </div>
        <transition name="slide-fade">
            <div
                v-if="menu"
                class="hum-menu"
            >
                <v-list>
                    <v-subheader>MENUS</v-subheader>
                        <v-list-item-group
                            color="primary"
                        >
                            <v-list-item
                                v-for="(item, i) in items"
                                :key="i"
                                @click="toEvent(item.click)"
                            >
                                <v-list-item-icon>
                                    <v-icon v-text="item.icon"></v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title v-text="item.text"></v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                </v-list>
            </div>
        </transition> -->

        <v-navigation-drawer
            v-model="drawer"
            absolute
            temporary
            left
        >
            <v-list-item>
                <v-list-item-avatar>
                    <v-img
                        src="http://localhost:8000/media/upload/logo2.jpg"
                    ></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class="text-h6">
                        alpha pos
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        menu
                    </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list
                nav
                dense
            >
                <v-list-item-group
                    v-model="group"
                    active-class="deep-purple--text text--accent-4"
                >
                    <v-list-item
                        @click="showLogoutConfirmDialog"
                    >
                        <v-list-item-title>ログアウト</v-list-item-title>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>

        <LogoutConfirm
            ref="logoutConfirm"
        />
    </div>
</template>

<script>

import LogoutConfirm from '@/components/common/dialog/LogoutConfirm'

const title = {
    'AccountHome': 'ホーム',
    'AccountOrderSelect': 'オーダー',
    'AccountOrderCheckSelect': '注文確認',
    'AccountNewVisit': '新規入店',
    'AccountBottle': 'ボトル',
    'AccountCustomer': '顧客情報照会',
    'AccountOrder': '注文商品選択',
    'AccountProductDetail': '注文商品選択',
    'AccountOrderCheck': '注文確認',
}

export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {},
        menu: false,
        absolute: true,
        items: [
            {
                text: 'ホーム',
                icon: 'mdi-clock',
                click: 0
            },
            {
                text: '設定',
                icon: 'mdi-account',
                click: 1
            },
            {
                text: 'ログアウト',
                icon: 'mdi-flag',
                click: 2
            },
        ],
        tab: null,
        drawer: false,
        group: null,
    }),
    components: {
        LogoutConfirm,
    },
    beforeCreate () {
    },
    created () {
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
    computed: {
        headerTitle () {
            return title[this.$route.name]
        },
    },
    methods: {
        toEvent (val) {
            switch (val) {
                case 0:
                    this.home()
                    break
                case 1:
                    this.setting()
                    break
                case 2:
                    this.logout()
                    break
                default:
                    break
            }
        },
        home () {
            console.log('home')
        },
        setting () {
            console.log('setting')
        },
        showLogoutConfirmDialog () {
            console.log('logout')
            this.$refs.logoutConfirm.open()
        },
    }
}
</script>

<style lang="scss" scoped>
#header_wrap {
    // background: $theme-color;
    // background: rgb(76, 169, 225);
    // box-shadow: 1px 2px 2px rgba(118, 215, 237, 0.5);
    // color: white;

    // border-bottom: 0.5px solid rgba(150, 150, 150, 0.5);

    height: 50px;
    // margin-bottom: 10px;
    padding-top: 5px;

    .header-title {
        height: 100%;
        text-align: center;
        align-items: flex-end;
        justify-content: center;
        display: flex;
    }
    .header-hum {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 8px;
        left: 10px;
    }

    .trans {
        transition: 0.5s;
        transform: rotate(0.5turn);
    }

    .trans2 {
        transform: rotate(-0.5turn);
    }

    // background-color: $theme-color;
    // color: white;
    //
    // .header_title {
    //     padding-left: 1rem;
    //     color: $menu-text-color;
    //     text-decoration: none;
    //     // font-family: 'Anton', sans-serif;
    //     // font-family: 'Roboto Condensed', sans-serif;
    //     position: relative;
    //     top: 2px;
    //     font-weight: bold;
    //     font-size: 22px;
    // }

    .hum-menu {
        z-index: 1000;
        width: 70%;
        left: 0;
        position: fixed;
        // top: 0;
        height: 100%;
        background: white;
        border: 1px solid rgba(100, 100, 100, 0.5);
        padding: 1rem;
        margin-top: 10px;
        // transition: 0.5s;
    }

    .slide-fade-enter-active {
        width: 70%;
        transition: all .2s ease;
    }
    .slide-fade-leave-active {
        width: 70%;
        transition: all .5s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }
    .slide-fade-enter, .slide-fade-leave-to
    /* .slide-fade-leave-active below version 2.1.8 */ {
        width: 0;
        transform: translateX(-100px);
        opacity: 0;
    }
}

</style>
