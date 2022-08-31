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
                        <b-row>
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
                                            required
                                            :autofocus="autoFucus"
                                            placeholder="会員No(必須)"
                                            @blur="checkCustomerNo"
                                        ></b-form-input>
                                        <b-form-invalid-feedback :state="customerNoError.length == 0">
                                            {{ customerNoError }}
                                        </b-form-invalid-feedback>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
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
                    <table>
                        <tr>
                            <th>商品名</th>
                            <th>定価</th>
                            <th>実価格</th>
                            <th>数量</th>
                            <th>ボトル登録</th>
                            <th>課税</th>
                            <th>総計(税抜)</th>
                            <!-- <th>総計(税込)</th> -->
                            <!-- <th>備考</th> -->
                            <th></th>
                        </tr>
                        <tr
                            v-for="(item, id) in inputSalesDetailData"
                            :key=id
                        >
                            <td>
                                <!-- <b-img
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
                                ></b-img> -->
                                <span>{{ item.name }}</span>
                            </td>
                            <td>{{ item.price | priceLocaleString }}</td>

                            <!-- ★カンマつかないときがある？ -->
                            <td>{{ item.actuallyPrice | priceLocaleString }}</td>
                            <td>{{ item.quantity | priceLocaleString }}</td>
                            <td>
                                <b-card-text v-if="item.bottle">有</b-card-text>
                                <b-card-text v-else>無</b-card-text>
                            </td>
                            <td>
                                <span v-if="item.taxation">有</span>
                                <span v-else>無</span>
                            </td>
                            <td>{{ item.totalPrice | priceLocaleString }}</td>
                            <!-- <td>{{ item.totalTaxPrice | priceLocaleString }}</td> -->
                            <!-- <td>{{ item.remarks }}</td> -->
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
                    <!-- label-cols-lg="3"
                    label="ボトル情報"
                    label-size="lg"
                    label-class="font-weight-bold pt-0" -->
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
                        <b-card-text v-if="customerInfo == null || inputSalesData.customerNo == '' || inputSalesData.customerNo == null">
                            正しい会員Noを入力してください。
                        </b-card-text>
                        <b-card-text v-else-if="customerInfo.bottle.length == 0">
                            ボトル情報がありません。
                        </b-card-text>
                        <b-row v-else>
                            <b-col
                                v-for="(item, i) in customerInfo.bottle"
                                :key="i"
                                cols="4"
                            >
                                <b-card>
                                    <div>
                                        <small class="text-muted">
                                            No.{{ i+1 }}
                                        </small>
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

                        <b-col
                            cols="2"
                        >
                            <b-card-sub-title>
                                注文数
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                {{ totalSalesDetailNum | priceLocaleString }}点
                            </b-card-title>
                        </b-col>

                        <b-col
                            cols="2"
                        >
                            <b-card-sub-title>
                                支払方法
                            </b-card-sub-title>
                            <b-card-title class="mb-0" v-if="inputSalesData.cardPayment">
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
                            @click="init"
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
                            @click="registerFailureDialog = false"
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


