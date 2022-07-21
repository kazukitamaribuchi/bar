<template>
    <span>
        {{ totalCnt }}
    </span>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
    name: 'SelectedProductTotalCntItem',
    props: {

    },
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'selectedProduct'
        ]),
        totalCnt () {
            if (this.selectedProduct != undefined) {
                let totalCnt = 0
                for (const i of this.selectedProduct) {
                    totalCnt += i.quantity
                }
                return totalCnt
            }
            return 0
        }
    },
    methods: {
    }
}

</script>

<style lang="scss" scoped>
</style>
