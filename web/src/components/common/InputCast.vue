<template>
    <div id="input_cast_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputCast"
            >
                <b-icon
                    icon="person-plus"
                    aria-hidden="true"
                ></b-icon> キャスト入力
            </b-button>
        </b-nav-item>

        <CreateCastDialog
            ref="createCastDialog"
        />
    </div>
</template>

<script>
import CreateCastDialog from '@/components/common/dialog/CreateCastDialog'

export default {
    name: 'InputCastItem',
    data: () => ({
    }),
    components: {
        CreateCastDialog,
    },
    methods: {
        showInputCast () {
            this.$refs.createCastDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_cast_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
