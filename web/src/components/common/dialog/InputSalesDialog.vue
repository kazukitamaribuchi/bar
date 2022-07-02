<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            :title="inputSalesDialogTitle"
            header-bg-variant="primary"
            header-text-variant="light"
        >
            <b-form class="input_sales_form">

                <b-card bg-variant="light" class="mt-3" style="min-height: 50px;">
                    <b-form-group
                        label-cols-lg="3"
                        label="基本料金"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                    >
                    <!-- <b-card-sub-title align="right" v-if="editMode">
                        伝票No {{ salesHeaderId }}
                    </b-card-sub-title> -->
                        <b-card-sub-title align="right">
                            <span style="color: red;">*</span> : 必須項目
                        </b-card-sub-title>
                        <b-row>
                            <b-col cols="4">
                                <b-card-sub-title>
                                    会員タイプ
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="customer_type_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="customer_type_info_icon"
                                        title="会員区分を選択してください。"
                                    ></b-tooltip>
                                </b-card-sub-title>
                                <b-form-group style="min-height: 40px;">
                                    <b-form-radio-group
                                        v-model="inputSalesData.customer_type"
                                        :options=customerTypeOptions
                                        button-variant="outline-primary"
                                        buttons
                                        style="min-height: 40px;"
                                    ></b-form-radio-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="3" v-if="inputSalesData.customer_type == 0">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': nonMemberNameInvalid}"
                                    >顧客名</label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="non_member_name_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="non_member_name_info_icon"
                                        title="任意で顧客名を入力してください。"
                                    ></b-tooltip>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.nonMemberName"
                                            type="text"
                                            placeholder="顧客名(任意)"
                                            autofocus
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="nonMemberNameError.length == 0">
                                            {{ nonMemberNameError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3" v-else>
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': customerNoInvalid}"
                                        class="form_required"
                                    >会員No</label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="non_customer_name_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="customer_no_info_icon"
                                        title="会員Noを入力してください。"
                                    ></b-tooltip>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.customerNo"
                                            required
                                            autofocus
                                            placeholder="会員No(必須)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNoError.length == 0">
                                            {{ customerNoError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3">
                            </b-col>
                            <b-col cols="3">
                                <b-form-group
                                >
                                    <label
                                        :class="{'invalid': totalVisitorsInvalid}"
                                        class="form_required"
                                    >来店人数</label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="total_visitors_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="total_visitors_info_icon"
                                        title="VIPで5人以上の場合、自動的に貸切に切り替わります。"
                                    ></b-tooltip>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.totalVisitors"
                                            required
                                            placeholder="来店人数(必須)"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="totalVisitorsError.length == 0">
                                            {{ totalVisitorsError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="3">
                                <b-form-group
                                    class="input_sales_date"
                                >
                                    <label>
                                        来店日
                                        <span
                                            style="display: inline-block; margin-left: 0.4rem;"
                                        >
                                            <b-icon
                                                id="account_date_info_icon"
                                                icon="info-circle"
                                                variant="primary"
                                            ></b-icon>
                                        </span>
                                        <b-tooltip
                                            target="account_date_info_icon"
                                            title="来店した日付を選択してください。"
                                        ></b-tooltip>
                                    </label>
                                    <b-form-datepicker
                                        v-model="inputSalesData.accountDate"
                                        placeholder="来店日を入力してください"
                                    ></b-form-datepicker>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row  v-if="inputSalesData.customer_type == 1">
                            <b-col cols="12">
                                <b-card>
                                    <label>
                                        顧客情報
                                    </label>
                                    <b-container>
                                        <b-row>
                                            <b-col cols="5" class="mt-0 pt-0">
                                                <div style="display: flex;">
                                                    <div>
                                                        <img
                                                            src="@/assets/img/男性3.jpg"
                                                            class="customer_detail_customer_icon"
                                                        >
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-if="customerInfo != null">
                                                        <b-card-title style="font-size: 15px;">
                                                            {{ customerInfo.name}}
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            {{ customerInfo.name_kana }}
                                                        </b-card-sub-title>
                                                    </div>
                                                    <div class="mt-2" style="margin-left: 15px;" v-else>
                                                        <b-card-title style="font-size: 15px;">
                                                            -
                                                        </b-card-title>
                                                        <b-card-sub-title style="font-size: 12px;">
                                                            -
                                                        </b-card-sub-title>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    年齢
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ customerInfo.age }} 歳
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="3" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    誕生日
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ getStrInData(customerInfo.birthday) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    ランク
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null">
                                                    {{ getStrInData(customerInfo.rank_name) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                        </b-row>
                                    </b-container>
                                </b-card>
                                <!-- <b-form-group
                                    label="会員No*"
                                    :class="{'invalid': customerNoInvalid}"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.customerNo"
                                            type="number"
                                            required
                                            autofocus
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNoError.length == 0">
                                            {{ customerNoError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group> -->
                            </b-col>

                        </b-row>
                        <b-row>
                            <b-col :cols=basicPlanAreaCol>
                                <b-card style="min-height: 540px;">
                                    <label>
                                        基本料金
                                    </label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="basic_price_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="basic_price_info_icon"
                                        title="入店時間、退店時間を入力すると自動的に料金が設定されます。"
                                    ></b-tooltip>
                                    <b-container>
                                        <b-row style="min-height: 80px;">
                                            <b-col cols="6">
                                                <b-card-sub-title>料金タイプ</b-card-sub-title>
                                                <b-form-group style="min-height: 40px;">
                                                    <b-form-radio-group
                                                        v-model="inputSalesData.basicPlanType"
                                                        :options=basicPlanOptions
                                                        button-variant="outline-primary"
                                                        buttons
                                                        style="min-height: 40px;"
                                                    ></b-form-radio-group>
                                                    <b-icon
                                                        v-if="inputSalesData.basicPlanType == 1"
                                                        font-scale="1.8"
                                                        icon="bookmark-star-fill"
                                                        variant="primary"
                                                        class="ml-3 pl-3"
                                                    ></b-icon>
                                                </b-form-group>
                                            </b-col>
                                            <b-col>
                                                <b-form-group>
                                                    <b-form-checkbox-group
                                                        v-if="inputSalesData.basicPlanType == 1"
                                                        style="margin-top: 14px;"
                                                        v-model="inputSalesData.isChartered"
                                                        :options=charterOptions
                                                        :disabled="inputSalesData.totalVisitors >= 5"
                                                        buttons
                                                        button-variant="primary"
                                                    ></b-form-checkbox-group>
                                                </b-form-group>
                                            </b-col>
                                            <b-col>
                                                <b-card-sub-title>
                                                    席移動
                                                </b-card-sub-title>
                                                <!-- style="margin-top: 14px;" -->
                                                <b-form-checkbox-group
                                                    :options=moveDiffSeatOptions
                                                    buttons
                                                    button-variant="success"
                                                    @change="showDiffBasicPlan = !showDiffBasicPlan"
                                                ></b-form-checkbox-group>
                                                <!-- <b-button
                                                    size="sm"
                                                    @click="showDiffBasicPlan = !showDiffBasicPlan"
                                                    class="mt-3"
                                                    pill
                                                    variant="outline-success"
                                                >
                                                    <b-icon
                                                        icon="arrow-left-right"
                                                        aria-hidden="true"
                                                    ></b-icon> 席移動
                                                </b-button> -->
                                            </b-col>
                                            <!-- <b-col>
                                                <b-button id="button-1" variant="outline-success">Live chat</b-button>
                                            </b-col> -->
                                        </b-row>
                                        <b-row class="pb-0">
                                            <b-col cols="6" class="input_sales_visit pb-0">
                                                <div class="input_sales_visit_time_wrap">
                                                    <div class="input_sales_visit_time">
                                                        <b-card-sub-title
                                                            class="input_sales_visit_time_title form_required"
                                                        >入店時間</b-card-sub-title>
                                                        <b-row>
                                                            <b-form-group class="input_sales_visit_time_select_wrap">
                                                                <b-form-group>
                                                                    <SelectForm
                                                                        :optionType=5
                                                                        v-model="inputSalesData.visitTimeHour"
                                                                    />
                                                                    ：
                                                                    <b v-if="inputSalesData.visitTimeHour != 20">
                                                                        <SelectForm
                                                                            :optionType=2
                                                                            v-model="inputSalesData.visitTimeMinute"
                                                                        />
                                                                    </b>
                                                                    <b v-else>
                                                                        <SelectForm
                                                                            :optionType=6
                                                                            v-model="inputSalesData.visitTimeMinute"
                                                                        />
                                                                    </b>
                                                                </b-form-group>
                                                            </b-form-group>
                                                        </b-row>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="6" class="input_sales_leave pb-0">
                                                <div class="input_sales_visit_time_wrap">
                                                    <div class="input_sales_visit_time">
                                                        <b-card-sub-title
                                                            class="input_sales_visit_time_title form_required"
                                                        >{{ moveSeatTimeText }}</b-card-sub-title>
                                                        <b-form-group class="input_sales_visit_time_select_wrap">
                                                            <b-form-group>
                                                                <SelectForm
                                                                    :optionType=5
                                                                    v-model="inputSalesData.leaveTimeHour"
                                                                />
                                                                ：
                                                                <b v-if="inputSalesData.leaveTimeHour != 20">
                                                                    <SelectForm
                                                                        :optionType=2
                                                                        v-model="inputSalesData.leaveTimeMinute"
                                                                    />
                                                                </b>
                                                                <b v-else>
                                                                    <SelectForm
                                                                        :optionType=6
                                                                        v-model="inputSalesData.leaveTimeMinute"
                                                                    />
                                                                </b>
                                                            </b-form-group>
                                                        </b-form-group>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="12" class="pt-0">
                                                <b-form-invalid-feedback :state="visitTimeError.length == 0">
                                                    {{ visitTimeError }}
                                                </b-form-invalid-feedback>
                                            </b-col>
                                            <b-col>
                                                <label>
                                                    滞在時間
                                                </label>
                                                <b-progress :max="maxHour" height="2rem">
                                                    <b-progress-bar :value=inputSalesData.stayHour variant="success">
                                                        <span><strong>{{ getStayHourStr(inputSalesData.stayHour) }}</strong></span>
                                                    </b-progress-bar>
                                                </b-progress>
                                            </b-col>
                                        </b-row>
                                        <b-row class="pl-3 pr-3">
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in basicPriceMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <SelectForm
                                                            :optionType=4
                                                            v-model="inputSalesData.selectedBasicPlan"
                                                        />
                                                    </td>
                                                    <td class="width20">
                                                        {{ basicPlanPrice }}
                                                    </td>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.selectedBasicPlanNum"
                                                            inline
                                                            max=1
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton>
                                                    </td>
                                                </tr>
                                            </table>
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in extentionPriceMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>30分</td>
                                                    <td class="width20">{{ extentionPrice }}</td>
                                                    <td class="width20">
                                                        <b-form-group
                                                        >
                                                            <SelectForm
                                                                :optionType=99
                                                                v-model="inputSalesData.extentionNum"
                                                            />
                                                        </b-form-group>
                                                    </td>
                                                </tr>
                                            </table>
                                        </b-row>
                                        <b-row v-if="inputSalesData.basicPlanType == 1" class="pl-3 pr-3">
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in basicPriceVipSeatMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        VIP Seat
                                                    </td>
                                                    <td class="width20">
                                                        {{ vipSeatPrice }}
                                                        <!-- {{ basicPriceVipSeat }} -->
                                                    </td>
                                                    <td class="width30">
                                                        <b-form-group
                                                        >
                                                            <SelectForm
                                                                :optionType=99
                                                                v-model="inputSalesData.vipSeatNum"
                                                            />
                                                        </b-form-group>
                                                        <!-- <b-form-spinbutton
                                                            v-model="inputSalesData.vipSeatNum"
                                                            inline
                                                            max=1
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton> -->
                                                    </td>
                                                </tr>
                                            </table>
                                        </b-row>
                                    </b-container>
                                </b-card>
                            </b-col>

                            <b-col cols="6" v-if="showDiffBasicPlan">
                                <b-card class="moveSeatCard" style="min-height: 540px;">
                                    <label>
                                        基本料金（席移動後）
                                        <span
                                            style="display: inline-block; margin-left: 0.4rem;"
                                        >
                                            <b-icon
                                                id="after_move_basic_plan_type_info_icon"
                                                icon="info-circle"
                                                variant="primary"
                                            ></b-icon>
                                        </span>
                                        <b-tooltip
                                            target="after_move_basic_plan_type_info_icon"
                                            title="席移動後の基本料金をそれぞれ入力してください。"
                                        ></b-tooltip>
                                    </label>
                                    <b-container>
                                        <b-row style="min-height: 80px;" align-h="between">
                                            <b-col cols="6">
                                                <b-card-sub-title>料金タイプ</b-card-sub-title>
                                                <b-form-group style="min-height: 40px;">
                                                    <b-form-radio-group
                                                        v-model="inputSalesData.basicPlanTypeOther"
                                                        :options=basicPlanOptions
                                                        button-variant="outline-primary"
                                                        buttons
                                                        style="min-height: 40px;"
                                                        disabled
                                                    ></b-form-radio-group>
                                                    <b-icon
                                                        v-if="inputSalesData.basicPlanTypeOther == 1"
                                                        font-scale="1.8"
                                                        icon="bookmark-star-fill"
                                                        variant="primary"
                                                        class="ml-3 pl-3"
                                                    ></b-icon>
                                                </b-form-group>
                                            </b-col>
                                            <b-col>
                                                <b-form-group>
                                                    <b-form-checkbox-group
                                                        v-if="inputSalesData.basicPlanTypeOther == 1"
                                                        style="margin-top: 14px;"
                                                        v-model="inputSalesData.isCharteredOther"
                                                        :options=charterOptions
                                                        buttons
                                                        button-variant="primary"
                                                    ></b-form-checkbox-group>
                                                </b-form-group>
                                            </b-col>
                                        </b-row>
                                        <b-row>
                                            <b-col cols="6" class="input_sales_visit">
                                                <div class="input_sales_visit_time_wrap">
                                                    <div class="input_sales_visit_time">
                                                        <b-card-sub-title
                                                            class="input_sales_visit_time_title form_required"
                                                        >席移動時間</b-card-sub-title>
                                                        <b-row>
                                                            <b-form-group class="input_sales_visit_time_select_wrap">
                                                                <b-form-group>
                                                                    <SelectForm
                                                                        :optionType=5
                                                                        v-model="inputSalesData.leaveTimeHour"
                                                                    />
                                                                    ：
                                                                    <b v-if="inputSalesData.leaveTimeHour != 20">
                                                                        <SelectForm
                                                                            :optionType=2
                                                                            v-model="inputSalesData.leaveTimeMinute"
                                                                        />
                                                                    </b>
                                                                    <b v-else>
                                                                        <SelectForm
                                                                            :optionType=6
                                                                            v-model="inputSalesData.leaveTimeMinute"
                                                                        />
                                                                    </b>
                                                                </b-form-group>
                                                            </b-form-group>
                                                        </b-row>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="6" class="input_sales_leave">
                                                <div class="input_sales_visit_time_wrap">
                                                    <div class="input_sales_visit_time">
                                                        <b-card-sub-title
                                                            class="input_sales_visit_time_title form_required"
                                                        >退店時間</b-card-sub-title>
                                                        <b-form-group class="input_sales_visit_time_select_wrap">
                                                            <b-form-group>
                                                                <SelectForm
                                                                    :optionType=5
                                                                    v-model="inputSalesData.leaveTimeHourAfterMove"
                                                                />
                                                                ：
                                                                <b v-if="inputSalesData.leaveTimeHourAfterMove != 20">
                                                                    <SelectForm
                                                                        :optionType=2
                                                                        v-model="inputSalesData.leaveTimeMinuteAfterMove"
                                                                    />
                                                                </b>
                                                                <b v-else>
                                                                    <SelectForm
                                                                        :optionType=6
                                                                        v-model="inputSalesData.leaveTimeMinuteAfterMove"
                                                                    />
                                                                </b>
                                                            </b-form-group>
                                                        </b-form-group>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="12" class="pt-0">
                                                <b-form-invalid-feedback :state="visitTimeOtherError.length == 0">
                                                    {{ visitTimeOtherError }}
                                                </b-form-invalid-feedback>
                                            </b-col>
                                            <b-col>
                                                <label>
                                                    滞在時間
                                                </label>
                                                <b-progress :max="maxHour" height="2rem">
                                                    <b-progress-bar :value=inputSalesData.stayHourOther variant="success">
                                                        <span><strong>{{ getStayHourStr(inputSalesData.stayHourOther) }}</strong></span>
                                                    </b-progress-bar>
                                                </b-progress>
                                            </b-col>
                                        </b-row>
                                        <b-row class="pl-3 pr-3">
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in basicPriceMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <SelectForm
                                                            :optionType=4
                                                            v-model="inputSalesData.selectedBasicPlanOther"
                                                        />
                                                    </td>
                                                    <td class="width20">{{ basicPlanPriceOther }}</td>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.selectedBasicPlanOtherNum"
                                                            inline
                                                            max=1
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton>
                                                    </td>
                                                </tr>
                                            </table>
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in extentionPriceMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>30分</td>
                                                    <td class="width20">{{ extentionPriceOther }}</td>
                                                    <td class="width20">
                                                        <b-form-group
                                                        >
                                                            <SelectForm
                                                                :optionType=99
                                                                v-model="inputSalesData.extentionOtherNum"
                                                            />
                                                        </b-form-group>
                                                    </td>
                                                </tr>
                                            </table>
                                        </b-row>
                                        <b-row v-if="inputSalesData.basicPlanTypeOther == 1" class="pl-3 pr-3">
                                            <table class="mt-3">
                                                <tr>
                                                    <th
                                                        v-for="(menuItem, id) in basicPriceVipSeatMenu"
                                                        :key=id
                                                        :class=menuItem.class
                                                    >{{ menuItem.text }}</th>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        VIP Seat
                                                    </td>
                                                    <td class="width20">
                                                        {{ vipSeatPriceOther }}
                                                        <!-- {{ basicPriceVipSeat }} -->
                                                    </td>
                                                    <td class="width30">
                                                        <b-form-group
                                                        >
                                                            <SelectForm
                                                                :optionType=99
                                                                v-model="inputSalesData.vipSeatNumOther"
                                                            />
                                                        </b-form-group>
                                                        <!-- <b-form-spinbutton
                                                            v-model="inputSalesData.vipSeatNumOther"
                                                            inline
                                                            max=1
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton> -->
                                                    </td>
                                                </tr>
                                            </table>
                                        </b-row>
                                    </b-container>
                                </b-card>
                            </b-col>
                            <b-col cols="12">
                                <b-card>
                                    <label class="mt-1">
                                        指名情報
                                    </label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="appoint_info_icon"
                                            icon="info-circle"
                                            variant="primary"
                                        ></b-icon>
                                    </span>
                                    <b-tooltip
                                        target="appoint_info_icon"
                                        title="指名の場合、キャストを追加してください。"
                                    ></b-tooltip>
                                    <b-container fluid class="appoint_cast_area_wrap" style="min-height: 100px; max-height: 347px;">
                                        <b-row>
                                            <b-col cols="3">
                                                <b-card-sub-title>指名有無</b-card-sub-title>
                                                <b-form-group>
                                                    <b-form-radio-group
                                                        v-model="inputSalesData.isAppointed"
                                                        :options=appointOptions
                                                        button-variant="outline-primary"
                                                        buttons
                                                    ></b-form-radio-group>
                                                </b-form-group>
                                            </b-col>

                                            <b-col>
                                                <b-button
                                                    v-if="inputSalesData.isAppointed == 1"
                                                    size="sm"
                                                    @click="showAddCastDialog"
                                                    class="mt-3"
                                                    pill
                                                    variant="outline-success"
                                                >
                                                    <b-icon
                                                        icon="person-plus"
                                                        aria-hidden="true"
                                                    ></b-icon> キャスト追加
                                                </b-button>
                                            </b-col>
                                        </b-row>
                                        <b-row>
                                            <table
                                                v-if="appointedCastDataList.length > 0 && inputSalesData.isAppointed == 1"
                                                class="appointed_cast_area"

                                            >
                                                <tr>
                                                    <th
                                                        v-for="(castHeader, id) in appointedCastHeader"
                                                        :key=id
                                                    >{{ castHeader.text }}</th>
                                                </tr>
                                                <tr
                                                    v-for="(castData, idx) in appointedCastDataList"
                                                    :key=idx
                                                >
                                                    <!-- <td>
                                                        <div>
                                                            <img
                                                                src="@/assets/img/女性11.jpg"
                                                                class="cast_icon"
                                                                top
                                                            >
                                                        </div>
                                                        <b-avatar
                                                            :src="apiPath + castData.cast.icon"
                                                            class="cast_icon"
                                                            v-if="castData.cast.icon != null"
                                                        ></b-avatar>
                                                        <b-avatar
                                                            :src="defaultCastIcon"
                                                            class="cast_icon"
                                                            v-else
                                                        ></b-avatar>
                                                    </td> -->
                                                    <td style="display: flex;">
                                                        <div>
                                                            <img
                                                                src="@/assets/img/女性11.jpg"
                                                                class="cast_icon"
                                                                top
                                                            >
                                                        </div>
                                                        <div class="mt-2" style="margin-left: 15px;">
                                                            <b-card-title style="font-size: 15px;">
                                                                {{ castData.cast.name }}
                                                            </b-card-title>
                                                            <b-card-sub-title style="font-size: 12px;">
                                                                {{ castData.cast.age }} 歳
                                                            </b-card-sub-title>
                                                        </div>
                                                    <td>{{ getAppointStr(castData.appointType) }}</td>
                                                    <td>{{ castData.appointPrice }}</td>
                                                    <td>{{ getDouhanStr(castData.isDouhan) }}</td>
                                                    <td class="ml-0 pl-0">
                                                        <b-form-group
                                                        >
                                                            <SelectForm
                                                                :optionType=99
                                                                v-model="appointedCastDataList[idx].quantity"
                                                            />
                                                            <!-- <b-form-select
                                                                v-model="appointedCastDataList[idx].quantity"
                                                                :options="numOptions"
                                                                value-field="value"
                                                                text-field="text"
                                                                class="input_sales_basic_price_select"
                                                            ></b-form-select> -->
                                                        </b-form-group>
                                                    </td>

                                                    <td>
                                                        <!-- <b-icon
                                                            icon="dash-square"
                                                            aria-hidden="true"
                                                            @click="deleteCast(castData, idx)"
                                                            variant="danger"
                                                            class="trash_icon"
                                                        ></b-icon> -->
                                                        <b-button
                                                            size="sm"
                                                            style="margin-right: 5px !important;"
                                                            @click="showEditAddCastDialog(castData, idx)"
                                                            variant="outline-primary"
                                                        >
                                                            <b-icon
                                                                icon="pencil"
                                                                aria-hidden="true"
                                                                class="mr-1"
                                                            ></b-icon>
                                                        </b-button>
                                                        <b-button
                                                            size="sm"
                                                            @click="deleteCast(castData, idx)"
                                                            variant="outline-danger"
                                                        >
                                                            <b-icon
                                                                icon="trash"
                                                                aria-hidden="true"
                                                                variant="danger"
                                                                class="trash_icon"
                                                            ></b-icon>
                                                        </b-button>
                                                    </td>
                                                </tr>
                                            </table>
                                        </b-row>
                                    </b-container>
                                </b-card>
                            </b-col>
                        </b-row>

                    </b-form-group>
                </b-card>

                <b-card bg-variant="light" class="mt-3">
                    <!-- label-cols-lg="3"
                    label="明細"
                    label-size="lg"
                    label-class="font-weight-bold pt-0" -->
                    <b-form-group
                        class="mb-0"
                    >
                        <label
                        >明細</label>
                        <span
                            style="display: inline-block; margin-left: 0.4rem;"
                        >
                            <b-icon
                                id="sales_detail_info_icon"
                                icon="info-circle"
                                variant="primary"
                            ></b-icon>
                        </span>
                        <b-tooltip
                            target="sales_detail_info_icon"
                            title="明細情報を追加してください。"
                        ></b-tooltip>
                        <b-row>
                            <b-col cols="4">
                                <b-button
                                    size="sm"
                                    @click="showAddDetailDialog"
                                    class="mt-3"
                                    variant="primary"
                                >
                                    <b-icon
                                        icon="plus-circle"
                                        aria-hidden="true"
                                    ></b-icon> 明細を追加...
                                </b-button>
                            </b-col>
                        </b-row>
                    </b-form-group>
                    <table>
                        <tr>
                            <th>商品名</th>
                            <!-- <th>定価</th> -->
                            <th>実価格</th>
                            <th>数量</th>
                            <th>ボトル</th>
                            <!-- <th>課税</th> -->
                            <th>総計(税抜)</th>
                            <th>総計(税込)</th>
                            <th>備考</th>
                            <th></th>
                        </tr>
                        <tr
                            v-for="(item, id) in inputSalesDetailData"
                            :key=id
                        >
                            <td>
                                <b-img
                                    v-if="item.thumbnail != null"
                                    :src="apiPath + item.thumbnail"
                                    alt="Selected Product"
                                    rounded
                                    height="50"
                                    width="50"
                                ></b-img>
                                <b-img
                                    v-else
                                    :src="defaultIcon"
                                    alt="Selected Product"
                                    rounded
                                    height="50"
                                    width="50"
                                ></b-img>
                                <span>{{ item.name }}</span>
                            </td>
                            <!-- <td>{{ item.price }}</td> -->
                            <td>{{ item.actuallyPrice }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>
                                <b-card-text v-if="item.bottle">登録</b-card-text>
                                <b-card-text v-else>--</b-card-text>
                            </td>
                            <!-- <td>
                                {{ item.taxation }}
                            </td> -->
                            <td>{{ item.totalPrice }}</td>
                            <td>{{ item.totalTaxPrice }}</td>
                            <td>{{ item.remarks }}</td>
                            <td>
                                <b-icon
                                    icon="dash-square"
                                    font-scale="1.5"
                                    variant="danger"
                                    class="mt-2 input_sales_delete_product_btn"
                                    @click="deleteSalesDetail(item)"
                                ></b-icon>
                            </td>
                        </tr>
                    </table>
                </b-card>
                <b-card bg-variant="light" class="mt-3" v-if="inputSalesData.customer_type == 1">
                    <b-form-group
                        label-cols-lg="3"
                        label="ボトル情報"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                    >
                        <b-card-text v-if="inputSalesData.customerNo == '' || inputSalesData.customerNo == null">
                            会員Noが入力されていません
                        </b-card-text>
                        <b-row v-else>
                            bottle
                        </b-row>
                    </b-form-group>
                </b-card>
                <b-card bg-variant="light" class="mt-3">
                    <b-form-group
                        label-cols-lg="3"
                        label="備考"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                    >
                        <b-form-textarea
                            rows="2"
                            no-resize
                            v-model="inputSalesData.remarks"
                        ></b-form-textarea>
                    </b-form-group>
                </b-card>
            </b-form>
            <template #modal-footer>
                <b-container fluid>
                    <b-row>
                        <b-col cols="2">
                            <b-card-sub-title>
                                総計(税抜)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                <b-icon icon="currency-yen"></b-icon> {{ totalPrice }}
                            </b-card-title>
                        </b-col>
                        <b-col cols="2">
                            <b-card-sub-title>
                                総計(税込)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                <b-icon icon="currency-yen"></b-icon> {{ totalTaxPrice }}
                            </b-card-title>
                        </b-col>
                        <b-col
                            cols="2"
                            class="mt-0 pt-0"
                        >
                            <b-form-group
                                label="税率"
                                class="mt-0 pt-0 mb-0 pb-0"
                            >
                                <SelectForm
                                    :optionType=3
                                    v-model="inputSalesData.totalSalesTax"
                                />%
                            </b-form-group>
                        </b-col>
                        <b-col
                            cols="2"
                            class="mt-0 pt-0"
                        >
                            <b-form-group
                                label="カード会計"
                                class="mt-0 pt-0 mb-0 pb-0"
                            >
                                <CheckboxForm
                                    v-model=inputSalesData.cardPayment
                                />
                            </b-form-group>
                        </b-col>
                        <b-col align="right" class="add_sales_detail_footer_col">
                            <b-button
                                variant="secondary"
                                @click="close"
                                class="btn_close"
                            >
                                閉じる
                            </b-button>
                            <b-button
                                variant="primary"
                                @click="registerOrUpdate"
                                :disabled=isDisabled
                            >
                                登録
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>

        <InputSalesAddDetailDialog
            ref="inputSalesAddDetailDialog"
        />

        <InputSalesAddCastDialog
            ref="inputSalesAddcastDialog"
            :appointed="appointedCastDataList"
            @add="addCastData"
            @update="updateCastData"
        />

        <ErrorModal
            ref="errorModal"
            :errorMsg="errorMsg"
        />
    </div>
</template>

<script>

import Vue from 'vue'
import _ from 'lodash'
import InputSalesDetailDialog from '@/components/common/dialog/InputSalesDetailDialog'
import InputSalesAddDetailDialog from '@/components/common/dialog/InputSalesAddDetailDialog'
import InputSalesAddCastDialog from '@/components/common/dialog/InputSalesAddCastDialog'
import SelectForm from '@/components/common/parts/SelectForm'
import ErrorModal from '@/components/common/dialog/ErrorModal'
import CheckboxForm from '@/components/common/parts/CheckboxForm'
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)
import Decimal from 'decimal.js'
const now = dayjs().format('YYYY-MM-DD')
const Con = new Const()
import utilsMixin from '@/mixins/utils'
import validateMixin from '@/mixins/validate'

export default {
    name: 'InputSalesDialogItem',
    props: {
    },
    components: {
        InputSalesDetailDialog,
        InputSalesAddCastDialog,
        InputSalesAddDetailDialog,
        SelectForm,
        CheckboxForm,
        ErrorModal
    },
    data: () => ({
        dialog: false,
        inputSalesData: {
            basicPlanType: 0, // 選択されている料金タイプの種類
            customerNo: null,
            totalVisitors: null,
            accountDate: now,
            visitTimeHour: null, // 来店時間（時）
            visitTimeMinute: null, // 来店時間（分）
            leaveTimeHour: null, // 退店時間（時）=> 席移動の場合は席移動時間（時）
            leaveTimeMinute: null, // 退店時間（分）=> 席移動の場合は席移動時間（分）
            selectedBasicPlan: 0, // SET料金のどれを選択しているか
            selectedBasicPlanNum: 0, // SET料金の数量 1 or 0。サービスも考慮
            stayHour: 0, // 滞在時間

            isChartered: [],
            isCharteredOther: [],

            // 延長はcomputedでextention_price
            extentionNum: 0, // 延長料金の数量 1 or 0。

            // VIP_SEATはbasicPlanType == 1の時
            vipSeatNum: 0, // VIPの席料金の数量 1 or 0。サービスも考慮

            basicPlanTypeOther: 1, // 選択されている料金タイプの種類（席移動先）basicPlanTypeと逆（computedで）
            leaveTimeHourAfterMove: null, // 席移動後の退店時間（時）
            leaveTimeMinuteAfterMove: null, // 席移動後の退店時間（分）
            stayHourOther: 0, // 滞在時間（席移動先）
            selectedBasicPlanOther: 0, // SET料金のどれを選択しているか（席移動後）
            selectedBasicPlanOtherNum: 1, // SET料金の数量 1 or 0。サービスも考慮（席移動後）
            extentionOtherNum: 0, // 延長料金の数量 1 or 0。
            vipSeatNumOther: 0, // VIPの席料金の数量 1 or 0。サービスも考慮

            totalSalesTax: Con.TAX_DEFAULT,
            cardPayment: false,
            isAppointed: 0,

            remarks: '',

            customer_type: 0,
        },

        showDiffBasicPlan: false, // 席移動入力状態。trueは席移動したと見なす


        inputSalesDetailData: [],
        appointedCastDataList: [],

        inputSalesDetailDialog: false,
        basicPriceVipSeat: Con.BASIC_PRICE_VIP_SEAT, // VIPの席料金


        taxOptions: Con.OPTIONS_TAX,
        numOptions: Con.OPTIONS_NUM,
        hourOptions: Con.OPTIONS_HOUR,
        hourAllOptions: Con.OPTIONS_HOUR_ALL,
        minuteOptions: Con.OPTIONS_MINUTE,

        maxHour: 300, // 滞在時間のMAXとなる
        apiPath: Con.API_PATH, // APIのURL
        defaultCastIcon: 'http://localhost:8000/media/upload/女性1111.png',
        defaultIcon: Con.DEFAULT_ALCOHOL_ICON, // デフォで酒の画像出しているが・・・
        appointedCastHeader: [
            // { text: '' },
            { text: '名前' },
            { text: '指名' },
            { text: '指名料' },
            { text: '同伴' },
            { text: '数量' },
            { text: '更新' },
        ],
        basicPriceMenu: [
            { text: 'SET料金', class: 'width50' },
            { text: '金額', class: 'width20' },
            { text: '数量', class: 'width30' },
        ],
        basicPriceVipSeatMenu: [
            { text: '席料金', class: 'width50' },
            { text: '金額', class: 'width20' },
            { text: '数量', class: 'width30' }
        ],
        extentionPriceMenu: [
            { text: '延長料金', class: 'width50' },
            { text: '金額', class: 'width20' },
            { text: '数量', class: 'width30' }
        ],
        basicPlanOptions: [
            { text: 'Normal', value: 0 },
            { text: 'VIP', value: 1 },
        ],
        appointOptions: [
            { text: 'フリー', value: 0 },
            { text: '指名', value: 1 },
        ],
        charterOptions: [
            { text: '貸切', value: 1 }
        ],
        moveDiffSeatOptions: [
            { text: '移動', value: 1 }
        ],
        errorMsg: [],
        totalVisitorsError: '',
        customerNoError: '',
        nonMemberNameError: '',
        visitTimeError: '',
        visitTimeOtherError: '',
        leaveTimeError: '',
        leaveAfterTimeError: '',
        moveTimeError: '',
        editMode: false,
        salesHeaderId: null,
        edit_sales_detail: [],
        edit_sales_service_detail: [],
        edit_sales_appoint_detail: [],
        customerInfo: null,

        customerTypeOptions: [
            { text: '非会員', value: 0 },
            { text: '会員', value: 1 },
        ],
    }),
    created () {
        this.$eventHub.$off('addCast')
        this.$eventHub.$on('addCast', this.addCast)

        this.$eventHub.$off('addSalesDetail')
        this.$eventHub.$on('addSalesDetail', this.addSalesDetail)
        this.$eventHub.$off('addSalesDetailList')
        this.$eventHub.$on('addSalesDetailList', this.addSalesDetailList)


        const now = dayjs()
        const one = dayjs('2022-01-01 23:00:00')
        const two = dayjs('2022-01-01 23:51:00')
        const res = two.diff(one, 'minute')
        const h = Math.floor(res / 60)
        const m = res % 60
    },
    computed: {
        ...mapGetters([
            'customer',
            'bottle',
        ]),
        inputSalesDialogTitle () {
            if (this.editMode) {
                return '売上入力（編集） 伝票No.' + this.salesHeaderId
            } else {
                return '売上入力（新規作成）'
            }
        },
        totalPrice () {
            let totalPrice = 0

            totalPrice += this.culcBasicPlanPrice + this.culcBasicPlanPriceOther
            totalPrice += this.culcExtentionPrice + this.culcExtentionOtherPrice
            totalPrice += this.appointPrice + this.douhanPrice
            totalPrice += this.salesDetailTotalPrice

            return totalPrice
        },
        totalTaxPrice () {
            let totalPrice = 0

            totalPrice += this.culcBasicPlanPrice + this.culcBasicPlanPriceOther
            totalPrice += this.culcExtentionPrice + this.culcExtentionOtherPrice
            totalPrice += this.appointPrice + this.douhanPrice
            // 課税対象外の商品は外す
            // totalPrice += this.salesDetailTotalPrice
            let tax = (this.inputSalesData.cardPayment) ? this.inputSalesData.totalSalesTax + 10 : this.inputSalesData.totalSalesTax
            totalPrice = this.roundDown(this.calcAddTaxPrice(totalPrice, tax))
            return totalPrice + this.salesDetailTotalPrice
        },
        isDisabled () {
            // 席移動選択時には席移動のもののチェックも必要
            if (!this.isPositiveNumber(this.inputSalesData.customerNo)
                || !this.isPositiveNumber(this.inputSalesData.totalVisitors)
                || this.totalVisitorsError.length != 0) {
                    return true
                }
            return false
        },
        basicPlanPrice () {
            if (this.inputSalesData.basicPlanType == 0) {
                return Con.BASIC_PLAN_NORMAL_PRICE[this.inputSalesData.selectedBasicPlan]
            }
            return Con.BASIC_PLAN_VIP_PRICE[this.inputSalesData.selectedBasicPlan]
        },
        basicPlanPriceOther () {
            if (this.inputSalesData.basicPlanTypeOther == 0) {
                return Con.BASIC_PLAN_NORMAL_PRICE[this.inputSalesData.selectedBasicPlan]
            }
            return Con.BASIC_PLAN_VIP_PRICE[this.inputSalesData.selectedBasicPlan]
        },
        extentionPrice () {
            return Con.BASIC_PLAN_EXTENTION[this.inputSalesData.basicPlanType]
        },
        extentionPriceOther () {
            return Con.BASIC_PLAN_EXTENTION[this.inputSalesData.basicPlanTypeOther]
        },
        culcBasicPlanPrice () {
            let total = 0
            total += this.basicPlanPrice * this.inputSalesData.selectedBasicPlanNum
            if (this.inputSalesData.basicPlanType == 1) {
                total += this.vipSeatPrice * this.inputSalesData.vipSeatNum
            }
            return total
        },
        culcBasicPlanPriceOther () {
            if (!this.showDiffBasicPlan) return 0

            let total = 0
            total += this.basicPlanPriceOther * this.inputSalesData.selectedBasicPlanOtherNum
            if (this.inputSalesData.basicPlanTypeOther == 1) {
                total += this.vipSeatPriceOther * this.inputSalesData.vipSeatNumOther
            }
            return total
        },
        culcExtentionPrice () {
            return this.extentionPrice * this.inputSalesData.extentionNum
        },
        culcExtentionOtherPrice () {
            if (!this.showDiffBasicPlan) return 0
            return this.extentionPriceOther * this.inputSalesData.extentionOtherNum
        },
        appointPrice () {
            if (this.inputSalesData.isAppointed == 0) return 0
            let total = 0
            for (const i in this.appointedCastDataList) {
                total += this.calcQuantityPrice(
                    this.appointedCastDataList[i].appointPrice,
                    this.appointedCastDataList[i].quantity,
                )
            }
            return total
        },
        douhanPrice () {
            let total = 0
            for (const i in this.appointedCastDataList) {
                total += this.appointedCastDataList[i].douhanPrice
            }
            return total
        },
        salesDetailTotalPrice () {
            let total = 0
            for (const i in this.inputSalesDetailData) {
                total += this.inputSalesDetailData[i].totalPrice
            }
            return total
        },
        salesDetailTotalTaxPrice () {
            let total = 0
            for (const i in this.inputSalesDetailData) {
                total += this.inputSalesData[i].totalTaxPrice
            }
            return total
        },
        moveSeatTimeText () {
            if (this.showDiffBasicPlan) {
                return '席移動時間'
            } else {
                return '退店時間'
            }
        },
        isExtention () {
            if (this.inputSalesData.stayHour > 60) {
                return true
            }
            return false
        },
        isExtentionOther () {
            if (this.showDiffBasicPlan && this.inputSalesData.stayHourOther > 60) {
                return true
            }
            return false
        },
        vipSeatPrice () {
            if (this.inputSalesData.isChartered.length > 0) {
                return Con.CHARTER_PRICE_VIP_SEAT
            }
            if (this.inputSalesData.totalVisitors > 0) {
                return Con.BASIC_PRICE_VIP_SEAT * this.inputSalesData.totalVisitors
            }
            return Con.BASIC_PRICE_VIP_SEAT
        },
        vipSeatPriceOther () {
            if (this.inputSalesData.isCharteredOther.length > 0) {
                return Con.CHARTER_PRICE_VIP_SEAT
            }
            if (this.inputSalesData.totalVisitors > 0) {
                return Con.BASIC_PRICE_VIP_SEAT * this.inputSalesData.totalVisitors
            }
            return Con.BASIC_PRICE_VIP_SEAT
        },
        totalVisitorsInvalid () {
            if (this.totalVisitorsError.length != 0) {
                return true
            }
            return false
        },
        customerNoInvalid () {
            if (this.customerNoError != '') {
                return true
            }
            return false
        },
        nonMemberNameInvalid () {
            if (this.nonMemberNameError != '') {
                return true
            }
            return false
        },
        basicPlanAreaCol () {
            if (this.showDiffBasicPlan) {
                return '6'
            } else {
                return '12'
            }
        }
    },
    watch: {
        'inputSalesData.visitTimeHour': function (val) {
            if (val != null
                && this.inputSalesData.visitTimeMinute != null
                && this.inputSalesData.leaveTimeHour != null
                && this.inputSalesData.leaveTimeMinute != null)
            {
                this.calcBasicPlan()
            }
        },
        'inputSalesData.visitTimeMinute': function (val) {
            if (val != null
                && this.inputSalesData.visitTimeHour != null
                && this.inputSalesData.leaveTimeHour != null
                && this.inputSalesData.leaveTimeMinute != null)
            {
                this.calcBasicPlan()
            }
        },
        'inputSalesData.leaveTimeHour': function (val) {
            if (val != null
                && this.inputSalesData.visitTimeHour != null
                && this.inputSalesData.visitTimeMinute != null
                && this.inputSalesData.leaveTimeMinute != null)
            {
                this.calcBasicPlan()
                if (this.showDiffBasicPlan) {
                    this.calcBasicPlanOther()
                }
            }
        },
        'inputSalesData.leaveTimeMinute': function (val) {
            if (val != null
                && this.inputSalesData.visitTimeHour != null
                && this.inputSalesData.visitTimeMinute != null
                && this.inputSalesData.leaveTimeHour != null)
            {
                this.calcBasicPlan()
                if (this.showDiffBasicPlan) {
                    this.calcBasicPlanOther()
                }
            }
        },
        'inputSalesData.leaveTimeHourAfterMove': function (val) {
            if (val != null
                && this.inputSalesData.leaveTimeHour != null
                && this.inputSalesData.leaveTimeMinute != null
                && this.inputSalesData.leaveTimeMinuteAfterMove != null)
            {
                this.calcBasicPlanOther()
            }
        },
        'inputSalesData.leaveTimeMinuteAfterMove': function (val) {
            if (val != null
                && this.inputSalesData.leaveTimeHour != null
                && this.inputSalesData.leaveTimeMinute != null
                && this.inputSalesData.leaveTimeHourAfterMove != null)
            {
                this.calcBasicPlanOther()
            }
        },
        'inputSalesData.basicPlanType': function (val) {
            if (val == 0) {
                this.inputSalesData.basicPlanTypeOther = 1
            } else {
                this.inputSalesData.basicPlanTypeOther = 0
            }
        },
        'inputSalesData.totalVisitors': function (val) {
            const reg = /^[0-9]+$/
            if (val == null) {
                this.totalVisitorsError = ''
                return
            }
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.totalVisitorsError = '正しい値を入力してください'
                } else if (val > 30) {
                    this.totalVisitorsError = '1 ~ 30の値を入力してください'
                } else {
                    this.totalVisitorsError = ''
                }
            } else {
                this.totalVisitorsError= '来店人数を入力してください'
            }

            if (this.inputSalesData.basicPlanType == 1) {
                if (val != '' && val >= Con.CHARTER_TOTAL_NUM) {
                    this.inputSalesData.isChartered = [1]
                }
            } else {
                this.inputSalesData.isChartered = []
            }
            if (this.inputSalesData.basicPlanTypeOther == 1) {
                if (val != '' && val >= Con.CHARTER_TOTAL_NUM) {
                    this.inputSalesData.isCharteredOther = [1]
                }
            } else {
                this.inputSalesData.isCharteredOther = []
            }
        },
        'inputSalesData.customerNo': function (val) {
            const reg = /^[0-9]+$/
            if (val == null) {
                this.customerNoError = ''
                return
            }
            if (val.length > 0) {
                if (val <= 0 || !reg.test(val)) {
                    this.customerNoError = '正しい値を入力してください'
                    this.customerInfo = null
                } else {
                    this.customerInfo = _.cloneDeep(this.customer.find(c => c.customer_no == val))
                    if (this.customerInfo == undefined) {
                        this.customerNoError = '存在しない会員Noです。'
                    } else {
                        this.customerNoError = ''
                    }
                }
            } else {
                // this.customerNoError= ''
                this.customerNoError= '会員Noを入力してください'
                this.customerInfo = null
            }
        },
        'inputSalesData.nonMemberName': function (val) {
            this.nonMemberNameError = this.validateName(val, false)
        },
        'inputSalesData.isChartered': function (val) {
            this.calcBasicPlan()
        },
        'inputSalesData.isCharteredOther': function (val) {
            this.calcBasicPlanOther()
        },
    },
    methods: {
        calcBasicPlan () {
            this.inputSalesData.selectedBasicPlanNum = 1
            const VISIT_TIME_FOR_DIFF = (this.inputSalesData.visitTimeHour >= 20) ? Con.BASIC_PLAN_TIME_FOR_DIFF_A : Con.BASIC_PLAN_TIME_FOR_DIFF_B
            const LEAVE_TIME_FOR_DIFF = (this.inputSalesData.leaveTimeHour >= 20) ? Con.BASIC_PLAN_TIME_FOR_DIFF_A : Con.BASIC_PLAN_TIME_FOR_DIFF_B
            // 来店時間
            const visitTime = dayjs(VISIT_TIME_FOR_DIFF + this.inputSalesData.visitTimeHour + ':' + this.inputSalesData.visitTimeMinute + ':00')
            // 退店時間（席移動時は席移動時間）
            const leaveTime = dayjs(LEAVE_TIME_FOR_DIFF + this.inputSalesData.leaveTimeHour + ':' + this.inputSalesData.leaveTimeMinute + ':00')

            // 退店時間と来店時間の差分（席移動時は席移動時間と来店時間の差分）
            const diff = leaveTime.diff(visitTime, 'minute')
            // 延長料金を出すためにSET料金分の1時間を引く
            const diff_minute = diff-60
            // 延長料金の数量を出すために30で割って切り上げする
            const extention_time = Math.ceil(diff_minute / 30)

            const isCharted = this.inputSalesData.isChartered.length > 0
            const vipSeatTypeMinute = (isCharted) ? 120 : 60

            if (diff_minute > 0) {
                // 延長料金が発生しているパターン
                this.inputSalesData.extentionNum = extention_time
            } else {
                // 延長料金は発生していないパターン
                this.inputSalesData.extentionNum = 0
            }

            if (visitTime.isSameOrAfter(leaveTime)) {
                this.inputSalesData.selectedBasicPlan = 0
                this.inputSalesData.extentionNum = 0
                this.inputSalesData.stayHour = 0
                this.inputSalesData.vipSeatNum = 0
                this.visitTimeError = '入店時間が退店時間より早い時間となるように入力してください。'
            } else {
                this.inputSalesData.vipSeatNum = Math.ceil(diff/vipSeatTypeMinute)
                this.visitTimeError = ''
                // プランAの判別（20:30~21:30）
                if (visitTime.isSameOrAfter(dayjs(Con.BASIC_PLAN_A_TIME))
                        && visitTime.isBefore(dayjs(Con.BASIC_PLAN_B_TIME))) {
                    this.inputSalesData.selectedBasicPlan = 0
                    this.inputSalesData.stayHour = diff

                // プランBの判別（21:30~22:30）
                } else if (visitTime.isSameOrAfter(dayjs(Con.BASIC_PLAN_B_TIME))
                        && visitTime.isBefore(dayjs(Con.BASIC_PLAN_C_TIME))) {
                    this.inputSalesData.selectedBasicPlan = 1
                    this.inputSalesData.stayHour = diff
                // プランCの判別（22:30~LAST）
                } else {
                    this.inputSalesData.selectedBasicPlan = 2
                    this.inputSalesData.stayHour = diff

                }
            }

        },
        calcBasicPlanOther () {
            const MOVE_TIME_FOR_DIFF = (this.inputSalesData.leaveTimeHour >= 20) ? Con.BASIC_PLAN_TIME_FOR_DIFF_A : Con.BASIC_PLAN_TIME_FOR_DIFF_B
            const LEAVE_TIME_FOR_DIFF = (this.inputSalesData.leaveTimeHourAfterMove >= 20) ? Con.BASIC_PLAN_TIME_FOR_DIFF_A : Con.BASIC_PLAN_TIME_FOR_DIFF_B
            // 来店時間
            const moveTime = dayjs(MOVE_TIME_FOR_DIFF + this.inputSalesData.leaveTimeHour + ':' + this.inputSalesData.leaveTimeMinute + ':00')
            // 退店時間（席移動時は席移動時間）
            const leaveTime = dayjs(LEAVE_TIME_FOR_DIFF + this.inputSalesData.leaveTimeHourAfterMove + ':' + this.inputSalesData.leaveTimeMinuteAfterMove + ':00')

            // 席移動時間と退店時間の差分
            const diff = leaveTime.diff(moveTime, 'minute')
            // 延長料金を出すためにSET料金分の1時間を引く
            const diff_minute = diff-60
            // 延長料金の数量を出すために30で割って切り上げする
            const extention_time = Math.ceil(diff_minute / 30)

            const isCharted = this.inputSalesData.isCharteredOther.length > 0
            const vipSeatTypeMinute = (isCharted) ? 120 : 60

            if (diff_minute > 0) {
                // 延長料金が発生しているパターン
                this.inputSalesData.extentionOtherNum = extention_time
            } else {
                // 延長料金は発生していないパターン
                this.inputSalesData.extentionOtherNum = 0
            }

            if (moveTime.isSameOrAfter(leaveTime)) {
                this.inputSalesData.selectedBasicPlanOther = 0
                this.inputSalesData.selectedBasicPlanOtherNum = 0
                this.inputSalesData.stayHourOther = 0
                this.inputSalesData.vipSeatNumOther = 0
                this.visitTimeOtherError = '入店時間が退店時間より早い時間となるように入力してください。'
            } else {
                this.visitTimeOtherError = ''
                this.inputSalesData.vipSeatNumOther = Math.ceil(diff/vipSeatTypeMinute)
                // プランAの判別（20:30~21:30）
                if (moveTime.isSameOrAfter(dayjs(Con.BASIC_PLAN_A_TIME))
                        && moveTime.isBefore(dayjs(Con.BASIC_PLAN_B_TIME))) {
                    this.inputSalesData.selectedBasicPlanOther = 0
                    this.inputSalesData.stayHourOther = diff

                // プランBの判別（21:30~22:30）
                } else if (moveTime.isSameOrAfter(dayjs(Con.BASIC_PLAN_B_TIME))
                        && moveTime.isBefore(dayjs(Con.BASIC_PLAN_C_TIME))) {
                    this.inputSalesData.selectedBasicPlanOther = 1
                    this.inputSalesData.stayHourOther = diff
                // プランCの判別（22:30~LAST）
                } else {
                    this.inputSalesData.selectedBasicPlanOtherNum = 1
                    this.inputSalesData.stayHourOther = diff
                }
            }
        },
        ...mapMutations([
            'addSalesList',
            'updateSalesList',
            'deleteSalesList',
            'addBottleList',
            'updateBottleList',
            'deleteBottleList',
        ]),
        registerOrUpdate () {
            if (!this.editMode) {
                this.register()
            } else {
                this.update()
            }
        },
        register () {

            let sales_detail_service_list = []
            let sales_detail_appoint_list = []
            let sales_detail_list = []

            // この会計は同伴かをヘッダに持たせる
            let douhanFlg = false


            // キャスト指名情報の追加
            for (const i in this.appointedCastDataList) {
                let large_category = 1
                let middle_category = 0
                let appointType = this.appointedCastDataList[i].appointType
                let isDouhan = this.appointedCastDataList[i].isDouhan
                let cast_id = this.appointedCastDataList[i].cast.id
                let quantity = this.appointedCastDataList[i].quantity
                let appointPrice = this.appointedCastDataList[i].appointPrice

                if (isDouhan) {
                    // この会計は同伴かをヘッダに持たせる
                    douhanFlg = true
                    sales_detail_appoint_list.push(this.createDouhan(this.appointedCastDataList[i]))
                }

                if (!isDouhan) {
                    switch (appointType) {
                        case 0:
                        break
                        case 1:
                        middle_category = 1
                        break
                        case 2:
                        middle_category = 2
                        break
                        default:
                        break
                    }
                }


                let total = this.calcQuantityPrice(appointPrice, quantity)
                let taxTotal = this.calcAddTaxPrice(total, Con.TAX_DEFAULT)

                // 指名料を値引きなどする場合、こちらから動的に指定する必要あり。
                const appointData = {
                    basic_plan_type: this.inputSalesData.basicPlanType,
                    large_category: large_category,
                    middle_category: middle_category,
                    cast_id: cast_id,
                    quantity: quantity,
                    fixed_price: appointPrice,
                    fixed_tax_price: this.calcAddTaxPrice(appointPrice, Con.TAX_DEFAULT),
                    total_price: total,
                    total_tax_price: taxTotal,
                }

                sales_detail_appoint_list.push(appointData)

            }

            // 明細情報の追加
            for (const i in this.inputSalesDetailData) {
                const salesDetailItem = this.inputSalesDetailData[i]
                const actually_price = salesDetailItem.actuallyPrice
                const actually_tax_price = salesDetailItem.actuallyTaxPrice
                const product_id = salesDetailItem.product.id
                const quantity = salesDetailItem.quantity
                const bottle = salesDetailItem.bottle
                const totalPrice = salesDetailItem.totalPrice
                const totalTaxPrice = salesDetailItem.totalTaxPrice
                const taxRate = salesDetailItem.taxRate
                const remarks = salesDetailItem.remarks
                // 後に商品にキャストを紐づける用
                const cast_id = null

                const productData = {
                    product_id: product_id,
                    cast_id: cast_id,
                    quantity: quantity,
                    bottle: bottle,
                    fixed_price: actually_price,
                    fixed_tax_price: actually_tax_price,
                    total_price: totalPrice,
                    total_tax_price: totalTaxPrice,
                    remarks: remarks,
                    tax_rate: taxRate,
                }

                sales_detail_list.push(productData)
            }



            let diffDay = false
            let moveDiffDay = false
            let leaveDay = this.inputSalesData.accountDate
            if (this.isDiffDayTime(this.inputSalesData.visitTimeHour, this.inputSalesData.leaveTimeHour)) {
                leaveDay = dayjs(this.inputSalesData.accountDate).add(1, 'd').format('YYYY-MM-DD')
            }

            const visit_time = this.inputSalesData.accountDate + ' ' + this.modifyStrTime(this.inputSalesData.visitTimeHour, this.inputSalesData.visitTimeMinute)
            let leave_time = leaveDay + ' ' + this.modifyStrTime(this.inputSalesData.leaveTimeHour, this.inputSalesData.leaveTimeMinute)
            let move_time = this.calcMoveTime(leaveDay)

            if (this.showDiffBasicPlan) {
                let tmp_leave_time = leave_time
                leave_time = move_time
                move_time = tmp_leave_time
            }

            // サービス料金の追加
            let basicPlanList = this.createBasicPlan()
            for (const plan of basicPlanList) {
                sales_detail_service_list.push(plan)
            }


            if (this.showDiffBasicPlan) {
                let basicPlanOtherList = this.createBasicPlanOther()
                for (const planOther of basicPlanOtherList) {
                    sales_detail_service_list.push(planOther)
                }
            }
            let stayHourOther = (this.showDiffBasicPlan) ? this.inputSalesData.stayHourOther : 0
            let totalStayHour = (this.showDiffBasicPlan) ? this.inputSalesData.stayHour + this.inputSalesData.stayHourOther : this.inputSalesData.stayHour

            let isCharted = false
            if (this.showDiffBasicPlan) {
                if (this.inputSalesData.isCharteredOther.length > 0) {
                    isCharted = true
                }
            } else {
                if (this.inputSalesData.isChartered.length > 0) {
                    isCharted = true
                }
            }

            const data = {
                'customer_no': this.inputSalesData.customerNo,
                'account_date': this.inputSalesData.accountDate,
                'move_diff_seat': this.showDiffBasicPlan,
                'visit_time': visit_time,
                'leave_time': leave_time,
                'move_time': move_time,
                'payment_type': (this.inputSalesData.cardPayment) ? 1 : 0,
                'appoint': this.appointedCastDataList.length != 0,
                'douhan': douhanFlg,
                'total_visitors': this.inputSalesData.totalVisitors,
                'is_charterd': isCharted,
                'tax_rate': this.inputSalesData.totalSalesTax,
                // 後々↓
                'booking': false,
                'basic_plan_type': this.inputSalesData.basicPlanType,
                'stay_hour': this.inputSalesData.stayHour,
                'stay_hour_other': stayHourOther,
                'total_stay_hour': totalStayHour,
                'total_sales': this.totalPrice,
                'total_tax_sales': this.totalTaxPrice,
                'sales_detail_service_list': sales_detail_service_list,
                'sales_detail_appoint_list': sales_detail_appoint_list,
                'sales_detail_list': sales_detail_list,
                'remarks': this.inputSalesData.remarks,
            }

            console.log('register', data)

            //バリデーション・・・
            // サーバーの方はトランザクションだからおかしかったら登録されないが・・・

            this.$axios({
                method: 'POST',
                url: '/api/sales/create_sales_data/',
                data: data
            })
            .then(res => {
                console.log(res)
                this.addSalesList(res.data.data)
                if (res.data.bottle.length != 0) {
                    this.addBottleList(res.data.bottle)
                }
                this.init()
                this.close()
            })
            .catch(e => {
                console.log(e)
            })
        },
        createBasicPlan () {
            let result = []
            const basic_plan_type = this.inputSalesData.basicPlanType
            const large_category = 0
            const middle_category = this.inputSalesData.selectedBasicPlan
            const quantity = this.inputSalesData.selectedBasicPlanNum
            // 将来的には可変に
            const fixed_price = Con.BASIC_PLAN_PRICE_DICT[basic_plan_type][middle_category] * quantity
            const fixed_tax_price = this.calcAddTaxPrice(fixed_price, Con.TAX_DEFAULT)
            let data = {
                basic_plan_type: basic_plan_type,
                large_category: large_category,
                middle_category: middle_category,
                quantity: quantity,
                fixed_price: fixed_price,
                fixed_tax_price: fixed_tax_price,
                total_price: fixed_price,
                total_tax_price: fixed_tax_price,
            }
            result.push(data)

            if (this.isExtention) {
                const extentionFixedPrice = Con.BASIC_PLAN_EXTENTION[basic_plan_type] * this.inputSalesData.extentionNum
                const extentionFixedTaxPrice = this.calcAddTaxPrice(extentionFixedPrice, Con.TAX_DEFAULT)
                result.push({
                    basic_plan_type: basic_plan_type,
                    large_category: 3,
                    middle_category: 0,
                    quantity: this.inputSalesData.extentionNum,
                    fixed_price: extentionFixedPrice,
                    fixed_tax_price: extentionFixedTaxPrice,
                    total_price: extentionFixedPrice,
                    total_tax_price: extentionFixedTaxPrice,
                })
            }

            if (basic_plan_type == 1) {
                let VipSeatPrice = this.inputSalesData.vipSeatNum * this.vipSeatPrice
                let VipSeatTaxPrice = this.calcAddTaxPrice(VipSeatPrice, Con.TAX_DEFAULT)
                result.push({
                    basic_plan_type: basic_plan_type,
                    large_category: 4,
                    middle_category: 0,
                    quantity: this.inputSalesData.vipSeatNum,
                    fixed_price: VipSeatPrice,
                    fixed_tax_price: VipSeatTaxPrice,
                    total_price: VipSeatPrice,
                    total_tax_price: VipSeatTaxPrice,
                })
            }
            return result
        },
        createBasicPlanOther () {
            let result = []
            const basic_plan_type = this.inputSalesData.basicPlanTypeOther
            const large_category = 0
            const middle_category = this.inputSalesData.selectedBasicPlanOther
            const quantity = this.inputSalesData.selectedBasicPlanOtherNum
            // 将来的には可変に
            const fixed_price = Con.BASIC_PLAN_PRICE_DICT[basic_plan_type][middle_category] * quantity
            const fixed_tax_price = this.calcAddTaxPrice(fixed_price, Con.TAX_DEFAULT)
            let data = {
                basic_plan_type: basic_plan_type,
                large_category: large_category,
                middle_category: middle_category,
                quantity: quantity,
                fixed_price: fixed_price,
                fixed_tax_price: fixed_tax_price,
                total_price: fixed_price,
                total_tax_price: fixed_tax_price,
            }
            result.push(data)

            if (this.isExtentionOther) {
                const extentionFixedPrice = Con.BASIC_PLAN_EXTENTION[basic_plan_type] * this.inputSalesData.extentionOtherNum
                const extentionFixedTaxPrice = this.calcAddTaxPrice(extentionFixedPrice, Con.TAX_DEFAULT)
                result.push({
                    basic_plan_type: basic_plan_type,
                    large_category: 3,
                    middle_category: 0,
                    quantity: this.inputSalesData.extentionOtherNum,
                    fixed_price: extentionFixedPrice,
                    fixed_tax_price: extentionFixedTaxPrice,
                    total_price: extentionFixedPrice,
                    total_tax_price: extentionFixedTaxPrice,
                })
            }

            if (basic_plan_type == 1) {
                let VipSeatPrice = this.inputSalesData.vipSeatNumOther * this.vipSeatPriceOther
                let VipSeatTaxPrice = this.calcAddTaxPrice(VipSeatPrice, Con.TAX_DEFAULT)
                result.push({
                    basic_plan_type: basic_plan_type,
                    large_category: 4,
                    middle_category: 0,
                    quantity: this.inputSalesData.vipSeatNumOther,
                    fixed_price: VipSeatPrice,
                    fixed_tax_price: VipSeatTaxPrice,
                    total_price: VipSeatPrice,
                    total_tax_price: VipSeatTaxPrice,
                })
            }
            return result
        },
        update () {
            let sales_detail_service_list = []
            let sales_detail_appoint_list = []
            let sales_detail_list = []

            // この会計は同伴かをヘッダに持たせる
            let douhanFlg = false


            // キャスト指名情報の追加
            for (const i in this.appointedCastDataList) {
                let large_category = 1
                let middle_category = 0
                let appointType = this.appointedCastDataList[i].appointType
                let isDouhan = this.appointedCastDataList[i].isDouhan
                let cast_id = this.appointedCastDataList[i].cast.id
                let quantity = this.appointedCastDataList[i].quantity
                let appointPrice = this.appointedCastDataList[i].appointPrice

                if (isDouhan) {
                    // この会計は同伴かをヘッダに持たせる
                    douhanFlg = true
                    sales_detail_appoint_list.push(this.createDouhan(this.appointedCastDataList[i]))
                }

                if (!isDouhan) {
                    switch (appointType) {
                        case 0:
                        break
                        case 1:
                        middle_category = 1
                        break
                        case 2:
                        middle_category = 2
                        break
                        default:
                        break
                    }
                }


                let total = this.calcQuantityPrice(appointPrice, quantity)
                let taxTotal = this.calcAddTaxPrice(total, Con.TAX_DEFAULT)

                // 指名料を値引きなどする場合、こちらから動的に指定する必要あり。
                const appointData = {
                    basic_plan_type: this.inputSalesData.basicPlanType,
                    large_category: large_category,
                    middle_category: middle_category,
                    cast_id: cast_id,
                    quantity: quantity,
                    fixed_price: appointPrice,
                    fixed_tax_price: this.calcAddTaxPrice(appointPrice, Con.TAX_DEFAULT),
                    total_price: total,
                    total_tax_price: taxTotal,
                }

                sales_detail_appoint_list.push(appointData)

            }

            // 明細情報の追加
            for (const i in this.inputSalesDetailData) {
                const salesDetailItem = this.inputSalesDetailData[i]
                const actually_price = salesDetailItem.actuallyPrice
                const actually_tax_price = salesDetailItem.actuallyTaxPrice
                const product_id = salesDetailItem.product.id
                const quantity = salesDetailItem.quantity
                const bottle = salesDetailItem.bottle
                const totalPrice = salesDetailItem.totalPrice
                const totalTaxPrice = salesDetailItem.totalTaxPrice
                const taxRate = salesDetailItem.taxRate
                const remarks = salesDetailItem.remarks
                // 後に商品にキャストを紐づける用
                const cast_id = null

                const productData = {
                    product_id: product_id,
                    cast_id: cast_id,
                    quantity: quantity,
                    bottle: bottle,
                    fixed_price: actually_price,
                    fixed_tax_price: actually_tax_price,
                    total_price: totalPrice,
                    total_tax_price: totalTaxPrice,
                    remarks: remarks,
                    tax_rate: taxRate,
                }

                sales_detail_list.push(productData)
            }



            let diffDay = false
            let moveDiffDay = false
            let leaveDay = this.inputSalesData.accountDate
            if (this.isDiffDayTime(this.inputSalesData.visitTimeHour, this.inputSalesData.leaveTimeHour)) {
                leaveDay = dayjs(this.inputSalesData.accountDate).add(1, 'd').format('YYYY-MM-DD')
            }

            const visit_time = this.inputSalesData.accountDate + ' ' + this.modifyStrTime(this.inputSalesData.visitTimeHour, this.inputSalesData.visitTimeMinute)
            let leave_time = leaveDay + ' ' + this.modifyStrTime(this.inputSalesData.leaveTimeHour, this.inputSalesData.leaveTimeMinute)
            let move_time = this.calcMoveTime(leaveDay)

            if (this.showDiffBasicPlan) {
                let tmp_leave_time = leave_time
                leave_time = move_time
                move_time = tmp_leave_time
            }

            // サービス料金の追加
            let basicPlanList = this.createBasicPlan()
            for (const plan of basicPlanList) {
                sales_detail_service_list.push(plan)
            }


            if (this.showDiffBasicPlan) {
                let basicPlanOtherList = this.createBasicPlanOther()
                for (const planOther of basicPlanOtherList) {
                    sales_detail_service_list.push(planOther)
                }
            }
            let stayHourOther = (this.showDiffBasicPlan) ? this.inputSalesData.stayHourOther : 0
            let totalStayHour = (this.showDiffBasicPlan) ? this.inputSalesData.stayHour + this.inputSalesData.stayHourOther : this.inputSalesData.stayHour

            let isCharted = false
            if (this.showDiffBasicPlan) {
                if (this.inputSalesData.isCharteredOther.length > 0) {
                    isCharted = true
                }
            } else {
                if (this.inputSalesData.isChartered.length > 0) {
                    isCharted = true
                }
            }

            const data = {
                'id': this.salesHeaderId,
                'customer_no': this.inputSalesData.customerNo,
                'account_date': this.inputSalesData.accountDate,
                'move_diff_seat': this.showDiffBasicPlan,
                'visit_time': visit_time,
                'leave_time': leave_time,
                'move_time': move_time,
                'payment_type': (this.inputSalesData.cardPayment) ? 1 : 0,
                'appoint': this.appointedCastDataList.length != 0,
                'douhan': douhanFlg,
                'total_visitors': this.inputSalesData.totalVisitors,
                'is_charterd': isCharted,
                'tax_rate': this.inputSalesData.totalSalesTax,
                // 後々↓
                'booking': false,
                'basic_plan_type': this.inputSalesData.basicPlanType,
                'stay_hour': this.inputSalesData.stayHour,
                'stay_hour_other': stayHourOther,
                'total_stay_hour': totalStayHour,
                'total_sales': this.totalPrice,
                'total_tax_sales': this.totalTaxPrice,
                'sales_detail_service_list': sales_detail_service_list,
                'sales_detail_appoint_list': sales_detail_appoint_list,
                'sales_detail_list': sales_detail_list,
                'remarks': this.inputSalesData.remarks,

                'edit_sales_detail': this.edit_sales_detail,
                'edit_sales_service_detail': this.edit_sales_service_detail,
                'edit_sales_appoint_detail': this.edit_sales_appoint_detail,
            }

            console.log('update', data)

            //バリデーション・・・
            // サーバーの方はトランザクションだからおかしかったら登録されないが・・・

            this.$axios({
                method: 'PUT',
                url: '/api/sales/update_sales_data/',
                data: data
            })
            .then(res => {
                console.log(res)
                this.updateSalesList(res.data)
                this.$eventHub.$emit('updateSalesDetail', res.data)
                this.init()
                this.close()
            })
            .catch(e => {
                console.log(e)
            })
        },
        createDouhan (data) {
            // 将来的に可変
            return {
                basic_plan_type: this.inputSalesData.basicPlanType,
                large_category: 2,
                middle_category: 0,
                cast_id: data.cast.id,
                quantity: 1,
                fixed_price: 5000,
                fixed_tax_price: 6750,
                total_price: 5000,
                total_tax_price: 6750,
            }
        },
        calcMoveTime (leaveDay) {
            if (this.showDiffBasicPlan) {
                if (this.isDiffDayTime(this.inputSalesData.leaveTimeHour, this.inputSalesData.leaveTimeHourAfterMove)) {
                    let day = dayjs(this.inputSalesData.accountDate).add(1, 'd').format('YYYY-MM-DD')
                    return day + ' ' + this.modifyStrTime(this.inputSalesData.leaveTimeHourAfterMove, this.inputSalesData.leaveTimeMinuteAfterMove)
                } else {
                    return leaveDay + ' ' + this.modifyStrTime(this.inputSalesData.leaveTimeHourAfterMove, this.inputSalesData.leaveTimeMinuteAfterMove)
                }
            }
            return null
        },
        init () {
            this.inputSalesData = {
                basicPlanType: 0, // 選択されている料金タイプの種類
                customerNo: null,
                totalVisitors: 1,
                accountDate: now,
                visitTimeHour: null, // 来店時間（時）
                visitTimeMinute: null, // 来店時間（分）
                leaveTimeHour: null, // 退店時間（時）=> 席移動の場合は席移動時間（時）
                leaveTimeMinute: null, // 退店時間（分）=> 席移動の場合は席移動時間（分）
                selectedBasicPlan: 0, // SET料金のどれを選択しているか
                selectedBasicPlanNum: 0, // SET料金の数量 1 or 0。サービスも考慮
                stayHour: 0, // 滞在時間

                isChartered: [],
                isCharteredOther: [],

                // 延長はcomputedでextention_price
                extentionNum: 0, // 延長料金の数量 1 or 0。

                // VIP_SEATはbasicPlanType == 1の時
                vipSeatNum: 0, // VIPの席料金の数量 1 or 0。サービスも考慮

                basicPlanTypeOther: 1, // 選択されている料金タイプの種類（席移動先）basicPlanTypeと逆（computedで）
                leaveTimeHourAfterMove: null, // 席移動後の退店時間（時）
                leaveTimeMinuteAfterMove: null, // 席移動後の退店時間（分）
                stayHourOther: 0, // 滞在時間（席移動先）
                selectedBasicPlanOther: 0, // SET料金のどれを選択しているか（席移動後）
                selectedBasicPlanOtherNum: 1, // SET料金の数量 1 or 0。サービスも考慮（席移動後）
                extentionOtherNum: 0, // 延長料金の数量 1 or 0。
                vipSeatNumOther: 0, // VIPの席料金の数量 1 or 0。サービスも考慮

                totalSalesTax: Con.TAX_DEFAULT,
                cardPayment: false,
                isAppointed: 0,

                remarks: '',
            }
            this.showDiffBasicPlan = false
            this.inputSalesDetailData = []
            this.appointedCastDataList = []
            this.errorMsg = []
            this.customerNoError = ''
            this.totalVisitorsError = ''
            this.editMode = false
            this.salesHeaderId = null
            this.edit_sales_detail = []
            this.edit_sales_service_detail = []
            this.edit_sales_appoint_detail = []
        },
        test () {
            console.log('test')
        },
        open (data) {
            this.dialog = true
            if (data) {
                this.convertData(data)
                this.editMode = true
                this.salesHeaderId = data.id
                console.log('編集モード')
            } else {
                this.editMode = false
                console.log('新規作成モード')
            }
        },
        close () {
            this.dialog = false
        },
        showAddCastDialog () {
            this.$refs.inputSalesAddcastDialog.open()
        },
        showAddDetailDialog () {
            this.$refs.inputSalesAddDetailDialog.open()
        },
        addCast (data) {
            // console.log('addCast', data)
            // this.appointedCastDataList.push(data)
        },
        getAppointStr (type) {
            if (type === 0) return '指名'
            if (type === 1) return '本指名'
            if (type === 2) return '場内指名'
            return '-'
        },
        getDouhanStr (isDouhan) {
            if (isDouhan) return '有'
            return '無'
        },
        deleteCast (castData, idx) {
            this.appointedCastDataList.splice(idx, 1)
        },
        editSalesDetail (data) {
            console.log('editSalesDetail', data)
        },
        deleteSalesDetail (data) {
            this.inputSalesDetailData.splice(data.index, 1)
        },
        addSalesDetail (data) {
            this.inputSalesDetailData.push(data)
        },
        addSalesDetailList (data) {
            console.log('addSalesDetailList', data)
            this.inputSalesDetailData = this.inputSalesDetailData.concat(data)
        },
        getStayHourStr (stayHour) {
            const h = Math.floor(stayHour / 60)
            const m = stayHour % 60
            if (h == 0) return  m + '分'
            return h + '時間' + m + '分'
        },
        convertData (data) {
            // 編集用にデータを置き換える処理
            console.log('convertData', data)
            this.edit_sales_detail = data.sales_detail
            this.edit_sales_service_detail = data.sales_service_detail
            this.edit_sales_appoint_detail = data.sales_appoint_detail

            this.inputSalesData.basicPlanType = data.basic_plan_type
            this.inputSalesData.customerNo = String(data.customer.customer_no)
            this.inputSalesData.totalVisitors = String(data.total_visitors)
            this.inputSalesData.accountDate = data.account_date.replaceAll('/', '-')
            this.inputSalesData.stayHour = data.stay_hour
            this.inputSalesData.stayHourOther = data.stay_hour_other
            this.inputSalesData.remarks = data.remarks

            let visitTime = data.visit_time.split(' ')[1]
            let leaveTime = data.leave_time.split(' ')[1]

            let visitTimeHour = Number(visitTime.split(':')[0])
            let visitTimeMinute = Number(visitTime.split(':')[1])
            let leaveTimeHour = Number(leaveTime.split(':')[0])
            let leaveTimeMinute = Number(leaveTime.split(':')[1])

            this.inputSalesData.visitTimeHour = visitTimeHour
            this.inputSalesData.visitTimeMinute = visitTimeMinute

            let moveTime = leaveTime
            let moveTimeHour = null
            let moveTimeMinute = null

            if (data.move_diff_seat) {
                moveTime = data.move_time.split(' ')[1]
                moveTimeHour = Number(moveTime.split(':')[0])
                moveTimeMinute = Number( moveTime.split(':')[1])

                this.inputSalesData.leaveTimeHour = moveTimeHour
                this.inputSalesData.leaveTimeMinute = moveTimeMinute
                this.inputSalesData.leaveTimeHourAfterMove = leaveTimeHour
                this.inputSalesData.leaveTimeMinuteAfterMove = leaveTimeMinute

            } else {
                this.inputSalesData.leaveTimeHour = leaveTimeHour
                this.inputSalesData.leaveTimeMinute = leaveTimeMinute
            }

            if (data.basic_plan_type == 0 && data.move_diff_seat) {
                // 席移動で貸し切り
                this.inputSalesData.isCharteredOther = (data.is_charterd) ? [1] : []
            } else if (data.basic_plan_type == 1) {
                // 貸し切り
                this.inputSalesData.isChartered = (data.is_charterd) ? [1] : []
            }

            this.inputSalesData.totalSalesTax = data.tax_rate
            this.inputSalesData.cardPayment = (data.payment == 1) ? true : false
            this.inputSalesData.isAppointed = (data.appoint) ? 1 : 0
            this.showDiffBasicPlan = data.move_diff_seat

            let service_detail_list = []
            let service_appoint_list = []
            for (const i in data.sales_detail) {
                const salesDetailItem = data.sales_detail[i]
                service_detail_list.push({
                    actuallyPrice: salesDetailItem.fixed_price,
                    actuallyTaxPrice: salesDetailItem.fixed_tax_price,
                    bottle: false,
                    category: salesDetailItem.product.category,
                    name: salesDetailItem.product.name,
                    price: salesDetailItem.product.price,
                    product: salesDetailItem.product,
                    quantity: Number(salesDetailItem.quantity),
                    remarks: '',
                    taxRate: 35,
                    taxation: false,
                    thumbnail: null,
                    totalPrice: salesDetailItem.total_price,
                    totalTaxPrice: salesDetailItem.total_tax_price,
                })
            }


            let appoint_info_list = []
            // {id: id, Obj: obj}
            // まずはまとめる

            for (const i in data.sales_appoint_detail) {
                const salesAppointItem = data.sales_appoint_detail[i]
                const index = appoint_info_list.findIndex(el => el.id == salesAppointItem.cast.id)

                if (index != -1) {
                    appoint_info_list[index].data.push(salesAppointItem)
                } else {
                    appoint_info_list.push({
                        id: salesAppointItem.cast.id,
                        data: [salesAppointItem]
                    })
                }

            }

            for (const i in appoint_info_list) {
                const appointData = appoint_info_list[i]
                let cast = null
                let appointType = 0
                let appointPrice = 0
                let quantity = 0
                let isDouhan = false
                let douhanPrice = 0
                for (const j in appointData.data) {
                    const item = appointData.data[j]
                    if (item.service.large_category == 2 && item.service.middle_category == 0) {
                        isDouhan = true
                        douhanPrice = item.total_price
                    } else {
                        appointType = item.service.middle_category
                        appointPrice = item.fixed_price
                        cast = item.cast
                        quantity = item.quantity
                    }
                }

                service_appoint_list.push({
                    cast: cast,
                    appointType: appointType,
                    appointPrice: appointPrice,
                    isDouhan: isDouhan,
                    douhanPrice: douhanPrice,
                    quantity: Number(quantity),
                })
            }


            this.inputSalesDetailData = service_detail_list
            this.appointedCastDataList = service_appoint_list
        },
        showEditAddCastDialog (data, idx) {
            console.log('showEditAddCastDialog')
            this.$refs.inputSalesAddcastDialog.open(data, idx)
        },
        addCastData (data) {
            console.log('addCastData', data)
            this.appointedCastDataList.push(data)
        },
        updateCastData (data, idx) {
            console.log('updateCastData', data, idx)
            Vue.set(this.appointedCastDataList, idx, data)
        }
    },
    mixins: [
        utilsMixin,
        validateMixin
    ]
}

</script>

<style lang="scss" scoped>

    .input_sales_form {
        padding: 20px;

        .input_sales_visit {
            // border: 1px solid rgba(155, 155, 155, 0.5);
            // background: rgba(184, 184, 184, 0.1);
            border-radius: 5px;
            // padding: 0 !important;
        }

        .input_sales_leave {
            // display: flex;
            // justify-content: space-between;
            // border: 1px solid rgba(155, 155, 155, 0.5);
            // background: rgba(184, 184, 184, 0.1);
            // border-radius: 5px;
        }

        .input_sales_visit_time_wrap {
            // display: flex;
            .input_sales_visit_time {
                // flex-direction: column;
                // padding: 10px 20px;

                .input_sales_visit_time_title {
                    padding: 2px 0 4px 1px;
                }

                .input_sales_visit_time_select {
                    padding: 3px 20px 3px 7px;
                    font-size: 16px;
                    font-weight: 200;
                }
                // .select_container::after {
                //     border-left: 4px solid transparent;
                //     border-right: 4px solid transparent;
                //     border-top: 4.5px solid rgba(50, 50, 50, 1);
                //     content: "";
                //     position: relative;
                //     right: 12px;
                //     top: 13px;
                //     width: 0;
                // }
            }
        }



        .input_sales_stay_hour_wrap {
            .input_sales_stay_hour {
                padding: 4px 9px;
                border-radius: 3px;
                border: 1px solid rgba(125, 125, 125, 0.6);
            }
        }

        .appoint_cast_area_wrap {
            margin-top: 1rem;
            margin-left: 8px !important;
            margin-right: 8px !important;
            padding-left: 8px !important;
            padding-right: 8px !important;

            .appointed_cast_area {
                margin-top: 1rem;
                margin-bottom: 2rem;
                width: 100%;
                // th:nth-child(1), td:nth-child(1) {
                //     width: 8%;
                // }
                // th:nth-child(2), td:nth-child(2) {
                //     width: 25%;
                // }
                // th:nth-child(3), td:nth-child(3) {
                //     width: 20%;
                // }
                // th:nth-child(4), td:nth-child(4) {
                //     width: 15%;
                // }
                // th:nth-child(5), td:nth-child(5) {
                //     width: 20%;
                // }

                .cast_icon {
                    border: 1px solid rgba(200, 200, 200, 0.5);
                }

                .trash_icon {
                    cursor: pointer;
                }
            }
        }

    }
    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }


    .table > :not(caption) {
        border-bottom-width: 0;
    }

    .input_sales_footer_tax {
        height: 38px;
        padding: 4px 9px;
        border-radius: 3px;
        border: 1px solid rgba(125, 125, 125, 0.6);
    }

    .input_sales_basic_price_select {
        border-radius: 3px;
        border: 1px solid rgba(125, 125, 125, 0.6);
    }

    table {
        width: 100%;
        // table-layout: fixed;

        th {
            // font-weight: normal;
        }

        td {
            padding-left: 0.5rem;
        }

        .width60 {
            width: 60%;
        }

        .width50 {
            width: 50%;
        }

        .width40 {
            width: 40%;
        }

        .width30 {
            width: 30%;
        }

        .width20 {
            width: 20%;
        }


        .moveSeatCard {
            border: 2px solid #cbcbcb;
        }
    }

    .invalid {
        color: red;
    }

    .form_required:after{
        content: '*';
        color: red;
    }

    .cast_icon {
        border-radius: 50%;
        width: 60px;
        height: 60px;
    }

    .customer_detail_customer_icon {
        border-radius: 50%;
        width: 50px;
        height: 50px;
    }
</style>
