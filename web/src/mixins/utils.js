import Decimal from 'decimal.js'
export default {
    methods: {
        calcAddTaxPrice (price, tax) {
            let taxRate = new Decimal(tax / 100)
            return price + Math.ceil(taxRate.times(price))
        },
        calcQuantityPrice (price, quantity) {
            // return Math.ceil(new Decimal(quantity).times(price).toNumber())
            return Math.ceil(quantity * price)
        },
        roundDown (value) {
            var digitVal = Math.pow(10, -2)
            return Math.ceil(value * digitVal) / digitVal
        },
        modifyStrTime (h, m) {
            return this.padStrTime(h).concat(':', this.padStrTime(m))
        },
        padStrTime (val) {
            return ('0' + val).slice(-2)
        },
        isDiffDayTime (start, end) {
            if ((start >= 20 && start <= 24) && (end <= 7)) {
                return true
            }
            return false
        },
        isPositiveNumber (val) {
            if (val == null) return false
            return /^\d+$/.test(val)
        },
        getStrInData (val) {
            if (val == undefined || val == null || val == '') {
                return '-'
            }
            return val
        },
        getNumInData (val) {
            if (val == undefined || val == null || val == '') {
                return '0'
            }
            return val
        },
    }
}
