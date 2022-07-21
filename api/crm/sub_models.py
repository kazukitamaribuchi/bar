from django.db import models
from django.utils.translation import gettext_lazy as _

from .db.base import (
    AbstractBaseModel
)




# class QuestionAnswer(AbstractBaseModel):
#     """
#     Q&A管理テーブル
#     """
#
#     question = models.ForeignKey(
#         'crm.MQuestion',
#         on_delete=models.CASCADE,
#     )
#
#     cast = models.ForeignKey(
#         'crm.MCast',
#         on_delete=models.CASCADE,
#     )
#
#     answer = models.TextField(
#         _('Q&A Answer')
#     )
#
#     def __str__(self):
#         return str(self.question.question) + ' 回答者:' + self.cast.name
#
#     class Meta:
#         verbose_name_plural = 'Q&A管理テーブル'

class CardManagement(AbstractBaseModel):
    """
    カード管理テーブル
        顧客:カード=1:1
        　カード紛失もあり得るため、カードで会員Noは管理。
          連番でカード上は0埋めで8桁とか？
    """

    customer_no = models.AutoField(
        _('会員No'),
        primary_key=True,
        editable=False,
    )

    total_point = models.IntegerField(
        _('ポイント総数'),
        default=0,
    )

    lost_flg = models.BooleanField(
        _('紛失フラグ'),
        default=False,
    )

    def __str__(self):
        return str(self.customer_no)

    class Meta:
        verbose_name_plural = 'カード管理テーブル'



class BottleManagement(AbstractBaseModel):
    """
    ボトル管理マスタ
        商品名
        開栓日

        会員の場合customer紐づく
        非会員の場合customerは紐づかない

    """

    open_date = models.DateTimeField(
        _('開封日'),
    )
    end_date = models.DateTimeField(
        _('飲み終えた日付'),
        null=True,
        blank=True,
    )
    deadline = models.DateTimeField(
        _('賞味期限'),
        null=True,
        blank=True,
    )
    end_flg = models.BooleanField(
        _('飲み終わったかフラグ'),
        default=False,
    )
    waste_flg = models.BooleanField(
        _('廃棄フラグ'),
        default=False
    )
    customer = models.ForeignKey(
        'crm.MCustomer',
        on_delete=models.PROTECT,
        related_name='bottle_customer',
        null=True,
        blank=True,
    )
    non_member_name = models.CharField(
        _('非会員の名前'),
        max_length=50,
        null=True,
        blank=True,
    )
    # リレーション大丈夫か
    product = models.ForeignKey(
        'crm.MProduct',
        on_delete=models.PROTECT,
        related_name='bottle_product'
    )

    def __str__(self):
        return self.customer.name + ' : ' + self.product.name

    class Meta:
        verbose_name_plural = 'ボトル管理テーブル'


class SalesHeader(AbstractBaseModel):
    """
    売上ヘッダ
        会計日
        総額
        顧客(1)
        担当(n)

        2022/06/24
            非会員の売上はcustomerが紐づかない
            =>名前で入力しない前提で設計
    """

    # on_delete要検討
    customer = models.ForeignKey(
        'crm.MCustomer',
        on_delete=models.DO_NOTHING,
        related_name='sales_header',
        null=True,
        blank=True,
    )

    male_visitors = models.SmallIntegerField(
        _('男性来店人数'),
        default=0,
    )

    female_visitors = models.SmallIntegerField(
        _('女性来店人数'),
        default=0,
    )

    # total_visitors = models.SmallIntegerField(
    #     _('来店人数'),
    #     default=1,
    # )

    # 5/14 => 指名管理の中間テーブルに変更
    # on_delete要検討
    cast = models.ManyToManyField(
        'crm.MCast',
        related_name='sales_header',
        blank=True,
    )

    # 5/17 => basic_service（基本料金や指名料、延長料、同伴料）と結び付けるようにする。
    # appoint = models.ManyToManyField(
    #     'crm.MCast',
    #     blank=True,
    #     through='AppointManagement',
    #     related_name='appoint'
    # )


    # move_diff_seat = models.BooleanField(
    #     _('席移動フラグ'),
    #     default=False
    # )

    # account_date = models.DateTimeField()

    visit_time = models.DateTimeField()
    leave_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    # move_time = models.DateTimeField(null=True, blank=True)

    payment = models.ForeignKey(
        'crm.MPayment',
        on_delete=models.CASCADE,
        related_name='sales_header',
        null=True,
    )

    # is_charterd = models.BooleanField(
    #     _('貸し切りフラグ'),
    #     default=False,
    # )

    # appoint = models.BooleanField(
    #     _('指名フラグ'),
    #     default=False,
    # )

    # douhan = models.BooleanField(
    #     _('同伴フラグ'),
    #     default=False,
    # )

    # 予約と結び付けも考慮しなきゃ・・・
    booking = models.BooleanField(
        _('予約フラグ'),
        default=False,
    )

    basic_plan_type = models.ForeignKey(
        'crm.MService',
        on_delete=models.CASCADE,
        related_name="sales_header_basic_plan_type"
    )

    stay_hour = models.SmallIntegerField(
        _('滞在時間'),
        default=0,
    )

    # stay_hour_other = models.SmallIntegerField(
    #     _('滞在時間（席移動後）'),
    #     default=0,
    # )

    # total_stay_hour = models.SmallIntegerField(
    #     _('総滞在時間'),
    #     default=0,
    # )

    total_sales = models.IntegerField(
        _('総計（税抜）'),
        default=0,
    )

    total_tax_sales = models.IntegerField(
        _('総計（税込）'),
        default=0,
    )

    tax_free_flg = models.BooleanField(
        _('非課税フラグ'),
        default=False,
    )

    tax_rate = models.SmallIntegerField(
        _('税率'),
        default=35,
    )

    seat = models.ForeignKey(
        'crm.MSeat',
        on_delete=models.CASCADE,
        related_name='sales_header',
        null=True,
        blank=True,
    )

    close_flg = models.BooleanField(
        _('締済フラグ'),
        default=False,
    )

    def __str__(self):
        return '売上No.' + str(self.id) + ' ' + str(self.total_tax_sales) + '円'

    class Meta:
        verbose_name_plural = '売上ヘッダ'
        indexes = [
            models.Index(fields=['customer'], name='sales_header_customer_idx'),
        ]


