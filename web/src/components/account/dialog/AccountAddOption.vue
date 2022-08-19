<template>
    <v-dialog
        v-model="dialog"
    >
        <v-card class="pt-3">
            <v-card-text>
                <label>商品名</label>
                <v-card-subtitle>
                    {{ item.name }}
                </v-card-subtitle>

                <label>実価格</label>
                <v-text-field
                    v-model="item.fixedPrice"
                    label="実価格"
                    placeholder="実価格"
                    class="right-input"
                ></v-text-field>

                <label>数量</label>
                <b-form-spinbutton
                    id="sb-inline"
                    v-model="item.quantity"
                    min="0"
                    size="lg"
                ></b-form-spinbutton>

                <v-checkbox
                    v-model="item.taxFree"
                    label="非課税"
                ></v-checkbox>

                <!-- <v-btn
                    block
                    @click="addSelectedProduct"
                >追加</v-btn> -->
                <vs-button
                    :disabled="isDisabled"
                    block
                    @click="addSelectedProduct"
                    size="large"
                >{{ btnText }}</vs-button>
            </v-card-text>


        </v-card>
    </v-dialog>
</template>

<script>
import { mapMutations } from 'vuex'
import _ from 'lodash'

export default {
    name: 'AccountAddOptionItem',
    props: {
    },
    data: () => ({
        dialog: false,
        item: {},
        index: null,
        editMode: false,
    }),
    computed: {
        isDisabled () {
            if (this.item.quantity == 0 && !this.editMode) {
                return true
            }
            return false
        },
        btnText () {
            if (this.editMode) return '更新'
            return '追加'
        }
    },
    methods: {
        ...mapMutations([
            'pushSelectedProduct',
            'updateSelectedProduct',
            'setSelectedProductSalesId',
            'deleteSelectedProduct',
        ]),
        open (item, idx) {
            this.dialog = true
            this.item = _.cloneDeep(item)
            this.index = idx

            // 2022-08-19 とりあえず追加かUPDATEで1回の注文で1パターンのみにする。
            if (this.item.quantity >= 1 ) {
                this.editMode = true
            } else {
                this.editMode = false
            }
            console.log('open', this.item)
        },
        close () {
            this.dialog = false
            this.item = {}
            this.index = null
            this.editMode = false
        },
        addSelectedProduct () {
            this.item.fixedPrice = Number(this.item.fixedPrice) 
            if (this.editMode) {
                if (this.item.quantity == 0) {
                    this.deleteSelectedProduct(this.item)
                } else {
                    this.updateSelectedProduct(this.item)
                }
            } else {
                this.pushSelectedProduct(this.item)
            }
            this.$emit('addSelectedProductOpt', this.item, this.index)
            this.setSelectedProductSalesId(this.$route.params.id)
            this.close()
        }
    }
}

</script>

<style lang="scss">
    .right-input input {
        text-align: right;
    }
</style>
