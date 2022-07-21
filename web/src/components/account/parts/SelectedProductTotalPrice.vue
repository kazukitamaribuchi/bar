<template>
    <span>
        <i class='bx bx-yen'></i>{{ totalPrice | priceLocaleString }}
    </span>
</template>

<script>

import Decimal from 'decimal.js'
import { mapGetters } from 'vuex'

export default {
    name: 'SelectedProductTotalPriceItem',
    props: {
        tax: {
            type: Boolean,
            required: false,
            default: false,
        },
    },
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'selectedProduct'
        ]),
        totalPrice () {
            let totalPrice = 0
            if (this.tax) {
                if (this.selectedProduct != undefined) {
                    let totalPrice = 0
                    for (const i of this.selectedProduct) {
                        if (i.taxFree) {
                            totalPrice += Number(i.fixedPrice) * i.quantity
                        } else {
                            const taxRate = new Decimal(i.tax.tax_rate / 100)
                            const total = Number(i.fixedPrice) * i.quantity
                            totalPrice += (total + Math.floor(taxRate.times(total)))
                        }
                    }
                    return totalPrice
                }
            } else {
                if (this.selectedProduct != undefined) {
                    for (const i of this.selectedProduct) {
                        totalPrice += Number(i.fixedPrice) * i.quantity
                    }
                }
            }
            return totalPrice
        }
    },
    methods: {
    }
}

</script>

<style lang="scss" scoped>
</style>
