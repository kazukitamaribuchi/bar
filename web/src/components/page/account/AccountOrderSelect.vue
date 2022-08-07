<template>
    <div>
        <AccountPageTitleArea
            to="AccountHome"
            title="伝票選択"
        />
        <AccountOrderList
        />
    </div>
</template>


<script>

    import AccountPageTitleArea from '@/components/account/AccountPageTitleArea'
    import AccountOrderList from '@/components/page/account/AccountOrderList'

    export default {
        name: 'AccountOrderSelectItem',
        components: {
            AccountPageTitleArea,
            AccountOrderList,
        },
        props: {
        },
        data: () => ({
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
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
