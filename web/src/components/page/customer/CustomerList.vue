<template>
    <div id="customer_list_wrap">
        <div v-if="!initStatus" class="loading">
            <div class="loading_icon">
                <b-spinner
                    style="width: 6rem; height: 6rem; display: block; margin: 0 auto;"
                    label="Large Spinner"
                    variant="light"
                ></b-spinner>
            </div>
        </div>
        <b-row v-else>
            <b-tabs card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setCustomerTopActive(0)"
                >
                    <b-row class="customer_list_top">
                        <b-col cols="8">
                            <b-row>
                                <b-col cols="4">
                                    <b-card class="customer_list_area customer_list_area1">
                                        <b-container fluid class="customer_list_area1_container">
                                            <b-card-text class="mb-1">
                                                総会員数
                                            </b-card-text>
                                            <b-row v-if="loadCustomerCnt">
                                                <b-skeleton-img
                                                ></b-skeleton-img>
                                            </b-row>

                                            <b-row v-else>
                                                <b-col cols="7">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalCustomerChartOptions"
                                                        :series="totalCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="5" align="right" class="pt-4">
                                                    <b-card-title>
                                                        {{ totalCustomer }}
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="4">
                                    <b-card class="customer_list_area customer_list_area1">
                                        <b-container fluid class="customer_list_area1_container">
                                            <b-card-text class="mb-1">
                                                アクティブ会員
                                            </b-card-text>
                                            <b-row v-if="loadActiveCustomerCnt">
                                                <b-skeleton-img
                                                ></b-skeleton-img>
                                            </b-row>
                                            <b-row v-else>
                                                <b-col cols="7">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="activeCustomerChartOptions"
                                                        :series="activeCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="5" align="right" class="pt-4">
                                                    <b-card-title>
                                                        {{ totalActiveCustomer }}
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="4">
                                    <b-card class="customer_list_area customer_list_area1">
                                        <b-container fluid class="customer_list_area1_container">
                                            <b-card-text class="mb-1">
                                                ノンアクティブ会員
                                            </b-card-text>
                                            <b-row v-if="loadNonActivceCustomerCnt">
                                                <b-skeleton-img
                                                ></b-skeleton-img>
                                            </b-row>
                                            <b-row v-else>
                                                <b-col cols="7" class="px-0">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="nonActiveCustomerChartOptions"
                                                        :series="nonActiveCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="5" align="right" class="pt-4">
                                                    <b-card-title>
                                                        {{ totalNonActiveCustomer}}
                                                    </b-card-title>
                                                    <b-card-sub-title>
                                                        customers
                                                    </b-card-sub-title>
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="6">
                                    <b-card class="customer_list_area customer_list_area2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                会員年齢層
                                            </b-card-text>
                                            <b-row>
                                                <b-col>
                                                    <b-skeleton-img
                                                        v-if="loadCustomerAge"
                                                    ></b-skeleton-img>
                                                    <!-- <b-skeleton-table
                                                        v-if="loadCustomerAge"
                                                        :rows="4"
                                                        :columns="4"
                                                        :table-props="{ bordered: true, striped: true }"
                                                    ></b-skeleton-table> -->
                                                    <VueApexCharts
                                                        v-else
                                                        height="280"
                                                        type="bar"
                                                        :options="customerAgeChartOptions"
                                                        :series="customerAgeSeries"
                                                    />
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                                <b-col cols="6">
                                    <b-card class="customer_list_area customer_list_area2">
                                        <b-container fluid>
                                            <b-card-text class="mb-1">
                                                ランク別会員数
                                            </b-card-text>
                                            <b-row>
                                                <b-skeleton-img
                                                    v-if="loadCustomerRank"
                                                ></b-skeleton-img>
                                                <VueApexCharts
                                                    v-else
                                                    height="280"
                                                    type="bar"
                                                    :options="customerRankChartOptions"
                                                    :series="customerRankSeries"
                                                />
                                            </b-row>
                                        </b-container>
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-col>
                        <b-col cols="4">
                            <b-skeleton-img
                                v-if="loadCustomerSalesRanking"
                                class="customer_list_area customer_list_area3"
                            ></b-skeleton-img>
                            <b-card
                                v-else
                                class="customer_list_area customer_list_area3"
                                header="売上ランキング"
                                header-bg-variant="dark"
                                header-text-variant="white"
                                header-class="customer_list_area3_header"
                            >
                                <b-row class="customer_list_area3_top">
                                    <b-col cols="2"/>
                                    <b-col cols="6">名前</b-col>
                                    <b-col align="right">総売上</b-col>
                                </b-row>
                                <b-row
                                    v-for="(item, i) in customerSalesRanking"
                                    :key=i
                                    class="customer_list_area3_middle customer_sales_ranking"
                                    @click="toCustomerDetail(item)"
                                >
                                    <b-col cols="2" style="padding-right: 0;">
                                        <b-card-text>{{ i + 1 }}</b-card-text>
                                    </b-col>
                                    <b-col cols="6" style="padding-left: 0; padding-right: 0;">
                                        <b-card-text>
                                            {{ item.customer.name | truncate(10) }}
                                        </b-card-text>
                                    </b-col>
                                    <b-col align="right" style="padding-left: 0;">
                                        <b-icon icon="currency-yen"></b-icon>
                                        <b>{{ item.total | priceLocaleString }}</b>
                                    </b-col>
                                </b-row>
                                <!-- <b-row>
                                    <b-button
                                        style="padding: 20px;"
                                        block
                                        variant="dark"
                                    >More Detail</b-button>
                                </b-row> -->
                            </b-card>
                        </b-col>
                    </b-row>
                </b-tab>
                <b-tab
                    title="顧客一覧"
                    class="customer_table_wrap"
                    :active=!topActive
                    @click="setCustomerTopActive(1)"
                >
                    <b-card class="customer_list_filter_card">
                        <b-card-title>
                            顧客検索
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
                                            <b-button :disabled="!filter" @click="initFilterParams">Clear</b-button>
                                        </b-input-group-append>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    class="mb-0"
                                    v-if="searchTypeSelected==1"
                                >
                                    <b-input-group size="sm">
                                        <b-form-input
                                            id="filter-input"
                                            v-model="filter"
                                            type="search"
                                            placeholder="キーワードを入力してください"
                                        ></b-form-input>
                                        <b-input-group-append>
                                            <b-button :disabled="!filter" @click="initFilterParams">Clear</b-button>
                                        </b-input-group-append>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    class="mb-0"
                                    v-if="searchTypeSelected==2"
                                >
                                    <b-input-group>
                                        <b-form-datepicker
                                            id="filter-input"
                                            v-model="searchDate"
                                            placeholder="日付を選択してください"
                                            @input="inputSearchAccountDate"
                                        ></b-form-datepicker>
                                        <b-input-group-append>
                                            <b-button :disabled="!searchDate" @click="initFilterParams">Clear</b-button>
                                        </b-input-group-append>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    class="mb-0"
                                    v-if="searchTypeSelected==3"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            id="filter-input"
                                            v-model="searchDate"
                                            type="date"
                                            @input="inputSearchBirthdayDate"
                                        ></b-form-input>
                                        <b-input-group-append>
                                            <b-button :disabled="!searchDate" @click="initFilterParams">Clear</b-button>
                                        </b-input-group-append>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    class="mb-0"
                                    v-if="searchTypeSelected==4"
                                >
                                    <b-input-group>
                                        <b-form-group v-slot="{ ariaDescribedby }">
                                            <b-form-radio-group
                                                id="radio-group-1"
                                                v-model="filter"
                                                :options="searchRankOptions"
                                                :aria-describedby="ariaDescribedby"
                                                name="radio-options"
                                            ></b-form-radio-group>
                                        </b-form-group>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                    </b-card>


                    <b-table
                        hover
                        :items="customer"
                        :fields="fields"
                        :dark="true"
                        caption-top
                        selectable
                        :per-page="perPage"
                        :current-page="currentPage"
                        :filter="filter"
                        :filter-included-fields="filterIncludedField"
                        :filter-ignored-fields="filterIgnoreField"
                        :sort-by.sync="sortBy"
                        :sort-desc.sync="sortDesc"
                        :sort-direction="sortDirection"
                        @row-selected="onRowSelected"
                        @filtered="onFiltered"
                    >
                        <template #cell(rank_id)="data">
                            <b v-if="data.value == 1">
                                <b-icon
                                    icon="credit-card2-front-fill"
                                ></b-icon>
                                <b>normal</b>
                            </b>
                            <b v-else-if="data.value == 2">
                                <!-- <b-icon
                                    icon="credit-card2-front-fill"
                                    style="color: #c0c0c0;"
                                ></b-icon>
                                <b>silver</b> -->
                                <b-icon
                                    icon="credit-card2-front-fill"
                                    style="color: #e1f30c;"
                                ></b-icon>
                                <b>gold</b>
                            </b>
                            <b v-else-if="data.value == 3">
                                <b-icon
                                    icon="credit-card2-front-fill"
                                    style="color: rgb(98,98,98);"
                                ></b-icon>
                                <b>platinum</b>
                            </b>
                            <b v-else-if="data.value == 4">
                                <b-icon
                                    icon="credit-card2-front"
                                ></b-icon>
                                <b>black</b>
                            </b>
                        </template>
                        <template #cell(age)="data">
                            <b v-if="data.value != ''">{{ data.value }} 歳</b>
                            <b v-else>-</b>
                        </template>
                        <template #cell(name)="data">
                            <b>{{ data.value | truncate(10) }}</b>
                        </template>
                        <template #cell(name_kana)="data">
                            <b>{{ data.value | truncate(10) }}</b>
                        </template>
                        <template #cell(birthday)="data">
                            <b v-if="data.value != ''">{{ data.value }}</b>
                            <b v-else>-</b>
                        </template>
                        <template #cell(total_visit)="data">
                            <b>{{ data.value }}</b> <b>回</b>
                        </template>
                        <template #cell(total_sales)="data">
                            <b><b-icon icon="currency-yen"></b-icon>{{ data.value | priceLocaleString }}</b>
                        </template>
                        <template #cell(first_visit)="data">
                            <b v-if="data.value != ''"><b>{{ data.value }}</b></b>
                            <b v-else>-</b>
                        </template>
                        <template #cell(caution_flg)="data">
                            <b v-if="data.value == true"><b>要注意</b></b>
                            <b v-else>-</b>
                        </template>
                    </b-table>
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
                </b-tab>
            </b-tabs>
        </b-row>
    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import utilsMixin from '@/mixins/utils'

