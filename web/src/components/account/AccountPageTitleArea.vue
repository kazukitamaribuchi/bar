<template>
    <div id="account_page_title_area">
        <UndoBtn
            :to="to"
            :params="params"
            :attention="true"
            @showDeleteSelectedProductDialog="showDeleteSelectedProductDialog"
        />
        <v-card-title class="pt-0 pb-1">
            {{ title }}
        </v-card-title>
    </div>
</template>
<script>
    import UndoBtn from '@/components/account/parts/UndoBtn'

    export default {
        name: 'AccountPageTitleAreaItem',
        components: {
            UndoBtn
        },
        props: {
            to: {
                type: String,
                required: false,
                default: 'AccountHome',
            },
            title: {
                type: String,
                required: false,
                default: '',
            },
            params: {
                type: Object,
                required: false,
                default: null,
            },
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
            showDeleteSelectedProductDialog () {
                this.$emit('showDeleteSelectedProductDialog')
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
</style>