export default {
    name: 'InputSalesDialogItem',
    props: {
    },
    components: {
        InputSalesDetailDialog,
        InputSalesAddDetailDialog,
        SelectForm,
        CheckboxForm,
        ErrorModal
    },
    data: () => ({
        dialog: false,
        inputSalesData: {
            // 選択されている料金タイプの種類
            // 通常(1, 2, 3) 貸切(4, 5, 6)
            basicPlanType: 1,

            customerNo: null,
            maleVisitors: 0,
            femaleVisitors: 0,

            // 日
            visitTime1: '',
            leaveTime1: '',
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
        customerNoError: '',
        totalVisitorsError: '',
        visitTimeError: '',
        leaveTimeError: '',
        visitLeaveTimeError: '',
        editMode: false,
        salesHeaderId: null,
        edit_sales_detail: [],
        edit_sales_service_detail: [],
        customerInfo: null,

        // seatOptions: [],

        totalPrice: 0,
        totalDetailPrice: 0,
        totalServicePrice: 0,
        bottleDeleteList: [],
        registerSuccessDialog: false,
        registerFailureDialog: false,

        autoFucus: false,
    }),
    created () {
        this.$eventHub.$off('addSalesDetail')
        this.$eventHub.$on('addSalesDetail', this.addSalesDetail)
        this.$eventHub.$off('addSalesDetailList')
        this.$eventHub.$on('addSalesDetailList', this.addSalesDetailList)

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

            // 明細の計算
            for (const item of this.inputSalesDetailData) {
                if (item.taxation) {
                    // 課税
                    totalTaxDetailPrice += item.actuallyPrice * item.quantity
                } else {
                    // 非課税
                    totalTaxFreeDetailPrice += item.actuallyPrice * item.quantity
                }
            }
            totalDetailPrice = (totalTaxDetailPrice + totalTaxFreeDetailPrice)

            // サービス料金の計算
            const normal1 = this.inputSalesData.basicPlanPrice1 * this.inputSalesData.basicPlanNum1
            const normal2 = this.inputSalesData.basicPlanPrice2 * this.inputSalesData.basicPlanNum2
            const extention1 = this.inputSalesData.basicPlanExtentionPrice1 * this.inputSalesData.basicPlanExtentionNum1
            const extention2 = this.inputSalesData.basicPlanExtentionPrice2 * this.inputSalesData.basicPlanExtentionNum2
            totalServicePrice += (normal1 + normal2 + extention1 + extention2)

            // 非課税は単純に全て足して算出
            totalPrice += (totalDetailPrice + totalServicePrice)

            // 課税分の計算
            let taxRate = this.inputSalesData.basicPlanServiceTax + this.inputSalesData.basicPlanTax + this.inputSalesData.basicPlanCardTax
            let taxTargetPrice = totalDetailPrice + totalServicePrice
            totalTaxPrice += this.roundDown(taxTargetPrice + taxTargetPrice * (taxRate/100))

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
        customerNoInvalid () {
            if (this.customerNoError != '') {
                return true
            }
            return false
        },
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
        }
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
            if (!this.editMode) {
                this.register()
            } else {
                this.update()
            }
        },
        register () {

            console.log('this.inputSalesDetailData', this.inputSalesDetailData)

            let salesServiceDetailList = []
            let salesDetailList = []

            for (const item of this.inputSalesDetailData) {
                salesDetailList.push({
                    id: item.product.id,
                    quantity: item.quantity,
                    fixed_price: item.actuallyPrice,
                    tax_free_flg: item.taxation == false,
                    bottle: item.bottle,
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

            const data = {
                customer_no: this.inputSalesData.customerNo,
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
            }

            console.log('data', data)

            this.$axios({
                method: 'POST',
                url: '/api/sales/create_sales_data/',
                data: data
            })
            .then(res => {
                console.log('createSalesHeader', res)
                this.addSalesListTop(res.data.data)
                if (res.data.bottle.length != 0) {
                    this.addBottleList(res.data.bottle)
                }
                this.registerSuccessDialog = true
                // this.init()
            })
            .catch(e => {
                console.log(e)
                this.registerFailureDialog = true
            })
        },
        update () {
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

                customerNo: null,
                maleVisitors: 0,
                femaleVisitors: 0,

                // 日
                visitTime1: '',
                leaveTime1: '',
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
            this.customerNoError = ''
            this.totalVisitorsError = ''
            this.editMode = false
            this.salesHeaderId = null
            this.edit_sales_detail = []
            this.edit_sales_service_detail = []

            this.customerInfo = null
            this.totalPrice = 0
            this.totalDetailPrice = 0
            this.totalServicePrice = 0
            this.bottleDeleteList = []

            this.registerSuccessDialog = false
            this.registerFailureDialog = false

            this.close()
        },
        initForm () {
            this.inputSalesData = {
                // 選択されている料金タイプの種類
                // 通常(1, 2, 3) 貸切(4, 5, 6)
                basicPlanType: 1,

                customerNo: null,
                maleVisitors: 0,
                femaleVisitors: 0,

                // 日
                visitTime1: '',
                leaveTime1: '',
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
            this.customerNoError = ''
            this.totalVisitorsError = ''
            this.editMode = false
            this.salesHeaderId = null
            this.edit_sales_detail = []
            this.edit_sales_service_detail = []

            this.customerInfo = null
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

            this.inputSalesData.basicPlanType = data.basic_plan_type.id
            this.inputSalesData.customerNo = String(data.customer.customer_no)
            this.customerInfo = data.customer
            this.inputSalesData.maleVisitors = data.male_visitors
            this.inputSalesData.femaleVisitors = data.female_visitors

            if (data.seat == null) {
                this.inputSalesData.seatId = 0
            } else {
                this.inputSalesData.seatId = data.seat.id
            }

            this.inputSalesData.basicPlanServiceTax = data.basic_plan_service_tax
            this.inputSalesData.basicPlanTax = data.basic_plan_tax
            this.inputSalesData.basicPlanCardTax = data.basic_plan_card_tax

            this.inputSalesData.cardPayment = (data.payment == 1) ? true : false
            this.inputSalesData.remarks = data.remarks

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
                    bottle: salesDetailItem.bottle_register,
                    category: salesDetailItem.product.category,
                    name: salesDetailItem.product.name,
                    price: salesDetailItem.product.price,
                    product: salesDetailItem.product,
                    quantity: salesDetailItem.quantity,
                    taxation: salesDetailItem.tax_free_flg,
                    totalPrice: salesDetailItem.total_price,
                })
            }
            this.inputSalesDetailData = service_detail_list
        },
        checkCustomerNo () {
            const val = this.inputSalesData.customerNo

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
                    // this.customerInfo = _.cloneDeep(this.customer.find(c => c.customer_no == val))
                    // if (this.customerInfo == undefined) {
                    //     this.customerNoError = '存在しない会員Noです。'
                    // } else {
                    //     this.customerNoError = ''
                    // }
                    this.searchCustomerNo(val)
                    .then(res => {
                        console.log(res)
                        this.customerInfo = res.data.data
                        this.customerNoError = ''
                    })
                    .catch(e => {
                        console.log(e)
                        this.customerNoError = '存在しない会員Noです。'
                        this.customerInfo = null
                    })
                }
            } else {
                // this.customerNoError= ''
                this.customerNoError= '会員Noを入力してください'
                this.customerInfo = null
            }
        },
        calcBasicPlanDetail () {

            if (this.totalVisitors == 0) {
                console.log('来店人数が0')
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
            if (this.inputSalesData.customerNo == null ||
                this.inputSalesData.customerNo.length == 0)
            {
                return true
            }

            if (this.inputSalesData.visitTime == null ||
                this.inputSalesData.leaveTime == null)
            {
                return true
            }

            if (this.totalVisitors == 0) {
                return true
            }

            if (this.customerNoError.length != 0 ||
                this.visitLeaveTimeError.length != 0 ||
                this.totalVisitorsError.length != 0)
            {
                return true
            }
            return false
        },
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

</style>