export default {
    name: 'CustomerListItem',
    data: () => ({
        selected: {},
        createCustomerDialog: false,
        fields: [
            // {
            //     key: 'id',
            //     sortable: true,
            //     label: 'ID',
            // },
            {
                key: 'customer_no',
                sortable: true,
                label: '会員No',
            },
            {
                key: 'name',
                sortable: true,
                label: '名前',
            },
            {
                key: 'name_kana',
                sortable: true,
                label: '名前(カナ)',
            },
            {
                key: 'age',
                sortable: true,
                label: '年齢',
            },
            {
                key: 'birthday',
                sortable: true,
                label: '誕生日',
            },
            {
                key: 'rank_id',
                sortable: true,
                label: '会員ランク',
            },
            {
                key: 'total_visit',
                sortable: true,
                label: '総来店回数',
            },
            {
                key: 'total_sales',
                sortable: true,
                label: '総売上',
            },
            {
                key: 'first_visit',
                sortable: true,
                label: '初回来店日',
            },
            {
                key: 'caution_flg',
                sortable: true,
                label: '要注意',
            }
        ],
        navHeader: [
            {
                id: 1,
                title: 'Customer List',
                active: false,
            },
            {
                id: 2,
                title: 'Customer Sales',
                active: false,
            },
            {
                id: 3,
                title: 'Customer Ranking',
                active: false,
            },
        ],
        activeHeader: 1,
        pSeries: [1024],
        totalCustomerChartOptions: {
            chart: {
              height: 350,
              type: 'radialBar',
              toolbar: {
                show: false
              }
            },
            plotOptions: {
              radialBar: {
                startAngle: -135,
                endAngle: 225,
                 hollow: {
                  margin: 0,
                  size: '80%',
                  background: '#fff',
                  image: undefined,
                  imageOffsetX: 0,
                  imageOffsetY: 0,
                  position: 'front',
                  dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                  }
                },
                track: {
                  background: '#fff',
                  strokeWidth: '67%',
                  margin: 0, // margin is in pixels
                  dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                  }
                },

                dataLabels: {
                  show: true,
                  name: {
                    offsetY: -10,
                    show: true,
                    color: '#888',
                    fontSize: '17px'
                  },
                  value: {
                    formatter: function(val) {
                      return parseInt(val);
                    },
                    color: '#111',
                    fontSize: '20px',
                    show: true,
                  }
                }
              }
            },
            fill: {
              type: 'gradient',
              gradient: {
                shade: 'dark',
                type: 'horizontal',
                shadeIntensity: 0.5,
                gradientToColors: ['#ABE5A1'],
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 100]
              }
            },
            stroke: {
              lineCap: 'round'
            },
            labels: ['total'],
        },
        totalCustomer: 0,
        totalActiveCustomer: 0,
        totalNonActiveCustomer: 0,
        customerAgeSeries: [{
            name: '年齢',
            data: []
            // data: [0, 0, 1, 2, 5, 1, 1, 0, 0]
        }],
        customerRankSeries: [{
            name: 'ランク',
            data: []
            // data: [78.0, 12.0, 5.0, 4.5, 0.5]
        }],
        customerAgeChartOptions: {

            chart: {
                type: 'bar',
                // ↓左上のdownloadとかやつ
                toolbar: {
                    show: false,
                },
            },
            plotOptions: {
                bar: {
                    borderRadius: 3,
                    dataLabels: {
                        position: 'top', // top, center, bottom
                    },
                }
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return val + "人";
                },
                offsetY: -20,
                style: {
                    fontSize: '10px',
                    // colors: ["#304758"]
                }
            },

            xaxis: {
                categories: ["10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代", "90代", "100代"],
                labels: {
                    style: {
                        colors: ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
                        fontSize: '10px',
                    },
                },
                position: 'top',
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false
                },
                crosshairs: {
                    fill: {
                        type: 'gradient',
                        gradient: {
                            colorFrom: '#D8E3F0',
                            colorTo: '#BED1E6',
                            stops: [0, 100],
                            opacityFrom: 0.4,
                            opacityTo: 0.5,
                        }
                    }
                },
            },
            yaxis: {
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                    formatter: function (val) {
                        return val + "人";
                    }
                },
            },
            tooltip: {
                theme: 'dark',
                followCursor: true
                // 分かるまでfalseにしておく
                // enabled: false,
                // fillSeriesColor: true,
                // style: {
                //     colors: ["#000000"]
                // },
                // theme: false,
            },
        },
        customerRankChartOptions: {

            chart: {
                type: 'bar',
                // ↓左上のdownloadとかやつ
                toolbar: {
                    show: false,
                },
                height: '400px'
            },
            plotOptions: {
                bar: {
                    borderRadius: 3,
                    dataLabels: {
                        position: 'top', // top, center, bottom
                    },
                    horizontal: true,
                    barHeight: '50%',
                    distributed: true,
                    colors: {
                        // ranges: [{
                        //     from: 0,
                        //     to: 0,
                        //     color: undefined
                        // }],
                        // backgroundBarColors: ["#ffffff"],
                        // backgroundBarOpacity: 0.4,
                        // backgroundBarRadius: 0,
                    },
                }
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return val + "人";
                },
                offsetY: -20,
                style: {
                    fontSize: '10px',
                    // colors: ["#304758"]
                }
            },

            xaxis: {
                categories: ["normal", "gold", "silver", "platinum", "black"],
                labels: {
                    style: {
                        colors: ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
                        fontSize: '10px',

                    },
                },
                position: 'top',
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false
                },
                crosshairs: {
                    fill: {
                        type: 'gradient',
                        gradient: {
                            colorFrom: '#D8E3F0',
                            colorTo: '#BED1E6',
                            stops: [0, 100],
                            opacityFrom: 0.4,
                            opacityTo: 0.5,
                        }
                    }
                },
                // tooltip: {
                //   enabled: true,
                // }
            },
            yaxis: {
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                    formatter: function (val) {
                        return val + "人";
                    }
                },
            },
            tooltip: {
                theme: 'dark',
                followCursor: true,
                // 分かるまでfalseにしておく
                // enabled: false,
                // fillSeriesColor: true,
                // style: {
                //     colors: ["#000000"]
                // },
                // theme: false,
            },
            // colors: ['#ffffff', '#dab300', '#bec1c3', '#F0F8FF', '#000000'],
        },
        activeCustomerChartOptions: {
            chart: {
              height: 350,
              type: 'radialBar',
              toolbar: {
                show: false
              }
            },
            plotOptions: {
              radialBar: {
                startAngle: -135,
                endAngle: 225,
                 hollow: {
                  margin: 0,
                  size: '80%',
                  background: '#fff',
                  image: undefined,
                  imageOffsetX: 0,
                  imageOffsetY: 0,
                  position: 'front',
                  dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                  }
                },
                track: {
                  background: '#fff',
                  strokeWidth: '67%',
                  margin: 0, // margin is in pixels
                  dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                  }
                },

                dataLabels: {
                  show: true,
                  name: {
                    offsetY: -10,
                    show: true,
                    color: '#888',
                    fontSize: '17px'
                  },
                  value: {
                    formatter: function(val) {
                      return parseInt(val);
                    },
                    color: '#111',
                    fontSize: '20px',
                    show: true,
                  }
                }
              }
            },
            // fill: {
            //   type: 'gradient',
            //   gradient: {
            //     shade: 'dark',
            //     type: 'horizontal',
            //     shadeIntensity: 0.5,
            //     gradientToColors: ['#ABE5A1'],
            //     inverseColors: true,
            //     opacityFrom: 1,
            //     opacityTo: 1,
            //     stops: [0, 100]
            //   }
            // },
            stroke: {
              lineCap: 'round'
            },
            labels: ['active'],
        },
        nonActiveCustomerChartOptions: {
            chart: {
              height: 350,
              type: 'radialBar',
              toolbar: {
                show: false
              }
            },
            plotOptions: {
              radialBar: {
                 hollow: {
                  margin: 0,
                  size: '80%',
                  background: '#fff',
                  image: undefined,
                  imageOffsetX: 0,
                  imageOffsetY: 0,
                  position: 'front',
                  dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 4,
                    opacity: 0.24
                  }
                },
                track: {
                  background: '#fff',
                  strokeWidth: '67%',
                  margin: 0, // margin is in pixels
                  dropShadow: {
                    enabled: true,
                    top: -3,
                    left: 0,
                    blur: 4,
                    opacity: 0.35
                  }
                },

                dataLabels: {
                  show: true,
                  name: {
                    offsetY: -10,
                    show: true,
                    color: '#888',
                    fontSize: '17px'
                  },
                  value: {
                    formatter: function(val) {
                      return parseInt(val);
                    },
                    color: '#111',
                    fontSize: '20px',
                    show: true,
                  }
                }
              }
            },
            stroke: {
              lineCap: 'round'
            },
            labels: ['non active'],
        },
        weekVisitSalesSeries: [
            {
                name: '売上',
                type: 'column',
                data: [120, 40, 12, 130, 9, 220, 130]
            },
            {
                name: '来店人数',
                type: 'line',
                data: [10, 4, 3, 9, 2, 12, 9]
            }
        ],
        weekVisitSalesChartOptions: {
            chart: {
              // height: 350,
              type: 'line',
              toolbar: {
                  show: false,
              },
            },
            stroke: {
              width: [0, 4]
            },
            dataLabels: {
              enabled: true,
              enabledOnSeries: [1]
            },
            labels: ['2022/06/25', '2022/06/26', '2022/06/27', '2022/06/28', '2022/06/29', '2022/06/30', '2022/06/31'],
            xaxis: {
              type: 'category',
            },
            yaxis: [{
              title: {
                text: '売上(万)',
              },

            }, {
              opposite: true,
              title: {
                text: '来店人数'
              }
            }]
        },
        loadCustomerSalesRanking: true,
        customerSalesRanking: [],
        loadCustomerAge: true,
        loadCustomerRank: true,
        loadCustomerCnt: true,
        loadActiveCustomerCnt: true,
        loadNonActivceCustomerCnt: true,

        currentPage: 1,
        totalRows: 1,
        perPage: 10,
        pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        filter: null,
        filterIncludedField: [],
        filterIgnoreField: [],
        dispCustomers: [],
        searchDate: null,
        searchNo: null,
        searchCustomerName: null,
        searchTypeSelected: 0,
        searchTypeOptions: [
            { text: '会員No', value: 0 },
            { text: '名称', value: 1 },
            { text: '来店日', value: 2 },
            { text: '誕生日', value: 3 },
            { text: 'ランク', value: 4 },
        ],
        searchRank: [],
        searchRankOptions: [
            { text: 'ノーマル', value: 'ノーマル' },
            { text: 'ゴールド', value: 'ゴールド' },
            { text: 'プラチナ', value: 'プラチナ' },
            { text: 'ブラック', value: 'ブラック' },
        ],
        loading: false,
    }),
    components: {
        // ListView,
        CreateCustomerDialog,
    },
    computed: {
        ...mapGetters([
            'customer',
            'customerTopActive',
            'initStatus',
            'currentTime',
        ]),
        sortOptions() {
            // Create an options list from our fields
        return this.fields
            .filter(f => f.sortable)
            .map(f => {
                return { text: f.label, value: f.key }
            })
        },
        totalCustomerMax () {
            return 100
        },
        // totalCustomer () {
        //     return this.customer.length
        // },
        totalCustomerSeries () {
            return [this.totalCustomer]
        },
        activeCustomerSeries () {
            return [this.totalActiveCustomer]
        },
        nonActiveCustomerSeries () {
            return [this.totalNonActiveCustomer]
        },
        topActive () {
            if (this.customerTopActive == undefined || this.customerTopActive == 0) {
                return true
            }
            return false
        }
    },
    created () {
        this.loading = true
        if (!this.$store.state.isAuth) {
            this.$router.push('/')
        }

        if (!this.initStatus) {
            this.appInitAction()
            .then(res => {
                this.getCurrentTime()
                this.setInitStatus(true)
            })
            .catch(e => {
                console.log(e)
            })
        }

        this.getAllCustomer()
        // .then(res => {
        //     console.log('Promiseできてる?')
        //     this.loading = false
        // })
        // .catch(e => {
        //     this.loading = false
        // })
        this.getCustomerRank()
        this.getCustomerAge()
        this.getCustomerSalesRanking()
        // this.getCustomerCnt()
        this.getActiveCustomerCnt()
        // this.totalCustomer = this.customer.length
        // this.totalRows = this.customer.length
        this.loading = false
    },
    mounted () {
    },
    watch: {
        selectedRank(newValue, oldValue) {
            if (newValue.length === 0) {
                this.indeterminate = false
                this.allRankSelected = false
            } else if (newValue.length === this.rankList.length) {
                this.indeterminate = false
                this.allRankSelected = true
            } else {
                this.indeterminate = true
                this.allRankSelected = false
            }
        }
    },
    methods: {
        ...mapMutations([
            'setCustomerTopActive',
            'setCustomerList',
            'setInitStatus',
        ]),
        ...mapActions([
            'getCustomerList',
            'appInitAction',
            'getCurrentTime',
        ]),
        showCustomerDetail (data) {
            // 1回クリック時
        },
        moveCustomerDetail (data) {
            // ダブルクリック時
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: data.customer_no
                }
            })
        },
        onRowSelected (item) {
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: item[0].customer_no
                }
            })
        },
        toCustomerDetail (item) {
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: item.customer.customer_no
                }
            })
        },
        // rowClass (item, type) {
        //     if (!item || type !== 'row') return
        //     if (item.caution_flg == true) return 'table-danger'
        // },
        navClick (item) {
            this.activeHeader = item.id
        },
        onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1

            console.log('onFilterd', filteredItems)
        },
        getCustomerAge () {
            this.$axios({
                method: 'GET',
                url: '/api/customer/get_customer_age/',
            })
            .then(res => {
                this.customerAgeSeries[0].data = res.data.data
                this.loadCustomerAge = false
            })
            .catch(e => {
                console.log(e)
                this.loadCustomerAge = false
            })
        },
        getCustomerRank () {
            this.$axios({
                method: 'GET',
                url: '/api/customer/get_customer_rank/',
            })
            .then(res => {
                this.customerRankSeries[0].data = res.data.data
                this.loadCustomerRank = false
            })
            .catch(e => {
                console.log(e)
                this.loadCustomerRank = false
            })
        },
        // getCustomerCnt () {
        //     this.$axios({
        //         method: 'GET',
        //         url: '/api/customer/get_customer_cnt/',
        //     })
        //     .then(res => {
        //         console.log(res.data)
        //         this.totalCustomer = res.data.cnt
        //         this.totalRows = res.data.cnt
        //     })
        //     .catch(e => {
        //         console.log(e)
        //         this.loadCustomerCnt = false
        //     })
        // },
        getActiveCustomerCnt () {
            this.$axios({
                method: 'GET',
                url: '/api/customer/get_active_customer_cnt/',
            })
            .then(res => {
                // console.log(res.data)
                this.totalActiveCustomer = res.data.activeCustomerCnt
                this.totalNonActiveCustomer = res.data.nonActiveCustomerCnt

                // this.loadCustomerCnt = false
                this.loadActiveCustomerCnt = false
                this.loadNonActivceCustomerCnt = false
            })
            .catch(e => {
                console.log(e)
                // this.loadCustomerCnt = false
                this.loadActiveCustomerCnt = false
                this.loadNonActivceCustomerCnt = false
            })
        },
        getCustomerSalesRanking () {
            this.$axios({
                method: 'GET',
                url: '/api/sales/get_total_customer_sales_ranking/',
            })
            .then(res => {
                // console.log(res.data)
                this.customerSalesRanking = res.data.salesRanking
                this.loadCustomerSalesRanking = false
            })
            .catch(e => {
                console.log(e)
                this.loadCustomerSalesRanking = false
            })
        },
        getAllCustomer () {
            return new Promise((resolve, reject) => {
                this.$axios({
                    method: 'GET',
                    url: '/api/customer/get_all_customer/',
                })
                .then(res => {
                    // console.log(res.data)
                    this.setCustomerList(res.data.customers)
                    const count = res.data.count
                    this.totalRows = count
                    this.totalCustomer = count
                    this.loadCustomerCnt = false
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    this.loadCustomerCnt = false
                    reject(e)
                })
            })
        },
        inputSearchAccountDate (item) {
            this.filterIncludedField = ['first_visit']
            this.filter = item.split('-').join('/')
        },
        inputSearchBirthdayDate (item) {
            this.filterIncludedField = ['birthday']
            this.filter = item.split('-').join('/')
        },
        inputSearchCustomerNo (item) {
            this.filterIncludedField = ['customer_no']
            this.filter = item
        },
        initFilterParams () {
            this.filter = null
            this.searchNo = null
            this.searchDate = null
            this.filterIncludedField = []
            this.filterIgnoreField = []
        },
    },
    mixins: [
        utilsMixin,
    ]
}
</script>

