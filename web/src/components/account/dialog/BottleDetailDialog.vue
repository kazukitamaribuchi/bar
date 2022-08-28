<template>
    <v-dialog
        v-model="dialog"
        fullscreen
        persistent
    >
        <v-card
            class="pt-3"
            flat
            v-if="bottleData != null"
        >
            <v-toolbar
                dark
                color="primary"
            >
                <v-btn
                    icon
                    dark
                    @click="close"
                >
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>ボトル情報</v-toolbar-title>
            </v-toolbar>

            <!-- <v-list-item>
                <v-list-item-content>
                    <v-card-title>
                        ボトル情報
                    </v-card-title>
                </v-list-item-content>
                <v-list-item-content>
                    <v-card-actions
                        style="justify-content: end; height: 40px;"
                    >
                        <vs-button
                            circle
                            icon
                            danger
                            @click="showDeleteConfirm"
                        >
                            <i class='bx bx-trash' ></i>
                        </vs-button>
                    </v-card-actions>
                </v-list-item-content>
            </v-list-item> -->

            <v-card-text class="text-right pb-0">
                <span style="font-size: 13px; color: rgba(40, 40, 40, 0.8);">
                    管理No: {{ bottleData.id }}
                </span>
            </v-card-text>

            <v-card-text>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>会員No</v-list-item-subtitle>
                        <v-list-item-title>{{ bottleData.customer.customer_no }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>顧客名</v-list-item-subtitle>
                        <v-list-item-title>{{ bottleData.customer.name }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>商品名</v-list-item-subtitle>
                        <div>{{ bottleData.product.name }}</div>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>開封日</v-list-item-subtitle>
                        <div>{{ bottleData.open_date }}</div>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>備考</v-list-item-subtitle>
                        <div>{{ bottleData.remarks | dispNone }}</div>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-subtitle>データ作成日時</v-list-item-subtitle>
                        <div>{{ bottleData.created_at }}</div>
                    </v-list-item-content>
                </v-list-item>
            </v-card-text>
            <v-card-actions>
                <v-btn
                    block
                    outlined
                    color="success"
                    @click="endConfirmDialog = true"
                >消込</v-btn>
            </v-card-actions>
            <v-card-actions>
                <v-btn
                    block
                    outlined
                    color="indigo"
                    @click="dialog = false"
                >閉じる</v-btn>
            </v-card-actions>
        </v-card>

        <v-dialog
            v-model="deleteConfirmDialog"
        >
            <v-card
                class="pt-3"
                flat
            >
                <v-card-title>
                    ボトルデータを削除します。<br>宜しいですか？
                </v-card-title>
                <v-card-actions>
                    <vs-button
                        transparent
                        size="large"
                        @click="deleteConfirmDialog = false"
                    >閉じる</vs-button>
                    <vs-button
                        primary
                        transparent
                        size="large"
                        @click="deleteBottle"
                    >はい</vs-button>
                </v-card-actions>

            </v-card>
        </v-dialog>

        <v-dialog
            v-model="endConfirmDialog"
        >
            <v-card
                class="pt-3"
                flat
            >
                <v-card-title>
                    ボトルを消込状態に更新します。<br>宜しいですか？
                </v-card-title>
                <v-card-actions>
                    <vs-button
                        transparent
                        size="large"
                        @click="endConfirmDialog = false"
                    >閉じる</vs-button>
                    <vs-button
                        primary
                        transparent
                        size="large"
                        @click="endBottle"
                    >はい</vs-button>
                </v-card-actions>

            </v-card>
        </v-dialog>

        <v-dialog
            v-model="updateSuccessDialog"
            persistent
        >
            <v-card
                class="pt-3"
                flat
            >
                <v-card-title>
                    データの更新に成功しました。
                </v-card-title>
                <v-card-actions>
                    <vs-button
                        primary
                        transparent
                        size="large"
                        @click="updateSuccess"
                    >はい</vs-button>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-dialog
            v-model="deleteSuccessDialog"
            persistent
        >
            <v-card
                class="pt-3"
                flat
            >
                <v-card-title>
                    データの削除に成功しました。
                </v-card-title>
                <v-card-actions>
                    <vs-button
                        primary
                        transparent
                        size="large"
                        @click="deleteSuccess"
                    >はい</vs-button>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-snackbar
            v-model="snackbar"
            timeout="2000"
        >
            データの更新に失敗しました。
            <template v-slot:action="{ attrs }">
                <v-btn
                    color="pink"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                >Close</v-btn>
            </template>
        </v-snackbar>
    </v-dialog>
</template>

<script>

    export default {
        name: 'CustomerDetailDialogItem',
        props: {
        },
        data: () => ({
            dialog: false,
            bottleData: null,
            // info: null,
            loading: false,
            updateDialog: false,
            endConfirmDialog: false,
            updateSuccessDialog: false,
            deleteConfirmDialog: false,
            snackbar: false,
            deleteSuccessDialog: false,
        }),
        computed: {
        },
        methods: {
            open (bottleData) {
                // this.loading = true

                this.bottleData = bottleData
                // this.$axios({
                //     method: 'get',
                //     url: `/api/customer/${customer.id}/`
                // })
                // .then(res => {
                //     console.log(res)
                //     this.info = res.data
                //     this.loading = false
                // })
                // .catch(e => {
                //     console.log(e)
                //     this.loading = false
                // })
                this.dialog = true
            },
            close () {
                // this.init()
                this.dialog = false
            },
            init () {
                // this.bottleData = null
            },
            showDeleteConfirm () {
                this.deleteConfirmDialog = true
            },
            deleteBottle () {
                this.deleteConfirmDialog = false
                this.$axios({
                    method: 'delete',
                    url: `/api/bottle/${this.bottleData.id}/`
                })
                .then(res => {
                    console.log(res)
                    this.deleteSuccessDialog = true
                })
                .catch(e => {
                    console.log(e)
                    this.snackbar = true
                })
            },
            deleteSuccess () {
                this.$emit('deleteBottleSuccess', this.bottleData)
                this.deleteSuccessDialog = false
                this.close()
            },
            endBottle () {
                this.$axios({
                    method: 'put',
                    url: '/api/bottle/end_bottle_data/',
                    data: {
                        id: this.bottleData.id,
                        endDate: '',
                    }
                })
                .then(res => {
                    console.log(res)
                    this.updateSuccessDialog = true
                })
                .catch(e => {
                    console.log(e)
                    this.snackbar = true
                })
            },
            updateSuccess () {
                this.$emit('deleteBottleSuccess', this.bottleData)
                // this.$emit('updateBottleSuccess', this.bottleData)
                this.updateSuccessDialog = false
                this.close()
            },
        }
    }

</script>

<style lang="scss" scoped>
    .con-content {
        width: 100%;
        p {
            font-size: .8rem;
            padding: 0px 10px;
            .vs-checkbox-label {
                font-size: .8rem;
            }
            .vs-input-parent {
                width: 100%;
            }
            .vs-input-content {
                margin: 10px 0px;
                width: calc(100%);
                .vs-input {
                    width: 100%;
                }
            }
        }
    }

    .con-footer {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        .vs-button {
            margin: 0px;
            .vs-button__content {
                padding: 10px 30px;
            }
        }
    }
</style>
