<template>
    <div id="login_wrap">
        <v-container>

            <div class="logo_area">
                <div class="logo">
                    LOGO
                </div>
            </div>

            <vs-input v-model="value1" placeholder="User name">
                <template #icon>
                    <i class='bx bx-user'></i>
                </template>
            </vs-input>

            <vs-input type="password" v-model="value2" placeholder="Password">
                <template #icon>
                    <i class='bx bx-lock-open-alt'></i>
                </template>
            </vs-input>

            <vs-button
                block
            >
            <i class='bx bxs-paint-roll' ></i> Edit Theme
            </vs-button>
        </v-container>

        <!-- <b-card
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
        </b-card> -->
    </div>

</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'AccountLoginItem',
    data: () => ({
        credentials: {
        },
        usernameError: '',
        passwordError: '',
        loginNameValue: false,
        loginPassValue: false,
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
                return
            }
            this.checkAuthToken(this.credentials)
            .then(res => {
                this.initState()
                this.credentials = {
                }
                this.$router.push({name: 'AccountHome'})
            })
            .catch(e => {
                console.log(e)
            })
        },
    }
}
</script>

<style lang="scss" scoped>
#login_wrap {
    // height: 100%;

    .logo_area {
        height: 200px;

        .logo {
            line-height: 200px;
            text-align: center;
            margin: 0 auto;
        }
    }

    // .input-group-text {
    //     height: 100%;
    //     border-radius: 5px 0 0 5px !important;
    // }
    //
    // .card-title {
    //     text-align: center;
    //     font-size: 20px;
    //     margin: 40px auto 30px;
    // }
    //
    // .card-body {
    //     padding: 0.5rem 3rem;
    // }
    //
    // .login_card {
    //     // width: 500px;
    //     margin: 0 auto;
    //     border: none;
    // }
    //
    // .submit_btn {
    //     margin: 1.5rem auto 2rem;
    //     width: 40%;
    //     display: block;
    // }
}
</style>