<style lang="scss" scoped>
    #customer_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        // height: $main-height;
        padding: 20px;

        .customer_list_top {
            height: 100%;
        }

        // .customer_list_area1 {
        //     background-color: $theme-color;
        //     // height: 30rem;
        //     height: 100%;
        //     color: white;
        // }
        .customer_list_area {
            background-color: $theme-color;
            color: white;
        }

        .customer_list_area1 {
            height: 220px;
            .customer_list_area1_container {
                padding-left: 0 !important;
                padding-right: 0 !important;
            }
        }

        .customer_list_area2 {
            height: 350px;
        }

        .customer_list_area3 {
            height: 100%;
            .card-body {
                padding: 0.5rem 1rem;
            }
            .customer_list_area3_top {
                border-bottom: 1px solid rgba(150, 150, 150, 0.5);
                background-color: rgba(35, 33, 38, 0.5);
                // background-color: rgba(15, 15, 22, 0.5);
            }
            .customer_list_area3_middle {
                background-color: rgba(35, 33, 38, 0.5);
                border-bottom: 1px solid rgba(150, 150, 150, 0.5);
                height: 3rem;
                // box-shadow: 1px 2px 1px rgba(10, 10, 10, 0.4);
                // margin-top: 10px;
            }
            .customer_sales_ranking {
                cursor: pointer;
            }
        }

        .customer_list_area3_header {
            text-align: center;
            padding: 20px;
        }

        .customer_list_area4 {
            height: 100%;
        }



        .customer_list_area5 {
            padding: 1.7rem;
            background-color: $theme-color;
            height: 100%;
            margin-top: 1rem;
        }

        .customer_table_wrap {

        }
    }

// .vs-con-table {
//     background: white;
// }

// .vs-table--tbody {
//     z-index: 200 !important;
// }

// .header-table {
//   padding-right: 100px !important;
//   margin-bottom: 20px !important;
// }
    .apexcharts-tooltip {
        background: #1e90ff;
        color: white;
    }

    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }

    .customer_list_filter_card {
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

    .loading {
        height: 100%;
        width: 100%;
        .loading_icon {
            display: block;
            margin: 0 auto;
            padding-top: 20%;
        }
    }

</style>