class SalesServiceDetail(AbstractBaseModel):
    """
    売上明細
        基本料金
    """

    header = models.ForeignKey(
        SalesHeader,
        on_delete=models.CASCADE,
        related_name='sales_service_detail'
    )

    service = models.ForeignKey(
        'crm.MService',
        on_delete=models.CASCADE,
        related_name="sales_service_detail"
    )

    # cast = models.ForeignKey(
    #     'crm.MCast',
    #     on_delete=models.PROTECT,
    #     null=True,
    #     blank=True,
    # )

    # quantity = models.DecimalField(
    #     _('数量'),
    #     max_digits=10,
    #     decimal_places=2,
    #     default=1.00,
    # )

    quantity = models.SmallIntegerField(
        _('個数'),
        default=1,
    )

    discount_flg = models.BooleanField(
        _('値引きフラグ(女性は50%OFF)'),
        default=False,
    )

    fixed_price = models.IntegerField(
        _('実価格（税抜）'),
    )

    # fixed_tax_price = models.IntegerField(
    #     _('実価格（税込）'),
    # )

    tax_free_flg = models.BooleanField(
        _('非課税フラグ'),
        default=False,
    )

    tax_rate = models.SmallIntegerField(
        _('税率'),
        default=35,
    )

    # total_price = models.IntegerField(
    #     _('総計')
    # )

    # total_tax_price = models.IntegerField(
    #     _('総計（税込）')
    # )

    def __str__(self):
        service = self.service.name
        return service

    class Meta:
        verbose_name_plural = '売上サービス明細'


# class SalesAppointDetail(AbstractBaseModel):
#     """
#     売上明細
#         指名料金
#     """
#
#     header = models.ForeignKey(
#         SalesHeader,
#         on_delete=models.CASCADE,
#         related_name='sales_appoint_detail'
#     )
#
#     service = models.ForeignKey(
#         'crm.MService',
#         on_delete=models.CASCADE,
#         related_name="sales_appoint_detail"
#     )
#
#     cast = models.ForeignKey(
#         'crm.MCast',
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#     )
#
#     quantity = models.DecimalField(
#         _('数量'),
#         max_digits=10,
#         decimal_places=2,
#         default=1.00,
#     )
#
#     fixed_price = models.IntegerField(
#         _('実価格（税抜）'),
#     )
#
#     fixed_tax_price = models.IntegerField(
#         _('実価格（税込）'),
#     )
#
#     total_price = models.IntegerField(
#         _('総計')
#     )
#
#     total_tax_price = models.IntegerField(
#         _('総計（税込）')
#     )
#
#     def __str__(self):
#         cast_name = self.cast.name
#         service = self.service
#         return '指名キャスト: ' + cast_name + ' ' + service.name
#
#     class Meta:
#         verbose_name_plural = '売上指名明細'


