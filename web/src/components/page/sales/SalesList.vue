<template>
    <div id="sales_list_wrap">
        <b-row>
            <!-- <div align="right" style="color: white; position: absolute; top: 105px; right: 80px; font-size: 15px; float: right; width: 300px;">
                現在時刻: {{ now.format('YYYY年MM月DD日 HH時MM分') }}
            </div> -->
            <b-tabs pill card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setSalesTopActive(0)"
                >
                    <b-tabs pills card fill>
                        <b-tab title="本日" active @click="dResetKey++">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left">
                                    <b-card class="sales_list_area sales_list_area_top_left">
                                        <CustomerDaySalesAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <TotalSalesAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <TotalVisitorsAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <BasicPlanTypeRatioAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <AppointRatioAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <CustomerDayStayHourAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="12">
                                    <b-card class="sales_list_area">
                                        <ProductDaySalesAnalytics
                                            :targetDate=today
                                            :key="dResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <!-- <b-col cols="5">
                                    <b-card class="sales_list_area">
                                        <b-card-text>
                                            キャスト別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="bar"
                                            :options="appointChartOptions"
                                            :series="appointSeries"
                                        />
                                    </b-card>
                                </b-col> -->
                            </b-row>
                        </b-tab>
                        <b-tab title="前日" @click="yResetKey++">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left">
                                    <b-card class="sales_list_area sales_list_area_top_left">
                                        <CustomerDaySalesAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <TotalSalesAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <TotalVisitorsAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <BasicPlanTypeRatioAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <AppointRatioAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <CustomerDayStayHourAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="12">
                                    <b-card class="sales_list_area">
                                        <ProductDaySalesAnalytics
                                            :targetDate=yesterday
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <!-- <b-col cols="5">
                                    <b-card class="sales_list_area">
                                        <b-card-text>
                                            キャスト別売上
                                        </b-card-text>
                                        <VueApexCharts
                                            height="200"
                                            type="bar"
                                            :options="appointChartOptions"
                                            :series="appointSeries"
                                        />
                                    </b-card>
                                </b-col> -->
                            </b-row>
                        </b-tab>
                        <b-tab title="1週間" @click="wResetKey++">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8"  class="sales_list_area_top_left">
                                    <b-card class="sales_list_area sales_list_area_top_left">
                                        <DaySalesAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4"  class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <TotalSalesAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <TotalVisitorsAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <BasicPlanTypeRatioAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <AppointRatioAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <CustomerDayTotalSalesAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="5" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <DayTotalVisitorsAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="7" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <ProductDayTotalSalesAnalytics
                                            :targetDate=weekAgo
                                            :range=8
                                            :key="wResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="1ヵ月間" @click="mResetKey++">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left">
                                    <b-card class="sales_list_area sales_list_area_top_left">
                                        <DaySalesAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <TotalSalesAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <TotalVisitorsAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <BasicPlanTypeRatioAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <AppointRatioAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <CustomerDayTotalSalesAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="5" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <DayTotalVisitorsAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="7" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <ProductDayTotalSalesAnalytics
                                            :targetDate=monthAgo
                                            :range=31
                                            :key="mResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                        <b-tab title="年" @click="yResetKey++">
                            <b-row class="sales_list_area_top">
                                <b-col cols="8" class="sales_list_area_top_left">
                                    <b-card class="sales_list_area sales_list_area_top_left">
                                        <DaySalesAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="4" class="sales_list_area_top_right">
                                    <b-card class="sales_list_area sales_list_area_top_right1">
                                        <TotalSalesAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                    <b-card class="sales_list_area sales_list_area_top_right2">
                                        <TotalVisitorsAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row class="sales_list_area_middle">
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <BasicPlanTypeRatioAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="3" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_left">
                                        <AppointRatioAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="6" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <CustomerDayTotalSalesAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col cols="5" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <DayTotalVisitorsAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                                <b-col cols="7" style="max-height: 100%;">
                                    <b-card class="sales_list_area sales_list_area_middle_right">
                                        <ProductDayTotalSalesAnalytics
                                            :targetDate=yearAgo
                                            :range=365
                                            :key="yResetKey"
                                        />
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-tab>
                    </b-tabs>


                    <!-- <b-row>
                        <b-col cols="7">
                            <b-card class="sales_list_area sales_list_1">
                                <b-container fluid>
                                    <b-card-text class="">
                                        売上/来店数
                                    </b-card-text>
                                    <b-row>
                                        <b-col>
                                            <VueApexCharts
                                                height="300"
                                                :options="salesVisitChartOptions"
                                                :series="salesVisitSeries"
                                            />
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card>
                        </b-col>
                        <b-col>
                            <b-card class="sales_list_area sales_list_2">
                            </b-card>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col cols="3">
                            <b-card class="sales_list_area sales_list_3">
                            </b-card>
                        </b-col>
                        <b-col cols="6">
                            <b-card class="sales_list_area sales_list_4">
                            </b-card>
                        </b-col>
                        <b-col>
                            <b-card class="sales_list_area sales_list_5">
                            </b-card>
                        </b-col>
                    </b-row> -->
                </b-tab>
                <b-tab
                    title="売上一覧"
                    :active=!topActive
                    @click="setSalesTopActive(1)"
                >
                    <v-row>
                        <b-table
                            hover
                            :items="sales"
                            :fields="fields"
                            dark
                            caption-top
                            selectable
                            :per-page="perPage"
                            :current-page="currentPage"
                            :filter="filter"
                            :filter-included-fields="filterOn"
                            @row-selected="onRowSelected"
                        >
                            <template #cell(appoint)="data">
                                <b v-if="data.value">
                                    有
                                </b>
                                <b v-else>
                                    フリー
                                </b>
                            </template>

                            <template #cell(douhan)="data">
                                <b v-if="data.value">
                                    有
                                </b>
                                <b v-else>
                                    無
                                </b>
                            </template>
                        </b-table>
                    </v-row>
                </b-tab>
            </b-tabs>
        </b-row>

        <!-- <InputSalesDialog
            @update="inputSalesDialog = $event"
            :inputSalesDialog="inputSalesDialog"
        /> -->
    </div>
