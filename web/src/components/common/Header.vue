<template>
    <b-row id="header_wrap" class="pt-2">
        <b-col cols="4">
            <router-link
                to='/'
                class="header_title"
            >Customer Management System</router-link>
        </b-col>
        <b-col cols="8">
            <b-nav align="right">
                <!-- <InputSales/> -->
                <InputCustomer/>
                <!-- <InputCast/> -->
                <!-- <InputAttendance/> -->
                <!-- <InputBooking/> -->
                <InputBottle/>
                <!-- <Settings/> -->
                <Logout/>
            </b-nav>
        </b-col>
    </b-row>
</template>

<script>
import InputSales from '@/components/common/InputSales'
import InputAttendance from '@/components/common/InputAttendance'
import InputBooking from '@/components/common/InputBooking'
import InputCustomer from '@/components/common/InputCustomer'
import InputCast from '@/components/common/InputCast'
import InputBottle from '@/components/common/InputBottle'
import Settings from '@/components/common/Settings'
import Logout from '@/components/common/Logout'

export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {}
    }),
    components: {
        InputSales,
        InputAttendance,
        InputBooking,
        InputCustomer,
        InputCast,
        InputBottle,
        Settings,
        Logout,
    }
}
</script>

<style lang="scss" scoped>
#header_wrap {
    height: $header-height;
    background-color: $theme-color;
    color: white;

    .header_title {
        padding-left: 1rem;
        color: $menu-text-color;
        text-decoration: none;
        // font-family: 'Anton', sans-serif;
        // font-family: 'Roboto Condensed', sans-serif;
        position: relative;
        top: 2px;
        font-weight: bold;
        font-size: 22px;
    }
}

</style>
