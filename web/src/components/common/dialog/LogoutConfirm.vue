<template>
    <b-modal
        v-model="dialog"
        hide-header
        @ok="logout"
        ok-title="ログアウト"
        cancel-title="閉じる"
    >
        ログアウトしますか？
    </b-modal>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    name: 'LogoutConfirmItem',
    props: {
    },
    data: () => ({
        dialog: false,
    }),
    computed: {
    },
    methods: {
        ...mapMutations([
            'initAuthToken',
        ]),
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
        logout () {
            this.initAuthToken()
            this.dialog = false
            console.log(this.$route)
            // const reg = /^.*\/account\/.*$/g
            const reg = /^.*\/account.*$/g
            // console.log(this.$route.path)
            // console.log(reg.test(this.$route.path))
            if (reg.test(this.$route.path)) {
                this.$router.push({name: 'AccountLogin'})
            } else {
                this.$router.push('/')
            }
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
