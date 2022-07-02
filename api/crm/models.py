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
        2:シルバー
        3:ゴールド
        4:プラチナ
        5:ブラック
        ※将来的な拡張性も考えてテーブルで管理する
    """

    rank_id = models.SmallIntegerField(
        _('ランクid'),
    )

    rank_name = models.CharField(
        _('ランク名称'),
        max_length=20,
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
        ・アラート系の制御
        ・予約時間のペナルティ
        ・予約上限（グループ換算☞1席何人か。何人で2席にするかなど）
    """


class MProductCategory(AbstractBaseModel):
    """
    商品のカテゴリ
    　大カテゴリ
        0: 基本料金 #削除
        1: 飲料
        2: フード
    　中カテゴリ
        【0】 #削除
            「0」:基本料金・・・pk:1
            「1」:指名料・・・pk:2
            「2」:場内指名料・・・pk:3
            「3」:VIP料金・・・pk:4
            「4」:同伴料金・・・pk:5
        【1】
            「0」:アルコール・・・
            「1」:ノンアルコール・・・pk:13
            「2」:ソフトドリンク・・・pk:14
        【2】【?】
            「0」:メイン・・・pk:15
            「1」:サラダ・・・pk:16
            「2」:おかず・・・pk:17 => 前菜(20220609)
            「3」:おつまみ・・・pk:18 => 揚げ物(20220609)
            「4」:デザート・・・pk:19 => 吸い物、御飯物(20220609)
            「5」:

    　小カテゴリ
        →飲料[0]アルコール[0]のみ。

        【1】【0】【?】
            「0」:シャンパン・・・pk:6
            「1」:ワイン・・・pk:7 => ウイスキー(20220609)
            「2」:焼酎・・・pk:8
            「3」:サワー・・・pk:9 => ワイン(赤)(20220609)
            「4」:カクテル・・・pk:10 => ワイン(白)(20220609)
            「5」:日本酒・・・pk:11 => 顧客ドリンク(20220609)
            「6」:ビール・・・pk:12 => キャストドリンク(20220609)
            「7」:

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
        指名料金
        同伴料金
        延長料金
            type:
                0(基本)
                    0:A 20:30~21:30
                    1:B 21:30~22:30
                    2:C 22:30~LAST
                1(指名)
                    0:指名
                    1:本指名
                    2:場内指名
                2(同伴)
                    0:同伴
                3(延長)
                    0:延長
                4(席料金)
                    0:席料金 (VIPの場合 席料金1)
                    1:席料金 (VIPのみで 席料金2)

        2022/06/06 => VIPの場合SET料金無しで席料金のみ
　　　　　　　　　　　　⇒1~4人・・・1時間20000
　　　　　　　　　　　　⇒5人以上・・・2時間100000で貸し切りみたいな形になる

        start_tile, end_time = 21:00のようにコロン区切り4桁文字列

        将来的に指名でもNormal Vipの料金違いにも対応出来るように

    """
    basic_plan_type = models.SmallIntegerField(_('Normal or VIP'), default=0)

    large_category = models.SmallIntegerField(_('大カテゴリ'), default=0)
    middle_category = models.SmallIntegerField(_('中カテゴリ'), default=0)

    start_time = models.DateTimeField(_('開始時間'), null=True, blank=True)
    end_time = models.DateTimeField(_('終了時間'), null=True, blank=True)


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

    tax_price = models.SmallIntegerField(
        _('税込価格'),
    )

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

    tax_price = models.IntegerField(
        _('税込価格'),
    )

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
        return str(self.SEAT_TYPE_CHOICES[seat_type] + seat_name)

    def __str__(self):
        return self.show_str(self.seat_type, self.seat_name)

    class Meta:
        verbose_name_plural = '席マスタ'
