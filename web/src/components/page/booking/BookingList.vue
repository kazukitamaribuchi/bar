<template>
    <div id="booking_list_wrap">
        <b-row>
            <b-col cols="9">
                <b-card class="booking_list_1">
                </b-card>
            </b-col>
            <b-col cols="3">
                <b-card class="booking_list_1">
                </b-card>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="12">
                <b-card class="booking_list_3">
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'BookingListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'booking'
        ]),
    },
    created () {
        this.getBookingList()
        .then(res => {
            this.setBookingList(res)
        })
    },
    mounted () {
        console.log('this.booking', this.booking)
    },
    methods: {
        ...mapMutations([
            'setBookingList',
        ]),
        ...mapActions([
            'getBookingList',
        ])
    }
}
</script>
<style lang="scss" scoped>
    #booking_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .booking_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .booking_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .booking_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .booking_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .booking_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }
    }
</style>
