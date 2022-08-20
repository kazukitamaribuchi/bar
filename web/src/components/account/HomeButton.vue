<template>
    <!-- <v-card
        id="home_button_wrap"
        @click="toHome"
    >
        <p class="text-center py-4 mb-0">ホームへ</p>
    </v-card> -->
    <v-btn
        block
        depressed
        outlined
        color="primary"
        @click="toHome"
    ><i class='bx bx-home'></i> ホームへ</v-btn>
    <!-- <vs-button
        block
        size="large"
        style="position: relative; left: -5px;"
        @click="toHome"
    >
        <i class='bx bx-home'></i> ホームへ
    </vs-button> -->
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
        background-color: rgba(0, 59, 102, 0.9);
        // background-color: $theme-color2;
        color: white;
    }
</style>
