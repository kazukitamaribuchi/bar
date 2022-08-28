<template>
    <v-dialog
        v-model="dialog"
    >
        <v-card>
            <v-card-title>
                対象の商品を削除します。宜しいですか？
            </v-card-title>
            <v-card-actions>
                <v-row class="ma-0">
                    <v-col class="ma-0">
                        <v-btn
                            block
                            color="blue-grey"
                            @click="close"
                            dark
                        >
                            いいえ
                        </v-btn>
                    </v-col>
                    <v-col class="ma-0">
                        <v-btn
                            block
                            color="primary"
                            @click="deleteTarget"
                        >
                            はい
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>

import dayjs from 'dayjs'
import { mapGetters, mapMutations } from 'vuex'

export default {
    name: 'DeleteConfirmDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        item: null
    }),
    computed: {
    },
    methods: {
        open (item) {
            this.item = item
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
        init () {
            this.item = null
            this.close()
        },
        deleteTarget () {
            this.$emit('delete', this.item)
            this.init()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
