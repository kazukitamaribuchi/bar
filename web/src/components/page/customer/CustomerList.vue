<template>
    <div id="customer_list_wrap">

        <b-row>
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
                                            <b-row>
                                                <b-col cols="8">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="totalCustomerChartOptions"
                                                        :series="totalCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="4" align="right" class="pt-4 ml-0 pl-0">
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
                                            <b-row>
                                                <b-col cols="8">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="activeCustomerChartOptions"
                                                        :series="activeCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="4" align="right" class="pt-4">
                                                    <b-card-title>
                                                        5
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
                                            <b-row>
                                                <b-col cols="8">
                                                    <VueApexCharts
                                                        width="150"
                                                        height="150"
                                                        type="radialBar"
                                                        :options="nonActiveCustomerChartOptions"
                                                        :series="nonActiveCustomerSeries"
                                                    />
                                                </b-col>
                                                <b-col cols="4" align="right" class="pt-4">
                                                    <b-card-title>
                                                        6
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
                            <b-card
                                class="customer_list_area customer_list_area3"
                                header="売上ランキング"
                                header-bg-variant="dark"
                                header-text-variant="white"
                                header-class="customer_list_area3_header"
                            >
                                <b-row class="customer_list_area3_top mb-2">
                                    <b-col cols="3">
                                        Rank
                                    </b-col>
                                    <b-col cols="5">
                                        名前
                                    </b-col>
                                    <!-- <b-col align="right">
                                        来店回数
                                    </b-col> -->
                                    <b-col align="right">
                                        総売上
                                    </b-col>
                                </b-row>
                                <b-row
                                    v-for="(item, i) in customerSalesRanking"
                                    :key=i
                                    class="customer_list_area3_middle pt-2 mb-0"
                                >
                                    <b-col cols="3">
                                        <b-card-text>{{ i + 1 }}</b-card-text>
                                    </b-col>
                                    <b-col cols="4" class="mt-0 pt-0 mb-0 pb-0">
                                        {{ item.name }}
                                        <b-card-sub-title
                                            style="font-size: 12px;"
                                            class="pt-1"
                                        >年齢 : {{ item.age }}  ランク : {{ item.rank }}</b-card-sub-title>
                                    </b-col>
                                    <!-- <b-col align="right">
                                        <b-card-text>{{ item.total_visit }}回</b-card-text>
                                    </b-col> -->
                                    <b-col align="right">
                                        <b-icon icon="currency-yen"></b-icon>
                                        <b>{{ item.sales }}</b>
                                    </b-col>
                                </b-row>
                                <b-row>
                                    <b-button
                                        style="padding: 20px;"
                                        block
                                        variant="dark"
                                    >More Detail</b-button>
                                </b-row>
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
                <b-card>
                    <!-- <b-row style="color: white;"> -->
                    <b-row>
                        <b-col lg="6" class="my-1">
                            <b-form-group
                                label="Sort"
                                label-for="sort-by-select"
                                label-cols-sm="3"
                                label-align-sm="right"
                                label-size="sm"
                                class="mb-0"
                                v-slot="{ ariaDescribedby }"
                            >
                                <b-input-group size="sm">
                                    <b-form-select
                                        id="sort-by-select"
                                        v-model="sortBy"
                                        :options="sortOptions"
                                        :aria-describedby="ariaDescribedby"
                                        class="w-75"
                                    >
                                        <template #first>
                                            <option value="">-- none --</option>
                                        </template>
                                    </b-form-select>

                                    <b-form-select
                                        v-model="sortDesc"
                                        :disabled="!sortBy"
                                        :aria-describedby="ariaDescribedby"
                                        size="sm"
                                        class="w-25"
                                    >
                                        <option :value="false">Asc</option>
                                        <option :value="true">Desc</option>
                                    </b-form-select>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                        <b-col lg="6" class="my-1">
                            <b-form-group
                                label="Initial sort"
                                label-for="initial-sort-select"
                                label-cols-sm="3"
                                label-align-sm="right"
                                label-size="sm"
                                class="mb-0"
                            >
                                <b-form-select
                                    id="initial-sort-select"
                                    v-model="sortDirection"
                                    :options="['asc', 'desc', 'last']"
                                    size="sm"
                                ></b-form-select>
                            </b-form-group>
                        </b-col>

                        <b-col lg="6" class="my-1">
                            <b-form-group
                                label="Filter"
                                label-for="filter-input"
                                label-cols-sm="3"
                                label-align-sm="right"
                                label-size="sm"
                                class="mb-0"
                            >
                                <b-input-group size="sm">
                                    <b-form-input
                                        id="filter-input"
                                        v-model="filter"
                                        type="search"
                                        placeholder="Type to Search"
                                    ></b-form-input>

                                    <b-input-group-append>
                                        <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                                    </b-input-group-append>
                                </b-input-group>
                            </b-form-group>
                        </b-col>

                        <b-col lg="6" class="my-1">
                            <b-form-group
                                v-model="sortDirection"
                                label="Filter On"
                                description="Leave all unchecked to filter on all data"
                                label-cols-sm="3"
                                label-align-sm="right"
                                label-size="sm"
                                class="mb-0"
                                v-slot="{ ariaDescribedby }"
                            >
                                <b-form-checkbox-group
                                    v-model="filterOn"
                                    :aria-describedby="ariaDescribedby"
                                    class="mt-1"
                                >
                                    <b-form-checkbox value="name">Name</b-form-checkbox>
                                    <b-form-checkbox value="age">Age</b-form-checkbox>
                                    <b-form-checkbox value="isActive">Active</b-form-checkbox>
                                </b-form-checkbox-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                </b-card>
                    <!-- <b-row class="mb-3">
                        <b-col cols="10">
                            <b-col cols="3">
                                <b-form-group
                                    class="mb-0"
                                    label="名前検索"
                                    style="color: white;"
                                >
                                    <b-input-group size="sm">
                                        <b-form-input
                                            id="filter-input"
                                            v-model="filter"
                                            type="search"
                                            placeholder="Name"
                                        ></b-form-input>
                                        <b-input-group-append>
                                            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                                        </b-input-group-append>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-col>
                    </b-row> -->

                    <b-row>
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
                            :filter-included-fields="filterOn"
                            :sort-by.sync="sortBy"
                            :sort-desc.sync="sortDesc"
                            :sort-direction="sortDirection"
                            @row-selected="onRowSelected"
                            @filtered="onFiltered"
                        >
                        <!-- @filterd="onFilterd" -->

                            <template #cell(rank_id)="data">
                                <b v-if="data.value == 1">
                                    <b-icon
                                        icon="credit-card2-front-fill"
                                    ></b-icon>
                                    <b>
                                        normal
                                    </b>
                                </b>
                                <b v-else-if="data.value == 2">
                                    <b-icon
                                        icon="credit-card2-front-fill"
                                        style="color: #c0c0c0;"
                                    ></b-icon>

                                    <b>
                                        silver
                                    </b>
                                </b>
                                <b v-else-if="data.value == 3">
                                    <b-icon
                                        icon="credit-card2-front-fill"
                                        style="color: #e1f30c;"
                                    ></b-icon>
                                    <b>
                                        gold
                                    </b>
                                </b>
                                <b v-else-if="data.value == 4">
                                    <b-icon
                                        icon="credit-card2-front-fill"
                                        style="color: rgb(98,98,98);"
                                    ></b-icon>
                                    <b>
                                        platinum
                                    </b>
                                </b>
                                <b v-else-if="data.value == 5">
                                    <b-icon
                                        icon="credit-card2-front"
                                    ></b-icon>
                                    <b>
                                        black
                                    </b>
                                </b>
                            </template>

                            <template #cell(age)="data">
                                <b v-if="data.value != ''">
                                    {{ data.value }} 歳
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(birthday)="data">
                                <b v-if="data.value != ''">
                                    {{ data.value }}
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(total_visit)="data">
                                <b>{{ data.value }}</b> <b>回</b>
                            </template>

                            <template #cell(total_sales)="data">
                                <b>￥{{ data.value }}</b>
                            </template>

                            <template #cell(first_visit)="data">
                                <b v-if="data.value != ''">
                                    <b>{{ data.value }}</b>
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(caution_flg)="data">
                                <b v-if="data.value == true">
                                    <b class="text-danger">要注意</b>
                                </b>
                                <b v-else>
                                    -
                                </b>
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
                </b-tab>
            </b-tabs>
        </b-row>


        <!-- <b-row>
            <b-col cols="6">
                <b-card class="customer_list_area customer_list_area4">
                    <b-container fluid>
                        <b-card-text class="mb-1">
                            週間来店売上
                        </b-card-text>
                        <b-row>
                            <VueApexCharts
                                type="line"
                                :options="weekVisitSalesChartOptions"
                                :series="weekVisitSalesSeries"
                            />
                        </b-row>
                    </b-container>
                </b-card>
            </b-col>
        </b-row> -->


    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'
