<template>
    <div id="cast_list_wrap">
        <b-row>
            <b-tabs pill card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setCastTopActive(0)"
                >
                    <b-row>
                        <b-col cols="3" style="max-height: 100%;">
                            <b-card class="cast_list_area" style="height: 48%;">
                                <b-container fluid>
                                    <b-card-text class="mb-1">
                                        在籍キャスト
                                    </b-card-text>
                                    <b-row>
                                        <b-col cols="8">
                                            <VueApexCharts
                                                width="160"
                                                height="160"
                                                type="radialBar"
                                                :options="totalCastChartOptions"
                                                :series="totalCastSeries"
                                            />
                                        </b-col>
                                        <b-col cols="4" align="right" class="pt-5 ml-0 pl-0">
                                            <b-card-title>
                                                {{ totalCast }}
                                            </b-card-title>
                                            <b-card-sub-title>
                                                casts
                                            </b-card-sub-title>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card>
                            <b-card class="cast_list_area" style="height: 48%; margin-top: 15px;">
                                <b-container fluid>
                                    <b-skeleton-img
                                        v-if="loadCastAvgAge"
                                    ></b-skeleton-img>
                                    <div v-else>
                                        <b-card-text class="mb-1">
                                            平均年齢
                                        </b-card-text>
                                        <b-row>
                                            <b-col cols="8">
                                                <VueApexCharts
                                                    width="155"
                                                    height="155"
                                                    type="radialBar"
                                                    :options="castAverageAgeChartOptions"
                                                    :series="castAverageAgeSeries"
                                                />
                                            </b-col>
                                            <b-col cols="4" align="right" class="pt-5">
                                                <b-card-title>
                                                    {{ castAvgAge }}
                                                </b-card-title>
                                                <b-card-sub-title>
                                                    age
                                                </b-card-sub-title>
                                            </b-col>
                                        </b-row>
                                    </div>
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="5" style="max-height: 100%;">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-card-text class="mb-3 mt-3">
                                        キャスト別売上
                                    </b-card-text>
                                    <VueApexCharts
                                        height="365"
                                        width="420"
                                        type="bar"
                                        :options="castSalesRankingChartOptions"
                                        :series="castSalesRankingSeries"
                                    />
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="4" style="max-height: 100%;">
                            <b-card
                                class="cast_list_area"
                                header="売上ランキング（全期間）"
                                header-bg-variant="dark"
                                header-text-variant="white"
                                header-class="cast_list_area_rank_header"
                                body-class="cast_list_area_rank_body"
                            >
                                <b-row class="cast_list_area_rank_top mb-2">
                                    <b-col cols="5">
                                        名前
                                    </b-col>
                                    <b-col cols="3" align="right">
                                        指名回数
                                    </b-col>
                                    <b-col cols="4" align="right">
                                        売上
                                    </b-col>
                                </b-row>
                                <b-row
                                    v-for="(item, i) in castSalesRanking"
                                    :key=i
                                    class="cast_list_area_rank_middle mb-0 mt-0"
                                >
                                    <b-col cols="5">
                                        <b-card-text><img
                                            src="@/assets/img/女性11.jpg"
                                            class="cast_list_area_sales_rank_cast_icon"
                                        > {{ item.name }}</b-card-text>
                                    </b-col>
                                    <b-col cols="3" align="right">
                                        {{ item.total_appoint }} 回
                                    </b-col>
                                    <b-col cols="4" align="right">
                                        <b-icon icon="currency-yen"></b-icon>
                                        <b>{{ item.total_sales }}</b>
                                    </b-col>
                                </b-row>
                            </b-card>
                        </b-col>

                    </b-row>
                    <b-row>
                        <b-col cols="6">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-skeleton-img
                                        v-if="loadCastAge"
                                    ></b-skeleton-img>
                                    <div v-else>
                                        <b-card-text class="mb-1 pt-3">
                                            年齢分布
                                        </b-card-text>
                                        <!-- <VueApexCharts
                                        height="250"
                                        type="bar"
                                        :options="castAgeChartOptions"
                                        :series="castAgeSeries"
                                        /> -->
                                        <VueApexCharts
                                            height="250"
                                            type="bar"
                                            :options="castAgeChartOptions"
                                            :series="castAgeSeries"
                                        />
                                    </div>
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col cols="6">
                            <b-card class="cast_list_area">
                                <b-container fluid>
                                    <b-card-text class="mb-1 pt-3">
                                        勤続年数
                                    </b-card-text>
                                    <VueApexCharts
                                        height="250"
                                        type="bar"
                                        :options="castServiceYearChartOptions"
                                        :series="castServiceYearSeries"
                                    />
                                </b-container>
                            </b-card>
                        </b-col>
                    </b-row>
                </b-tab>
                <b-tab
                    title="キャスト一覧"
                    :active=!topActive
                    @click="setCastTopActive(1)"
                >
                    <b-row class="mb-3">
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


                    </b-row>
                    <b-row>
                        <b-table
                            hover
                            :items="cast"
                            :fields="fields"
                            :dark="true"
                            caption-top
                            selectable
                            :per-page="perPage"
                            :current-page="currentPage"
                            :filter="filter"
                            :filter-included-fields="filterOn"
                            @row-selected="onRowSelected"
                        >

                            <template #cell(age)="data">
                                <b v-if="data.value != ''">
                                    {{ data.value }} 歳
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(real_age)="data">
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

                            <template #cell(phone)="data">
                                <b v-if="data.value != ''">
                                    {{ data.value }}
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(start_working_date)="data">
                                <b v-if="data.value != ''">
                                    {{ data.value }}
                                </b>
                                <b v-else>
                                    -
                                </b>
                            </template>

                            <template #cell(resign_flg)="data">
                                <b v-if="data.value == true">
                                    <b class="text-danger">退職済み</b>
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



                    <!-- <b-row>
                        <b-col
                            cols="3"
                            v-for="item in filterdCast"
                            :key=item.id
                        >
                            <b-card
                                @click="showCastDetail"
                                style="cursor: pointer;"
                            >
                                <b-row>
                                    <b-col cols="6">
                                        <img
                                            src="@/assets/img/女性11.jpg"
                                            class="cast_list_area_cast_icon"
                                            top
                                        >
                                    </b-col>
                                    <b-col cols="5" align="right">
                                        <b-card-title class="mt-4">
                                            {{ item.name }}
                                        </b-card-title>
                                        <b-card-sub-title>
                                            {{ item.age }}
                                        </b-card-sub-title>
                                    </b-col>
                                    <b-col></b-col>
                                </b-row>
                            </b-card>
                        </b-col>
                    </b-row> -->
                </b-tab>
            </b-tabs>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)

