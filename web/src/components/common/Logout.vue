<template>
    <div id="logout_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showLogoutConfirm"
            >
                <b-icon
                    icon="box-arrow-right"
                    aria-hidden="true"
                ></b-icon> ログアウト
            </b-button>
        </b-nav-item>
        <LogoutConfirm
            ref="logoutConfirm"
        />
    </div>
</template>

<script>
import LogoutConfirm from '@/components/common/dialog/LogoutConfirm'

export default {
    name: 'LogoutItem',
    data: () => ({
    }),
    components: {
        LogoutConfirm,
    },
    methods: {
        showLogoutConfirm () {
            this.$refs.logoutConfirm.open()
        }
    }
}
</script>

<style lang="scss" scoped>
    #logout_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
