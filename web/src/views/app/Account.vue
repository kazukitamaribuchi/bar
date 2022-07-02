<template>
    <v-app>
        <Header/>
        <v-container
            id="account_wrap"
            fluid
        >
            <router-view/>
        </v-container>
    </v-app>
</template>

<script>
import Header from '@/components/account/Header'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'AccountItem',
    data: () => ({
    }),
    components: {
        Header,
    },
    computed: {
    },
    created () {
    },
    methods: {
    }
}
</script>

<style lang="scss" scoped>
</style>
