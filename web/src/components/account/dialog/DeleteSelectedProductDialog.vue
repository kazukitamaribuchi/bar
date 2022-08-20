<template>
    <v-dialog
        v-model="dialog"
        persistent
    >
        <v-card>
            <v-card-title>
                選択中の商品が存在するため削除されます。宜しいですか？
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
                            @click="deleteSelectedProduct"
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
    name: 'DeleteSelectedProductDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
    }),
    computed: {
    },
    methods: {
        ...mapMutations([
            'initSelectedProduct'
        ]),
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
        deleteSelectedProduct () {
            this.initSelectedProduct()
            this.$router.push({
                name: 'AccountOrderSelect',
            })
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
