<template>
    <div id="login_wrap">
        <b-card
            title="Login"
            class="login_card"
        >
            <b-form>
                <b-form-group
                    class="login_input"
                >
                    <b-input-group>
                        <b-input-group-prepend is-text>
                            <b-icon icon="person-fill"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input
                            v-model="credentials.username"
                            type="text"
                            placeholder="username"
                            required
                            :state="nameState"
                            @keyup.enter="checkLogin"
                            @keypress="setlogin1"
                        ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback">
                            {{ usernameError }}
                        </b-form-invalid-feedback>
                    </b-input-group>
                </b-form-group>

                <b-form-group
                    class="password_input mt-3 mb-3"
                >
                    <b-input-group>
                        <b-input-group-prepend is-text>
                            <b-icon icon="lock-fill"></b-icon>
                        </b-input-group-prepend>
                        <b-form-input
                            v-model="credentials.password"
                            type="password"
                            placeholder="password"
                            :state="passState"
                            required
                            @keyup.enter="checkLogin"
                            @keypress="setlogin2"
                        ></b-form-input>
                        <b-form-invalid-feedback id="input-live-feedback">
                            {{ passwordError }}
                        </b-form-invalid-feedback>
                    </b-input-group>
                </b-form-group>

                <b-button
                    block
                    variant="primary"
                    class="submit_btn"
                    @click="login"
                >Login</b-button>
            </b-form>
        </b-card>

        <b-modal
            v-model="loginFailureDialog"
            hide-header
        >
            <div>
                ログインに失敗しました。
                IDとパスワードを確認してください。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="loginFailureDialog = false"
                        >
                            閉じる
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
    </div>

</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'LoginItem',
    data: () => ({
        credentials: {
        },
        usernameError: '',
        passwordError: '',
        loginNameValue: false,
        loginPassValue: false,
        loginFailureDialog: false,
    }),
    created () {
    },
    computed: {
        nameState () {
            if (this.credentials.username == undefined) {
                return false
            }
            if (this.credentials.username == '') {
                this.setNameErrorMsg(0)
                return false
            }
            return true
        },
        passState () {
            if (this.credentials.password == undefined) {
                return false
            }
            if (this.credentials.password == '') {
                this.setPassErrorMsg(0)
                return false
            }
            return true
        }
    },
    methods: {
        setlogin1 () {
            this.loginNameValue = true
        },
        setlogin2 () {
            this.loginPassValue = true
        },
        checkLogin () {
            if (!this.loginNameValue || !this.loginPassValue) return
            this.login()
            this.loginNameValue = false
            this.loginPassValue = false
        },
        setNameErrorMsg (val) {
            switch (val) {
                case 0:
                    this.usernameError = 'ユーザーネームを入力してください'
                    break;
                default:
            }
        },
        setPassErrorMsg (val) {
            switch (val) {
                case 0:
                    this.passwordError = 'パスワードを入力してください'
                    break;
                default:
            }
        },
        ...mapMutations([
            'initState',
        ]),
        ...mapActions([
            'checkAuthToken',
        ]),
        login () {
            // バリデーション
            if (!this.nameState
                || !this.passState
                || !this.loginNameValue
                || !this.loginPassValue) {
                    console.log('値がおかしい')
                return
            }
            console.log('ログイン試行')
            this.checkAuthToken(this.credentials)
            .then(res => {
                this.initState()
                this.credentials = {
                }
                this.$router.push({name: 'CustomerList'})
            })
            .catch(e => {
                console.log(e)
                this.loginFailureDialog = true
            })
        },
    }
}
</script>

<style lang="scss" scoped>
#login_wrap {
    height: 100%;
    padding-top: 13rem;
    // font-family: Hiragino Kaku Gothic Pro,ヒラギノ角ゴ Pro,Yu Gothic Medium,游ゴシック Medium,YuGothic,游ゴシック体,メイリオ,sans-serif;

    // background-color: $theme-color;
    background-color: $theme-color2;

    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }

    .card-title {
        text-align: center;
        font-size: 20px;
        margin: 40px auto 30px;
        // color: white;
    }

    .card-body {
        padding: 0.5rem 3rem;
    }

    .login_card {
        width: 500px;
        margin: 0 auto;

        // background-color: $theme-color2;
    }

    .submit_btn {
        margin: 1.5rem auto 2rem;
        width: 40%;
        display: block;
    }
}
</style>
