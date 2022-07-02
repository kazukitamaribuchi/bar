<template>
    <b-modal
        v-model="dialog"
        title="キャスト追加"
        header-bg-variant="primary"
        header-text-variant="light"
        ok-title="追加"
        cancel-title="閉じる"
        size="lg"
    >
        <b-row>
            <b-col cols="6">
                <b-input-group>
                    <b-input-group-prepend is-text>
                        <b-icon icon="search"></b-icon>
                    </b-input-group-prepend>
                    <b-form-input
                        v-model="searchWord"
                        type="text"
                        placeholder="キャスト名で検索"
                    ></b-form-input>
                </b-input-group>
            </b-col>
            <b-col cols="6" align="right">
                <b-button
                    variant="outline-primary"
                >
                    <b-icon
                        icon="filter"
                    ></b-icon>
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col
                cols="3"
                v-for="item in filterdCast"
                :key=item.id
            >
                <b-card
                    class="addCastCard"
                    @click="select(item)"
                    @dblclick="addOrUpdate"
                    :class="{'isAppointed': isAppointed(item)}"
                >
                    <!-- <b-card-img
                        :src="apiPath + item.icon"
                        alt="castImage"
                        top
                        height="100px"
                        :class="{'isAppointed': isAppointed(item)}"
                        v-if="item.icon != null"
                    ></b-card-img>
                    <b-card-img
                        :src="defaultIcon"
                        alt="castImage"
                        top
                        height="100px"
                        :class="{'isAppointed': isAppointed(item)}"
                        v-else
                    ></b-card-img> -->
                    <div style="text-align: center;">
                        <img
                            src="@/assets/img/女性11.jpg"
                            class="cast_icon"
                            top
                        >
                    </div>
                    <b-card-text>
                        {{ item.name }} ({{ item.age }})
                        <!-- <span><small>{{ getIsAppointedStr(item) }}</small></span> -->
                    </b-card-text>
                </b-card>
            </b-col>
        </b-row>
        <template #modal-footer>
            <b-container fluid>
            <b-row>
                <b-col cols="3" class="add_cast_footer_col">
                    <b-card-sub-title>選択キャスト</b-card-sub-title>
                    <div class="selected_cast_area">
                        <img
                            src="@/assets/img/女性11.jpg"
                            class="selected_cast_icon"
                            top
                        >
                        <!-- <b-avatar :src="apiPath + selected.icon" v-if="selected.icon != null"></b-avatar>
                        <b-avatar :src="defaultIcon" v-else></b-avatar> -->
                        <span v-if="Object.keys(selected).length">{{ selected.name }}</span>
                        <span v-else> - </span>
                    </div>
                </b-col>
                <b-col cols="9" class="add_cast_footer_col">
                    <b-row align="center">
                        <b-col cols="7" class="add_cast_footer_col">
                            <b-card-sub-title>指名タイプ</b-card-sub-title>
                            <b-form-group>
                                <b-form-radio-group
                                    v-model="appointType"
                                    :options=appointOptions
                                    buttons
                                    button-variant="primary"
                                ></b-form-radio-group>
                            </b-form-group>
                        </b-col>
                        <b-col class="add_cast_footer_col">
                            <!-- <b-card-sub-title>同伴出勤</b-card-sub-title> -->
                            <b-form-group>
                                <b-form-checkbox-group
                                    style="margin-top: 14px;"
                                    v-model="isDouhan"
                                    :options=douhanOptions
                                    buttons
                                    button-variant="primary"
                                    @change="douhanClick"
                                ></b-form-checkbox-group>
                            </b-form-group>
                        </b-col>
                        <b-col class="add_cast_footer_col">
                            <b-card-sub-title>数量</b-card-sub-title>
                            <b-form-group
                            >
                                <SelectForm
                                    :optionType=99
                                    v-model="quantity"
                                />
                            </b-form-group>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="add_cast_footer_bottom_area mt-5">
                <b-col align="right" class="add_cast_footer_col">
                    <b-button
                        variant="secondary"
                        @click="close"
                        class="btn_close add_cast_footer_area4"
                    >
                        閉じる
                    </b-button>
                    <b-button
                        variant="primary"
                        @click="addOrUpdate"
                        class="add_cast_footer_area4"
                        :disabled=isDisabled
                    >
                        追加
                    </b-button>
                </b-col>
            </b-row>
            </b-container>
        </template>
    </b-modal>
</template>

