<template>
    <v-row class="account_check_footer_wrap">
        <v-col
            cols="7"
            class="account_detail pr-0"
            v-if="mode == 0"
        >
            <v-card-subtitle class="ma-0 pb-1 pt-0 px-0">
                注文数 : {{ totalOrder }}点
            </v-card-subtitle>
            <v-card-subtitle class="ma-0 pb-1 pt-0 px-0">
                合計(税抜) : <i class='bx bx-yen'></i>{{ totalPrice | priceLocaleString }}
            </v-card-subtitle>
            <v-card-subtitle class="ma-0 py-0 px-0">
                合計(税込) : <i class='bx bx-yen'></i>{{ totalTaxPrice | priceLocaleString }}
            </v-card-subtitle>
        </v-col>
        <v-col
            v-else
            cols="7"
            class="account_close_cancel pr-0"
            @click="accountCloseCancel"
        >
            <p class="account_close_cancel_text">キャンセル</p>
        </v-col>
        <v-col
            cols="5"
            class="account_check"
            @click="accountCloseCheck"
            :class="{account_close_confirm: isAccountClose}"
        >
            <p class="account_check_text">{{ accountCloseText }}</p>
        </v-col>

        <v-dialog
            v-model="dialog"
        >
            <!-- <div class="con-content">
                締め処理を行います。<br>
                宜しいですか？
            </div>
            <template #footer>
                <div class="con-footer">
                    <vs-button
                        transparent
                        size="large"
                        @click="dialog = false"
                    >いいえ</vs-button>
                    <vs-button
                        primary
                        transparent
                        size="large"
                        @click="closeAccount"
                    >はい</vs-button>
                </div>
            </template> -->
            <v-card>
                <v-card-title>
                    締め処理を行います。<br>
                    宜しいですか？
                </v-card-title>
                <v-card-actions>
                    <v-row class="ma-0">
                        <v-col class="ma-0">
                            <v-btn
                                block
                                color="blue-grey"
                                @click="dialog = false"
                                dark
                            >
                                いいえ
                            </v-btn>
                        </v-col>
                        <v-col class="ma-0">
                            <v-btn
                                block
                                color="primary"
                                @click="closeAccount"
                            >
                                はい
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>

import { mapGetters, mapMutations } from 'vuex'

export default {
    name: 'EndSalesFooterItem',
    props: {
        totalOrder: {
            type: Number,
            required: true,
        },
        totalPrice: {
            type: Number,
            required: true,
        },
        totalTaxPrice: {
            type: Number,
            required: true,
        },
        mode: {
            type: Number,
            required: true,
        }
    },
    data: () => ({
        dialog: false,
        dialogText: '',
        sendStatus: false,
    }),
    components: {
    },
    computed: {
        accountCloseText () {
            if (this.mode == 1) {
                return '会計締め'
            }
            return '会計'
        },
        isAccountClose () {
            if (this.mode == 1) {
                return true
            }
            return false
        }
    },
    methods: {
        ...mapMutations([
        ]),
        accountCloseCheck () {
            if (this.isAccountClose) {
                this.dialog = true
            } else {
                this.$emit('changeMode', 1)
            }
        },
        closeAccount () {
            this.$emit("closeAccount")
            this.dialog = false
        },
        toHome () {
            if (this.sendStatus) {
                this.$router.push({
                    name: 'AccountHome',
                })
            }
            this.dialog = false
        },
        accountCloseCancel () {
            this.$emit('changeMode', 0)
        }
    }
}
</script>

<style lang="scss" scoped>
    .account_check_footer_wrap {
        margin: 0;
        z-index: 1000;
        position: fixed;
        height: 110px;
        width: 100%;
        bottom: 0;
        background: white;

        .account_detail {
            background-color: rgb(142, 142, 142);
            color: white;
            padding-left: 30px;
            padding-top: 15px;
        }

        .account_close_cancel {
            background-color: rgba(142, 142, 142, 1);
            color: white;
            cursor: pointer;
            .account_close_cancel_text {
                line-height: 85px;
                text-align: center;
                padding-bottom: 0;
                margin-bottom: 0;
            }
        }

        .account_close_cancel:hover {
            // background-color: rgba(193, 60, 60, 1);
            background-color: rgba(142, 142, 142, 0.6);
            transition: 0.5s;
        }

        .account_check {
            cursor: pointer;
            border-left: 1px solid rgba(112, 104, 104, 0.7);
            // background-color: rgba(193, 80, 80, 0.7);
            background-color: rgba(0, 78, 227, 0.7);
            color: white;
            .account_check_text {
                line-height: 85px;
                text-align: center;
                padding-bottom: 0;
                margin-bottom: 0;
            }
        }
        .account_check:hover {
            // background-color: rgba(193, 60, 60, 1);
            background-color: rgba(0, 78, 227, 1);
            transition: 0.5s;
        }
        .account_close_confirm {
            background-color: rgba(193, 80, 80, 1);
        }
        .account_close_confirm:hover {
            background-color: rgba(243, 80, 80, 1);
            transition: 0.5s;
        }
    }

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
