<template>
    <div id="input_customer_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputCustomer"
            >
                <b-icon
                    icon="person-plus-fill"
                    aria-hidden="true"
                ></b-icon> 顧客入力
            </b-button>
        </b-nav-item>

        <CreateCustomerDialog
            ref="createCustomerDialog"
        />
    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'

export default {
    name: 'InputCustomerItem',
    data: () => ({
    }),
    components: {
        CreateCustomerDialog,
    },
    methods: {
        showInputCustomer () {
            this.$refs.createCustomerDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_customer_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
