<template>
    <v-dialog
        v-model="dialog"
    >
        <v-card class="pt-3">
            <v-card-title>
                test
            </v-card-title>
        </v-card>
    </v-dialog>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import _ from 'lodash'

export default {
    name: 'SelectedProductConfirmItem',
    props: {
    },
    data: () => ({
        dialog: false,
    }),
    computed: {
        ...mapGetters([
            'selectedProduct',
        ])
    },
    methods: {
        ...mapMutations([
        ]),
        open (item) {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
    }
}

</script>

<style lang="scss">
</style>
