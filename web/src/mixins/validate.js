import { Const } from '@/assets/js/const'
const Con = new Const()
export default {
    methods: {
        validateName (value, required) {
            const reg = /^[\wＡ-Ｚａ-ｚ\sぁ-んーァ-ヶーｱ-ﾝﾞﾟ一-龠]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.Name.Incorrect
                } else {
                    return ''
                }
            } else {
                if (!required) {
                    return ''
                } else {
                    return Con.ERROR_MSG.Name.NoInput.replace('{}', '名前')
                }
            }
        },
        validateNameKana (value) {
            const reg = /^[ぁ-んーァ-ヶーｱ-ﾝﾞﾟ]+[\s]*[ぁ-んーァ-ヶーｱ-ﾝﾞﾟ]*$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.NameKana.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
                // return Con.ERROR_MSG.NameKana.NoInput.replace('{}', '名前(カナ)')
            }
        },
        validateRealName (value, kana) {
            const reg = /^[\wＡ-Ｚａ-ｚ\sぁ-んーァ-ヶーｱ-ﾝﾞﾟ一-龠]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.RealName.Incorrect
                } else {
                    return ''
                }
            } else {
                if (kana != '') {
                    return Con.ERROR_MSG.RealName.Illegal
                } else {
                    return ''
                }
            }
        },
        validateRealNameKana (value, name) {
            const reg = /^[ぁ-んーァ-ヶーｱ-ﾝﾞﾟ]+[\s]*[ぁ-んーァ-ヶーｱ-ﾝﾞﾟ]*$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.RealNameKana.Incorrect
                } else {
                    if (name == '') {
                        return Con.ERROR_MSG.RealNameKana.Illegal
                    } else {
                        return ''
                    }
                }
            } else {
                return ''
                // return Con.ERROR_MSG.NameKana.NoInput.replace('{}', '名前(カナ)')
            }
        },
        validateNum (value) {
            const reg = /^[0-9]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (value <= 0 || !reg.test(value)) {
                    return Con.ERROR_MSG.Num.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
            }
        },
        validateAge (value) {
            const reg = /^[0-9]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (value <= 0 || !reg.test(value) || value >= 120) {
                    return Con.ERROR_MSG.Age.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
            }
        },
        validatePhone (value) {
            const reg = /^0\d{9,10}$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.Phone.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
            }
        },
        validateMail (value) {
            const reg = /^[A-Za-z0-9]{1}[A-Za-z0-9_.-]*@{1}[A-Za-z0-9_.-]+.[A-Za-z0-9]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.Mail.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
            }
        },
        validateBirthday (value) {
            console.log('value', value)
            const reg = /^[0-9]+$/
            if (value == null) {
                return ''
            }

            if (value.length > 0) {
                if (!reg.test(value)) {
                    return Con.ERROR_MSG.Mail.Incorrect
                } else {
                    return ''
                }
            } else {
                return ''
            }
        }
    }
}
