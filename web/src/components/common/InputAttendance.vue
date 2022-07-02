<template>
    <div id="input_attendance_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputAttendance"
            >
                <b-icon
                    icon="calendar-plus"
                    aria-hidden="true"
                ></b-icon> 勤怠入力
            </b-button>
        </b-nav-item>

        <InputAttendanceDialog
            ref="inputAttendanceDialog"
        />
    </div>
</template>

<script>
import InputAttendanceDialog from '@/components/common/dialog/InputAttendanceDialog'

export default {
    name: 'InputAttendanceItem',
    data: () => ({
    }),
    components: {
        InputAttendanceDialog,
    },
    methods: {
        showInputAttendance () {
            this.$refs.inputAttendanceDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_attendance_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
