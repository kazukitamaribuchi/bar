<template>
    <div id="settings_wrap">
        <b-nav-item>
            <b-button
                size="sm"
                @click="showSettings"
            >
                <b-icon
                    icon="gear-fill"
                    aria-hidden="true"
                ></b-icon> 設定
            </b-button>
        </b-nav-item>
    </div>
</template>

<script>

export default {
    name: 'SettingItem',
    data: () => ({
    }),
    components: {
    },
    methods: {
        showSettings () {
        }
    }
}
</script>

<style lang="scss" scoped>
    #settings_wrap {
        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
            // border-color: #6c757d;
        }
    }
</style>
