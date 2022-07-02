<template>
    <div id="input_bottle_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showInputBottle"
            >
                <b-icon
                    icon="person-plus-fill"
                    aria-hidden="true"
                ></b-icon> ボトル入力
            </b-button>
        </b-nav-item>

        <CreateBottleDialog
            ref="createBottleDialog"
        />
    </div>
</template>

<script>
import CreateBottleDialog from '@/components/common/dialog/CreateBottleDialog'

export default {
    name: 'InputBottleItem',
    data: () => ({
    }),
    components: {
        CreateBottleDialog,
    },
    methods: {
        showInputBottle () {
            this.$refs.createBottleDialog.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #input_bottle_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
