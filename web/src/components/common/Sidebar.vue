<template>
    <div id="sidebar_wrap" class="pt-5">
        <div
            v-for="(item, id) in items"
            :key="id"
            class="sidebar_item"
            @click="toPage(item)"
        >
            <span>
                <b-icon
                    :icon=item.icon
                    aria-hidden="true"
                    class="sidebar_icon"
                ></b-icon>
            </span>
            <span class="sidebar_text">
                {{ item.text }}
            </span>
        </div>
        <!-- <b-icon icon="people" aria-hidden="true"></b-icon>
        <b-icon icon="people-fill" aria-hidden="true"></b-icon>
        <b-icon icon="people-filcircles" aria-hidden="true"></b-icon>
        <b-icon icon="person-fill" aria-hidden="true"></b-icon>
        <b-icon icon="person-plus" aria-hidden="true"></b-icon>
        <b-icon icon="person-plus-fill" aria-hidden="true"></b-icon>
        <b-icon icon="person-square" aria-hidden="true"></b/</b-icon>
        <b-icon icon="clipboard-check" aria-hidden="true"></b-icon>
        <b-icon icon="clipboard-data" aria-hidden="true"></b-icon>
        <b-icon icon="plus-circle-fill" aria-hidden="true"></b-icon>
        <b-icon icon="plus-lg" aria-hidden="true"></b-icon>
        <b-icon icon="plus-square" aria-hidden="true"></b-icon>
        <b-icon icon="receipt" aria-hidden="true"></b-icon>
        <b-icon icon="search" aria-hidden="true"></b-icon>
        <b-icon icon="calendar" aria-hidden="true"></b-icon>
        <b-icon icon="calendar2" aria-hidden="true"></b-icon>
        <b-icon icon="calendar2-check" aria-hidden="true"></b-icon>
        <b-icon icon="calendar2-date" aria-hidden="true"></b-icon> -->

        <SearchCustomerNoDialog
            ref="searchCustomerNo"
        />
    </div>


    <!-- <v-container id="sidebar-wrap">
        <v-list>
            <v-list-item
                v-for="(menu, i) in menus"
                :key="i"
            >
                <v-btn
                    text
                    @click="toPage(menu)"
                >
                    <v-list-item-icon>
                        <i :class='menu.icon' :style='menu.style'></i>
                    </v-list-item-icon>
                    <v-list-item-title>{{ menu.title }}</v-list-item-title>
                </v-btn>
            </v-list-item>
        </v-list>

        <SearchCustomerNoDialog
            ref="searchCustomerNo"
        />
    </v-container> -->
</template>

<script>
import SearchCustomerNoDialog from '@/components/common/dialog/SearchCustomerNoDialog'
import { mapMutations } from 'vuex'

export default {
    name: 'SidebarItem',
    components: {
        SearchCustomerNoDialog
    },
    data: () => ({
        active: false,
        items: [
            {
                icon: 'people-fill',
                link: 'CustomerList',
                type: 'Page',
                text: '顧客管理',
                active: 0,
            },
            {
                icon: 'credit-card',
                link: 'SalesList',
                type: 'Page',
                text: '売上管理',
                active: 1,
            },
            {
                icon: 'person-square',
                link: 'CastList',
                type: 'Page',
                text: 'キャスト管理',
                active: 2,
            },
            // {
            //     icon: 'calendar2-date',
            //     link: 'AttendanceList',
            //     type: 'Page',
            //     text: '勤怠管理',
            //     active: 3,
            // },
            // {
            //     icon: 'clipboard-check',
            //     link: 'BookingList',
            //     type: 'Page',
            //     text: '予約管理',
            //     active: 4,
            // },
            // ボトルのアイコンどうするか・・・
            // {
            //     icon: 'calendar2-date',
            // },
            {
                icon: 'search',
                link: 'BottleList',
                type: 'Page',
                text: 'ボトル管理',
                active: 3,
            },
            {
                icon: 'search',
                ref: 'searchCustomerNo',
                type: 'Dialog',
                text: '顧客検索',
                active: 99,
            },
        ],
        // menus: [
        //     {
        //         title: '顧客管理',
        //         icon: 'bx bxs-user-badge',
        //         // icon: 'bx bxs-user',
        //         style: 'color:#914240',
        //         link: 'CustomerList',
        //         type: 'Page'
        //     },
        //     {
        //         title: '売上管理',
        //         icon: 'bx bx-calculator',
        //         style: 'color:#757733',
        //         link: 'SalesList',
        //         type: 'Page'
        //     },
        //     {
        //         title: '勤怠管理',
        //         icon: 'bx bxs-calendar',
        //         style: 'color:#657733',
        //         link: 'AttendanceList',
        //         type: 'Page'
        //     },
        //     {
        //         title: 'キャスト管理',
        //         icon: 'bx bx-user',
        //         style: 'color:#657733',
        //         link: 'CastList',
        //         type: 'Page'
        //     },
        //     {
        //         title: '予約管理',
        //         icon: 'bx bxs-book',
        //         style: 'color:#657733',
        //         link: 'BookingList',
        //         type: 'Page'
        //     },
        //     {
        //         title: 'ボトル管理',
        //         icon: 'bx bxs-drink',
        //         style: 'color:#657733',
        //         link: 'BottleList',
        //         type: 'Page'
        //     },
        //     {
        //         title: '顧客No検索',
        //         icon: 'bx bx-search-alt-2',
        //         style: 'color:#914240',
        //         ref: 'searchCustomerNo',
        //         type: 'Dialog'
        //     }
        // ]
    }),
    methods: {
        ...mapMutations([
            'setCustomerTopActive',
            'setSalesTopActive',
            'setCastTopActive',
        ]),
        toPage (item) {
            switch (item.active) {
                case 0:
                    this.setCustomerTopActive(0)
                    break
                case 1:
                    this.setSalesTopActive(0)
                    break
                case 2:
                    this.setCastTopActive(0)
                    break
                default:
                    break
            }
            if (item.type == 'Dialog') {
                this.$refs[item.ref].open()
            } else {
                this.$router.push({name: item.link})
            }
        }
    }
}
</script>

<style lang="scss" scoped>
    #sidebar_wrap {
        width: $sidebar-width;
        background-color: $theme-color;

        // height: calc( #{$sidebar-height} - #{$header-height} );
        // margin-top: 1rem;
        color: white;

        .sidebar_item {
            cursor: pointer;
            height: 80px;
            padding-left: 10px;

            .sidebar_icon {
                font-size: 20px;
                // display: block;
                // margin: 0 auto;
                // cursor: pointer;
            }

            .sidebar_text {
                font-size: 13px;
            }
        }
    }
</style>
