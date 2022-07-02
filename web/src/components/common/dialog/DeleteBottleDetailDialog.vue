<template>
    <b-modal
        v-model="dialog"
        title="ボトルデータ削除"
        @ok="deleteBottleDetail"
        ok-title="削除"
        cancel-title="キャンセル"
    >
        {{ confirmText }}
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'DeleteBottleDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        bottleDetail: {},
    }),
    computed: {
        confirmText () {
            if (this.bottleDetail.delete_flg) {
                return 'ボトルの削除状態を元の状態へ更新しますか？'
            } else {
                return 'ボトルデータを削除しますか？'
            }
        }
    },
    methods: {
        ...mapActions([
            'deleteBottleListAction',
        ]),
        open (data) {
            this.dialog = true
            this.bottleDetail = data
        },
        close () {
            this.dialog = false
            this.bottleDetail = {}
        },
        deleteBottleDetail () {
            this.deleteBottleListAction(this.bottleDetail)
            // this.$router.push('/bottle')
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