</template>

<script>
import InputSalesDialog from '@/components/common/dialog/InputSalesDialog'
import CustomerDaySalesAnalytics from '@/components/common/analytics/CustomerDaySalesAnalytics'
import CustomerDayTotalSalesAnalytics from '@/components/common/analytics/CustomerDayTotalSalesAnalytics'
import DaySalesAnalytics from '@/components/common/analytics/DaySalesAnalytics'
import DayTotalVisitorsAnalytics from '@/components/common/analytics/DayTotalVisitorsAnalytics'
import CustomerDayStayHourAnalytics from '@/components/common/analytics/CustomerDayStayHourAnalytics'
import TotalSalesAnalytics from '@/components/common/analytics/TotalSalesAnalytics'
import TotalVisitorsAnalytics from '@/components/common/analytics/TotalVisitorsAnalytics'
import BasicPlanTypeRatioAnalytics from '@/components/common/analytics/BasicPlanTypeRatioAnalytics'
import AppointRatioAnalytics from '@/components/common/analytics/AppointRatioAnalytics'
import ProductDaySalesAnalytics from '@/components/common/analytics/ProductDaySalesAnalytics'
import ProductDayTotalSalesAnalytics from '@/components/common/analytics/ProductDayTotalSalesAnalytics'
import { mapGetters, mapMutations, mapActions } from 'vuex'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)
import utilsMixin from '@/mixins/utils'

dayjs.extend(require('dayjs/plugin/timezone'))
dayjs.extend(require('dayjs/plugin/utc'))
dayjs.tz.setDefault('Asia/Tokyo')