// import ListView from '@/components/parts/ListView'/

export default {
    name: 'CustomerListItem',
    data: () => ({
        selected: {},
        createCustomerDialog: false,
        fields: [
            {
                key: 'id',
                sortable: true,
                label: 'ID',
            },
            {
                key: 'name',
                sortable: true,
                label: '名前',
            },
            {
                key: 'customer_no',
                sortable: true,
                label: '会員No',
            },
            {
                key: 'name_kana',
                sortable: true,
                label: '名前(カナ)',
            },
            // {
            //     key: 'rank_id',
            //     sortable: true,
            //     label: '会員ランク',
            // },
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
                categories: ["10代", "20代", "30代", "40代", "50代", "60代", "70代", "80代"],
                labels: {
                    style: {
                        colors: ["#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff", "#ffffff"],
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
        customerSalesRanking: [
            {
                name: '田中道彦',
                sales: 99999999,
                age: '45',
                rank: 'black',
                total_visit: 144,
            },
            {
                name: '田中三郎',
                sales: 99999999,
                age: '45',
                rank: 'black',
                total_visit: 122,
            },
            {
                name: '田中五郎',
                sales: 999999,
                age: '45',
                rank: 'black',
                total_visit: 114,
            },
            {
                name: '田中一郎',
                sales: 99999,
                age: '45',
                rank: 'black',
                total_visit: 10,
            },
            {
                name: '山口達也',
                sales: 99999,
                age: '45',
                rank: 'black',
                total_visit: 33,
            },
            // {
            //     name: '田中道彦',
            //     sales: 99999,
            //     age: '45',
            //     rank: 'black',
            // },
            // {
            //     name: '田中三郎',
            //     sales: 99999,
            //     age: '45',
            //     rank: 'black',
            // },
            // {
            //     name: '田中五郎',
            //     sales: 99999,
            //     age: '45',
            //     rank: 'black',
            // },
            // {
            //     name: '田中一郎',
            //     sales: 99999,
            //     age: '45',
            //     rank: 'black',
            // },
            // {
            //     name: '山口達也',
            //     sales: 99999,
            //     age: '45',
            //     rank: 'black',
            // },
        ],
        loadCustomerAge: true,
        loadCustomerRank: true,
        currentPage: 1,
        totalRows: 1,
        perPage: 15,
        pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        filter: null,
        filterOn: [],
    }),
    components: {
        // ListView,
        CreateCustomerDialog,
    },
    computed: {
        ...mapGetters([
            'customer',
            'customerTopActive',
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
            return [this.customer.length]
        },
        activeCustomerSeries () {
            return [5]
        },
        nonActiveCustomerSeries () {
            return [6]
        },
        topActive () {
            if (this.customerTopActive == undefined || this.customerTopActive == 0) {
                return true
            }
            return false
        }
    },
    created () {
        this.getCustomerRank()
        this.getCustomerAge()
        this.totalCustomer = this.customer.length
        this.totalRows = this.customer.length
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
            'setCustomerTopActive'
        ]),
        showCustomerDetail (data) {
            // 1回クリック時
        },
        moveCustomerDetail (data) {
            // ダブルクリック時
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: data.id
                }
            })
        },
        onRowSelected (item) {
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: item[0].id
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
        }
    }
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
                padding-left: 1rem !important;
                padding-right: 1rem !important;
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
                border-bottom: 1px solid rgba(50, 50, 50, 0.5);
                height: 4.3rem;
                box-shadow: 1px 2px 1px rgba(10, 10, 10, 0.4);
                margin-top: 10px;
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

</style>