<script>
import SelectForm from '@/components/common/parts/SelectForm'
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'InputSalesAddCastDialogItem',
    props: {
        appointed: {
            type: Array,
            required: true,
            default: () => ([])
        },
    },
    components: {
        SelectForm,
    },
    data: () => ({
        dialog: false,
        selected: {},
        filterdCast: [],
        searchWord: '',
        appointType: 0,
        appointedCastId: new Set(),
        isDouhan: [],
        douhanOptions: [
            { text: '同伴', value: 1 }
        ],
        appointOptions: [
            { text: '指名', value: 0 },
            { text: '本指名', value: 1 },
            { text: '場内指名', value: 2 },
        ],
        defaultIcon: 'http://localhost:8000/media/upload/女性1111.png',
        apiPath: 'http://localhost:8000',
        quantity: 1,
        mode: 0,
        editIdx: 0,
    }),
    computed: {
        ...mapGetters([
            'cast',
        ]),
        isDisabled () {
            if (this.isEmptyObject(this.selected)) return true
            return false
        },
    },
    watch: {
        searchWord: function (val) {
            if (val.length > 0) {
                this.search(val)
            } else {
                // このメソッドは重くないか?
                this.filterdCast = _.cloneDeep(this.cast)
            }
        }
    },
    created () {
        // console.log(this.cast)
        // this.filterdCast = _.cloneDeep(this.cast)
    },
    methods: {
        open (data, idx) {
            this.dialog = true
            this.filterdCast = _.cloneDeep(this.cast)
            this.appointedCastId = new Set()
            for (const i in this.appointed) {
                const item = this.appointed[i]
                this.appointedCastId.add(item.cast.id)
            }
            if (data) {
                this.convertData(data)
                this.mode = 1
                this.editIdx = idx
            } else {
                this.mode = 0
            }
        },
        close () {
            this.dialog = false
            this.init()
        },

        addOrUpdate () {
            if (this.mode == 0) {
                this.add()
            } else if (this.mode == 1) {
                this.update()
            }
        },
        // 指名料の税を可変にする場合ここで考慮する必要あり

        add () {
            let douhan = this.isDouhan.length !== 0
            let douhanPrice = (douhan) ? Con.DOUHAN_PRICE : 0
            const castData = {
                cast: this.selected,
                appointType: this.appointType,
                isDouhan: douhan,
                appointPrice: Con.APPOINT_PRICE,
                douhanPrice: douhanPrice,
                quantity: this.quantity,
            }
            // this.$eventHub.$emit('addCast', castData)
            this.$emit('add', castData)
            this.close()
        },
        update () {
            let douhan = this.isDouhan.length !== 0
            let douhanPrice = (douhan) ? Con.DOUHAN_PRICE : 0
            const castData = {
                cast: this.selected,
                appointType: this.appointType,
                isDouhan: douhan,
                appointPrice: Con.APPOINT_PRICE,
                douhanPrice: douhanPrice,
                quantity: this.quantity,
            }
            // this.$eventHub.$emit('addCast', castData)
            this.$emit('update', castData, this.editIdx)
            this.close()
        },
        init () {
            this.selected = {}
            this.filterdCast = {}
            this.searchWord = ''
            this.appointType = 0
            this.isDouhan = []
            this.appointedCastId = new Set()
            this.errorMsg = []
            this.quantity = 1
            this.editIdx = 0
            this.mode = 0
        },
        select (item) {
            if (this.isAppointed(item)) return
            this.selected = item
        },
        search: _.debounce(function search (searchText) {
            const targetCastList = _.cloneDeep(this.cast)
            const reg = new RegExp("^" + searchText)
            const res = targetCastList.filter(target => {
                // 検索に本名は含める？・・・
                if (target.name.match(reg) || target.real_name.match(reg)) {
                    return true
                }
            }, 4000)
            this.filterdCast = res
        }),
        getIsAppointedStr (cast) {
            if (this.isAppointed(cast)) return '選択済み'
            return ''
        },
        isAppointed (cast) {
            if(this.appointedCastId.has(cast.id)) return true
            return false
        },
        isEmptyObject (obj) {
            return !Object.keys(obj).length
        },
        douhanClick () {
            if (this.isDouhan.length != 0) {
                this.appointType = 1
            }
        },
        convertData (data) {
            console.log('convertData', data)
        }
    },
}

</script>

<style lang="scss" scoped>

.input-group-text {
    height: 100%;
    border-radius: 5px 0 0 5px !important;
}

.addCastCard {
    cursor: pointer;
}

.addCastCard:hover {
    box-shadow: 1px 1px 2px 1px rgba(150, 150, 150, 0.5);
}

.add_cast_footer_col {
    margin: 0;
    padding: 0;
}

.btn_close {
    display: inline-block;
    margin-right: 8px;
}

.selected_cast_area {
    margin-top: 2px;
}

.add_cast_footer_area3 {
    display: inline-block;
}

.add_cast_stay_hour {
    height: 38px;
    padding: 4px 9px;
    border-radius: 3px;
    border: 1px solid rgba(125, 125, 125, 0.6);
}

.add_cast_footer_area4 {
    margin-top: 15px;
    margin-bottom: 13px;
}

.add_cast_footer_bottom_area {
    margin-top: 20px;
    border-top: 1px solid rgba(155, 155, 155, 0.5);
}

.isAppointed {
    background-color: rgba(255, 255, 255, 1);
    filter: opacity(30%);
}

.cast_icon {
    width: 120px;
    height: 120px;
}

.selected_cast_icon {
    border-radius: 50%;
    width: 40px;
    height: 40px;
}
</style>
