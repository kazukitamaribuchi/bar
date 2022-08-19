<template>
    <div>
        <vs-input
            class="mt-3 mb-0"
            placeholder="会員No"
            label="会員No(必須)"
            v-model="customerNo"
            @blur="focusOutCustomerNo"
        >
            <template
                v-if="custonerNoSuccess"
                #message-success
            >
                OK
            </template>
            <template
                v-if="customerNoError"
                #message-danger
            >
                {{ customerNoErrorText }}
            </template>
        </vs-input>

        <v-card
            flat
            class="mt-4"
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-subtitle>名前</v-list-item-subtitle>
                    <v-list-item-title>{{ customerName }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-subtitle>年齢</v-list-item-subtitle>
                    <v-list-item-title>{{ customerAge }}</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                    <v-list-item-subtitle>ランク</v-list-item-subtitle>
                    <v-list-item-title>{{ customerRank }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-card>
    </div>
</template>

<script>

export default {
    name: 'SearchCustomerInfoItem',
    props: {
    },
    data: () => ({
        customerNo: '',
        customerInfo: null,
        customerNoError: false,
        customerNoErrorText: '',
        custonerNoSuccess: false,
    }),
    components: {
    },
    computed: {
        customerName () {
            if (this.customerInfo != null) {
                return this.customerInfo.name
            }
            return '-'
        },
        customerAge () {
            if (this.customerInfo != null) {
                return this.customerInfo.age
            }
            return '-'
        },
        customerRank () {
            if (this.customerInfo != null) {
                return this.customerInfo.rank_name
            }
            return '-'
        },
    },
    methods: {
        toHome () {
            this.$router.push({
                name: 'AccountHome'
            })
        },
        focusOutCustomerNo () {
            if (this.customerNo != '') {
                const reg = /^[0-9]+$/
                if (this.customerNo <= 0 || !reg.test(this.customerNo)) {
                    this.showError('正しい会員Noを入力してください。')
                } else {
                    this.customerNoError = false
                    this.$axios({
                        method: 'get',
                        url: `/api/customer/${this.customerNo}/`,
                    })
                    .then(res => {
                        console.log(res)
                        this.customerInfo = res.data
                        this.custonerNoSuccess = true
                        this.$emit('updateCustomerInfo', this.customerInfo)
                    })
                    .catch(e => {
                        console.log(e)
                        this.showError('会員情報の取得に失敗しました。')
                        this.$emit('updateCustomerInfo', null)
                    })
                }

            } else {
                this.custonerNoSuccess = false
                this.hideError()
                this.$emit('updateCustomerInfo', null)
            }
        },
        showError (text) {
            this.custonerNoSuccess = false
            this.customerNoError = true
            this.customerInfo = null
            this.customerNoErrorText = text
        },
        hideError () {
            this.customerNoError = false
            this.customerInfo = null
            this.customerNoErrorText = ''
        },
        init () {
            this.customerNo = ''
            this.customerInfo = null
            this.customerNoError = false
            this.customerNoErrorText = ''
            this.custonerNoSuccess = false
        }
    }
}
</script>

<style lang="scss" scoped>
    .vs-input-parent::v-deep {
        width: 100%;
        .vs-input {
            width: 100%;
        }
    }
</style>
