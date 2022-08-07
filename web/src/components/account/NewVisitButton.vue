<template>
    <!-- <v-card
        id="new_visit_button_wrap"
        @click="toNewVisit"
    >
        <p class="text-center py-4 mb-0">新規入店</p>
    </v-card> -->
    <v-btn
        block
        depressed
        color="success"
        @click="toNewVisit"
    ><i class='bx bx-id-card'></i> 新規入店</v-btn>
    <!-- <vs-button
        block
        outlined
        success
        size="large"
        style="position: relative; left: -5px;"
        @click="toNewVisit"
    >
        <i class='bx bx-id-card'></i> 新規入店
    </vs-button> -->
</template>

<script>

export default {
    name: 'NewVisitButtonItem',
    data: () => ({
    }),
    components: {
    },
    computed: {
    },
    methods: {
        toNewVisit () {
            this.$router.push({
                name: 'AccountNewVisit'
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    #new_visit_button_wrap {
        cursor: pointer;
        background-color: rgba(37, 119, 224, 0.87);
        color: white;
    }
</style>
