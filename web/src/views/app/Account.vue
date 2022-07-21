<template>
    <v-app>
        <Header
            v-if="isAuth"
        />
        <v-container
            id="account_wrap"
            fluid
        >
            <router-view/>
        </v-container>
        <v-overlay
            :value="humMenu"
            :zIndex="0"
        ></v-overlay>
    </v-app>
</template>

<script>
import Header from '@/components/account/Header'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'AccountItem',
    data: () => ({
        humMenu: false,
    }),
    components: {
        Header,
    },
    computed: {
        ...mapGetters([
            'isAuth',
        ])
    },
    beforeCreate () {
    },
    created () {
    },
    beforeMount () {
    },
    mounted () {
        if (!this.isAuth) {
            this.$router.push({ name: 'AccountLogin' })
        }
    },
    beforeUpdate () {
    },
    update () {
    },
    beforeDestroy () {
    },
    destoryd () {
    },
    methods: {
    }
}
</script>

<style lang="scss" scoped>
    // .humActive {
    //     background: yellow;
    //     z-index: 9999;
    // }
</style>
