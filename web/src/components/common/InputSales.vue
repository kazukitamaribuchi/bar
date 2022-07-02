<template>
    <div id="input_sales_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputSales"
            >
                <b-icon
                    icon="plus-circle"
                    aria-hidden="true"
                ></b-icon> 売上入力
            </b-button>
        </b-nav-item>

        <InputSalesDialog
            ref="inputSalesDialog"
        />
    </div>
</template>

<script>
import InputSalesDialog from '@/components/common/dialog/InputSalesDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'InputSalesItem',
    data: () => ({
    }),
    components: {
        InputSalesDialog,
    },
    computed: {
        ...mapGetters([
            'sales'
        ]),
    },
    methods: {
        showInputSales () {
            this.$refs.inputSalesDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_sales_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