export default {
    name: 'SalesListItem',
    data: () => ({
        inputSalesDialog: false,
        salesVisitSeries: [
            {
                name: 'Website Blog',
                type: 'column',
                data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
            },
            {
                name: 'Social Media',
                type: 'line',
                data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
            }
        ],
        salesVisitChartOptions: {
            chart: {
                height: 350,
                type: 'line',
            },
            stroke: {
                width: [0, 4]
            },
            title: {
                text: 'Traffic Sources'
            },
            dataLabels: {
                enabled: true,
                enabledOnSeries: [1]
            },
            labels: ['01 Jan 2001', '02 Jan 2001', '03 Jan 2001', '04 Jan 2001', '05 Jan 2001', '06 Jan 2001', '07 Jan 2001', '08 Jan 2001', '09 Jan 2001', '10 Jan 2001', '11 Jan 2001', '12 Jan 2001'],
            xaxis: {
                type: 'datetime'
            },
            yaxis: [{
                title: {
                    text: 'Website Blog',
                },
            }, {
                opposite: true,
                title: {
                    text: 'Social Media'
                }
            }]
        },
        salesEachPeriodSeries: [
            {
              data: [
                  8107.85,
                  8128.0,
                  8122.9,
                  8165.5,
                  8340.7,
                  8423.7,
                  8423.5,
                  8514.3,
                  8481.85,
                  8487.7,
                  8506.9,
                  8626.2,
                  8668.95,
                  8602.3,
                  8607.55,
                  8512.9,
                  8496.25,
                  8600.65,
                  8881.1,
                  9340.85
                ],
            },
        ],
        salesEachPeriodChartOptions: {
            chart: {
              height: 350,
              type: 'line',
              id: 'areachart-2'
            },
            annotations: {
              yaxis: [{
                y: 8200,
                borderColor: '#00E396',
                label: {
                  borderColor: '#00E396',
                  style: {
                    color: '#fff',
                    background: '#00E396',
                  },
                  text: 'Support',
                }
              }, {
                y: 8600,
                y2: 9000,
                borderColor: '#000',
                fillColor: '#FEB019',
                opacity: 0.2,
                label: {
                  borderColor: '#333',
                  style: {
                    fontSize: '10px',
                    color: '#333',
                    background: '#FEB019',
                  },
                  text: 'Y-axis range',
                }
              }],
              xaxis: [{
                x: new Date('23 Nov 2017').getTime(),
                strokeDashArray: 0,
                borderColor: '#775DD0',
                label: {
                  borderColor: '#775DD0',
                  style: {
                    color: '#fff',
                    background: '#775DD0',
                  },
                  text: 'Anno Test',
                }
              }, {
                x: new Date('26 Nov 2017').getTime(),
                x2: new Date('28 Nov 2017').getTime(),
                fillColor: '#B3F7CA',
                opacity: 0.4,
                label: {
                  borderColor: '#B3F7CA',
                  style: {
                    fontSize: '10px',
                    color: '#fff',
                    background: '#00E396',
                  },
                  offsetY: -10,
                  text: 'X-axis range',
                }
              }],
              points: [{
                x: new Date('01 Dec 2017').getTime(),
                y: 8607.55,
                marker: {
                  size: 8,
                  fillColor: '#fff',
                  strokeColor: 'red',
                  radius: 2,
                  cssClass: 'apexcharts-custom-class'
                },
                label: {
                  borderColor: '#FF4560',
                  offsetY: 0,
                  style: {
                    color: '#fff',
                    background: '#FF4560',
                  },

                  text: 'Point Annotation',
                }
              }, {
                x: new Date('08 Dec 2017').getTime(),
                y: 9340.85,
                marker: {
                  size: 0
                },
                image: {
                  path: '../../assets/images/ico-instagram.png'
                }
              }]
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            grid: {
              padding: {
                right: 30,
                left: 20
              }
            },
            title: {
              text: 'Line with Annotations',
              align: 'left'
            },
            labels: [
                "13 Nov 2017",
                "14 Nov 2017",
                "15 Nov 2017",
                "16 Nov 2017",
                "17 Nov 2017",
                "20 Nov 2017",
                "21 Nov 2017",
                "22 Nov 2017",
                "23 Nov 2017",
                "24 Nov 2017",
                "27 Nov 2017",
                "28 Nov 2017",
                "29 Nov 2017",
                "30 Nov 2017",
                "01 Dec 2017",
                "04 Dec 2017",
                "05 Dec 2017",
                "06 Dec 2017",
                "07 Dec 2017",
                "08 Dec 2017"
            ],
            xaxis: {
              type: 'datetime',
            },
        },
        totalSalesChartOptions: {
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
        totalSalesChartOptions2: {
            chart: {
                height: 160,
                type: 'area',
                sparkline: {
                    enabled: true
                },
            },
            stroke: {
                curve: 'straight'
            },
            fill: {
                opacity: 1,
                gradient: {
                    shade: 'dark',
                    type: "horizontal",
                    shadeIntensity: 0.5,
                    gradientToColors: undefined,
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 50, 100],
                    colorStops: []
                },
            },
            labels: [...Array(24).keys()].map(n => `2018-09-0${n+1}`),
            yaxis: {
                min: 0
            },
            xaxis: {
                type: 'datetime',
                    labels: {
                        datetimeUTC: false,
                    },
                },
            colors: ['#DCE6EC'],
        },
        totalSalesSeries2: [
            {
                name: 'Sales',
                data: [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46]
            }
        ],
        appointChartOptions: {
            chart: {
              type: 'bar',
              height: 350
            },
            plotOptions: {
              bar: {
                horizontal: false,
                columnWidth: '55%',
                endingShape: 'rounded'
              },
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              show: true,
              width: 2,
              colors: ['transparent']
            },
            xaxis: {
              categories: ['愛理', '華恋', '乙女', '理沙', '美鈴'],
            },
            yaxis: {
              title: {
                text: '￥ (万円)'
              }
            },
            fill: {
              opacity: 1
            },
            tooltip: {
              y: {
                formatter: function (val) {
                  return "$ " + val + " thousands"
                }
              }
            }
        },
        appointSeries: [
            {
                name: '指名料',
                data: [44, 55, 0, 56, 61]
            },
            {
                name: 'ドリンク',
                data: [76, 85, 30, 98, 87]
            },
            {
                name: '同伴料',
                data: [0, 30, 0, 0, 0]
            }
        ],
        productSalesSeries: [
            {
                name: 'Inflation',
                data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
            }
        ],
        productSalesChartOptions: {
            chart: {
                height: 350,
                type: 'bar',
            },
            plotOptions: {
                bar: {
                    borderRadius: 10,
                    dataLabels: {
                        position: 'top', // top, center, bottom
                    },
                }
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return val + "%";
                },
                offsetY: -20,
                style: {
                    fontSize: '12px',
                    colors: ["#ffffff"]
                }
            },
            xaxis: {
                categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
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
                tooltip: {
                    enabled: true,
                }
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
                      return val + "%";
                    }
                }
            },
            title: {
                text: 'Monthly Inflation in Argentina, 2002',
                floating: true,
                offsetY: 330,
                align: 'center',
                style: {
                    color: '#444'
                }
            }
        },
        currentPage: 1,
        totalRows: 1,
        perPage: 15,
        filter: null,
        filterOn: [],
        fields: [
            {
                key: 'id',
                label: '伝票NO'
            },
            {
                key: 'account_date',
                label: '来店日'
            },
            {
                key: 'customer.customer_no',
                label: '会員No',
            },
            {
                key: 'customer.name',
                label: '顧客名'
            },
            {
                key: 'total_sales',
                label: '総計(税抜)'
            },
            {
                key: 'total_tax_sales',
                label: '総計(税込)'
            },
            {
                key: 'visit_time',
                label: '来店時間'
            },
            {
                key: 'leave_time',
                label: '退店時間'
            },
            {
                key: 'appoint',
                label: '指名'
            },
            {
                key: 'douhan',
                label: '同伴'
            }
        ],
        dResetKey: 0,
        yResetKey: 0,
        tResetKey: 0,
        wResetKey: 0,
        mResetKey: 0,
        YResetKey: 0,
    }),
    components: {
        InputSalesDialog,
        CustomerDaySalesAnalytics,
        CustomerDayTotalSalesAnalytics,
        DaySalesAnalytics,
        DayTotalVisitorsAnalytics,
        CustomerDayStayHourAnalytics,
        TotalSalesAnalytics,
        TotalVisitorsAnalytics,
        BasicPlanTypeRatioAnalytics,
        AppointRatioAnalytics,
        ProductDaySalesAnalytics,
        ProductDayTotalSalesAnalytics,
    },
    computed: {
        ...mapGetters([
            'sales',
            'salesTopActive',
            'currentTime',
        ]),
        topActive () {
            if (this.salesTopActive == undefined || this.salesTopActive == 0) {
                return true
            }
            return false
        },
        now () {
            return dayjs(this.currentTime)
        },
        target_day () {
            let border_line = dayjs(this.now.format('YYYY-MM-DD') + ' 07:00:00')
            if (this.now.isAfter(border_line)) {
                return this.now
            }
            return this.now.subtract(1, 'd')
        },
        today () {
            return this.target_day.format('YYYY-MM-DD')
        },
        yesterday () {
            return this.target_day.subtract(1, 'd').format('YYYY-MM-DD')
        },
        weekAgo () {
            return this.target_day.subtract(7, 'd').format('YYYY-MM-DD')
        },
        monthAgo () {
            return this.target_day.subtract(31, 'd').format('YYYY-MM-DD')
        },
        yearAgo () {
            return this.target_day.subtract(365, 'd').format('YYYY-MM-DD')
        },
    },
    created () {
    },
    mounted () {
        this.totalRows = this.sales.length
    },
    methods: {
        ...mapMutations([
            'setSalesTopActive'
        ]),
        onRowSelected (item) {
            this.$router.push({
                name: 'SalesDetail',
                params: {
                    id: item[0].id
                }
            })
        },
    },
    mixins: [
        utilsMixin
    ]
}
</script>

<style lang="scss" scoped>
    #sales_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .sales_list_area {
            background-color: $theme-color;
            color: white;
        }

        .total_sales_content {
            font-size: 23px;
        }

        .sales_list_area_top {
            height: 430px;
            .sales_list_area_top_left {
                height: 100%;
            }
            .sales_list_area_top_right {
                height: 100%;
                .sales_list_area_top_right1 {
                    height: 50%;
                }
                .sales_list_area_top_right2 {
                    margin-top: 2%;
                    height: 48%;
                }
            }
        }

        .sales_list_area_middle {
            height: 350px;

            .sales_list_area_middle_left {
                height: 100%;
            }

            .sales_list_area_middle_right {
                height: 100%;
            }
        }
    }
</style>
