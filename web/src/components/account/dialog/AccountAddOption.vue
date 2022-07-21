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
                >追加</vs-button>
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
    }),
    computed: {
        isDisabled () {
            if (this.item.quantity == 0) {
                return true
            }
            return false
        }
    },
    methods: {
        ...mapMutations([
            'pushSelectedProduct',
            'setSelectedProductSalesId',
        ]),
        open (item, idx) {
            this.dialog = true
            this.item = _.cloneDeep(item)
            this.index = idx
            console.log(this.item)
        },
        close () {
            this.dialog = false
            this.item = {}
            this.index = null
        },
        addSelectedProduct () {
            this.pushSelectedProduct(this.item)
            this.setSelectedProductSalesId(this.$route.params.id)
            this.$emit('addSelectedProductOpt', this.item, this.index)
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
