<template>
    <div id="input_booking_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputBooking"
            >
                <!-- telephone-plus-fill -->
                <b-icon
                    icon="bookmark-plus"
                    aria-hidden="true"
                ></b-icon> 予約入力
            </b-button>
        </b-nav-item>

        <InputBookingDialog
            ref="inputBookingDialog"
        />
    </div>
</template>

<script>
import InputBookingDialog from '@/components/common/dialog/InputBookingDialog'

export default {
    name: 'InputBookingItem',
    data: () => ({
    }),
    components: {
        InputBookingDialog,
    },
    methods: {
        showInputBooking () {
            this.$refs.inputBookingDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_booking_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
