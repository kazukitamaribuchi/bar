<template>
    <div id="attendance_list_wrap">
        <b-row>
            <b-col cols="7">
                <b-card class="attendance_list_1">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="attendance_list_2">
                </b-card>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="12">
                <b-card class="attendance_list_3">
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AttendanceListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'attendance'
        ]),
    },
    created () {
        this.getAttendanceList()
        .then(res => {
            this.setAttendanceList(res)
        })
    },
    mounted () {
        console.log('this.attendance', this.attendance)
    },
    methods: {
        ...mapMutations([
            'setAttendanceList',
        ]),
        ...mapActions([
            'getAttendanceList',
        ])
    }
}
</script>
<style lang="scss" scoped>
    #attendance_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .attendance_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .attendance_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .attendance_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .attendance_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .attendance_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }
    }
</style>
