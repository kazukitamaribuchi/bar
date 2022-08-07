<template>
    <div
        class="undo_btn_wrap"
        @click="undo"
    >
        <i class='bx bx-arrow-back'></i>
    </div>
</template>
<script>
    import { mapGetters, mapMutations, mapActions } from 'vuex'

    export default {
        name: 'UndoBtnItem',
        components: {
        },
        props: {
            to: {
                type: String,
                required: false,
                default: 'AccountHome',
            },
            AccountOrder: {
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
            ...mapGetters([
                'selectedProduct',
            ])
        },
        methods: {
            undo () {
                if (this.selectedProduct.length != 0) {
                    console.log('カートの中身破棄するか確認する')
                    // this.initSelectedProduct()
                    this.$router.push({
                        name: this.to,
                    })
                } else {
                    if (this.params != null) {
                        this.$router.push({
                            name: this.to,
                            params: this.params,
                        })
                    } else {
                        this.$router.push({
                            name: this.to,
                        })
                    }
                }
            }
        },
        mixins: [],
    }
</script>
<style lang="scss" scoped>
    .undo_btn_wrap {
        padding-left: 15px;
        padding-top: 15px;
        font-size: 25px;
        width: 50px;
        cursor: pointer;
    }
</style>
