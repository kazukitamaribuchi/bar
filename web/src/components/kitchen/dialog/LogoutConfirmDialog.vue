<template>
    <vs-dialog
        v-model="dialog"
    >
        <v-card
            class="pt-3"
            flat
        >
            <v-card-title
                class="text-h5"
            >
                ログアウトします。
                よろしいでしょうか？
            </v-card-title>
            <v-card-actions>
                <v-spacer></v-spacer>
                    <v-btn
                        outlined
                        color="indigo"
                        @click="close"
                    >
                        いいえ
                    </v-btn>
                    <v-btn
                        outlined
                        color="green darken-1"
                        @click="logout"
                    >
                        はい
                    </v-btn>
            </v-card-actions>
        </v-card>
    </vs-dialog>
</template>
<script>
    import { mapMutations } from 'vuex'

    export default {
        name: 'LogoutConfirmDialogItem',
        components: {
        },
        props: {
        },
        data: () => ({
            dialog: false,
        }),
        beforeCreate () {
        },
        created () {
        },
        beforeMount () {
        },
        mounted () {
        },
        beforeUpdate () {
        },
        update () {
        },
        beforeDestroy () {
        },
        destoryd () {
        },
        watch: {
        },
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
                this.close()
                this.$router.push({name: 'KitchenLogin'})
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
