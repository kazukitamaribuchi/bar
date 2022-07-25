<template>
    <div>
        <i
            @click="undo"
            class='bx bx-undo undo-btn'
        ></i>
        <p class="text-center" style="font-size: 13px;">
            伝票選択
        </p>
        <AccountOrderList
        />
    </div>
</template>


<script>

    import AccountOrderList from '@/components/page/account/AccountOrderList'

    export default {
        name: 'AccountOrderSelectItem',
        components: {
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
            undo () {
                this.$router.push({
                    name: 'AccountHome',
                })
            },
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .undo-btn {
        font-size: 25px;
        cursor: pointer;
        position: absolute;
        top: 55px;
        left: 20px;
    }
</style>
