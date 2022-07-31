<template>
    <div id="login_wrap">
        <v-container class="pa-9">
            <div class="logo_area">
                <div class="logo">
                    <v-img
                        style="margin: 0 auto;"
                        height="50px"
                        width="50px"
                        src="http://localhost:8000/media/upload/logo2.jpg"
                    ></v-img>
                </div>
                <div class="logo_text">
                    alpha pos
                </div>
            </div>

            <v-row>
                <v-col/>
                <v-col
                    cols="10"
                    xs="10"
                    sm="8"
                    md="6"
                    :key="center"
                    :align-self="center"
                >
                    <vs-input
                        class="my-3"
                        v-model="credentials.username"
                        placeholder="User name"
                        @keyup.enter="checkLogin"
                        @keypress="setlogin1"
                    >
                        <template #icon>
                            <i class='bx bx-user'></i>
                        </template>
                    </vs-input>

                    <vs-input
                        class="my-3"
                        v-model="credentials.password"
                        placeholder="Password"
                        @keyup.enter="checkLogin"
                        @keypress="setlogin2"
                    >
                        <template #icon>
                            <i class='bx bx-lock-open-alt'></i>
                        </template>
                    </vs-input>

                    <vs-button
                        class="mt-9"
                        block
                        @click="login"
                        size="large"
                    >
                        <i class='bx bxs-lock-open'></i> Login
                    </vs-button>
                </v-col>
                <v-col/>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'KitchenLoginItem',
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
                this.$router.push({name: 'KitchenHome'})
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
        height: 300px;
        padding: 100px;

        .logo {
            // line-height: 200px;
            text-align: center;
            margin: 0 auto;
        }
        .logo_text {
            // line-height: 200px;
            text-align: center;
            margin: 0 auto;
        }
    }

    .vs-input-parent::v-deep {
        width: 100%;
        .vs-input {
            width: 100%;
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
