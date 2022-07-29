<template>
    <v-dialog
        v-model="dialog"
        max-width="100px"
    >
        <v-card>
            <v-card-text>
                明細を削除します。宜しいですか？
            </v-card-text>
            <!-- <v-card-actions>
                <v-btn
                    depressed
                    @click="deleteSalesDetail"
                >はい</v-btn>
                <v-btn
                    depressed
                    @click="deleteSalesDetail"
                >閉じる</v-btn>
            </v-card-actions> -->

        </v-card>
    </v-dialog>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters } from 'vuex'

export default {
    name: 'DeleteSalesDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        item: null,
        idx: null
    }),
    computed: {
    },
    methods: {
        open (item, idx) {
            this.dialog = true
            this.item = item
            this.index = idx
        },
        close () {
            this.dialog = false
            this.item = null
            this.idx = null
        },
        deleteSalesDetail () {
            this.$emit('deleteSalesDetail', this.item, this.index)
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
