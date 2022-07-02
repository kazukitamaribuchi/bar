<template>
    <v-card
        id="home_button_wrap"
        @click="toHome"
    >
        <p class="text-center py-4 mb-0">ホームへ</p>
    </v-card>
</template>

<script>

export default {
    name: 'HomeButtonItem',
    data: () => ({
    }),
    components: {
    },
    computed: {
    },
    methods: {
        toHome () {
            this.$router.push({
                name: 'AccountHome'
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    #home_button_wrap {
        cursor: pointer;
    }
</style>