class SalesDetail(AbstractBaseModel):
    """
    売上明細
        商品の売上
    """

    # CASCADEの認識正しいか？
    header = models.ForeignKey(
        SalesHeader,
        on_delete=models.CASCADE,
        related_name='sales_detail'
    )

    product = models.ForeignKey(
        'crm.MProduct',
        on_delete=models.CASCADE,
        related_name='sales_detail',
    )

    # cast_order = Trueの場合、キャストが必ず紐づく
    # cast_order = models.BooleanField(
    #     _('キャストの頼んだ商品か'),
    #     default=False,
    # )

    # これは誰のキャストの売上か
    # 　☞将来的にはキャストに対するバックを換算するため商品1つ1つに紐づけが必要なため。
    cast = models.ForeignKey(
        'crm.MCast',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    # quantity = models.DecimalField(
    #     _('個数'),
    #     max_digits=10,
    #     decimal_places=2,
    #     default=1.00,
    # )

    quantity = models.SmallIntegerField(
        _('個数'),
        default=1,
    )

    fixed_price = models.IntegerField(
        _('実価格（税抜）'),
        default=0,
    )

    # fixed_tax_price = models.IntegerField(
    #     _('実価格（税込）'),
    # )

    tax_free_flg = models.BooleanField(
        _('非課税フラグ'),
        default=False,
    )

    tax_rate = models.SmallIntegerField(
        _('税率'),
        default=35,
    )

    # total_price = models.IntegerField(
    #     _('総計'),
    #     default=0,
    # )

    # total_tax_price = models.IntegerField(
    #     _('総計（税込）')
    # )

    end_flg = models.BooleanField(
        # 作ったら更新 => 届けたら更新も必要？
        _('締めフラグ'),
        default=False,
    )

    order_time = models.DateTimeField(
        _('注文時間'),
    )

    def __str__(self):
        product_name = self.product.name
        return '売上No.' + str(self.header.id) + ' ' + product_name

    class Meta:
        verbose_name_plural = '売上明細'




# class AppointManagement(AbstractBaseModel):
#     """
#     """
#     sales_header = models.ForeignKey(
#         SalesHeader,
#         on_delete=models.PROTECT,
#         related_name='sales_header',
#     )
#
#     cast = models.ForeignKey(
#         'crm.MCast',
#         on_delete=models.PROTECT,
#         related_name='cast',
#     )
#
#     appoint = models.ForeignKey(
#         'crm.MAppointService',
#         on_delete=models.PROTECT,
#         related_name='appoint',
#     )
#
#     appoint_time = models.IntegerField(
#         _('指名時間'),
#     )


class BookingManagement(AbstractBaseModel):
    """
    予約情報
        開始時間
        終了時間
        席
        担当
        顧客
        キャンセルフラグ
        人数
    """

    register_date = models.DateTimeField(
        _('予約登録日')
    )

    booking_start = models.DateTimeField(
        _('予約開始時間')
    )

    booking_end = models.DateTimeField(
        _('予約終了時間'),
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        'crm.MCustomer',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    non_member_name = models.CharField(
        _('非会員の名前'),
        max_length=50,
        null=True,
        blank=True,
    )

    cast = models.ManyToManyField(
        'crm.MCast',
        related_name='booking',
        blank=True,
    )

    total_person = models.SmallIntegerField(
        _('予約人数'),
        default=1,
    )

    cancel_flg = models.BooleanField(
        _('キャンセルフラグ'),
        default=False,
    )

    # キャンセル時刻
    cancel_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    seat = models.ForeignKey(
        'crm.MSeat',
        on_delete=models.CASCADE,
        related_name='booking',
        null=True,
        blank=True,
    )

    def __str__(self):
        start = self.booking_start.strftime('%Y年%m月%d日 %H時%M分')
        end = self.booking_end.strftime('%H時%M分') if self.booking_end != None else ''
        return self.customer.name + '様 ' + start + '~' + end

    class Meta:
        verbose_name_plural = '予約管理テーブル'


# class AttendanceManagement(AbstractBaseModel):
#     """
#     勤怠管理テーブル
#     """
#     cast = models.ForeignKey(
#         'crm.MCast',
#         on_delete=models.CASCADE,
#         related_name='attendance',
#     )
#
#     start = models.DateTimeField(
#         _('勤務開始時間'),
#     )
#
#     end = models.DateTimeField(
#         _('勤務終了時間'),
#         null=True,
#         blank=True,
#     )
#
#     late_flg = models.BooleanField(
#         _('遅刻フラグ'),
#         default=False,
#     )
#
#     # 4桁文字数
#     late_time = models.CharField(_('遅刻時間'), max_length=10, null=True, blank=True)
#
#     attend_flg = models.BooleanField(
#         _('出勤フラグ'),
#         default=False,
#     )
#
#     absent_flg = models.BooleanField(
#         _('欠勤フラグ'),
#         default=False,
#     )
#
#     def __str__(self):
#         attend = '〇' if self.attend_flg else '×'
#         return self.cast.name + ' ' + self.date.strftime('%Y年%m月%d日') + '→' + attend
#
#     class Meta:
#         verbose_name_plural = '勤怠管理テーブル'
#         indexes = [
#             models.Index(fields=['cast'], name='attendance_cast_idx'),
#         ]
