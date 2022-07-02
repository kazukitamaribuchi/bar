<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            title="勤怠入力"
            header-bg-variant="dark"
            header-text-variant="light"
        >
            <b-form class="create_cast_form">
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'InputAttendanceDialogItem',
    props: {
    },
    data: () => ({
        inputBookingData: {},
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
    }),
    computed: {
    },
    methods: {
        ...mapMutations([
            // 'addCastList',
        ]),
        register () {
            console.log('register', this.createCastData)
            // const data = this.createCustomerData
            // const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            // this.$axios({
            //     method: 'POST',
            //     url: '/api/customer/',
            //     data: {
            //         name: data.name,
            //         name_kana: data.name_kana,
            //         age: data.age,
            //         birthday_str: birthday,
            //         job: data.job,
            //         company: data.company,
            //         customer_no: data.customer_no,
            //         // ランクは最初から上位で作る事も許容させるか？
            //         rank_id: 1,
            //     }
            // })
            // .then(res => {
            //     console.log(res)
            //     this.addCustomerList(res)
            //     this.init()
            // })
            // .catch(e => {
            //     console.log(e)
            // })
        },
        init () {
            this.inputAttendanceData = {}
        },
        close () {
            this.dialog = false
            this.init()
        },
        open () {
            this.dialog = true
        }
    }
}

</script>

<style lang="scss" scoped>

</style>
