<template>
    <b-modal
        v-model="dialog"
        title="入力項目エラー"
        cancel-title="閉じる"
    >
        <b-card-text class="mb-2">
            入力項目を確認してください。
        </b-card-text>

        <b-card-text
            v-for="(item, i) in errorDetailList"
        >
            {{ item }}
        </b-card-text>
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'FormErrorDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        errorDetailList: [],
    }),
    computed: {
    },
    methods: {
        ...mapActions([
            'deleteBottleListAction',
        ]),
        open (data) {
            this.dialog = true
            this.errorDetailList = data
        },
        close () {
            this.dialog = false
            this.errorDetailList = {}
        },
    }
}

</script>

<style lang="scss" scoped>
</style>
