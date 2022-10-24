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
                        <b-card-sub-title align="right">
                            <span style="color: red;">*</span> : 必須項目
                        </b-card-sub-title>
                        <!-- <b-row>
                            <b-col cols="3">
                                <b-form-group>
                                    <label
                                        :class="{'invalid': customerNoInvalid}"
                                        class="form_required"
                                    >会員No</label>
                                    <span
                                        style="display: inline-block; margin-left: 0.4rem;"
                                    >
                                        <b-icon
                                            id="customer_no_info_icon"
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
                                            type="number"
                                            required
                                            :autofocus="autoFucus"
                                            placeholder="会員No(必須)"
                                            @blur="checkCustomerNo"
                                            :disabled="editMode"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNoError.length == 0">
                                            {{ customerNoError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row> -->
                        <b-row>
                            <b-col cols="12">
                                <b-card
                                    :class="{'disabled': editMode}"
                                    style="min-height: 150px;"
                                >
                                    <div style="display: flex;">
                                        <label>
                                            顧客情報1
                                        </label>
                                        <div style="margin-left: auto;" v-if="customerInfo != null && customerInfo.length > 0 && !editMode">
                                            <b-button
                                                size="sm"
                                                variant="outline-primary"
                                                @click="showEditCustomerDialog(customerInfo[0], 0)"
                                            >
                                                <b-icon
                                                    icon="pencil"
                                                    aria-hidden="true"
                                                    variant="success"
                                                    class="edit_icon"
                                                ></b-icon>
                                            </b-button>
                                            <b-button
                                                size="sm"
                                                style="position: relative; left: 10px;"
                                                variant="outline-danger"
                                                @click="deleteCustomerInfo(0)"
                                            >
                                                <b-icon
                                                    icon="trash"
                                                    aria-hidden="true"
                                                    variant="danger"
                                                    class="trash_icon"
                                                ></b-icon>
                                            </b-button>
                                        </div>
                                    </div>
                                    <b-container>
                                        <b-row>
                                            <b-col cols="6" class="mt-0 pt-0">
                                                <div style="display: flex;">
                                                    <div>
                                                        <img
                                                            src="@/assets/img/男性3.jpg"
                                                            class="customer_detail_customer_icon"
                                                        >
                                                    </div>

                                                    <div class="mt-0" style="margin-left: 30px;">
                                                        <b-card-sub-title>
                                                            会員No
                                                        </b-card-sub-title>
                                                        <b-card-text v-if="customerInfo != null && customerInfo.length > 0" style="font-size: 15px;">
                                                            {{ customerInfo[0].customer_no}}
                                                        </b-card-text>
                                                        <b-card-text v-else style="font-size: 15px;">
                                                            -
                                                        </b-card-text>
                                                    </div>

                                                    <div class="mt-0" style="margin-left: 30px;">
                                                        <b-card-sub-title>
                                                            名前
                                                        </b-card-sub-title>
                                                        <b-card-text v-if="customerInfo != null && customerInfo.length > 0" style="font-size: 15px;">
                                                            {{ customerInfo[0].name | truncate(20) }}
                                                        </b-card-text>
                                                        <b-card-text v-else style="font-size: 15px;">
                                                            -
                                                        </b-card-text>
                                                    </div>
                                                </div>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    年齢
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null && customerInfo.length > 0">
                                                    {{ getStrInData(customerInfo[0].age) }} 歳
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    誕生日
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null && customerInfo.length > 0">
                                                    {{ getStrInData(customerInfo[0].birthday) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                            <b-col cols="2" class="mt-0 pt-0">
                                                <b-card-sub-title>
                                                    ランク
                                                </b-card-sub-title>
                                                <b-card-text v-if="customerInfo != null && customerInfo.length > 0">
                                                    {{ getStrInData(customerInfo[0].rank_name) }}
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    -
                                                </b-card-text>
                                            </b-col>
                                        </b-row>
                                    </b-container>
                                </b-card>
                                <b-row v-if="customerInfo != null && customerInfo.length > 1">
                                    <b-col
                                        cols="4"
                                        v-for="(item, i) in customerInfo.slice(1)"
                                        :key="i"
                                        class="pa-0"
                                    >
                                        <b-card
                                            :class="{'disabled': editMode}"
                                        >
                                            <div style="display: flex;">
                                                <label>
                                                    顧客情報{{ i + 2 }}
                                                </label>
                                                <div style="margin-left: auto;" v-if="!editMode">
                                                    <b-button
                                                        size="sm"
                                                        variant="outline-primary"
                                                        @click="showEditCustomerDialog(item, i+1)"
                                                    >
                                                        <b-icon
                                                            icon="pencil"
                                                            aria-hidden="true"
                                                            variant="success"
                                                            class="edit_icon"
                                                        ></b-icon>
                                                    </b-button>
                                                    <b-button
                                                        size="sm"
                                                        style="position: relative; left: 10px;"
                                                        variant="outline-danger"
                                                        @click="deleteCustomerInfo(i+1)"
                                                    >
                                                        <b-icon
                                                            icon="trash"
                                                            aria-hidden="true"
                                                            variant="danger"
                                                            class="trash_icon"
                                                        ></b-icon>
                                                    </b-button>
                                                </div>
                                            </div>
                                            <b-container>
                                                <b-row>
                                                    <b-col cols="4">
                                                        <div>
                                                            <img
                                                                src="@/assets/img/男性3.jpg"
                                                                class="customer_detail_customer_icon"
                                                            >
                                                        </div>
                                                        <b-card-sub-title style="font-size: 12px; margin-top: 10px;">
                                                            会員No
                                                        </b-card-sub-title>
                                                        <b-card-text style="font-size: 13px;">
                                                            {{ item.customer_no }}
                                                        </b-card-text>
                                                    </b-col>
                                                    <b-col cols="8">
                                                        <div style="margin-left: 15px;">
                                                            <b-card-sub-title>
                                                                名前
                                                            </b-card-sub-title>
                                                            <b-card-text style="font-size: 15px;">
                                                                {{ item.name }}
                                                            </b-card-text>
                                                            <b-card-sub-title>
                                                                ランク
                                                            </b-card-sub-title>
                                                            <b-card-text style="font-size: 15px;">
                                                                {{ getStrInData(item.rank_name) }}
                                                            </b-card-text>
                                                        </div>
                                                    </b-col>
                                                </b-row>
                                            </b-container>

                                        </b-card>
                                    </b-col>
                                </b-row>

                                <div class="mt-3" v-if="!editMode">
                                    <b-button
                                        size="sm"
                                        @click="showAddCustomerDialog"
                                        class="mb-3"
                                        variant="primary"
                                    >
                                        <b-icon
                                            icon="plus-circle"
                                            aria-hidden="true"
                                        ></b-icon> 会員を追加...
                                    </b-button>
                                </div>

                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-card style="min-height: 540px;">
                                    <label>
                                        基本情報
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
                                        title="必須項目を入力すると自動的に滞在時間などが設定されます。"
                                    ></b-tooltip>
                                    <b-container>
                                        <b-row>
                                            <b-col cols="6">
                                                <b-card-sub-title
                                                    class="form_required"
                                                >料金プラン</b-card-sub-title>
                                                <b-form-group style="min-height: 40px;">
                                                    <SelectForm
                                                        :optionType=12
                                                        :fullSize=true
                                                        v-model="inputSalesData.basicPlanType"
                                                    />
                                                </b-form-group>
                                            </b-col>
                                            <b-col cols="6">
                                                <b-card-sub-title>座席</b-card-sub-title>
                                                <b-form-group style="min-height: 40px;">
                                                    <SelectForm
                                                        :dispOptions="seatOptions"
                                                        :disabled=false
                                                        :firstValue=0
                                                        initVal="指定無し"
                                                        v-model="inputSalesData.seatId"
                                                    />
                                                </b-form-group>
                                            </b-col>
                                            <b-col cols="6">
                                                <b-form-group style="display: inline; margin-right: 20px;">
                                                    <b-card-sub-title
                                                        class="form_required"
                                                    >来店時間</b-card-sub-title>
                                                    <b-form-input
                                                        v-model="inputSalesData.visitTime1"
                                                        type="date"
                                                    ></b-form-input>
                                                    <b-form-input
                                                        v-model="inputSalesData.visitTime2"
                                                        type="time"
                                                    ></b-form-input>
                                                    <!-- <b-form-timepicker
                                                        v-model="inputSalesData.visitTime2"
                                                        now-button
                                                        reset-button
                                                        locale="en"
                                                    ></b-form-timepicker> -->
                                                </b-form-group>
                                                <b-form-group style="display: inline;">
                                                    <b-card-sub-title
                                                        class="form_required"
                                                    >退店時間</b-card-sub-title>
                                                    <b-form-input
                                                        v-model="inputSalesData.leaveTime1"
                                                        type="date"
                                                    ></b-form-input>
                                                    <b-form-input
                                                        v-model="inputSalesData.leaveTime2"
                                                        type="time"
                                                    ></b-form-input>
                                                    <!-- <b-form-timepicker
                                                        v-model="inputSalesData.leaveTime2"
                                                        now-button
                                                        reset-button
                                                        locale="en"
                                                    ></b-form-timepicker> -->
                                                </b-form-group>
                                                <b-form-invalid-feedback :state="visitLeaveTimeError.length == 0">
                                                    {{ visitLeaveTimeError }}
                                                </b-form-invalid-feedback>

                                                <AutoInputLeaveTime
                                                    :inputSalesData="inputSalesData"
                                                    :visitTime="inputSalesData.visitTime"
                                                    @update="updateInputSalesData"
                                                    class="mt-3"
                                                />
                                            </b-col>
                                            <b-col cols="6">
                                                <b-card-sub-title
                                                    class="form_required"
                                                    style="display: inline-block;"
                                                >
                                                    来店客数
                                                </b-card-sub-title>
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
                                                    title="1人以上になるように、来店客数を設定してください。"
                                                ></b-tooltip>
                                                <b-card-text>
                                                    {{ totalVisitors }}人
                                                </b-card-text>
                                                <b-form-group style="display: inline; margin-right: 20px;">
                                                    <b-card-sub-title>男性客数</b-card-sub-title>
                                                    <b-form-spinbutton
                                                        v-model="inputSalesData.maleVisitors"
                                                        min="0"
                                                        inline
                                                    ></b-form-spinbutton>
                                                </b-form-group>
                                                <b-form-group style="display: inline;">
                                                    <b-card-sub-title>女性客数</b-card-sub-title>
                                                    <b-form-spinbutton
                                                        v-model="inputSalesData.femaleVisitors"
                                                        min="0"
                                                        inline
                                                    ></b-form-spinbutton>
                                                </b-form-group>
                                                <b-form-invalid-feedback :state="totalVisitorsError.length == 0">
                                                    {{ totalVisitorsError }}
                                                </b-form-invalid-feedback>
                                            </b-col>
                                            <b-col cols="2">
                                                <b-card-sub-title>
                                                    滞在時間
                                                </b-card-sub-title>
                                                <b-card-text>
                                                    {{ stayHour }}
                                                </b-card-text>
                                                <!-- <b-progress :max="maxHour" height="2rem">
                                                    <b-progress-bar :value=inputSalesData.stayHour variant="success">
                                                        <span><strong>{{ getStayHourStr(inputSalesData.stayHour) }}</strong></span>
                                                    </b-progress-bar>
                                                </b-progress> -->
                                            </b-col>
                                            <b-col cols="2">
                                                <b-card-sub-title>
                                                    同伴
                                                </b-card-sub-title>
                                                <b-card-text v-if="isDouhan">
                                                    有
                                                </b-card-text>
                                                <b-card-text v-else>
                                                    無
                                                </b-card-text>
                                            </b-col>
                                            <!-- <b-col cols="12" class="pt-0">
                                                <b-form-invalid-feedback :state="visitTimeError.length == 0">
                                                    {{ visitTimeError }}
                                                </b-form-invalid-feedback>
                                            </b-col> -->
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
                                                    <td class="width20">
                                                        一般料金
                                                    </td>
                                                    <td class="width20">
                                                        <b-input-group>
                                                            <b-form-input
                                                                v-model="inputSalesData.basicPlanPrice1"
                                                                type="number"
                                                                required
                                                            ></b-form-input>
                                                        </b-input-group>
                                                    </td>
                                                    <td class="width5"/>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.basicPlanNum1"
                                                            inline
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="width20">
                                                        割引料金
                                                    </td>
                                                    <td class="width20">
                                                        <b-input-group>
                                                            <b-form-input
                                                                v-model="inputSalesData.basicPlanPrice2"
                                                                type="number"
                                                                required
                                                            ></b-form-input>
                                                        </b-input-group>
                                                    </td>
                                                    <td class="width5"/>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.basicPlanNum2"
                                                            inline
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
                                                    <td class="width20">
                                                        一般料金
                                                    </td>
                                                    <td class="width20">
                                                        <b-input-group>
                                                            <b-form-input
                                                                v-model="inputSalesData.basicPlanExtentionPrice1"
                                                                type="number"
                                                                required
                                                            ></b-form-input>
                                                        </b-input-group>
                                                    </td>
                                                    <td class="width5"/>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.basicPlanExtentionNum1"
                                                            inline
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="width20">
                                                        割引料金
                                                    </td>
                                                    <td class="width20">
                                                        <b-input-group>
                                                            <b-form-input
                                                                v-model="inputSalesData.basicPlanExtentionPrice2"
                                                                type="number"
                                                                required
                                                            ></b-form-input>
                                                        </b-input-group>
                                                    </td>
                                                    <td class="width5"/>
                                                    <td class="width30">
                                                        <b-form-spinbutton
                                                            v-model="inputSalesData.basicPlanExtentionNum2"
                                                            inline
                                                            min=0
                                                            size="sm"
                                                        ></b-form-spinbutton>
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
                        <label>明細</label>
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
                                    class="mb-3"
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
                    <table v-if="inputSalesDetailData.length > 0">
                        <tr>
                            <th>商品名</th>
                            <th>定価</th>
                            <th>実価格</th>
                            <th>数量</th>
                            <th>課税</th>
                            <th>ボトル登録</th>
                            <th>ボトル登録会員</th>
                            <th></th>
                        </tr>
                        <tr
                            v-for="(item, id) in inputSalesDetailData"
                            :key=id
                        >
                            <td>
                                <span>{{ item.name | truncate(20) }}</span>
                            </td>
                            <td>
                                {{ item.price | priceLocaleString }}
                            </td>

                            <td>
                                <b-form-input
                                    v-model="item.actuallyPrice"
                                    type="number"
                                    required
                                ></b-form-input>
                            </td>
                            <td>
                                <b-form-spinbutton
                                    v-model="item.quantity"
                                    inline
                                    min=1
                                    size="sm"
                                ></b-form-spinbutton>
                            </td>
                            <td>
                                <v-checkbox
                                    class="mt-3"
                                    v-model="item.taxation"
                                ></v-checkbox>
                            </td>
                            <td>
                                <div v-if="!isBottleCustomerDisabledRow(item)">
                                    <b-button
                                        v-if="item.customer == null"
                                        variant="primary"
                                        @click="addBottleCustomerInfo(2, id)"
                                        :disabled="customerInfo == null || customerInfo.length == 0"
                                    >
                                        顧客選択
                                    </b-button>
                                    <b-button
                                        v-else
                                        variant="danger"
                                        @click="deleteCustomerSelectedProductList(id)"
                                    >
                                        選択解除
                                    </b-button>
                                </div>
                                <div v-else>-</div>
                            </td>
                            <td>
                                <div v-if="item.customer != null">{{ item.customer.name }}</div>
                                <div v-else>-</div>
                            </td>
                            <td>
                                <b-icon
                                    icon="dash-square"
                                    font-scale="1.5"
                                    variant="danger"
                                    class="mt-0 input_sales_delete_product_btn"
                                    @click="deleteSalesDetail(id)"
                                ></b-icon>
                            </td>
                        </tr>
                    </table>
                </b-card>
                <b-card bg-variant="light" class="mt-3">
                    <label>総計</label>

                    <b-row>
                        <b-col cols="2">
                            <small style="display: block;" class="text-muted">サービス税</small>
                            <SelectForm
                                :dispOptions="basicPlanServiceTaxList"
                                v-model="inputSalesData.basicPlanServiceTax"
                            />
                        </b-col>
                        <b-col cols="2">
                            <small style="display: block;" class="text-muted">消費税</small>
                            <SelectForm
                                :dispOptions="basicPlanServiceTaxList"
                                v-model="inputSalesData.basicPlanTax"
                            />
                        </b-col>
                        <b-col cols="2">
                            <small style="display: block;" class="text-muted">カード支払</small>
                            <SelectForm
                                :dispOptions="basicPlanServiceTaxList"
                                :formDisabled="inputFixedPrice"
                                v-model="inputSalesData.basicPlanCardTax"
                            />
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col cols="2">
                            <small class="text-muted">注文数</small>
                            <b-card-text>{{ totalSalesDetailNum | priceLocaleString }}点</b-card-text>
                        </b-col>
                        <b-col cols="2">
                            <small class="text-muted">注文料金(税抜)</small>
                            <b-card-text>{{ totalDetailPrice | priceLocaleString }}円</b-card-text>
                        </b-col>
                        <b-col cols="2">
                            <small class="text-muted">サービス料金(税抜)</small>
                            <b-card-text>{{ totalServicePrice | priceLocaleString }}円</b-card-text>
                        </b-col>
                        <b-col cols="2">
                            <small class="text-muted">カード支払い</small>
                            <b-card-text>
                                <v-checkbox
                                    class="mt-0"
                                    v-model="inputSalesData.cardPayment"
                                    :disabled=inputFixedPrice
                                ></v-checkbox>
                            </b-card-text>
                        </b-col>
                        <b-col cols="2">
                            <small class="text-muted">総計(税抜)</small>
                            <b-card-text>{{ totalPrice | priceLocaleString }}円</b-card-text>
                        </b-col>
                        <b-col cols="2">
                            <small class="text-muted">総計(税込)</small>
                            <b-card-text>{{ totalTaxPrice | priceLocaleString }}円</b-card-text>
                        </b-col>
                    </b-row>

                </b-card>
                <b-card bg-variant="light" class="mt-3">
                    <b-form-group
                        class="mb-0"
                    >
                        <label>ボトル</label>
                        <span
                            style="display: inline-block; margin-left: 0.4rem;"
                        >
                            <b-icon
                                id="bottle_info_icon"
                                icon="info-circle"
                                variant="primary"
                            ></b-icon>
                        </span>
                        <b-tooltip
                            target="bottle_info_icon"
                            title="消込を行うボトルを選択してください。"
                        ></b-tooltip>

                        <b-card-text v-if="customerInfo == null || customerInfo.length == 0">
                            会員情報を入力してください。
                        </b-card-text>
                        <b-card-text v-else-if="bottleInfo.length == 0">
                            ボトル情報がありません。
                        </b-card-text>
                        <b-row v-else>
                            <b-col
                                v-for="(item, i) in bottleInfo"
                                :key="i"
                                cols="4"
                            >
                                <b-card>
                                    <div style="dispaly: flex; justify-content: space-between;">
                                        <div>
                                            <small class="text-muted">
                                                No.{{ i+1 }}
                                            </small>
                                        </div>

                                        <div class="bottle_card_customer_no_area">
                                            <small class="text-muted">会員No</small>
                                            <b-card-text>{{ item.customer.customer_no }}</b-card-text>
                                        </div>
                                    </div>

                                    <div class="bottle_card_customer_name_area">
                                        <small class="text-muted">会員名</small>
                                        <b-card-text>{{ item.customer.name | truncate(15) }}</b-card-text>
                                    </div>

                                    <div class="bottle_card_product_name_area">
                                        <small class="text-muted">商品名</small>
                                        <b-card-text>{{ item.product.name }}</b-card-text>
                                    </div>

                                    <div style="display: flex; justify-content: space-between;">
                                        <div>
                                            <small class="text-muted">開封日</small>
                                            <b-card-sub-title>{{ item.open_date }}</b-card-sub-title>
                                        </div>

                                        <b-form-checkbox
                                            class="mt-3"
                                            v-model="item.bottleDelete"
                                            @change="updateBottleDelete(item)"
                                        >
                                            消込
                                        </b-form-checkbox>
                                    </div>
                                </b-card>
                            </b-col>
                        </b-row>
                    </b-form-group>
                </b-card>
                <b-card bg-variant="light" class="mt-3">
                    <!-- label-cols-lg="3"
                    label="備考"
                    label-size="lg"
                    label-class="font-weight-bold pt-0" -->
                    <b-form-group
                        class="mb-0"
                    >
                        <label>備考</label>
                        <b-form-textarea
                            rows="2"
                            no-resize
                            v-model="inputSalesData.remarks"
                        ></b-form-textarea>
                    </b-form-group>
                </b-card>

                <b-button
                    style="margin-top: 25px;"
                    @click="initForm"
                    variant="outline-secondary"
                >フォーム初期化</b-button>
            </b-form>
            <template #modal-footer>
                <b-container fluid v-if="inputFixedPrice">
                    <b-card bg-variant="light">
                        <label>実支払価格</label>
                        <span
                            style="display: inline-block; margin-left: 0.4rem;"
                        >
                            <b-icon
                                id="fixed_payment_info_icon"
                                icon="info-circle"
                                variant="primary"
                            ></b-icon>
                        </span>
                        <b-tooltip
                            target="fixed_payment_info_icon"
                            title="実際に支払った価格を入力してください。"
                        ></b-tooltip>
                        <b-row>
                            <b-col cols="2">
                                会員No
                            </b-col>
                            <b-col cols="3">
                                名前
                            </b-col>
                            <b-col cols="3">
                                支払額
                            </b-col>
                            <b-col cols="2">
                                カード支払い
                            </b-col>
                            <b-col cols="2">
                                カード手数料
                            </b-col>
                        </b-row>
                        <!-- <b-row>
                            <b-col cols="2">
                                No. {{ customerInfo.customer_no }}
                            </b-col>
                            <b-col cols="3">
                                {{ customerInfo.name }}
                            </b-col>
                            <b-col cols="3">
                                <b-form-input
                                    type="number"
                                    required
                                ></b-form-input>
                            </b-col>
                            <b-col cols="2">
                                <v-checkbox
                                    class="mt-0"
                                ></v-checkbox>
                            </b-col>
                            <b-col cols="2">
                                <SelectForm
                                    :dispOptions="basicPlanServiceTaxList"
                                    v-model="inputSalesData.basicPlanCardTax"
                                />
                            </b-col>
                        </b-row> -->
                        <b-row
                            v-for="(item, i) in customerInfo"
                            :key="i"
                        >
                            <b-col cols="2">
                                No. {{ item.customer_no }}
                            </b-col>
                            <b-col cols="3">
                                {{ item.name }}
                            </b-col>
                            <b-col cols="3">
                                <b-form-input
                                    type="number"
                                    required
                                    v-model="item.amountPaid"
                                    @change="calcTotalAmountPaid"
                                    min="0"
                                ></b-form-input>
                            </b-col>
                            <b-col cols="2">
                                <v-checkbox
                                    class="mt-0"
                                    v-model="item.cardPayment"
                                    @change="changeCardPayment(item.cardPayment, i)"
                                ></v-checkbox>
                            </b-col>
                            <b-col cols="2">
                                <SelectForm
                                    :dispOptions="basicPlanServiceTaxList"
                                    v-model="item.basicPlanCardTax"
                                />
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="7">
                            </b-col>
                            <b-col cols="2" align="right">
                                実支払総額
                            </b-col>
                            <b-col align="right">
                                <b-card-title style="color: red;">
                                    <b-icon icon="currency-yen"></b-icon> {{ totalAmountPaid | priceLocaleString }}
                                </b-card-title>
                            </b-col>
                        </b-row>
                    </b-card>
                </b-container>
                <b-container fluid>
                    <b-row>
                        <b-col cols="3">
                            <b-card-sub-title>
                                総計(税抜)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                <b-icon icon="currency-yen"></b-icon> {{ totalPrice | priceLocaleString }}
                            </b-card-title>
                        </b-col>
                        <b-col cols="3">
                            <b-card-sub-title>
                                総計(税込)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                <b-icon icon="currency-yen"></b-icon> {{ totalTaxPrice | priceLocaleString }}
                            </b-card-title>
                        </b-col>

                        <b-col cols="2">
                            <b-card-sub-title>
                                実価格を入力
                            </b-card-sub-title>

                            <b-card-text>
                                <v-checkbox
                                    class="mt-0"
                                    v-model="inputFixedPrice"
                                    :disabled="customerInfo == null || customerInfo.length == 0"
                                ></v-checkbox>
                            </b-card-text>
                        </b-col>

                        <b-col
                            cols="1"
                        >
                            <b-card-sub-title>
                                注文数
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                {{ totalSalesDetailNum | priceLocaleString }}点
                            </b-card-title>
                        </b-col>

                        <b-col
                            cols="1"
                        >
                            <b-card-sub-title>
                                支払方法
                            </b-card-sub-title>
                            <b-card-title style="font-size: 15px;" class="mb-0" v-if="inputSalesData.cardPayment">
                                カード
                            </b-card-title>
                            <b-card-title class="mb-0" v-else>
                                現金
                            </b-card-title>
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
                                :disabled=isDisabled
                                @click="registerOrUpdate"
                            >
                                {{ registerOrUpdateStr }}
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>

        <InputSalesAddDetailDialog
            ref="inputSalesAddDetailDialog"
            :customerList="customerInfo"
            @addSalesDetail="addSalesDetail"
            @addSalesDetailList="addSalesDetailList"
        />

        <InputSalesAddCustomerDialog
            ref="inputSalesAddCustomerDialog"
            :customerList="customerInfo"
            @addCustomer="addCustomer"
            @updateCustomer="updateCustomer"
        />

        <InputSalesSelectCustomerDialog
            ref="inputSalesSelectCustomerDialog"
            :customerList="customerInfo"
            @selectCustomer="selectCustomer"
            msg="会計をした会員を選択してください。"
            title="支払会員選択"
        />

        <InputSalesSelectCustomerDialog
            ref="inputSalesBottleSelectCustomerDialog"
            :customerList="customerInfo"
            @selectBottleCustomerProductList="selectBottleCustomerProductList"
            msg="ボトル登録を行う会員を選択してください。"
            title="ボトル登録会員選択"
        />

        <ErrorModal
            ref="errorModal"
            :errorMsg="errorMsg"
        />

        <b-modal
            v-model="registerSuccessDialog"
            hide-header
        >
            <div>
                売上データの作成に成功しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="initClose"
                        >
                            OK
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="registerFailureDialog"
            hide-header
        >
            <div>
                売上データの作成に失敗しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="registerFailure"
                        >
                            閉じる
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="updateSuccessDialog"
            hide-header
        >
            <div>
                売上データの更新に成功しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="initClose"
                        >
                            OK
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
        <b-modal
            v-model="updateFailureDialog"
            hide-header
        >
            <div>
                売上データの更新に失敗しました。
            </div>
            <template #modal-footer>
                <b-row>
                    <b-col
                        align="right"
                        style="padding: 0;"
                    >
                        <b-button
                            variant="primary"
                            @click="updateFailure"
                        >
                            閉じる
                        </b-button>
                    </b-col>
                </b-row>
            </template>
        </b-modal>
    </div>
</template>

<script>

import Vue from 'vue'
import _ from 'lodash'
import InputSalesDetailDialog from '@/components/common/dialog/InputSalesDetailDialog'
import InputSalesAddDetailDialog from '@/components/common/dialog/InputSalesAddDetailDialog'
import InputSalesAddCustomerDialog from '@/components/common/dialog/InputSalesAddCustomerDialog'
import InputSalesSelectCustomerDialog from '@/components/common/dialog/InputSalesSelectCustomerDialog'
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
import customerMixin from '@/mixins/customer'
import utilsMixin from '@/mixins/utils'
import validateMixin from '@/mixins/validate'

import AutoInputLeaveTime from '@/components/common/dialog/parts/inputSalesDialog/AutoInputLeaveTime'

export default {
    name: 'InputSalesDialogItem',
    props: {
    },
    components: {
        InputSalesDetailDialog,
        InputSalesAddDetailDialog,
        InputSalesAddCustomerDialog,
        InputSalesSelectCustomerDialog,
        SelectForm,
        CheckboxForm,
        ErrorModal,
        AutoInputLeaveTime,
    },
    data: () => ({
        dialog: false,
        inputSalesData: {
            // 選択されている料金タイプの種類
            // 通常(1, 2, 3) 貸切(4, 5, 6)
            basicPlanType: 1,

            // customerNo: null,
            maleVisitors: 0,
            femaleVisitors: 0,

            // 日
            visitTime1: now,
            leaveTime1: now,
            // 時刻
            visitTime2: '',
            leaveTime2: '',

            visitTime: null,
            leaveTime: null,
            seatId: 0,
            stayHour: 0,

            basicPlanPrice1: 0,
            basicPlanNum1: 0,
            basicPlanPrice2: 0,
            basicPlanNum2: 0,
            basicPlanExtentionPrice1: 0,
            basicPlanExtentionNum1: 0,
            basicPlanExtentionPrice2: 0,
            basicPlanExtentionNum2: 0,

            basicPlanServiceTax: 10,
            basicPlanTax: 10,
            basicPlanCardTax: 0,

            totalSalesTax: Con.TAX_DEFAULT,
            cardPayment: false,
            remarks: '',
        },

        inputSalesDetailData: [],

        inputSalesDetailDialog: false,

        inputFixedPrice: false,

        totalAmountPaid: 0,

        bottleInfo: [],


        taxOptions: Con.OPTIONS_TAX,
        numOptions: Con.OPTIONS_NUM,
        hourOptions: Con.OPTIONS_HOUR,
        hourAllOptions: Con.OPTIONS_HOUR_ALL,
        minuteOptions: Con.OPTIONS_MINUTE,

        maxHour: 300, // 滞在時間のMAXとなる
        apiPath: Con.API_PATH, // APIのURL
        defaultIcon: Con.DEFAULT_ALCOHOL_ICON, // デフォで酒の画像出しているが・・・
        basicPriceMenu: [
            { text: '料金種別', class: 'width20' },
            { text: '金額', class: 'width20' },
            { text: '', class: 'width5' },
            { text: '数量', class: 'width30' },
        ],
        extentionPriceMenu: [
            { text: '延長料金', class: 'width20' },
            { text: '金額', class: 'width20' },
            { text: '', class: 'width5' },
            { text: '数量', class: 'width30' }
        ],
        basicPlanOptions: [
            { text: '通常', value: 0 },
            { text: '貸切', value: 1 },
        ],
        basicPlanServiceTaxList: [
            { text: '10%', value: 10 },
            { text: '0%', value: 0 },
        ],
        errorMsg: [],
        // customerNoError: '',
        totalVisitorsError: '',
        visitTimeError: '',
        leaveTimeError: '',
        visitLeaveTimeError: '',
        editMode: false,
        salesHeaderId: null,
        edit_sales_detail: [],
        edit_sales_service_detail: [],
        customerInfo: [],

        // seatOptions: [],

        totalPrice: 0,
        totalDetailPrice: 0,
        totalServicePrice: 0,
        bottleDeleteList: [],
        registerSuccessDialog: false,
        registerFailureDialog: false,

        updateSuccessDialog: false,
        updateFailureDialog: false,

        autoFucus: false,

        waitServerResponse: false,
    }),
    created () {
        // this.$eventHub.$off('addSalesDetail')
        // this.$eventHub.$on('addSalesDetail', this.addSalesDetail)
        // this.$eventHub.$off('addSalesDetailList')
        // this.$eventHub.$on('addSalesDetailList', this.addSalesDetailList)

        // let arr = []
        // for (const item of this.seat) {
        //     arr.push({
        //         value: item.id,
        //         text: item.seat_name,
        //     })
        // }
        // this.seatOptions = arr
    },
    computed: {
        ...mapGetters([
            'customer',
            'bottle',
            'seat',
            'service',
        ]),
        seatOptions () {
            if (this.seat == undefined || this.seat == null) {
                return []
            }
            let arr = []
            for (const item of this.seat) {
                arr.push({
                    value: item.id,
                    text: item.seat_name,
                })
            }
            return arr
        },
        inputSalesDialogTitle () {
            if (this.editMode) {
                return '売上入力（編集） 伝票No.' + this.salesHeaderId
            } else {
                return '売上入力（新規作成）'
            }
        },
        totalTaxPrice () {
            // 総計(税抜)
            let totalPrice = 0
            // 総計(税込)
            let totalTaxPrice = 0

            // 明細の総計
            let totalDetailPrice = 0
            // サービス料金総計
            let totalServicePrice = 0

            // 課税の明細総計
            let totalTaxDetailPrice = 0
            // 非課税の明細総計
            let totalTaxFreeDetailPrice = 0

            // console.log('this.inputSalesDetailData', this.inputSalesDetailData)

            // 明細の計算
            for (const item of this.inputSalesDetailData) {
                if (item.taxation) {
                    // console.log('課税対象')
                    // 課税
                    totalTaxDetailPrice += item.actuallyPrice * item.quantity
                } else {
                    // console.log('非課税')
                    // 非課税
                    totalTaxFreeDetailPrice += item.actuallyPrice * item.quantity
                }
            }
            // 明細の合計(税抜)
            totalDetailPrice = (totalTaxDetailPrice + totalTaxFreeDetailPrice)

            // サービス料金の計算
            const normal1 = this.inputSalesData.basicPlanPrice1 * this.inputSalesData.basicPlanNum1
            const normal2 = this.inputSalesData.basicPlanPrice2 * this.inputSalesData.basicPlanNum2
            const extention1 = this.inputSalesData.basicPlanExtentionPrice1 * this.inputSalesData.basicPlanExtentionNum1
            const extention2 = this.inputSalesData.basicPlanExtentionPrice2 * this.inputSalesData.basicPlanExtentionNum2
            // サービス料金の合計(税抜)
            totalServicePrice += (normal1 + normal2 + extention1 + extention2)

            // 非課税は単純に全て足して算出
            totalPrice += (totalDetailPrice + totalServicePrice)

            let cardTax = 0

            // 課税分の計算
            if (!this.inputFixedPrice) {
                cardTax = this.inputSalesData.basicPlanCardTax
            }

            let taxRate = this.inputSalesData.basicPlanServiceTax + this.inputSalesData.basicPlanTax + cardTax
            // 課税対象の明細と税抜のサービス料金に税をかける
            let taxTargetPrice = totalTaxDetailPrice + totalServicePrice
            totalTaxPrice += this.roundDown(taxTargetPrice + taxTargetPrice * (taxRate/100))
            // 非課税分は単純に足す
            totalTaxPrice += totalTaxFreeDetailPrice

            // 諸々セット
            this.setTotalPrice(totalPrice)
            this.setTotalDetailPrice(totalDetailPrice)
            this.setTotalSerivicePrice(totalServicePrice)

            return totalTaxPrice
        },
        isDisabled () {
            // 正しい会員Noが入力されているか
            // 正しい来店時間、退店時間が入力されているか
            // 来店人数が1人以上になっているか
            //  ➡上記が満たされていない場合、return trueで非活性
            if (this.checkError()) {
                return true
            }

            return false
        },
        basicPlanPrice () {
            return 0
        },
        extentionPrice () {
            // return Con.BASIC_PLAN_EXTENTION[this.inputSalesData.basicPlanType]
            return 0
        },
        culcBasicPlanPrice () {
            return 0
        },
        culcExtentionPrice () {
            return 0
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
        isExtention () {
            if (this.inputSalesData.stayHour > 60) {
                return true
            }
            return false
        },
        // customerNoInvalid () {
        //     if (this.customerNoError != '') {
        //         return true
        //     }
        //     return false
        // },
        totalVisitorsInvalid () {
            if (this.totalVisitorsError != '') {
                return true
            }
            return false
        },
        totalSalesDetailNum () {
            return this.inputSalesDetailData.length
        },
        totalVisitors () {
            return this.inputSalesData.maleVisitors + this.inputSalesData.femaleVisitors
        },
        isDouhan () {
            if (this.inputSalesData.maleVisitors > 0 && this.inputSalesData.femaleVisitors > 0) return true
            return false
        },
        validVisitLeaveTime () {
            if (this.inputSalesData.visitTime == null || this.inputSalesData.leaveTime == null) return false
            const leave = dayjs(this.inputSalesData.leaveTime)
            const visit = dayjs(this.inputSalesData.visitTime)
            if (leave.isAfter(visit)) {
                return true
            }
            return false
        },
        stayHour () {
            if (this.inputSalesData.visitTime == null || this.inputSalesData.leaveTime == null) return '0分'
            const leave = dayjs(this.inputSalesData.leaveTime)
            const visit = dayjs(this.inputSalesData.visitTime)

            const diff = leave.diff(visit, 'minute')
            // console.log('diff', diff)
            if (diff < 0) {
                return '0分'
            }

            const hour = Math.floor(diff / 60)
            const min = diff - (hour * 60)
            let res = min + '分'
            if (hour > 0) {
                return hour + '時間' + res
            } else {
                return res
            }
        },
        registerOrUpdateStr () {
            if (this.editMode) {
                return '更新'
            } else {
                return '登録'
            }
        },
    },
    watch: {
        'inputSalesData.cardPayment': function (val) {
            if (val) {
                this.inputSalesData.basicPlanCardTax = 10
            } else {
                this.inputSalesData.basicPlanCardTax = 0
            }
        },
        'inputSalesData.basicPlanType': function (val) {
            this.calcBasicPlanDetail()
        },

        // 来店人数が1以上=>0になったらエラーメッセージ
        // 'totalVisitors': function (val) {
        //     this.calcBasicPlanDetail()
        // },
        totalVisitors: {
            deep: false,
            handler(newValue, oldValue) {
                if (oldValue > 0 && newValue == 0) {
                    this.totalVisitorsError = '来店客数を入力してください'
                } else if (newValue > 0) {
                    this.totalVisitorsError = ''
                }
                this.calcBasicPlanDetail()
            }
        },


        'inputSalesData.visitTime1': function (val) {
            this.checkVisitTime()
        },
        'inputSalesData.visitTime2': function (val) {
            this.checkVisitTime()
        },
        'inputSalesData.leaveTime1': function (val) {
            this.checkLeaveTime()
        },
        'inputSalesData.leaveTime2': function (val) {
            this.checkLeaveTime()
        },
    },
    methods: {
        calcBasicPlan () {
        },
        ...mapMutations([
            'addSalesList',
            'addSalesListTop',
            'updateSalesList',
            'deleteSalesList',
            'addBottleList',
            'updateBottleList',
            'deleteBottleList',
        ]),
        registerOrUpdate () {
            if (this.waitServerResponse) {
                console.log('サーバー応答待ち')
                return
            }
            if (this.customerInfo.length >= 2 &&
                !this.inputFixedPrice
            ) {
                // 複数顧客入力で実価格入力がされない場合、選択モーダル表示
                this.$refs.inputSalesSelectCustomerDialog.open()
            } else {
                if (!this.editMode) {
                    this.register()
                } else {
                    this.update()
                }
            }
        },
        register () {

            // console.log('this.inputSalesDetailData', this.inputSalesDetailData)

            let salesServiceDetailList = []
            let salesDetailList = []

            for (const item of this.inputSalesDetailData) {
                salesDetailList.push({
                    id: item.product.id,
                    quantity: item.quantity,
                    fixed_price: item.actuallyPrice,
                    tax_free_flg: item.taxation == false,
                    bottle: item.customer != null,
                    customer: item.customer,
                })
            }

            const selectedService = _.cloneDeep(this.service.filter(i => i.id == this.inputSalesData.basicPlanType))
            if (this.inputSalesData.basicPlanNum1 > 0) {
                salesServiceDetailList.push({
                    service: selectedService[0],
                    discount_flg: false,
                    quantity: this.inputSalesData.basicPlanNum1,
                    fixed_price: this.inputSalesData.basicPlanPrice1,
                })
            }
            if (this.inputSalesData.basicPlanNum2 > 0) {
                salesServiceDetailList.push({
                    service: selectedService[0],
                    discount_flg: true,
                    quantity: this.inputSalesData.basicPlanNum2,
                    fixed_price: this.inputSalesData.basicPlanPrice2,
                })
            }
            if (this.inputSalesData.basicPlanExtentionNum1 > 0) {
                salesServiceDetailList.push({
                    service: {
                        'large_category': 1,
                        'middle_category': (selectedService.middle_category == 1) ? true: false,
                        'small_category': 0,
                    },
                    discount_flg: false,
                    quantity: this.inputSalesData.basicPlanExtentionNum1,
                    fixed_price: this.inputSalesData.basicPlanExtentionPrice1,
                })
            }
            if (this.inputSalesData.basicPlanExtentionNum2 > 0) {
                salesServiceDetailList.push({
                    service: {
                        'large_category': 1,
                        'middle_category': (selectedService.middle_category == 1) ? true: false,
                        'small_category': 0,
                    },
                    discount_flg: true,
                    quantity: this.inputSalesData.basicPlanExtentionNum2,
                    fixed_price: this.inputSalesData.basicPlanExtentionPrice2,
                })
            }

            // 20221016 会員情報複数入力
            // 実価格入力（paymentが会員分）
            // 入力しなければ、一番上の会員がpayment全額、他は0
            let salesPayment = []

            let fixedTotalTaxSales = (!this.inputFixedPrice) ? this.totalTaxPrice : this.totalAmountPaid

            if (this.inputFixedPrice) {
                for (const item of this.customerInfo) {
                    let amountPaid = item.amountPaid
                    salesPayment.push({
                        customer_pk: item.id,
                        customer_no: item.customer_no,
                        name: item.name,
                        amount_paid: amountPaid,
                        payment: item.cardPayment,
                        basic_plan_card_tax: item.basicPlanCardTax,
                    })
                }
            } else {
                for (const item of this.customerInfo) {
                    salesPayment.push({
                        customer_pk: item.id,
                        customer_no: item.customer_no,
                        name: item.name,
                        amount_paid: 0,
                        payment: false,
                        basic_plan_card_tax: 0,
                    })
                }
                salesPayment[0].amount_paid = this.totalTaxPrice
                salesPayment[0].payment = this.inputSalesData.cardPayment
                salesPayment[0].basic_plan_card_tax = this.inputSalesData.basicPlanCardTax
            }

            const data = {
                sales_payment: salesPayment,
                // customer_no: this.inputSalesData.customerNo,
                male_visitors: this.inputSalesData.maleVisitors,
                female_visitors: this.inputSalesData.femaleVisitors,
                seat_id: this.inputSalesData.seatId,
                basic_plan_type: this.inputSalesData.basicPlanType,
                total_sales: this.totalPrice,
                total_tax_sales: this.totalTaxPrice,
                basic_plan_service_tax: this.inputSalesData.basicPlanServiceTax,
                basic_plan_tax: this.inputSalesData.basicPlanTax,
                basic_plan_card_tax: this.inputSalesData.basicPlanCardTax,
                payment: (this.inputSalesData.cardPayment) ? 1 : 0,
                remarks: this.inputSalesData.remarks,
                visit_time: this.inputSalesData.visitTime,
                leave_time: this.inputSalesData.leaveTime,
                bottle_delete_list: this.bottleDeleteList,
                sales_service_detail: salesServiceDetailList,
                sales_detail_list: salesDetailList,
                fixed_total_tax_sales: fixedTotalTaxSales,
            }

            console.log('data', data)

            this.waitServerResponse = true

            this.$axios({
                method: 'POST',
                url: '/api/sales/create_sales_data/',
                data: data
            })
            .then(res => {
                console.log('createSalesData', res)
                this.addSalesListTop(res.data.data)
                // 追加したボトル更新
                // 削除したものは?
                // if (res.data.bottle.length > 0) {
                //     this.addBottleList(res.data.bottle)
                // }
                // this.registerSuccessDialog = true
                this.initClose()
            })
            .catch(e => {
                console.log(e)
                this.registerFailureDialog = true
                this.waitServerResponse = false
            })
        },
        update () {

            // console.log('this.inputSalesData', this.inputSalesData)
            // console.log('this.inputSalesDetailData', this.inputSalesDetailData)

            let salesServiceDetailList = []
            let salesDetailList = []

            for (const item of this.inputSalesDetailData) {
                salesDetailList.push({
                    id: item.product.id,
                    quantity: item.quantity,
                    fixed_price: item.actuallyPrice,
                    tax_free_flg: item.taxation == false,
                    bottle: item.customer != null,
                    customer: item.customer,
                })
            }
            const selectedService = _.cloneDeep(this.service.filter(i => i.id == this.inputSalesData.basicPlanType))
            if (this.inputSalesData.basicPlanNum1 > 0) {
                salesServiceDetailList.push({
                    service: selectedService[0],
                    discount_flg: false,
                    quantity: this.inputSalesData.basicPlanNum1,
                    fixed_price: this.inputSalesData.basicPlanPrice1,
                })
            }
            if (this.inputSalesData.basicPlanNum2 > 0) {
                salesServiceDetailList.push({
                    service: selectedService[0],
                    discount_flg: true,
                    quantity: this.inputSalesData.basicPlanNum2,
                    fixed_price: this.inputSalesData.basicPlanPrice2,
                })
            }
            if (this.inputSalesData.basicPlanExtentionNum1 > 0) {
                salesServiceDetailList.push({
                    service: {
                        'large_category': 1,
                        'middle_category': (selectedService.middle_category == 1) ? true: false,
                        'small_category': 0,
                    },
                    discount_flg: false,
                    quantity: this.inputSalesData.basicPlanExtentionNum1,
                    fixed_price: this.inputSalesData.basicPlanExtentionPrice1,
                })
            }
            if (this.inputSalesData.basicPlanExtentionNum2 > 0) {
                salesServiceDetailList.push({
                    service: {
                        'large_category': 1,
                        'middle_category': (selectedService.middle_category == 1) ? true: false,
                        'small_category': 0,
                    },
                    discount_flg: true,
                    quantity: this.inputSalesData.basicPlanExtentionNum2,
                    fixed_price: this.inputSalesData.basicPlanExtentionPrice2,
                })
            }

            // 20221016 会員情報複数入力
            // 実価格入力（paymentが会員分）
            // 入力しなければ、一番上の会員がpayment全額、他は0
            let salesPayment = []

            let fixedTotalTaxSales = (!this.inputFixedPrice) ? this.totalTaxPrice : this.totalAmountPaid

            if (this.inputFixedPrice) {
                for (const item of this.customerInfo) {
                    let amountPaid = item.amountPaid
                    salesPayment.push({
                        customer_pk: item.id,
                        customer_no: item.customer_no,
                        name: item.name,
                        amount_paid: amountPaid,
                        payment: item.cardPayment,
                        basic_plan_card_tax: item.basicPlanCardTax,
                    })
                }
            } else {
                for (const item of this.customerInfo) {
                    salesPayment.push({
                        customer_pk: item.id,
                        customer_no: item.customer_no,
                        name: item.name,
                        amount_paid: 0,
                        payment: false,
                        basic_plan_card_tax: 0,
                    })
                }
                salesPayment[0].amount_paid = this.totalTaxPrice
                salesPayment[0].payment = this.inputSalesData.cardPayment
                salesPayment[0].basic_plan_card_tax = this.inputSalesData.basicPlanCardTax
            }

            const data = {
                sales_payment: salesPayment,
                sales_header_id: this.salesHeaderId,
                // customer_no: this.inputSalesData.customerNo,
                male_visitors: this.inputSalesData.maleVisitors,
                female_visitors: this.inputSalesData.femaleVisitors,
                seat_id: this.inputSalesData.seatId,
                basic_plan_type: this.inputSalesData.basicPlanType,
                total_sales: this.totalPrice,
                total_tax_sales: this.totalTaxPrice,
                basic_plan_service_tax: this.inputSalesData.basicPlanServiceTax,
                basic_plan_tax: this.inputSalesData.basicPlanTax,
                basic_plan_card_tax: this.inputSalesData.basicPlanCardTax,
                payment: (this.inputSalesData.cardPayment) ? 1 : 0,
                remarks: this.inputSalesData.remarks,
                visit_time: this.inputSalesData.visitTime,
                leave_time: this.inputSalesData.leaveTime,
                bottle_delete_list: this.bottleDeleteList,
                sales_service_detail: salesServiceDetailList,
                sales_detail_list: salesDetailList,
                fixed_total_tax_sales: fixedTotalTaxSales,
            }
            console.log('update sales data', data)

            this.waitServerResponse = true

            this.$axios({
                method: 'PUT',
                url: '/api/sales/update_sales_data/',
                data: data
            })
            .then(res => {
                console.log('updateSalesHeader', res)

                // 削除したボトル、追加したボトル更新
                this.$emit('update', res.data.data)

                // this.updateSuccessDialog = true
                this.initClose()
            })
            .catch(e => {
                console.log(e)
                this.updateFailureDialog = true
                this.waitServerResponse = false
            })

        },
        createDouhan (data) {
            // 将来的に可変
            return {
                basic_plan_type: this.inputSalesData.basicPlanType,
                large_category: 2,
                middle_category: 0,
                quantity: 1,
                fixed_price: 5000,
                fixed_tax_price: 6750,
                total_price: 5000,
                total_tax_price: 6750,
            }
        },
        init () {
            this.inputSalesData = {
                // 選択されている料金タイプの種類
                // 通常(1, 2, 3) 貸切(4, 5, 6)
                basicPlanType: 1,

                // customerNo: null,
                maleVisitors: 0,
                femaleVisitors: 0,

                // 日
                visitTime1: now,
                leaveTime1: now,
                // 時刻
                visitTime2: '',
                leaveTime2: '',

                visitTime: null,
                leaveTime: null,
                seatId: 0,
                stayHour: 0,

                basicPlanPrice1: 0,
                basicPlanNum1: 0,
                basicPlanPrice2: 0,
                basicPlanNum2: 0,
                basicPlanExtentionPrice1: 0,
                basicPlanExtentionNum1: 0,
                basicPlanExtentionPrice2: 0,
                basicPlanExtentionNum2: 0,

                basicPlanServiceTax: 10,
                basicPlanTax: 10,
                basicPlanCardTax: 0,

                totalSalesTax: Con.TAX_DEFAULT,
                cardPayment: false,
                remarks: '',
            }
            this.inputSalesDetailData = []
            this.errorMsg = []
            // this.customerNoError = ''
            this.totalVisitorsError = ''
            this.editMode = false
            this.salesHeaderId = null
            this.edit_sales_detail = []
            this.edit_sales_service_detail = []

            this.customerInfo = []

            this.inputFixedPrice = false
            this.totalAmountPaid = 0

            this.totalPrice = 0
            this.totalDetailPrice = 0
            this.totalServicePrice = 0
            this.bottleDeleteList = []

            this.registerSuccessDialog = false
            this.registerFailureDialog = false

            this.updateSuccessDialog = false
            this.updateFailureDialog = false

            this.waitServerResponse = false

            // this.close()
        },
        initClose () {
            this.init()
            this.close()
        },
        initForm () {
            this.inputSalesData = {
                // 選択されている料金タイプの種類
                // 通常(1, 2, 3) 貸切(4, 5, 6)
                basicPlanType: 1,

                // customerNo: null,
                maleVisitors: 0,
                femaleVisitors: 0,

                // 日
                visitTime1: now,
                leaveTime1: now,
                // 時刻
                visitTime2: '',
                leaveTime2: '',

                visitTime: null,
                leaveTime: null,
                seatId: 0,
                stayHour: 0,

                basicPlanPrice1: 0,
                basicPlanNum1: 0,
                basicPlanPrice2: 0,
                basicPlanNum2: 0,
                basicPlanExtentionPrice1: 0,
                basicPlanExtentionNum1: 0,
                basicPlanExtentionPrice2: 0,
                basicPlanExtentionNum2: 0,

                basicPlanServiceTax: 10,
                basicPlanTax: 10,
                basicPlanCardTax: 0,

                totalSalesTax: Con.TAX_DEFAULT,
                cardPayment: false,
                remarks: '',
            }
            this.inputSalesDetailData = []
            this.errorMsg = []
            // this.customerNoError = ''
            this.totalVisitorsError = ''
            this.editMode = false
            this.salesHeaderId = null
            this.edit_sales_detail = []
            this.edit_sales_service_detail = []

            this.inputFixedPrice = false
            this.totalAmountPaid = 0

            this.customerInfo = []
            this.totalPrice = 0
            this.totalDetailPrice = 0
            this.totalServicePrice = 0
            this.bottleDeleteList = []
        },
        open (data) {
            this.dialog = true
            if (data) {
                this.autoFucus = false
                this.convertData(data)
                this.editMode = true
                this.salesHeaderId = data.id
                // console.log('編集モード')
            } else {
                this.autoFucus = true
                this.editMode = false
                // console.log('新規作成モード')
            }
        },
        close () {
            this.dialog = false
        },
        showAddDetailDialog () {
            this.$refs.inputSalesAddDetailDialog.open()
        },
        showAddCustomerDialog () {
            this.$refs.inputSalesAddCustomerDialog.open()
        },
        showEditCustomerDialog (data, index) {
            this.$refs.inputSalesAddCustomerDialog.open(data, index)
        },
        addCustomer (data) {
            console.log('addCustomer', data)
            this.customerInfo.push(data)
            this.updateBottleInfo()
        },
        updateCustomer (data, index) {
            console.log('updateCustomer', data)
            Vue.set(this.customerInfo, index, data)
            // this.customerInfo.push(data)
            this.updateBottleInfo()
            this.updateSelectedProductList()
        },
        selectCustomer (idx) {
            // 複数顧客選択時に支払った会員を選択するモーダルから選択した際のメソッド
            // console.log('selectCustomer', idx, this.customerInfo)
            this.inputFixedPrice = true
            this.customerInfo.map(val => val.amountPaid = 0)
            this.customerInfo.map(val => val.cardPayment = false)
            this.customerInfo.map(val => val.basicPlanCardTax = 0)
            this.customerInfo[idx].amountPaid = this.totalTaxPrice
            this.customerInfo[idx].cardPayment = this.inputSalesData.cardPayment
            this.customerInfo[idx].basicPlanCardTax = this.inputSalesData.basicPlanCardTax
            this.calcTotalAmountPaid()
            // console.log('選択後', this.customerInfo)
        },
        deleteCustomerInfo (index) {
            this.customerInfo.splice(index, 1)
            if (this.customerInfo.length == 0) {
                this.inputFixedPrice = false
                this.totalAmountPaid = 0
            }
            this.updateBottleInfo()
            this.updateSelectedProductList()
        },
        deleteSalesDetail (index) {
            this.inputSalesDetailData.splice(index, 1)
        },
        addSalesDetail (data) {
            this.inputSalesDetailData.push(data)
        },
        addSalesDetailList (data) {
            const arr = this.inputSalesDetailData.concat(data)
            this.inputSalesDetailData = arr
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

            this.inputSalesData.basicPlanType = data.basic_plan_type.id
            let c_list = data.customer_list
            // this.customerInfo = data.customer_list
            for (const c of c_list) {
                for (const p of data.sales_payment) {
                    if (c.customer_no == p.customer.customer_no) {
                        c.amountPaid = p.amount_paid
                        c.cardPayment = (p.payment == 1) ? true : false
                        c.basicPlanCardTax = p.basic_plan_card_tax
                    }
                }
            }
            this.customerInfo = c_list
            this.calcTotalAmountPaid()
            // console.log('this.customerInfo', this.customerInfo)

            this.inputSalesData.maleVisitors = data.male_visitors
            this.inputSalesData.femaleVisitors = data.female_visitors

            if (data.seat == null) {
                this.inputSalesData.seatId = 0
            } else {
                this.inputSalesData.seatId = data.seat.id
            }

            this.inputSalesData.basicPlanServiceTax = data.basic_plan_service_tax
            this.inputSalesData.basicPlanTax = data.basic_plan_tax

            this.inputSalesData.cardPayment = (data.payment == 1) ? true : false
            this.inputSalesData.remarks = data.remarks

            this.inputFixedPrice = true


            let visitTime = data.visit_time.split(' ')
            let leaveTime = data.leave_time.split(' ')
            this.inputSalesData.visitTime1 = visitTime[0].replaceAll('/', '-')
            this.inputSalesData.visitTime2 = visitTime[1]
            this.inputSalesData.leaveTime1 = leaveTime[0].replaceAll('/', '-')
            this.inputSalesData.leaveTime2 = leaveTime[1]

            for (const i in data.sales_service_detail) {
                const salesServiceDetailItem = data.sales_service_detail[i]
                if (!salesServiceDetailItem.discount_flg) {
                    if (salesServiceDetailItem.service.large_category == 0) {
                        // 通常
                        this.inputSalesData.basicPlanPrice1 = salesServiceDetailItem.fixed_price
                        this.inputSalesData.basicPlanNum1 = salesServiceDetailItem.quantity
                    } else {
                        // 延長
                        this.inputSalesData.basicPlanExtentionPrice1 = salesServiceDetailItem.fixed_price
                        this.inputSalesData.basicPlanExtentionNum1 = salesServiceDetailItem.quantity
                    }
                } else {
                    if (salesServiceDetailItem.service.large_category == 0) {
                        // 通常（値引）
                        this.inputSalesData.basicPlanPrice2 = salesServiceDetailItem.fixed_price
                        this.inputSalesData.basicPlanNum2 = salesServiceDetailItem.quantity
                    } else {
                        // 延長（値引）
                        this.inputSalesData.basicPlanExtentionPrice2 = salesServiceDetailItem.fixed_price
                        this.inputSalesData.basicPlanExtentionNum2 = salesServiceDetailItem.quantity
                    }
                }
            }

            let service_detail_list = []
            for (const i in data.sales_detail) {
                const salesDetailItem = data.sales_detail[i]
                service_detail_list.push({
                    actuallyPrice: salesDetailItem.fixed_price,
                    // bottle: salesDetailItem.bottle_register,
                    // 2022/09/10 編集時のボトル登録フラグは折っておく。
                    bottle: false,
                    customer: null,
                    category: salesDetailItem.product.category,
                    name: salesDetailItem.product.name,
                    price: salesDetailItem.product.price,
                    product: salesDetailItem.product,
                    quantity: salesDetailItem.quantity,
                    taxation: !salesDetailItem.tax_free_flg,
                    totalPrice: salesDetailItem.total_price,
                })
            }
            this.inputSalesDetailData = service_detail_list
            this.inputSalesDetailData.push({})
            this.inputSalesDetailData.pop()
            console.log('this.inputSalesDetailData', this.inputSalesDetailData)
            console.log('this.customerInfo', this.customerInfo)
        },
        // checkCustomerNo () {
        //     const val = this.inputSalesData.customerNo
        //
        //     const reg = /^[0-9]+$/
        //     if (val == null) {
        //         this.customerNoError = ''
        //         return
        //     }
        //     if (val.length > 0) {
        //         if (val <= 0 || !reg.test(val)) {
        //             this.customerNoError = '正しい値を入力してください'
        //             this.customerInfo = null
        //         } else {
        //             // this.customerInfo = _.cloneDeep(this.customer.find(c => c.customer_no == val))
        //             // if (this.customerInfo == undefined) {
        //             //     this.customerNoError = '存在しない会員Noです。'
        //             // } else {
        //             //     this.customerNoError = ''
        //             // }
        //             this.searchCustomerNo(val)
        //             .then(res => {
        //                 console.log(res)
        //                 this.customerInfo = res.data.data
        //                 this.customerNoError = ''
        //             })
        //             .catch(e => {
        //                 console.log(e)
        //                 this.customerNoError = '存在しない会員Noです。'
        //                 this.customerInfo = null
        //             })
        //         }
        //     } else {
        //         // this.customerNoError= ''
        //         this.customerNoError= '会員Noを入力してください'
        //         this.customerInfo = null
        //     }
        // },
        calcBasicPlanDetail () {

            if (this.totalVisitors == 0) {
                // console.log('来店人数が0')
                this.initBasicPlanPrice()
                return
            }

            const maleVisitors = this.inputSalesData.maleVisitors
            const femaleVisitors = this.inputSalesData.femaleVisitors

            let isCharted = this.inputSalesData.basicPlanType >= 4

            let basicPlanNormalNum1 = 0
            let basicPlanNormalNum2 = 0
            if (this.isDouhan && !isCharted) {
                // 同伴で通常プランの場合 => 女性は半額
                // 基本料金の数量 = 男性客数分
                basicPlanNormalNum1 = maleVisitors
                // 基本料金(割引)の数量 = 女性客数分
                basicPlanNormalNum2 = femaleVisitors
            } else {
                // それ以外は割引無
                basicPlanNormalNum1 += (maleVisitors + femaleVisitors)
            }
            // 基本料金の値段をプランによって設定
            const basicPlanNormalPrice1 = Con.BASIC_PLAN_PRICE_FOR_CRM[this.inputSalesData.basicPlanType]
            this.inputSalesData.basicPlanPrice1 = basicPlanNormalPrice1
            this.inputSalesData.basicPlanPrice2 = basicPlanNormalPrice1 / 2
            this.inputSalesData.basicPlanNum1 = basicPlanNormalNum1
            this.inputSalesData.basicPlanNum2 = basicPlanNormalNum2

            const basicPlanExtentionPrice1 = (isCharted) ? Con.EXTENTION_PRICE[1] : Con.EXTENTION_PRICE[0]
            this.inputSalesData.basicPlanExtentionPrice1 = basicPlanExtentionPrice1
            this.inputSalesData.basicPlanExtentionPrice2 = basicPlanExtentionPrice1 / 2

            if (this.inputSalesData.visitTime == null ||
                this.inputSalesData.leaveTime == null) {
                // console.log(this.inputSalesData.visitTime, this.inputSalesData.leaveTime)
                // console.log('来店時間または退店時間が空')
                return
            }

            // あと延長の数
            // 基本料金によって区切りが違う(最初ののみ。後は1時間区切り)
            // 退店時刻(画面開いた時間)を取得を取得
            const now = dayjs(this.inputSalesData.leaveTime)
            // 来店時刻との差分を分で取得
            const diff = now.diff(dayjs(this.inputSalesData.visitTime), 'minute')

            // 全体の分数から基本プランの分数引いた数を取得
            const diffMinute = diff - Con.BASIC_PLAN_SEP_MINUTE_FOR_CRM[this.inputSalesData.basicPlanType]

            // 延長の時間を切り上げで取得
            let extentionNum = 0
            if (diffMinute > 0) {
                extentionNum = Math.ceil(diffMinute / 60)
            }

            if (this.isDouhan && !isCharted) {
                this.inputSalesData.basicPlanExtentionNum1 = maleVisitors * extentionNum
                this.inputSalesData.basicPlanExtentionNum2 = femaleVisitors * extentionNum
            } else {
                this.inputSalesData.basicPlanExtentionNum1 = (maleVisitors + femaleVisitors) * extentionNum
                this.inputSalesData.basicPlanExtentionNum2 = 0
            }
        },
        initBasicPlanPrice () {
            this.inputSalesData.basicPlanPrice1 = 0
            this.inputSalesData.basicPlanNum1 = 0
            this.inputSalesData.basicPlanPrice2 = 0
            this.inputSalesData.basicPlanNum2 = 0
            this.inputSalesData.basicPlanExtentionPrice1 = 0
            this.inputSalesData.basicPlanExtentionNum1 = 0
            this.inputSalesData.basicPlanExtentionPrice2 = 0
            this.inputSalesData.basicPlanExtentionNum2 = 0
        },
        initExtentionNum () {
            this.inputSalesData.basicPlanExtentionNum1 = 0
            this.inputSalesData.basicPlanExtentionNum2 = 0
        },
        checkVisitTime () {
            const day = this.inputSalesData.visitTime1
            const time = this.inputSalesData.visitTime2
            if (day == '' || time == '') {
                // console.log('来店時間どっちかが空', day, time)
                this.inputSalesData.visitTime = null
                this.initExtentionNum()
            } else {
                this.inputSalesData.visitTime = day + ' ' + time
                // console.log('来店時間:', this.inputSalesData.visitTime)
                if (this.validVisitLeaveTime) {
                    this.calcBasicPlanDetail()
                } else {
                    this.initExtentionNum()
                }

                this.checkVisitLeaveTimeError()
            }
        },
        checkLeaveTime () {
            const day = this.inputSalesData.leaveTime1
            const time = this.inputSalesData.leaveTime2
            if (day == '' || time == '') {
                // console.log('退店時間どっちかが空', day, time)
                this.inputSalesData.leaveTime = null
                this.initExtentionNum()
            } else {
                this.inputSalesData.leaveTime = day + ' ' + time
                // console.log('退店時間:', this.inputSalesData.leaveTime)
                if (this.validVisitLeaveTime) {
                    this.calcBasicPlanDetail()
                } else {
                    this.initExtentionNum()
                }

                this.checkVisitLeaveTimeError()
            }
        },
        checkVisitLeaveTimeError () {
            if (this.inputSalesData.visitTime != null && this.inputSalesData.leaveTime != null) {
                const visit = dayjs(this.inputSalesData.visitTime)
                const leave = dayjs(this.inputSalesData.leaveTime)
                if (visit.isAfter(leave)) {
                    this.visitLeaveTimeError = '来店時間を退店時間より前の時間になるように入力して下さい。'
                } else {
                    this.visitLeaveTimeError = ''
                }
            } else {
                this.visitLeaveTimeError = ''
            }
        },
        setTotalPrice (val) {
            this.totalPrice = val
        },
        setTotalDetailPrice (val) {
            this.totalDetailPrice = val
        },
        setTotalSerivicePrice (val) {
            this.totalServicePrice = val
        },
        updateBottleDelete (item) {
            console.log('updateBottleDelete', item)
            if (item.bottleDelete) {
                this.bottleDeleteList.push(item)
            } else {
                this.bottleDeleteList = this.bottleDeleteList.filter(e => e.id !== item.id)
            }
            console.log('this.bottleDeleteList', this.bottleDeleteList)
        },
        checkError () {
            // if (this.inputSalesData.customerNo == null ||
            //     this.inputSalesData.customerNo.length == 0)
            // {
            //     return true
            // }

            if (this.inputSalesData.visitTime == null ||
                this.inputSalesData.leaveTime == null)
            {
                return true
            }

            if (this.totalVisitors == 0) {
                return true
            }

            if (this.visitLeaveTimeError.length != 0 ||
                this.totalVisitorsError.length != 0)
            {
                return true
            }
            return false
        },
        dispTotalPrice (item) {
            // console.log('dispTotalPrice', item)
            if (item.actuallyPrice != null && item.actuallyPrice > 0) {
                return item.actuallyPrice * item.quantity
            }
            return 0
        },
        registerFailure () {
            this.registerFailureDialog = false
            this.waitServerResponse = false
        },
        updateFailure () {
            this.updateFailureDialog = false
            this.waitServerResponse = false
        },
        updateInputSalesData (val) {
            this.inputSalesData = val
        },
        calcTotalAmountPaid () {
            let result = 0
            for (const item of this.customerInfo) {
                result += Number(item.amountPaid)
            }
            this.totalAmountPaid = result
        },
        changeCardPayment (val, idx) {
            let res = 0
            if (val) res = 10
            this.customerInfo[idx].basicPlanCardTax = res
        },
        updateBottleInfo () {
            let result = []
            for (const item of this.customerInfo) {
                for (const b of item.bottle) {
                    result.push(b)
                }
            }
            this.bottleInfo = result
        },
        updateSelectedProductList () {
            // console.log('updateSelectedProductList')
            // console.log('this.customerInfo', this.customerInfo)
            // console.log('this.inputSalesDetailData', this.inputSalesDetailData)
            let customerNoList = []
            for (const item of this.customerInfo) {
                customerNoList.push(item.customer_no)
            }

            // console.log('customerNoList', customerNoList)

            for (const detail of this.inputSalesDetailData) {
                if (detail.customer != null) {
                    if (!customerNoList.includes(detail.customer.customer_no)) {
                        // console.log('削除or更新された会員なのでボトル登録削除')
                        // console.log('detail', detail)
                        detail.bottle = false
                        detail.customer = null
                    }
                }
            }

        },
        addBottleCustomerInfo (val, updateIdx) {
            this.$refs.inputSalesBottleSelectCustomerDialog.open(val, updateIdx)
        },
        selectBottleCustomerProductList (idx, updateIdx) {
            console.log('before ', this.inputSalesDetailData)
            this.inputSalesDetailData[updateIdx].customer = this.customerInfo[idx]
            console.log('after ', this.inputSalesDetailData)
        },
        deleteCustomerSelectedProductList (idx) {
            this.inputSalesDetailData[idx].customer = null
        },
        isBottleCustomerDisabledRow (item) {
            if (item.product.category.large_category == 1 &&
                item.product.category.middle_category == 0)
            {
                if (item.product.category.small_category != 4) {
                    return false
                } else {
                    return true
                }
            }
            return true
        },
        // isSalesDetailBottleCustomerDisabled () {
        //     if (this.customerInfo == null || this.customerInfo.length == 0) {
        //         return true
        //     }
        //     return false
        // },
        // updateTotalTaxPrice () {
        //     / 総計(税抜)
        //     let totalPrice = 0
        //     // 総計(税込)
        //     let totalTaxPrice = 0
        //
        //     // 明細の総計
        //     let totalDetailPrice = 0
        //     // サービス料金総計
        //     let totalServicePrice = 0
        //
        //     // 課税の明細総計
        //     let totalTaxDetailPrice = 0
        //     // 非課税の明細総計
        //     let totalTaxFreeDetailPrice = 0
        //
        //     // console.log('this.inputSalesDetailData', this.inputSalesDetailData)
        //
        //     // 明細の計算
        //     for (const item of this.inputSalesDetailData) {
        //         if (item.taxation) {
        //             // console.log('課税対象')
        //             // 課税
        //             totalTaxDetailPrice += item.actuallyPrice * item.quantity
        //         } else {
        //             // console.log('非課税')
        //             // 非課税
        //             totalTaxFreeDetailPrice += item.actuallyPrice * item.quantity
        //         }
        //     }
        //     // 明細の合計(税抜)
        //     totalDetailPrice = (totalTaxDetailPrice + totalTaxFreeDetailPrice)
        //
        //     // サービス料金の計算
        //     const normal1 = this.inputSalesData.basicPlanPrice1 * this.inputSalesData.basicPlanNum1
        //     const normal2 = this.inputSalesData.basicPlanPrice2 * this.inputSalesData.basicPlanNum2
        //     const extention1 = this.inputSalesData.basicPlanExtentionPrice1 * this.inputSalesData.basicPlanExtentionNum1
        //     const extention2 = this.inputSalesData.basicPlanExtentionPrice2 * this.inputSalesData.basicPlanExtentionNum2
        //     // サービス料金の合計(税抜)
        //     totalServicePrice += (normal1 + normal2 + extention1 + extention2)
        //
        //     // 非課税は単純に全て足して算出
        //     totalPrice += (totalDetailPrice + totalServicePrice)
        //
        //     let cardTax = 0
        //
        //     // 課税分の計算
        //     if (!this.inputFixedPrice) {
        //         cardTax = this.inputSalesData.basicPlanCardTax
        //     }
        //
        //     let taxRate = this.inputSalesData.basicPlanServiceTax + this.inputSalesData.basicPlanTax + cardTax
        //     // 課税対象の明細と税抜のサービス料金に税をかける
        //     let taxTargetPrice = totalTaxDetailPrice + totalServicePrice
        //     totalTaxPrice += this.roundDown(taxTargetPrice + taxTargetPrice * (taxRate/100))
        //     // 非課税分は単純に足す
        //     totalTaxPrice += totalTaxFreeDetailPrice
        //
        //     // 諸々セット
        //     this.setTotalPrice(totalPrice)
        //     this.setTotalDetailPrice(totalDetailPrice)
        //     this.setTotalSerivicePrice(totalServicePrice)
        //     return totalTaxPrice
        // }
    },
    mixins: [
        customerMixin,
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

        .width10 {
            width: 10%;
        }

        .width5 {
            width: 5%;
        }


    }

    .invalid {
        color: red;
    }

    .form_required:after{
        content: '*';
        color: red;
    }

    .customer_detail_customer_icon {
        border-radius: 50%;
        width: 50px;
        height: 50px;
    }

    .bottle_card_product_name_area {
        height: 80px;
    }

    .disabled {
        background-color: rgba(170, 170, 170, 0.2);
    }

    .input_sales_delete_product_btn {
        cursor: pointer;
    }

</style>
