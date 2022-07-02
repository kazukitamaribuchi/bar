<template>
    <b-modal
        v-model="dialog"
        title="キャストデータ削除"
        @ok="deleteCastDetail"
        ok-title="削除"
        cancel-title="キャンセル"
    >
        キャストNo{{ castDetail.id }}のキャストデータを削除しますか？
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'DeleteCastDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        castDetail: {},
    }),
    computed: {
    },
    methods: {
        ...mapActions([
            'deleteCastListAction',
        ]),
        open (data) {
            this.dialog = true
            this.castDetail = data
        },
        close () {
            this.dialog = false
            this.castDetail = {}
        },
        deleteCastDetail () {
            this.deleteCastListAction(this.castDetail)
            this.dialog = false
            this.$router.push('/cast')
            this.castDetail = {}
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
