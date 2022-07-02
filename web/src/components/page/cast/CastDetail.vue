<template>
    <div id="cast_detail_wrap">
        <b-row>
            <b-tabs pill>
                <b-tab
                    title="キャスト詳細"
                >
                    <b-card
                        class="cast_detail_area"
                    >
                        <b-container fluid>
                            <b-row>
                                <b-col cols="5">
                                    <b-card-title>
                                        キャスト詳細
                                    </b-card-title>
                                    <div style="display: flex; margin-left: 30px; margin-top: 30px;">
                                        <div>
                                            <img
                                                src="@/assets/img/女性11.jpg"
                                                class="cast_list_area_cast_icon"
                                                top
                                            >
                                        </div>
                                        <div class="mt-3" style="margin-left: 15px;">
                                            <b style="font-size: 20px;">
                                                {{ castData.name }}
                                            </b>
                                            <b-card-sub-title>
                                                {{ getStrInData(castData.name_kana) }}
                                            </b-card-sub-title>
                                        </div>
                                    </div>
                                </b-col>
                                <b-col cols="2" style="padding-top: 70px;">
                                    <b-card-sub-title>
                                        年齢
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;">
                                        {{ getStrInData(castData.age) }} 歳
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2" style="padding-top: 70px;">
                                    <b-card-sub-title>
                                        誕生日
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;">
                                        {{ getStrInData(castData.birthday) }}
                                    </b-card-text>
                                </b-col>
                                <b-col cols="1" style="padding-top: 70px;">
                                    <b-card-sub-title>
                                        経験
                                    </b-card-sub-title>
                                    <b-card-text style="font-size: 24px;" v-if="castData.experienced">
                                        有
                                    </b-card-text>
                                    <b-card-text style="font-size: 24px;" v-else>
                                        無
                                    </b-card-text>
                                </b-col>
                                <b-col cols="2" align-self="stretch">
                                    <b-button
                                        size="sm"
                                        @click="showEditCastDialog"
                                    >
                                        <b-icon
                                            icon="pencil"
                                            aria-hidden="true"
                                        ></b-icon> 編集
                                    </b-button>
                                    <b-button
                                        size="sm"
                                        style="position: relative; left: 10px;"
                                        @click="showDeleteCastDetailDialog"
                                    >
                                        <b-icon
                                            icon="trash"
                                            aria-hidden="true"
                                        ></b-icon> 削除
                                    </b-button>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-tabs pill card fill>
                                    <b-tab
                                        title="詳細情報"
                                    >
                                        <!-- <b-card-text
                                            style="border-bottom: 1px solid rgba(200, 200, 200, 0.1); margin-top: 10px; padding-bottom: 14px;"
                                        >
                                            個人情報
                                        </b-card-text> -->
                                        <b-row>
                                            <b-col cols="7">
                                                <b-card-sub-title class="mt-3" style="font-size: 15px;">
                                                    本名
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(castData.real_name) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    実年齢
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(castData.real_age) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    住所
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(castData.address) }}
                                                </b-card-title>


                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    備考
                                                </b-card-sub-title>
                                                <b-card-text style="font-size: 20px; white-space: pre-line;">
                                                    {{ castData.remarks }}
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="5">
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    電話番号
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(castData.phone) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    メールアドレス
                                                </b-card-sub-title>
                                                <b-card-title style="font-size: 20px;">
                                                    {{ getStrInData(castData.mail) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    勤務開始日
                                                </b-card-sub-title>
                                                <b-card-title  style="font-size: 20px;">
                                                    {{ getStrInData(castData.start_working_date) }}
                                                </b-card-title>
                                                <b-card-sub-title class="mt-4" style="font-size: 15px;">
                                                    退職
                                                </b-card-sub-title>
                                                <b-card-title  style="font-size: 20px;" v-if="castData.resign_flg">
                                                    退職済 {{ castData.resign_date }}
                                                </b-card-title>
                                                <b-card-title  style="font-size: 20px;" v-else-if="castData.resign_date != null && castData.resign_date != ''">
                                                    退職予定 {{ castData.resign_date }}
                                                </b-card-title>
                                                <b-card-title  style="font-size: 20px;" v-else>
                                                    -
                                                </b-card-title>
                                            </b-col>
                                        </b-row>
                                    </b-tab>
                                    <b-tab
                                        title="指名データ"
                                    >
                                    </b-tab>
                                    <b-tab
                                        title="売上データ"
                                    >
                                    </b-tab>
                                </b-tabs>
                            </b-row>
                        </b-container>
                    </b-card>
                </b-tab>
            </b-tabs>
        </b-row>


        <CreateCastDialog
            ref="createCast"
            @update="castData = $event"
        />

        <DeleteCastDetailDialog
            ref="deleteCastDetailDialog"
        />
    </div>
</template>

<script>
import CreateCastDialog from '@/components/common/dialog/CreateCastDialog'
import { mapGetters } from 'vuex'
import _ from 'lodash'
import utilsMixin from '@/mixins/utils'
import DeleteCastDetailDialog from '@/components/common/dialog/DeleteCastDetailDialog'

export default {
    name: 'CastDetailItem',
    data: () => ({
        castId: '',
        castData: {},
        editCastData: {},
        colorx: 'rgb(16, 16, 179)',
        editCastDialog: false,
    }),
    props: {
    },
    components: {
        CreateCastDialog,
        DeleteCastDetailDialog,
    },
    computed: {
        ...mapGetters([
            'cast',
        ]),
        backColorBasis () {
            return 'light'
        },
        textColorBasis () {
            return 'black'
        },
        backColorHeaderBasis () {
            return 'dark'
        },
        backColorHeaderRank () {
            return 'dark'
        },
        backColorRank () {
            return 'light'
        },
        textColorRank () {
            return 'black'
        },
    },
    created () {
        // this.$axios({
        //     method: 'GET',
        //     url: `/api/customer/${this.$route.params['id']}`,
        // })
        // .then(res => {
        //     console.log(res)
        //     this.customerData = _.cloneDeep(res.data)
        //     this.isDanger = this.customerData.caution_flg
        // })
        // .catch(e => {
        //     console.log(e)
        // })
        // 検索から詳細きてうまくいかせるやり方わかったら、↓の様にstoreから取得する方法に切り替え
        this.castData = _.cloneDeep(this.cast.find(c => c.id == this.$route.params['id']))
    },
    mounted () {
        // console.log(this.$router.referrer)
        // console.log(this.$router.toPage)
    },
    // beforeRouteUpdate (to, from, next) {
    //     this.cusotmerId = to.query.id
    //     this.customerData = _.cloneDeep(this.customer.find(c => c.id === this.customerId))
    //     console.log(this.customer)
    //     console.log(this.customerId)
    //     console.log(this.customerData)
    //     next()
    // },
    methods: {
        showEditCastDialog () {
            this.$refs.createCast.open(this.castData)
        },
        showDeleteCastDetailDialog () {
            this.$refs.deleteCastDetailDialog.open(this.castData)
        },
    },
    mixins: [
        utilsMixin
    ]
}
</script>

<style lang="scss" scoped>
    #cast_detail_wrap {
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        color: white;
        padding: 20px;

        .btn-secondary {
            background-color: $theme-color;
            border-color: $theme-color;
        }

        .cast_detail_area {
            background-color: $theme-color;
            padding: 0;
            margin: 0;

            .cast_detail_cast_icon {
                border-radius: 50%;
                width: 100px;
                height: 100px;
            }
        }

        // .customer_detail {
        //     background-color: $theme-color;
        //     height: 100%;
        //
        //     .customer_detail_card_body {
        //         padding: 0 1.5rem;
        //
        //
        //         .input-group-text {
        //             height: 100%;
        //             border-radius: 5px 0 0 5px !important;
        //         }
        //
        //         .customer_detail_age {
        //             width: 6rem;
        //         }
        //
        //         .customer_detail_birthday {
        //             width: 8rem;
        //         }
        //
        //         .customer_detail_job {
        //             width: 12rem;
        //         }
        //
        //         .customer_detail_rank_detail {
        //             display: block;
        //         }
        //
        //     }
        //
        // }

    }


    .cast_list_area_cast_icon {
        border-radius: 50%;
        width: 140px;
        height: 140px;
        // box-shadow: 1px 1px 2px 1px rgba(100, 100, 100, 0.5);
        // border: 1px solid rgba(100, 100, 100, 0.3);
    }
</style>