export default {
    name: 'CastListItem',
    data: () => ({
        filterdCast: [],
        searchWord: '',
        defaultIcon: 'http://localhost:8000/media/upload/女性1111.png',
        apiPath: 'http://localhost:8000',
        totalCastChartOptions: {
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
        totalCast: 0,
        castAverageAgeChartOptions: {
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
            labels: ['avg'],
        },
        currentPage: 1,
        totalRows: 1,
        perPage: 15,
        filter: null,
        filterOn: [],
        castAgeChartOptions: {
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
                categories: ["10代", "20代前半", "20代後半", "30代前半", "30代後半", "40代以降"],
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
                // // 分かるまでfalseにしておく
                // enabled: false,
                // fillSeriesColor: true,
                // style: {
                //     colors: ["#000000"]
                // },
                // theme: false,
            },
        },
        castAgeSeries: [
            {
                name: '年齢分布',
                data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6]
            }
        ],
        castServiceYearChartOptions: {
            chart: {
                type: 'bar',
                height: 250
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
            },
            colors: ['#00E396'],
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            xaxis: {
                categories: ['愛理', '理沙', '美鈴', '絵美', '樹里亜'],
            },
            yaxis: {
                title: {
                    text: '勤続年数(ヵ月)'
                }
            },
                fill: {
                    opacity: 1
                },
            tooltip: {

                y: {
                    formatter: function (val) {
                        return val + " ヵ月"
                    }
                },
                theme: 'dark',
                followCursor: true
            },
            legend: {
                show: true,
                showForSingleSeries: true,
                customLegendItems: ['勤続年数'],
                markers: {
                    fillColors: ['#00E396']
                }
            }
        },
        castServiceYearSeries: [
            {
                name: '勤続年数',
                data: [0.5, 13, 7, 2, 3]
            }
        ],
        castSalesRankingSeries: [
            {
                data: [10, 220, 340, 120, 30, 1240]
            }
        ],
        castSalesRankingChartOptions: {
            chart: {
              type: 'bar',
              events: {
                // click: function(chart, w, e) {
                //   console.log(chart, w, e)
                // }
              }
            },
            plotOptions: {
              bar: {
                columnWidth: '45%',
                distributed: true,
              }
            },
            dataLabels: {
              enabled: false
            },
            legend: {
              show: false
            },
            colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#A5978B'],
            xaxis: {
              categories: [
                ['test'],
                ['test'],
                ['test'],
                'test',
                ['test'],
                ['test'],
              ],
              labels: {
                style: {
                  colors: ['#33b2df', '#546E7A', '#d4526e', '#13d8aa', '#A5978B', '#A5978B'],
                  fontSize: '12px'
                }
              }
            }
        },
        castSalesRanking: [
            {
                name: 'test',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: 'test',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: 'test',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: 'test',
                total_sales: 99999999,
                total_appoint: 240,
            },
            {
                name: 'test',
                total_sales: 99999999,
                total_appoint: 240,
            },
        ],
        loadCastAvgAge: true,
        loadCastAge: true,
        castAvgAge: 0,
        fields: [
            {
                key: 'id',
                sortable: true,
                label: 'id',
            },
            {
                key: 'name',
                sortable: true,
                label: '名前',
            },
            {
                key: 'real_name',
                sortable: true,
                label: '本名',
            },
            {
                key: 'age',
                sortable: true,
                label: '年齢',
            },
            {
                key: 'real_age',
                sortable: true,
                label: '実年齢',
            },
            {
                key: 'birthday',
                sortable: true,
                label: '誕生日',
            },
            {
                key: 'start_working_date',
                sortable: true,
                label: '勤務開始日',
            },
            {
                key: 'resign_flg',
                sortable: true,
                label: '退職',
            },
        ],
    }),
    computed: {
        ...mapGetters([
            'cast',
            'castTopActive',
        ]),
        topActive () {
            if (this.castTopActive == undefined || this.castTopActive == 0) {
                return true
            }
            return false
        },
        totalCastSeries () {
            return [this.cast.length]
        },
        castAverageAgeSeries () {
            return [this.castAvgAge]
        },
    },
    created () {
        this.filterdCast = _.cloneDeep(this.cast)
        this.totalCast = this.cast.length
        this.totalRows = this.cast.length
        this.getCastAvgAge()
        this.getCastAge()
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
            'setCastList',
            'setCastTopActive',
        ]),
        ...mapActions([
            'getCastList',
        ]),
        onFiltered(filteredItems) {
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        showCastDetail () {
        },
        onRowSelected (item) {
            this.$router.push({
                name: 'CastDetail',
                params: {
                    id: item[0].id
                }
            })
        },
        getCastAvgAge() {
            this.$axios({
                method: 'GET',
                url: '/api/cast/get_cast_avg_age/',
            })
            .then(res => {
                this.castAvgAge = res.data.data.avg
                this.loadCastAvgAge = false
            })
            .catch(e => {
                console.log(e)
            })
        },
        getCastAge () {
            this.$axios({
                method: 'GET',
                url: '/api/cast/get_cast_age/',
            })
            .then(res => {
                this.castAgeSeries[0].data = res.data.data
                this.loadCastAge = false
            })
            .catch(e => {
                console.log(e)
            })
        },
    }
}
</script>

<style lang="scss" scoped>
    #cast_list_wrap {
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        // height: $main-height;
        padding: 20px;

        .cast_list_area {
            background-color: $theme-color;
            color: white;
        }

        .cast_list_area_rank_header {
            text-align: center;
            padding: 15px;
        }

        .cast_list_area_rank_body {
            margin-top: 0;
            padding-top: 0;
        }

        .cast_list_area_sales_rank_cast_icon {
            border-radius: 50%;
            width: 45px;
            height: 45px;
        }

        .cast_list_area_cast_icon {
            border-radius: 50%;
            width: 140px;
            height: 140px;
            // box-shadow: 1px 1px 2px 1px rgba(100, 100, 100, 0.5);
            // border: 1px solid rgba(100, 100, 100, 0.3);
        }

    }
    .card-header {
        background-color: $theme-color !important;
        border-bottom: 0px !important;
    }
</style>
