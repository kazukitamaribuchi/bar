from rest_framework import serializers
from django.db.models import Q


from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MProductCategory,
    MSeat,
    MSetting,
    MPayment,
    MService,
    # MQuestion,
)

from .sub_models import (
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    SalesServiceDetail,
    # SalesAppointDetail,
    # AttendanceManagement,
    BookingManagement,
    # QuestionAnswer,
)

from .utils import (
    utc_to_jst,
    users_card,
    other_users_card,
    get_card_user,
    get_val_in_validated_data,
)

from datetime import (
    timezone,
    datetime,
    timedelta
)

from django.db import (
    models
)

from django.db.models.functions import Coalesce


import logging
import pytz


logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')


logger = logging.getLogger(__name__)




class DatetimeMixin:

    def get_created_at(self, obj):
        if obj.created_at == None:
            return ''
        return utc_to_jst(obj.created_at).strftime('%Y/%m/%d %H:%M')

    def get_updated_at(self, obj):
        if obj.updated_at == None:
            return ''
        return utc_to_jst(obj.updated_at).strftime('%Y/%m/%d %H:%M')




class DynamicFieldsModelSerializer(serializers.ModelSerializer, DatetimeMixin):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)




class CardSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CardManagement
        fields = [
            'customer_no',
            'total_point',
            'lost_flg',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

class RankSerializer(DynamicFieldsModelSerializer):

    # customer = serializers.StringRelatedField(many=True)
    customer = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = MRank
        fields = [
            'id',
            'rank_id',
            'rank_name',
            'customer'
        ]


class CustomerSerializer(DynamicFieldsModelSerializer):

    # card = CardSerializer()
    first_visit = serializers.SerializerMethodField(allow_null=True)
    birthday = serializers.SerializerMethodField(allow_null=True)
    birthday_str = serializers.CharField(write_only=True, allow_blank=True, allow_null=True)
    job = serializers.CharField(default='', allow_null=True)
    mail = serializers.EmailField(default='', allow_null=True)
    phone = serializers.CharField(default='', allow_null=True)
    company = serializers.CharField(default='', allow_null=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    # total_visit = serializers.IntegerField(default=0, allow_null=True)
    # total_sales = serializers.IntegerField(default=0, allow_null=True)
    total_visit = serializers.SerializerMethodField(allow_null=True)
    total_sales = serializers.SerializerMethodField(allow_null=True)
    customer_no = serializers.IntegerField(source='card.customer_no', allow_null=True)
    delete_flg = serializers.BooleanField(default=False)
    caution_flg = serializers.BooleanField(default=False)
    is_caution = serializers.SerializerMethodField()
    remarks = serializers.CharField(default='', allow_null=True)

    # 2022/6/20 ボトル機能追加⇒create, update確認
    bottle = serializers.SerializerMethodField(read_only=True, allow_null=True)

    rank_id = serializers.IntegerField(source='rank.rank_id', allow_null=True)
    rank_name = serializers.CharField(
        source='rank.rank_name',
        read_only=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MCustomer
        fields = [
            'id',
            'name',
            'name_kana',
            'age',
            'birthday',
            'birthday_str',
            'job',
            'mail',
            'phone',
            'company',
            'address',
            'rank_id',
            'rank_name',
            'remarks',
            # 'card',
            'first_visit',
            'total_visit',
            'total_sales',
            'caution_flg',
            'is_caution',
            'created_at',
            'updated_at',
            'delete_flg',
            'customer_no',
            'bottle',
        ]

    def get_first_visit(self, obj):
        # if obj.first_visit == None:
        #     return ''
        # return obj.first_visit.strftime('%Y/%m/%d')
        sales_data = SalesHeader.objects.filter(
            Q(customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(customer=obj) &
            Q(close_flg=True)
        )
        if len(sales_data) != 0:
            return sales_data.order_by('visit_time').first().visit_time.strftime('%Y/%m/%d')
        else:
            return '-'

    def get_birthday(self, obj):
        if obj.birthday == None:
            return '-'
        return obj.birthday.strftime('%Y/%m/%d')

    def get_job(self, obj):
        if obj.job == None:
            return ''
        return obj.job

    def get_phone(self, obj):
        if obj.phone == None:
            return ''
        return obj.phone

    def get_mail(self, obj):
        if obj.mail == None:
            return ''
        return obj.mail

    def get_company(self, obj):
        if obj.company == None:
            return ''
        return obj.company

    def get_address(self, obj):
        if obj.address == None:
            return ''
        return obj.address

    def get_is_caution(self, obj):
        if obj.caution_flg:
            return '要注意'
        return '-'

    def get_bottle(self, obj):

        return BottleSerializer(
            obj.bottle_customer.filter(
                delete_flg=False,
                end_flg=False,
            ),
            fields=[
                'id',
                'product',
                'open_date',
                'end_flg',
                'waste_flg',
                'remarks',
            ],
            many=True,
        ).data

    def get_total_visit(self, obj):
        return SalesHeader.objects.filter(
            Q(customer__isnull=False) &
            Q(customer=obj) &
            Q(customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(close_flg=True)
        ).count()

    def get_total_sales(self, obj):
        return SalesHeader.objects.filter(
            Q(customer__isnull=False) &
            Q(customer=obj) &
            Q(customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(close_flg=True)
        ).aggregate(total=Coalesce(models.Sum('total_tax_sales'), 0))['total']

    def create(self, validated_data):
        logger.debug('★Serializerのcreate')
        logger.debug(validated_data)


        if users_card(validated_data['card']['customer_no']):
            return None

        try:
            rank = MRank.objects.get(
                rank_id = validated_data['rank']['rank_id']
            )
        except MRank.DoesNotExist:
            logger.error('存在しないランクIDです。')
            return None

        card, c_created = CardManagement.objects.get_or_create(
            customer_no = validated_data['card']['customer_no']
        )

        name = get_val_in_validated_data('name', validated_data)
        name_kana = get_val_in_validated_data('name_kana', validated_data)
        age = get_val_in_validated_data('age', validated_data)
        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != None else None
        job = get_val_in_validated_data('job', validated_data)
        mail = get_val_in_validated_data('mail', validated_data)
        phone = get_val_in_validated_data('phone', validated_data)
        company = get_val_in_validated_data('company', validated_data)
        caution_flg = get_val_in_validated_data('caution_flg', validated_data)
        remarks = get_val_in_validated_data('remarks', validated_data)

        customer = MCustomer.objects.create(
            name=name,
            name_kana=name_kana,
            age=age,
            birthday=birthday,
            job=job,
            mail=mail,
            phone=phone,
            company=company,
            caution_flg=caution_flg,
            remarks=remarks,
            rank=rank,
            card=card,
        )

        return customer

    def update(self, instance, validated_data):
        logger.debug('★Serializerのupdate')
        logger.debug(instance)
        logger.debug(validated_data)

        card_user = get_card_user(validated_data['card']['customer_no'])
        if card_user != None and card_user != instance:
            logger.debug(card_user)
            logger.debug(instance)
            logger.error('既に他のユーザーと紐づいているカードです。')
            return None

        try:
            rank = MRank.objects.get(
                rank_id = validated_data['rank']['rank_id']
            )
        except MRank.DoesNotExist:
            logger.error('存在しないランクIDです。')
            return None

        card, c_created = CardManagement.objects.get_or_create(
            customer_no = validated_data['card']['customer_no']
        )

        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        logger.debug(birthday_str)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != None else None
        job = get_val_in_validated_data('job', validated_data)
        mail = get_val_in_validated_data('mail', validated_data)
        phone = get_val_in_validated_data('phone', validated_data)
        company = get_val_in_validated_data('company', validated_data)
        remarks = get_val_in_validated_data('remarks', validated_data)
        caution_flg = get_val_in_validated_data('caution_flg', validated_data)

        instance.card = card
        instance.name = validated_data['name']
        instance.name_kana = validated_data['name_kana']
        instance.rank = rank
        instance.age = validated_data['age']
        instance.birthday = birthday
        instance.job = job
        instance.mail = mail
        instance.phone = phone
        instance.company = company
        instance.caution_flg = caution_flg
        instance.remarks = remarks
        instance.save()
        return instance


class CustomerSubSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = MCustomer
        fields = [
            'id',
            'name',
        ]



class CastSerializer(DynamicFieldsModelSerializer):


    mail = serializers.EmailField(default='', allow_null=True)
    phone = serializers.CharField(default='', allow_null=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    birthday = serializers.SerializerMethodField(allow_null=True)
    birthday_str = serializers.CharField(write_only=True, allow_blank=True, allow_null=True)
    start_working_date = serializers.SerializerMethodField(allow_null=True)
    start_working_date_str = serializers.CharField(write_only=True, allow_blank=True, allow_null=True)
    resign_date = serializers.SerializerMethodField(allow_null=True)
    resign_date_str = serializers.CharField(write_only=True, allow_blank=True, allow_null=True)
    age = serializers.IntegerField(allow_null=True)
    real_age = serializers.IntegerField(allow_null=True)
    mail = serializers.EmailField(allow_null=True)
    phone = serializers.IntegerField(allow_null=True)
    remarks = serializers.CharField(allow_null=True, allow_blank=True)

    delete_flg = serializers.BooleanField(default=False)
    remarks = serializers.CharField(default='', allow_null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MCast
        fields = [
            'id',
            'name',
            'name_kana',
            'age',
            'icon',
            'real_name',
            'real_name_kana',
            'real_age',
            'birthday',
            'birthday_str',
            'address',
            'start_working_date',
            'start_working_date_str',
            'total_appoint',
            'resign_flg',
            'resign_date',
            'resign_date_str',
            'salary',
            'created_at',
            'updated_at',
            'delete_flg',
            'mail',
            'phone',
            'experienced',
            'remarks',
        ]

    def get_birthday(self, obj):
        if obj.birthday == None:
            return ''
        return obj.birthday.strftime('%Y/%m/%d')

    def get_start_working_date(self, obj):
        if obj.start_working_date == None:
            return ''
        return obj.start_working_date.strftime('%Y/%m/%d')

    def get_resign_date(self, obj):
        if obj.resign_date == None:
            return ''
        return obj.resign_date.strftime('%Y/%m/%d')


    def create(self, validated_data):
        logger.debug('★Serializerのcreate')
        logger.debug(validated_data)

        name = get_val_in_validated_data('name', validated_data)
        name_kana = get_val_in_validated_data('name_kana', validated_data)
        real_name = get_val_in_validated_data('real_name', validated_data)
        real_name_kana = get_val_in_validated_data('real_name_kana', validated_data)
        age = get_val_in_validated_data('age', validated_data)
        real_age = get_val_in_validated_data('real_age', validated_data)
        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != None else None
        # icon = get_val_in_validated_data('birthday_str', validated_data)
        experienced = get_val_in_validated_data('experienced', validated_data)
        mail = get_val_in_validated_data('mail', validated_data)
        phone = get_val_in_validated_data('phone', validated_data)
        resign_flg = get_val_in_validated_data('resign_flg', validated_data)
        resign_date_str = get_val_in_validated_data('resign_date_str', validated_data)
        resign_date = datetime.strptime(resign_date_str, '%Y/%m/%d') if resign_date_str != None else None
        start_working_date_str =  get_val_in_validated_data('start_working_date_str', validated_data)
        start_working_date = datetime.strptime(start_working_date_str, '%Y/%m/%d') if start_working_date_str != None else None
        address = get_val_in_validated_data('address', validated_data)
        remarks = get_val_in_validated_data('remarks', validated_data)

        cast = MCast.objects.create(
            name=name,
            name_kana=name_kana,
            real_name=real_name,
            real_name_kana=real_name_kana,
            age=age,
            real_age=real_age,
            birthday=birthday,
            # icon=icon,
            experienced=experienced,
            mail=mail,
            phone=phone,
            resign_flg=resign_flg,
            resign_date=resign_date,
            start_working_date=start_working_date,
            remarks=remarks,
            address=address,
        )

        return cast

    def update(self, instance, validated_data):
        logger.debug('★Serializerのupdate')
        logger.debug(instance)
        logger.debug(validated_data)

        name = get_val_in_validated_data('name', validated_data)
        name_kana = get_val_in_validated_data('name_kana', validated_data)
        real_name = get_val_in_validated_data('real_name', validated_data)
        real_name_kana = get_val_in_validated_data('real_name_kana', validated_data)
        age = get_val_in_validated_data('age', validated_data)
        real_age = get_val_in_validated_data('real_age', validated_data)
        birthday_str = get_val_in_validated_data('birthday_str', validated_data)
        birthday = datetime.strptime(birthday_str, '%Y/%m/%d') if birthday_str != None else None

        experienced = get_val_in_validated_data('experienced', validated_data)
        mail = get_val_in_validated_data('mail', validated_data)
        phone = get_val_in_validated_data('phone', validated_data)
        resign_flg = get_val_in_validated_data('resign_flg', validated_data)
        resign_date_str = get_val_in_validated_data('resign_date_str', validated_data)
        resign_date = datetime.strptime(resign_date_str, '%Y/%m/%d') if resign_date_str != None else None
        start_working_date_str =  get_val_in_validated_data('start_working_date_str', validated_data)
        start_working_date = datetime.strptime(start_working_date_str, '%Y/%m/%d') if start_working_date_str != None else None
        address = get_val_in_validated_data('address', validated_data)
        remarks = get_val_in_validated_data('remarks', validated_data)

        instance.name = name
        instance.name_kana = name_kana
        instance.real_name = real_name
        instance.real_name_kana = real_name_kana
        instance.age = age
        instance.real_age = real_age
        instance.birthday = birthday
        # instance.icon=icon,
        instance.experienced = experienced
        instance.mail = mail
        instance.phone = phone
        instance.resign_flg = resign_flg
        instance.resign_date = resign_date
        instance.start_working_date = start_working_date
        instance.address = address
        instance.remarks = remarks
        instance.save()
        return instance



class CastSubSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = MCast
        fields = [
            'id',
            'name',
        ]



class TaxSerializer(DynamicFieldsModelSerializer):

    product = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = MTax
        fields = [
            'id',
            'tax_rate',
            'product',
        ]


# class QuestionSerializer(DynamicFieldsModelSerializer):
#
#     value = serializers.IntegerField(read_only=True, source='id')
#     text = serializers.CharField(read_only=True, source='question')
#
#     class Meta:
#         model = MQuestion
#         fields = [
#             # 'id',
#             # 'question',
#             'value',
#             'text'
#         ]


class ProductCategorySerializer(DynamicFieldsModelSerializer):

    LARGE_CATEGORIES = {
        # 0: '基本料金',
        1: '飲料',
        2: 'フード'
    }

    CATEGORIES = {
        # 0: {
        #     0: '基本料金',
        #     1: '指名料',
        #     2: '場内指名料',
        #     3: 'VIP料金',
        #     4: '同伴料金',
        # },
        1: {
            0: [
                'アルコール',
                {
                    0: 'シャンパン1',
                    # 1: 'シャンパン2',
                    1: 'ウイスキー',
                    2: '焼酎',
                    3: 'ワイン',
                    4: 'ドリンク',
                },
            ],
            1: 'ノンアルコール',
            2: 'ソフトドリンク',
        },
        2: {
            0: 'メイン',
            1: 'サラダ',
            2: '一品物',
            3: '揚げ物',
            4: '吸い物、御飯物',
        }
    }

    large_category_label = serializers.SerializerMethodField()
    middle_category_label = serializers.SerializerMethodField()
    small_category_label = serializers.SerializerMethodField()

    class Meta:
        model = MProductCategory
        fields = [
            'id',
            'large_category',
            'middle_category',
            'small_category',
            'large_category_label',
            'middle_category_label',
            'small_category_label',
        ]

    def get_large_category_label(self, obj):
        return self.LARGE_CATEGORIES[obj.large_category]

    def get_middle_category_label(self, obj):
        # logger.debug('large' + str(obj.large_category))
        # logger.debug('middle' + str(obj.middle_category))
        # logger.debug('small' + str(obj.small_category))
        if obj.large_category == 1 and obj.middle_category == 0:
            return self.CATEGORIES[obj.large_category][obj.middle_category][0]
        return self.CATEGORIES[obj.large_category][obj.middle_category]

    def get_small_category_label(self, obj):
        if obj.large_category == 1 and obj.middle_category == 0:
            return self.CATEGORIES[obj.large_category][obj.middle_category][1][obj.small_category]
        return 'なし'


class ProductSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    category = ProductCategorySerializer()
    tax = TaxSerializer(fields=['id', 'tax_rate'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MProduct
        fields = [
            'id',
            'name',
            'name_kana',
            'filter_key',
            'price',
            'category',
            'tax',
            # 'tax_price',
            'created_at',
            'updated_at',
            'delete_flg',
            'thumbnail',
        ]


class ServiceSerializer(DynamicFieldsModelSerializer):

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    tax = TaxSerializer(fields=['id', 'tax_rate'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MService
        fields = [
            'id',
            'name',
            'price',
            # 'basic_plan_type',
            'large_category',
            'middle_category',
            'small_category',

            'tax',
            # 'tax_price',
            'created_at',
            'updated_at',
            'delete_flg',
        ]


class SeatSerializer(DynamicFieldsModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MSeat
        fields = [
            'id',
            'seat_type',
            'seat_name',
            'limit',
        ]



class SettingSerializer(DynamicFieldsModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MSetting
        fields = [
            'id',
            'sales_separate_time',
        ]



class BottleSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer(
        fields=[
            'id',
            'name',
            'customer_no',
        ]
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    deadline = serializers.SerializerMethodField()
    open_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()
    customer_type = serializers.SerializerMethodField()

    # b-tableで区分によって表示する方法分からんからここで渡す 2022/06/25
    # ➡filterがオブジェクトだといけない模様。正規表現だから文字列か数字のみか？
    # そのため多少冗長だがname, noなどそのまま渡す・・・
    customer_no = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    customer_name_kana = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product = ProductSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BottleManagement
        fields = [
            'id',
            'product',
            'customer',
            'deadline',
            'open_date',
            'end_date',
            'end_flg',
            'waste_flg',
            'created_at',
            'updated_at',
            'delete_flg',
            'non_member_name',
            'customer_type',
            'customer_no',
            'customer_name',
            'customer_name_kana',
            'remarks',
            'product_name'
        ]

    def get_deadline(self, obj):
        if obj.deadline == None:
            return ''
        return utc_to_jst(obj.deadline).strftime('%Y/%m/%d')

    def get_open_date(self, obj):
        if obj.open_date == None:
            return ''
        return utc_to_jst(obj.open_date).strftime('%Y/%m/%d')

    def get_end_date(self, obj):
        if obj.end_date == None:
            return ''
        return utc_to_jst(obj.end_date).strftime('%Y/%m/%d')

    def get_customer_type(self, obj):
        if (obj.customer == None):
            return 0
        return 1

    def get_customer_name(self, obj):
        if (obj.customer == None):
            return obj.non_member_name
        return obj.customer.name

    def get_customer_name_kana(self, obj):
        if (obj.customer == None):
            return obj.non_member_name
        return obj.customer.name_kana

    def get_customer_no(self, obj):
        if (obj.customer == None):
            return '-'
        return obj.customer.card.customer_no

    def get_product_name(self, obj):
        return obj.product.name



class SalesDetailSerializer(DynamicFieldsModelSerializer):

    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    order_time = serializers.SerializerMethodField()
    disp_seat_name = serializers.SerializerMethodField()
    header = serializers.SerializerMethodField()

    class Meta:
        model = SalesDetail
        fields = [
            'id',
            'product',
            'header',
            # 'cast',
            'quantity',
            'fixed_price',
            # 'fixed_tax_price',
            'total_price',
            # 'total_tax_price',
            'end_flg',
            'end_time',
            'order_time',
            'tax_free_flg',
            'disp_seat_name',
            'bottle_register',
        ]

    def get_header(self, obj):
        return SalesSerializer(
            obj.header,
            fields=[
                'id',
            ],
        ).data

    def get_total_price(self, obj):
        return obj.fixed_price * obj.quantity

    def get_end_time(self, obj):
        if obj.end_time == None:
            return '-'
        return utc_to_jst(obj.end_time).strftime('%Y/%m/%d %H:%M')

    def get_order_time(self, obj):
        if obj.order_time == None:
            return '-'
        return utc_to_jst(obj.order_time).strftime('%Y/%m/%d %H:%M')

    def get_disp_seat_name(self, obj):
        if obj.header.seat == None:
            return '席指定無し'
        return obj.header.seat.seat_name


class SubSalesDetailSerializer(DynamicFieldsModelSerializer):

    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()
    order_time = serializers.SerializerMethodField()
    disp_order_time = serializers.SerializerMethodField()
    seat = SeatSerializer(source='header.seat')
    header_id = serializers.SerializerMethodField()
    disp_seat_name = serializers.SerializerMethodField()
    header = serializers.SerializerMethodField()

    class Meta:
        model = SalesDetail
        fields = [
            'id',
            'product',
            # 'cast',
            'quantity',
            'fixed_price',
            # 'fixed_tax_price',
            'total_price',
            # 'total_tax_price',
            'end_flg',
            'order_time',
            'seat',
            'header_id',
            'header',
            'disp_order_time',
            'disp_seat_name',
            'tax_free_flg',
            'bottle_register',
        ]

    def get_header(self, obj):
        return SalesSerializer(
            obj.header,
            fields=[
                'id',
            ],
        ).data

    def get_total_price(self, obj):
        return obj.fixed_price * obj.quantity

    def get_order_time(self, obj):
        return utc_to_jst(obj.order_time).strftime('%Y/%m/%d %H:%M')

    def get_disp_order_time(self, obj):
        return utc_to_jst(obj.order_time).strftime('%H:%M')

    def get_header_id(self, obj):
        return str(obj.header.id).zfill(8)

    def get_disp_seat_name(self, obj):
        if obj.header.seat == None:
            return '席指定無し'
        return obj.header.seat.seat_name


class SalesServiceDetailSerializer(DynamicFieldsModelSerializer):

    service = ServiceSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = SalesServiceDetail
        fields = [
            'id',
            'service',
            # 'cast',
            'quantity',
            'discount_flg',
            'fixed_price',
            # 'fixed_tax_price',
            'total_price',
            # 'total_tax_price',
        ]

    def get_total_price(self, obj):
        return obj.fixed_price * obj.quantity

# class SalesAppointDetailSerializer(DynamicFieldsModelSerializer):
#
#     service = ServiceSerializer()
#     cast = CastSerializer()
#
#     class Meta:
#         model = SalesDetail
#         fields = [
#             'id',
#             'service',
#             'cast',
#             'quantity',
#             'fixed_price',
#             'fixed_tax_price',
#             'total_price',
#             'total_tax_price',
#         ]

class SalesSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    basic_plan_type = ServiceSerializer()
    seat = SeatSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    sales_detail = serializers.SerializerMethodField()
    # sales_appoint_detail = serializers.SerializerMethodField()
    sales_service_detail = serializers.SerializerMethodField()
    total_visitors = serializers.SerializerMethodField()
    visit_time = serializers.SerializerMethodField()
    leave_time = serializers.SerializerMethodField()
    header_id = serializers.SerializerMethodField()
    disp_seat_name = serializers.SerializerMethodField()
    account_date = serializers.SerializerMethodField()
    stay_hour = serializers.SerializerMethodField()
    # move_time = serializers.SerializerMethodField()
    sales_detail_total_price = serializers.SerializerMethodField()
    # sales_detail_total_tax_price = serializers.SerializerMethodField()
    # sales_appoint_detail_total_price = serializers.SerializerMethodField()
    # sales_appoint_detail_total_tax_price = serializers.SerializerMethodField()
    sales_service_detail_total_price = serializers.SerializerMethodField()
    # sales_service_detail_total_tax_price = serializers.SerializerMethodField()
    customer_no = serializers.CharField(source="customer.card", allow_null=True, allow_blank=True)
    customer_name = serializers.CharField(source="customer.name", allow_null=True, allow_blank=True)
    customer_name_kana = serializers.CharField(source="customer.name_kana", allow_null=True, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = SalesHeader
        fields = [
            'id',
            'customer',

            # ↓b-tableの検索用・・・
            'customer_no',
            'customer_name',
            'customer_name_kana',


            # 'total_visitors',
            'male_visitors',
            'female_visitors',
            'total_visitors',
            # 'move_diff_seat',
            'account_date',
            'visit_time',
            'leave_time',
            # 'move_time',
            'payment',
            # 'appoint',
            # 'douhan',
            # 'is_charterd',
            # 'tax_rate',
            'booking',
            'basic_plan_type',
            'stay_hour',
            # 'stay_hour_other',
            # 'total_stay_hour',
            'total_sales',
            'total_tax_sales',
            'created_at',
            'updated_at',
            'delete_flg',
            'sales_detail',
            # 'sales_appoint_detail',
            'sales_service_detail',
            'sales_detail_total_price',
            # 'sales_detail_total_tax_price',
            # 'sales_appoint_detail_total_price',
            # 'sales_appoint_detail_total_tax_price',
            'sales_service_detail_total_price',
            # 'sales_service_detail_total_tax_price',
            'remarks',
            'close_flg',
            'seat',
            'header_id',
            'disp_seat_name',
            'basic_plan_service_tax',
            'basic_plan_tax',
            'basic_plan_card_tax',
        ]

    def get_sales_detail(self, obj):
        return SalesDetailSerializer(
            SalesDetail.objects.filter(header=obj),
            many=True
        ).data

    # def get_sales_appoint_detail(self, obj):
    #     return SalesAppointDetailSerializer(
    #         SalesAppointDetail.objects.filter(header=obj),
    #         many=True
    #     ).data

    def get_sales_service_detail(self, obj):
        return SalesServiceDetailSerializer(
            SalesServiceDetail.objects.filter(header=obj),
            many=True
        ).data

    # def get_account_date(self, obj):
    #     if obj.account_date == None:
    #         return ''
    #     return utc_to_jst(obj.account_date).strftime('%Y/%m/%d')

    def get_account_date(self, obj):
        if obj.visit_time == None:
            return ''
        return utc_to_jst(obj.visit_time).strftime('%Y/%m/%d')

    def get_visit_time(self, obj):
        if obj.visit_time == None:
            return ''
        return utc_to_jst(obj.visit_time).strftime('%Y/%m/%d %H:%M')

    def get_leave_time(self, obj):
        if obj.leave_time == None:
            return ''
        return utc_to_jst(obj.leave_time).strftime('%Y/%m/%d %H:%M')

    # どうする？
    def get_stay_hour(self, obj):
        if obj.visit_time == None or obj.leave_time == None:
            return 0
        return 0

    # def get_move_time(self, obj):
    #     if obj.move_time == None:
    #         return ''
    #     return utc_to_jst(obj.move_time).strftime('%Y/%m/%d %H:%M')

    def get_sales_detail_total_price(self, obj):
        return obj.sales_detail.all().aggregate(models.Sum('fixed_price', field="fixed_price*quantity"))['fixed_price__sum']

    # def get_sales_detail_total_tax_price(self, obj):
    #     return obj.sales_detail.all().aggregate(models.Sum('total_tax_price'))['total_tax_price__sum']

    # def get_sales_appoint_detail_total_price(self, obj):
    #     return obj.sales_appoint_detail.all().aggregate(models.Sum('total_price'))['total_price__sum']

    # def get_sales_appoint_detail_total_tax_price(self, obj):
    #     return obj.sales_appoint_detail.all().aggregate(models.Sum('total_tax_price'))['total_tax_price__sum']

    def get_sales_service_detail_total_price(self, obj):
        return obj.sales_service_detail.all().aggregate(models.Sum('fixed_price', field="fixed_price*quantity"))['fixed_price__sum']

    # def get_sales_service_detail_total_tax_price(self, obj):
    #     return obj.sales_service_detail.all().aggregate(models.Sum('total_tax_price'))['total_tax_price__sum']

    def get_total_visitors(self, obj):
        return obj.male_visitors + obj.female_visitors

    def get_header_id(self, obj):
        return str(obj.id).zfill(8)

    def get_disp_seat_name(self, obj):
        if obj.seat == None:
            return '席指定無し'
        return obj.seat.seat_name

class CustomerSalesSerializer(serializers.Serializer):

    customer = serializers.SerializerMethodField()
    total = serializers.IntegerField(default=0)
    total_visit = serializers.IntegerField(default=0)

    def get_customer(self, obj):
        return CustomerSerializer(
            MCustomer.objects.get(pk=obj['customer']),
            fields=[
                'id',
                'name',
                'age',
                'rank_name',
                'customer_no',
            ]
        ).data


class ProductSalesSerializer(serializers.Serializer):

    sales_detail = serializers.SerializerMethodField()
    total = serializers.IntegerField()
    total_cnt = serializers.IntegerField()

    def get_sales_detail(self, obj):
        return ProductSerializer(MProduct.objects.get(pk=obj['sales_detail__product'])).data


# class AttendanceSerializer(DynamicFieldsModelSerializer):
#
#     cast = CastSerializer()
#     start = serializers.SerializerMethodField()
#     end = serializers.SerializerMethodField()
#     created_at = serializers.SerializerMethodField()
#     updated_at = serializers.SerializerMethodField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = AttendanceManagement
#         fields = [
#             'id',
#             'cast',
#             'attend_flg',
#             'start',
#             'end',
#             'absent_flg',
#             'late_flg',
#             'created_at',
#             'updated_at',
#             'delete_flg',
#         ]
#
#
#     def get_start(self, obj):
#         if obj.start == None:
#             return ''
#         return utc_to_jst(obj.start).strftime('%Y/%m/%d %H:%M')
#
#     def get_end(self, obj):
#         if obj.end == None:
#             return ''
#         return utc_to_jst(obj.end).strftime('%Y/%m/%d %H:%M')


class BookingSerializer(DynamicFieldsModelSerializer):

    customer = CustomerSerializer()
    cast = CastSerializer(many=True)
    register_date = serializers.SerializerMethodField()
    booking_start = serializers.SerializerMethodField()
    booking_end = serializers.SerializerMethodField()
    seat = SeatSerializer()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = BookingManagement
        fields = [
            'id',
            'customer',
            'cast',
            'total_person',
            'register_date',
            'booking_start',
            'booking_end',
            'cancel_flg',
            'seat',
            'created_at',
            'updated_at',
            'delete_flg',
        ]

    def get_register_date(self, obj):
        if obj.register_date == None:
            return ''
        return utc_to_jst(obj.register_date).strftime('%Y/%m/%d')

    def get_booking_start(self, obj):
        if obj.booking_start == None:
            return ''
        return utc_to_jst(obj.booking_start).strftime('%Y/%m/%d %H:%M')

    def get_booking_end(self, obj):
        if obj.booking_end == None:
            return ''
        return utc_to_jst(obj.booking_end).strftime('%Y/%m/%d %H:%M')
