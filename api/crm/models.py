from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from .db.base import (
    AbstractBaseModel,
    AbstractHumanModel,
    AbstractServiceModel,
)
from .sub_models import (
    CardManagement,
)
import os
import uuid
import logging

logger = logging.getLogger(__name__)

# from django.db.models.signals import ModelSignal
#
# pre_bulk_create = ModelSignal(use_caching=True)
# post_bulk_create = ModelSignal(use_caching=True)
#
# class CreateManager(models.QuerySet):
#
#     def create(self, **kwargs):
#         pre_bulk_create.send(sender=self.model, queryset=self, update_kwargs=kwargs)
#         res = super(CreateManager, self).create(**kwargs)
#         post_bulk_create.send(sender=self.model, queryset=self, update_kwargs=kwargs)
#         return res


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Username is required field')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(username, email, password, **extra_fields)

class mUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('Username'), max_length=70, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=70, unique=True)

    description = models.TextField(_('Description'))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    is_staff = models.BooleanField(
        _('Staff Status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    is_active = models.BooleanField(
        _('Active Flag'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        verbose_name_plural = 'ユーザーマスタ'

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)




class MRank(models.Model):
    """
    顧客のランクマスタ
        1:ノーマル
        # 2:シルバー => 廃止
        2:ゴールド
        3:プラチナ
        4:ブラック
        ※将来的な拡張性も考えてテーブルで管理する
    """

    rank_id = models.SmallIntegerField(
        _('ランクid'),
    )

    rank_name = models.CharField(
        _('ランク名称'),
        max_length=20,
    )

    bottom_line_sales = models.IntegerField(
        _('売上ボトムライン'),
        default=0,
    )

    top_line_sales = models.IntegerField(
        _('売上トップライン'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.rank_name

    class Meta:
        verbose_name_plural = 'ランクマスタ'


class MTax(models.Model):
    """
    税区分（必要に応じて追加
    """
    TAX_CHOICES = (
        (0, _('非課税')),
        (8, _('8%')),
        (10, _('10%')),
        (15, _('15%')),
        (20, _('20%')),
        (30, _('30%')),
        (35, _('35%')),
    )

    tax_rate = models.SmallIntegerField(
        _('Price included Tax'),
        choices=TAX_CHOICES,
        default=35,
    )

    def __str__(self):
        return str(self.tax_rate) + '%'

    class Meta:
        verbose_name_plural = '税マスタ'


class MCustomer(AbstractHumanModel):
    """
    顧客マスタ
        総売り上げ
        総来店回数
        所属

        会員 ⇒ cardが紐づく
        非会員 ⇒ cardは紐づかない

    """
    job = models.CharField(
        _('職業'),
        null=True,
        blank=True,
        max_length=100,
    )
    mail = models.CharField(
        _('メールアドレス'),
        null=True,
        blank=True,
        max_length=200,
    )
    phone = models.CharField(
        _('電話'),
        null=True,
        blank=True,
        max_length=20,
    )
    company = models.CharField(
        _('会社'),
        null=True,
        blank=True,
        max_length=100,
    )
    # 2022/06/24 => ここで持つと更新が大変なため廃止。↓と同じくSalesHeaderから取得
    # total_visit = models.IntegerField(
    #     _('来店回数'),
    #     default=0,
    # )
    # 2022/06/06 => ここ持つと更新が大変なため廃止
    # total_sales = models.BigIntegerField(
    #     _('総売上'),
    #     default=0,
    # )
    first_visit = models.DateField(
        _('初来店日'),
        null=True,
        blank=True,
    )
    rank = models.ForeignKey(
        MRank,
        on_delete=models.PROTECT,
        related_name='customer',
    )
    card = models.OneToOneField(
        'crm.CardManagement',
        on_delete=models.PROTECT,
        related_name='customer',
        null=True,
        blank=True,
    )
    caution_flg = models.BooleanField(
        _('要注意人物フラグ'),
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '顧客マスタ'
        indexes = [
            models.Index(fields=['name'], name='mcustomer_name_idx'),
            models.Index(fields=['rank'], name='mcustomer_rank_idx'),
        ]


class MCast(AbstractHumanModel):
    """
    キャストマスタ
    """
    icon = models.ImageField(
        _('顔写真'),
        upload_to='upload/',
        null=True,
        blank=True,
    )
    real_name = models.CharField(
        _('本名'),
        max_length=100,
        null=True,
        blank=True,
    )
    real_name_kana = models.CharField(
        _('本名(フリガナ)'),
        max_length=150,
        null=True,
        blank=True,
    )
    real_age = models.SmallIntegerField(
        _('実年齢'),
        null=True,
        blank=True,
    )
    start_working_date = models.DateField(
        _('勤務開始日'),
        null=True,
        blank=True,
    )
    total_appoint = models.IntegerField(
        _('総指名数'),
        default=0,
    )
    resign_flg = models.BooleanField(
        _('退職フラグ'),
        default=False,
    )
    resign_date = models.DateTimeField(
        _('退職日時'),
        null=True,
        blank=True,
    )
    # 今後考える？・・・
    salary = models.IntegerField(
        _('時給'),
        null=True,
        blank=True,
        default=0,
    )

    mail = models.CharField(
        _('メールアドレス'),
        null=True,
        blank=True,
        max_length=200,
    )
    phone = models.CharField(
        _('電話'),
        null=True,
        blank=True,
        max_length=20,
    )
    experienced = models.BooleanField(
        _('経験者フラグ'),
        default=False,
    )

    # qa = models.ManyToManyField(
    #     'crm.QuestionAnswer',
    #     blank=True,
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'キャストマスタ'
        indexes = [
            models.Index(fields=['name'], name='mcast_name_idx')
        ]


class MSetting(AbstractBaseModel):
    """
    設定情報マスタ
        ・1日の区切り時間
    """

    sales_separate_time = models.CharField(
        _('売上の1日を何時始まりとするか'),
        max_length=4,
        default='1800',
    )



class MProductCategory(AbstractBaseModel):
    """
    商品のカテゴリ
    　大カテゴリ
        0: 基本料金 #削除
        1: 飲料
        2: フード
    　中カテゴリ
        【0】 #削除 => サービスに移行
            「0」:基本料金・・・pk:1
        【1】
            「0」:アルコール・・・
            「1」:ノンアルコール・・・pk:7
            「2」:ソフトドリンク・・・pk:8
        【2】【?】
            「0」:メイン・・・pk:9
            「1」:サラダ・・・pk:10
            「2」:一品物・・・pk:11
            「3」:揚げ物・・・pk:12
            「4」:吸い物、御飯物・・・pk:13

    　小カテゴリ
        【1】【0】【?】
            「0」:シャンパン1・・・pk:2
            「1」:ウイスキー・・・pk:3
            「2」:焼酎・・・pk:4
            「3」:ワイン・・・pk:5
            「4」:ドリンク・・・pk:6
    """

    large_category = models.SmallIntegerField(
        _('大カテゴリー'),
    )

    middle_category = models.SmallIntegerField(
        _('中カテゴリー'),
    )

    small_category = models.SmallIntegerField(
        _('小カテゴリー'),
        default=0,
    )

    def __str__(self):
        return str(self.large_category) + '-' + str(self.middle_category) + '-' + str(self.small_category)

    class Meta:
        verbose_name_plural = '商品カテゴリ'



class MPayment(AbstractBaseModel):
    """
    支払い方法マスタ
        現金:0
        カード:1
    """
    type = models.IntegerField(_('支払いタイプ'), default=0, primary_key=True)

    type_name = models.CharField(max_length=20)

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='payment',
    )





class MService(AbstractServiceModel):
    """
    サービス情報のマスタ
        基本料金
        延長料金
            type:
                0(基本)
                    0:通常
                    1:貸切
                1(延長)
                    0:延長（通常）
                    1:延長（貸切）

            large0, middle0 [0, 1, 2]
            large0, middle1 [0, 1, 2]
            large1, middle0 0
            large1, middle1 0

    """

    large_category = models.SmallIntegerField(_('大カテゴリ'), default=0)
    middle_category = models.SmallIntegerField(_('中カテゴリ'), default=0)
    small_category = models.SmallIntegerField(_('小カテゴリ'), default=0)


    description = models.TextField(
        _('説明'),
        null=True,
        blank=True,
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='basic_service',
    )

    # tax_price = models.SmallIntegerField(
    #     _('税込価格'),
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '基本料金マスタ'

# class MAppointService(AbstractServiceModel):
#     """
#     指名料金マスタ
#     """
#
#     # 一応・・・
#     thumbnail = models.ImageField(
#         _('サムネイル'),
#         upload_to='upload/',
#         null=True,
#         blank=True,
#     )
#
#     tax = models.ForeignKey(
#         MTax,
#         on_delete=models.PROTECT,
#         related_name='appoint_service',
#     )
#
#     tax_price = models.IntegerField(
#         _('税込価格'),
#     )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = '指名料金マスタ'


class MProduct(AbstractServiceModel):
    """
    商品マスタ
        商品名
        商品カテゴリ
        金額（税区分によって

        filter_key:
            0: ア
            1: カ
            2: サ
            3: タ
            4: ナ
            5: ハ
            6: マ
            7: ヤ
            8: ラ
            9: ワ
            10: 他
    """

    thumbnail = models.ImageField(
        _('サムネイル'),
        upload_to='upload/',
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        MProductCategory,
        on_delete=models.PROTECT,
        related_name='product'
    )

    tax = models.ForeignKey(
        MTax,
        on_delete=models.PROTECT,
        related_name='product',
    )

    # tax_price = models.IntegerField(
    #     _('税込価格'),
    # )

    like = models.BooleanField(
        _('お気に入り'),
        default=False,
    )

    # cast_price = models.SmallIntegerField(
    #     _('キャスト価格 => キャストが頼む際の料金')
    # )

    priority = models.SmallIntegerField(
        _('優先順位'),
        default=0,
    )

    filter_key= models.SmallIntegerField(
        _('フィルターのkey'),
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '商品マスタ'


# class MQuestion(AbstractBaseModel):
#     """
#     Questionマスタ
#     """
#     question = models.CharField(
#         _('質問内容'),
#         max_length=200,
#     )
#
#     def __str__(self):
#         return str(self.question)
#
#     class Meta:
#         verbose_name_plural = '質問マスタ'


class MSeat(models.Model):
    """
    座席マスタ
        予約と紐づけ
    """

    # SEAT_TYPE_CHOICES = (
    #     (0, _('VIP')),
    #     (1, _('Normal')),
    # )

    SEAT_TYPE_CHOICES = (
        (0, _('Counter')),
        (1, _('Table')),
    )

    seat_type = models.SmallIntegerField(
        _('座席種別'),
        choices=SEAT_TYPE_CHOICES,
    )

    seat_name = models.CharField(
        _('席名'),
        max_length=20,
    )

    limit = models.SmallIntegerField(
        _('上限人数'),
        default=1,
    )

    def show_str(self, type, no):
        # return str(self.SEAT_TYPE_CHOICES[seat_type] + seat_name)
        return self.seat_name

    def __str__(self):
        return self.show_str(self.seat_type, self.seat_name)

    class Meta:
        verbose_name_plural = '席マスタ'
