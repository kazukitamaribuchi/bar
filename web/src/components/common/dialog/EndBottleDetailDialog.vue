<template>
    <b-modal
        v-model="dialog"
        title="ボトルデータ消込状態更新"
        @ok="endBottleDetail"
        ok-title="はい"
        cancel-title="キャンセル"
    >
        <b-row>
            <b-col cols="12">
                <b-card-text>
                    {{ confirmText }}
                </b-card-text>
            </b-col>
            <!-- <b-col cols="6" v-if="!this.bottleDetail.end_flg">
                <b-card-sub-title
                    class="form_required"
                >
                    飲み終えた日付
                </b-card-sub-title>
                <b-form-datepicker
                    v-model="bottleDetail.endDate"
                    placeholder="日付を選択してください"
                    class="mt-1"
                ></b-form-datepicker>
            </b-col> -->
        </b-row>
    </b-modal>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import dayjs from 'dayjs'
const now = dayjs().format('YYYY-MM-DD')

export default {
    name: 'EndBottleDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        bottleDetail: {},
    }),
    computed: {
        ...mapGetters([
            'customer',
        ]),
        confirmText () {
            if (this.bottleDetail.end_flg) {
                return 'ボトルデータの消込を解除します。よろしいですか？'
            } else {
                return 'ボトルデータの消込を行います。よろしいですか？'
            }
        }
    },
    methods: {
        ...mapActions([
            'endBottleListAction',
        ]),
        ...mapMutations([
            'deleteCustomerBottle',
        ]),
        open (data) {
            this.dialog = true
            this.bottleDetail = _.cloneDeep(data)
            let endData = this.bottleDetail.end_date
            if (endData == null || endData == '') {
                this.bottleDetail.endDate = now
            } else {
                this.bottleDetail.endDate = endData.replace('年', '-').replace('月', '-').replace('日', '')
            }
        },
        close () {
            this.dialog = false
            this.bottleDetail = {}
        },
        endBottleDetail () {
            console.log('this.bottleDetail', this.bottleDetail)
            this.endBottleListAction(this.bottleDetail)

            // 顧客データが持つボトルデータも
            this.deleteCustomerBottle(this.bottleDetail.id)

            this.$emit('deleteCustomerBottleDetail', this.bottleDetail)
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
    .form_required:after{
        content: '*';
        color: red;
    }
</style>
