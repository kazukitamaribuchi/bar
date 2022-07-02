<template>
    <b-modal
        v-model="dialog"
        hide-header
        ok-title="正しく入力してください"
        cancel-title="閉じる"
    >
        <b
            v-for="(item, i) in errorMsg"
            :key="i"
        >
            {{ item.text }}
        </b>
    </b-modal>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    name: 'ErrorModalItem',
    props: {
        errorMsg: {
            type: Array,
            required: true,
        }
    },
    data: () => ({
        dialog: false,
    }),
    computed: {
    },
    methods: {
        ...mapMutations([
        ]),
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
    }
}

</script>

<style lang="scss" scoped>
</style>
