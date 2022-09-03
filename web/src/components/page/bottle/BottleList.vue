<template>
    <div id="bottle_list_wrap">
        <b-row class="mb-3">
            <b-card class="bottle_list_filter_card">
                <!-- <b-row style="color: white;"> -->
                <b-card-title>
                    ボトル検索
                </b-card-title>
                <b-row>
                    <b-form-group v-slot="{ ariaDescribedby }">
                        <b-form-radio-group
                            id="btn-radios-1"
                            v-model="searchTypeSelected"
                            :options="searchTypeOptions"
                            :aria-describedby="ariaDescribedby"
                            name="radios-btn-default"
                            buttons
                            @change="initFilterParams"
                        ></b-form-radio-group>
                    </b-form-group>

                    <b-col lg="4" class="my-1">
                        <b-form-group
                            class="mb-0"
                            v-if="searchTypeSelected==0"
                        >
                            <b-input-group size="sm">
                                <b-form-input
                                    id="filter-input"
                                    v-model="searchNo"
                                    type="number"
                                    placeholder="会員Noを入力してください"
                                    @input="inputSearchCustomerNo"
                                ></b-form-input>
                                <b-input-group-append>
                                    <b-button :disabled="!searchNo" @click="initFilterParams">Clear</b-button>
                                </b-input-group-append>
                            </b-input-group>
                        </b-form-group>

                        <b-form-group
                            class="mb-0"
                            v-if="searchTypeSelected==1"
                        >
                            <b-input-group size="sm">
                                <b-button
                                    size="sm"
                                    @click="showAddBottleDialog"
                                    class="mzt-3"
                                    variant="primary"
                                >
                                    <b-icon
                                        icon="plus-circle"
                                        aria-hidden="true"
                                    ></b-icon> ボトルを選択
                                </b-button>

                                <b>{{ searchSelectedBottle }}</b>

                                <b-form-input
                                    id="filter-input"
                                    v-model="searchName"
                                    type="search"
                                    placeholder="商品名を入力してください"
                                    @input="inputSearchProductName"
                                ></b-form-input>
                                <b-input-group-append>
                                    <b-button :disabled="!searchName" @click="initFilterParams">Clear</b-button>
                                </b-input-group-append>
                            </b-input-group>
                        </b-form-group>
                        <b-form-group
                            class="mb-0"
                            v-if="searchTypeSelected==2"
                        >
                            <b-input-group size="sm">
                                <b-form-input
                                    id="filter-input"
                                    v-model="searchName"
                                    type="search"
                                    placeholder="顧客名を入力してください"
                                    @input="inputSearchCustomerName"
                                ></b-form-input>
                                <b-input-group-append>
                                    <b-button :disabled="!searchName" @click="initFilterParams">Clear</b-button>
                                </b-input-group-append>
                            </b-input-group>
                        </b-form-group>
                        <b-form-group
                            class="mb-0"
                            v-if="searchTypeSelected==3"
                        >
                            <b-input-group>
                                <b-form-datepicker
                                    id="filter-input"
                                    v-model="searchDate"
                                    placeholder="日付を選択してください"
                                    @input="inputSearchOpenDate"
                                ></b-form-datepicker>
                                <b-input-group-append>
                                    <b-button :disabled="!searchDate" @click="initFilterParams">Clear</b-button>
                                </b-input-group-append>
                            </b-input-group>
                        </b-form-group>
                    </b-col>
                </b-row>
            </b-card>
        </b-row>
        <b-row>
            <b-table
                hover
                :items="bottle"
                :fields="fields"
                :dark="true"
                caption-top
                :per-page="perPage"
                :current-page="currentPage"
                :filter="filter"
                :filter-included-fields="filterIncludedField"
                :filter-ignored-fields="filterIgnoreField"
                :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc"
                :sort-direction="sortDirection"
                @filtered="onFiltered"
            >

                <!-- <template #cell(customer_type)="data">
                    <b-card-text v-if="data.value == 0">
                        非会員
                    </b-card-text>
                    <b-card-text v-else>
                        会員
                    </b-card-text>
                </template> -->

                <template #cell(custoner_no)="data">
                    <b-card-text v-if="data.value == null">-</b-card-text>
                    <b-card-text v-else>{{ data.value }}</b-card-text>
                </template>

                <template #cell(end_flg)="data">
                    <b-card-text v-if="data.value">消込</b-card-text>
                    <b-card-text v-else>-</b-card-text>
                </template>

                <template #cell(actions)="row">
                    <!-- <b-button size="sm" @click="row.toggleDetails">
                        {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
                    </b-button> -->
                    <b-button
                        size="sm"
                        style="margin-right: 5px !important;"
                        @click="showEndBottleDialog(row)"
                        :variant="isEnd(row.item.end_flg)"
                    >
                        <b-icon
                            icon="check2-circle"
                            aria-hidden="true"
                            class="mr-1"
                        ></b-icon>
                    </b-button>
                    <b-button
                        size="sm"
                        style="margin-right: 5px !important;"
                        @click="showEditBottleDialog(row)"
                        :variant="isEndOrDelete(row.item)"
                    >
                        <b-icon
                            icon="pencil"
                            aria-hidden="true"
                            class="mr-1"
                        ></b-icon>
                    </b-button>
                    <b-button
                        size="sm"
                        class="ml-1"
                        @click="showDeleteBottleDetailDialog(row)"
                        :variant="isDanger(row.item.delete_flg)"
                    >
                        <b-icon
                            icon="trash"
                            aria-hidden="true"
                        ></b-icon>
                    </b-button>
                </template>
            </b-table>
        </b-row>
        <b-row>
            <b-col cols="5">
                <b-card-sub-title>
                    Page {{ currentPage }} of {{ Math.floor(totalRows / perPage) + 1 }}
                </b-card-sub-title>
            </b-col>
            <b-col cols="2">
                <b-pagination
                    v-model="currentPage"
                    :total-rows="totalRows"
                    :per-page="perPage"
                    align="fill"
                    size="sm"
                    class="my-0"
                ></b-pagination>
            </b-col>
            <b-col cols="5">
            </b-col>
        </b-row>

        <EndBottleDetailDialog
            ref="endBottleDetailDialog"
        />

        <CreateBottleDialog
            ref="editBottleDialog"
        />

        <DeleteBottleDetailDialog
            ref="deleteBottleDetailDialog"
        />

        <AddBottleDialog
            ref="addBottleDialog"
            @update="selectSearchBottle"
        />
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import EndBottleDetailDialog from '@/components/common/dialog/EndBottleDetailDialog'
import CreateBottleDialog from '@/components/common/dialog/CreateBottleDialog'
import DeleteBottleDetailDialog from '@/components/common/dialog/DeleteBottleDetailDialog'
import AddBottleDialog from '@/components/common/dialog/AddBottleDialog'

export default {
    name: 'BottleListItem',
    components: {
        EndBottleDetailDialog,
        CreateBottleDialog,
        DeleteBottleDetailDialog,
        AddBottleDialog
    },
    data: () => ({
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        currentPage: 1,
        totalRows: 1,
        perPage: 10,
        filter: null,
        filterIncludedField: [],
        filterIgnoreField: [],
        searchDate: null,
        searchNo: null,
        searchName: null,
        searchSelectedBottle: null,
        searchTypeSelected: 0,
        searchTypeOptions: [
            { text: '会員No', value: 0 },
            { text: '商品名', value: 1 },
            { text: '顧客名', value: 2 },
            { text: '開封日', value: 3 },
        ],
        fields: [
            {
                key: 'id',
                sortable: true,
                label: 'id',
            },
            {
                key: 'product_name',
                sortable: true,
                label: '商品名',
            },
            // {
            //     key: 'customer_type',
            //     sortable: true,
            //     label: '会員区分',
            // },
            {
                key: 'customer_no',
                sortable: true,
                label: '会員No',
            },
            {
                key: 'customer_name',
                sortable: true,
                label: '顧客名',
            },
            {
                key: 'customer_name_kana',
                sortable: true,
                label: '顧客名(カナ)',
            },
            {
                key: 'open_date',
                sortable: true,
                label: '開封日',
            },
            {
                key: 'end_flg',
                sortable: true,
                label: '消込',
            },
            {
                key: 'end_date',
                sortable: true,
                label: '消込日付',
            },
            // {
            //     key: 'waste_flg',
            //     sortable: true,
            //     label: '廃棄',
            // },
            // {
            //     key: 'delete_flg',
            //     sortable: true,
            //     label: '削除',
            // },
            {
                key: 'actions',
                label: '更新'
            }
        ],
    }),
    computed: {
        ...mapGetters([
            'bottle'
        ]),
        sortOptions() {
            // Create an options list from our fields
            return this.fields
                .filter(f => f.sortable)
                .map(f => {
                    return { text: f.label, value: f.key }
                })
        },
    },
    created () {
        // this.totalRows = this.bottle.length
        this.getAllBottle()
    },
    mounted () {
        console.log('this.bottle', this.bottle)
    },
    methods: {
        ...mapMutations([
            'setBottleList',
        ]),
        ...mapActions([
            'getBottleList',
        ]),
        isDanger (flg) {
            if (flg) {
                return 'primary'
            } else {
                return 'danger'
            }
        },
        isEnd (flg) {
            if (flg) {
                return 'primary'
            } else {
                return 'success'
            }
        },
        isEndOrDelete (item) {
            if (item.delete_flg || item.end_flg) {
                return
            } else {
                return 'primary'
            }
        },
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        showEditBottleDialog (row) {
            // console.log('row', row)
            if (row.item.delete_flg || row.item.end_flg) return
            this.$refs.editBottleDialog.open(row.item)
        },
        showDeleteBottleDetailDialog (row) {
            // console.log('row', row)
            this.$refs.deleteBottleDetailDialog.open(row.item)
        },
        showEndBottleDialog (row) {
            // console.log('row', row)
            this.$refs.endBottleDetailDialog.open(row.item)
        },
        getAllBottle () {
            this.$axios({
                method: 'GET',
                url: '/api/bottle/get_all_bottle/',
            })
            .then(res => {
                // console.log(res.data)
                this.setBottleList(res.data.bottle)
                const count = res.data.count
                this.totalRows = count
            })
            .catch(e => {
                console.log(e)
            })
        },
        inputSearchOpenDate (item) {
            this.filterIncludedField = ['open_date']
            this.filter = item.split('-').join('/')
        },
        inputSearchCustomerNo (item) {
            this.filterIncludedField = ['customer_no']
            this.filter = item
        },
        inputSearchProductName (item) {
            this.filterIncludedField = ['product_name']
            this.filter = item
        },
        inputSearchCustomerName (item) {
            this.filterIncludedField = ['customer_name', 'customer_name_kana']
            this.filter = item
        },
        initFilterParams () {
            this.filter = null
            this.searchNo = null
            this.searchDate = null
            this.searchName = null
            this.filterIncludedField = []
            this.filterIgnoreField = []
        },
        showAddBottleDialog () {
            this.$refs.addBottleDialog.open()
        },
        selectSearchBottle (item) {
            this.filterIncludedField = ['product_name']
            this.filter = item.name
            this.searchName = item.name
        }
    }
}
</script>

<style lang="scss" scoped>
    #bottle_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .bottle_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }



        .bottle_list_filter_card {
            background-color: $theme-color;
            color: white;
            margin-bottom: 20px;

            .customer_sort_input_group {
            }

            #sort-by-select {
                // color: white !important;
                color: rgba(50, 50, 50, 0.7) !important;
                // background-color: $theme-color !important;
                background-color: white !important;
                border: 1px solid rgba(200, 200, 200, 0.5);
                padding: 8px 10px;
                border-radius: 4px 0 0 4px;
                // font-size: 12px;
                transition: 0.5s;
            }
            #sort-by-select:first-child {
                font-size: 0.875rem;
            }

            #sort-by-select-asc {
                // color: white !important;
                color: rgba(50, 50, 50, 0.7) !important;
                // background-color: $theme-color !important;
                background-color: white !important;
                border: 1px solid rgba(200, 200, 200, 0.5);
                padding: 8px 10px;
                border-radius: 0 4px 4px 0;
                transition: 0.5s;
            }

        }

        .table-dark {
            background-color: $theme-color;
            --bs-table-bg: $theme-color;
        }

        select:disabled {
            opacity: 0.5 !important;
            color: #6c757d !important;
            background-color: #e9ecef !important;
            transition: 0.5s;
        }
    }



</style>
