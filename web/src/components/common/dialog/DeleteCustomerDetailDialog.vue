<template>
    <b-modal
        v-model="dialog"
        title="顧客データ削除"
        @ok="deleteCustomerDetail"
        ok-title="削除"
        cancel-title="キャンセル"
    >
        会員No{{ customerDetail.customer_no }}の顧客データを削除しますか？
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'DeleteCustomerDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        customerDetail: {},
    }),
    computed: {
    },
    methods: {
        ...mapActions([
            'deleteCustomerListAction',
        ]),
        open (data) {
            this.dialog = true
            this.customerDetail = data
        },
        close () {
            this.dialog = false
            this.customerDetail = {}
        },
        deleteCustomerDetail () {
            this.deleteCustomerListAction(this.customerDetail)
            this.dialog = false
            this.$router.push('/customer')
            this.customerDetail = {}
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
