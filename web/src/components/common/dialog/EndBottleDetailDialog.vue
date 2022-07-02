<template>
    <b-modal
        v-model="dialog"
        title="ボトルデータ空状態更新"
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
            <b-col cols="6" v-if="!this.bottleDetail.end_flg">
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
            </b-col>
        </b-row>
    </b-modal>
</template>

<script>
import _ from 'lodash'
import { mapMutations, mapActions } from 'vuex'
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
        confirmText () {
            if (this.bottleDetail.end_flg) {
                return 'ボトルの空状態を元の状態へ更新しますか？'
            } else {
                return 'ボトルを空状態に更新しますか？'
            }
        }
    },
    methods: {
        ...mapActions([
            'endBottleListAction',
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
            this.endBottleListAction(this.bottleDetail)
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
