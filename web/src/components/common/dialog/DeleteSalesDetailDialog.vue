<template>
    <b-modal
        v-model="dialog"
        title="売上データ削除"
        @ok="deleteSalesDetail"
        ok-title="削除"
        cancel-title="キャンセル"
    >
        伝票No{{ salesDetail.id }}を削除しますか？
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'DeleteSalesDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        salesDetail: {},
    }),
    computed: {
    },
    methods: {
        ...mapActions([
            'deleteSalesListAction',
        ]),
        open (data) {
            this.dialog = true
            this.salesDetail = data
        },
        close () {
            this.dialog = false
            this.salesDetail = {}
        },
        deleteSalesDetail () {
            this.deleteSalesListAction(this.salesDetail)
            .then(res => {
                this.dialog = false
                this.$router.push('/sales')
                this.salesDetail = {}
            })
            .catch(e => {
                console.log(e)
                this.dialog = false
            })
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
