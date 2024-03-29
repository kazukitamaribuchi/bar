from rest_framework import (
    generics,
    permissions,
    authentication,
    status,
    viewsets,
    filters,
)

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction, models
from django.db.models import Sum, Q, CharField, F
from django.db.models.functions import (
    TruncMonth,
)

from django.db.models.functions import (
    Concat,
    # Lower,
)

from datetime import (
    datetime,
    timedelta,
)

from dateutil.relativedelta import relativedelta

from pytz import timezone

from .serializers import (
    CustomerSerializer,
    CastSerializer,
    RankSerializer,
    TaxSerializer,
    ProductSerializer,
    SeatSerializer,
    SettingSerializer,
    CardSerializer,
    BottleSerializer,
    SalesSerializer,
    SalesDetailSerializer,
    SubSalesDetailSerializer,
    # AttendanceSerializer,
    BookingSerializer,
    # QuestionSerializer,
    CustomerSalesSerializer,
    ProductSalesSerializer,
    ProductCategorySerializer,
)

from .models import (
    mUser,
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
    SalesPayment,
)

from .exceptions import (
    WrongUserException
)

from .utils import (
    utc_to_jst,
    users_card,
    update_customer_rank,
    get_setting,
    get_sales_separate_time,
)

from .filters import (
    CustomerFilter,
    BottleFilter,
)


from django.db.models.functions import Coalesce

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import copy
import logging

logger = logging.getLogger(__name__)

PRODUCT_CATEGORY = {
    # 基本料金は別で管理
    # 0: [0,1,2,3,4],

    1: {
        # アルコール
        0: [0,1,2,3,4],

        # ノンアル
        1: [0],

        # ソフトドリンク
        2: [0],
    },
    2: {
        # メイン
        0: [0],
        # サラダ
        1: [0],
        # 一品物
        2: [0],
        # 揚げ物
        3: [0],
        # 吸い物、御飯物
        4: [0],
        5: [0],
    }
}

# OPEN_HOUR = 20
# OPEN_MINUTE = 30
# CLOSE_HOUR = 7
# CLOSE_MINUTE = 0
OPEN_HOUR = 18
OPEN_MINUTE = 00
CLOSE_HOUR = 17
CLOSE_MINUTE = 59




class BaseModelViewSet(viewsets.ModelViewSet):
    """
    """

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        """
        共通で論理削除とする
        """

        logger.debug('★共通のDestroyですとろい')

        instance = self.get_object()
        instance.delete_flg = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class CustomerViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MCustomer.objects.all()
    serializer_class = CustomerSerializer
    filter_class = CustomerFilter

    def create(self, request, *args, **kwargs):
        """
        顧客作成
        　・必須項目
            custoner_no(CardManagement) => カードNoは渡したカードのNo

            name
            name_kana
            age
            birthday
            job
            company

            ※後は要望に応じて
        """

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(self.get_serializer(serializer.instance).data,
                status=status.HTTP_201_CREATED)

        logger.debug(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        logger.debug("★UPDATE")
        logger.debug(request.data)
        logger.debug(request.data['id'])

        queryset = self.queryset.get(pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        logger.debug(serializer)
        logger.debug(serializer.is_valid())
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # try:
        #     customer = MCustomer.objects.get(pk=request.data['id'])
        # except MCustomer.DoesNotExist:
        #     return
        #
        # # 会員Noが正しいか
        # # ・誰とも紐づいていない会員NoだったらOK。自分だったらそのまま
        #
        # customer_no = request.data['customer_no']
        #
        # try:
        #     card_user = MCustomer.objects.get(card__customer_no=customer_no)
        #     if card_user != customer:
        #         raise WrongUserException
        # except WrongUserException:
        #     logger.error('既に他のユーザーと紐づいているカードなのでNG')
        # except MCustomer.DoesNotExist:
        #     logger.debug('顧客情報が見つからないので新たに紐づけ直す')
        # else:
        #     logger.debug('会員Noはそのまま')
        #
        #
        #
        # # 該当会員Noを持った顧客の取得
        # #  MCustomer.objects.get(card__customer_no=1)
        # # 該当会員Noのカードを取得
        # #  CardManagement.objects.get(customer_no=1).customer
        #
        # # ★変わった項目のみ更新したい・・・
        # customer.name = request.data['name']
        # customer.name_kana = request.data['name_kana']
        # customer.age = request.data['age']
        # customer.birthday = datetime.strptime(request.data['birthday'], '%Y-%m-%d')
        # customer.job = request.data['job']
        # customer.company = request.data['company']
        # customer.age = request.data['age']
        # customer.age = request.data['age']
        # customer.save()
        #
        # return Response(self.get_serializer(customer).data, status=status.HTTP_200_OK)


    # def destroy(self, request, *args, **kwargs):
    #     logger.debug("★DELETE")
    #     logger.debug(request.data)
    #
    #     instance = self.get_object()
    #     logger.debug(instance)
    #
    #     instance.delete_flg = True
    #     instance.save()
    #     return Response(CustomerSerializer(instance).data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def update_customer_data(self, request):

        logger.debug('update_customer_data')
        logger.debug(request.data)

        id = request.data['id']
        name = request.data['name']
        name_kana = request.data['name_kana']
        age = request.data['age']
        birthday_str = request.data['birthday_str']
        job = request.data['job']
        mail = request.data['mail']
        phone = request.data['phone']
        company = request.data['company']
        customer_no = request.data['customer_no']
        caution_flg = request.data['caution_flg']
        remarks = request.data['remarks']
        try:
            customer = MCustomer.objects.get(pk=id)
        except MCustomer.DoesNotExist:
            return Response(status.status.HTTP_400_BAD_REQUEST)

        try:
            card = CardManagement.objects.get(customer_no=customer_no)
        except CardManagement.DoesNotExist:
            card = CardManagement.objects.create(
                customer_no=customer_no,
            )

        birthday = None
        if birthday_str != '' and birthday_str != None:
            birthday = datetime.strptime(birthday_str, '%Y/%m/%d').astimezone(timezone('Asia/Tokyo'))

        customer.name = name
        customer.name_kana = name_kana
        customer.age = age
        customer.birthday = birthday
        customer.job = job
        customer.mail = mail
        customer.phone = phone
        customer.company = company
        customer.caution_flg = caution_flg
        customer.remarks = remarks
        customer.card = card
        customer.save()

        return Response(CustomerSerializer(customer).data)



    @action(methods=['get'], detail=False)
    def get_all_customer(self, reuqest):

        customers = self.get_queryset().filter(
            delete_flg=False,
        ).order_by('-rank_id')

        res = {
            'customers': CustomerSerializer(customers, many=True).data,
            'count': customers.count(),
        }

        return Response(
            res,
            status=status.HTTP_200_OK
        )


    @action(methods=['post'], detail=False)
    def get_customer_no_duplicate(self, request):
        """
        顧客Noが重複していないかのチェック
        """
        logger.debug(request.data)
        logger.debug(request.query_params)
        customer_no = request.data['customer_no']

        if users_card(customer_no):
            return Response({
                'status': 'success',
                'result': False,
                'msg': '既に他のユーザーと紐づいているカードです'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'success', 'result': True}, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False)
    def get_customer_age(self, request):

        res = [
            MCustomer.objects.filter(age__gte=bottom*10+10, age__lte=top, delete_flg=False).count() for bottom, top in enumerate(range(19, 110, 10))
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False)
    def get_customer_rank(self, request):

        res = [
            MCustomer.objects.filter(rank=rank, delete_flg=False).count() for rank in range(1, 5)
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_customer_cnt(self, request):

        res = {
            'cnt': MCustomer.objects.filter(delete_flg=False).count()
        }

        return Response(res, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_active_customer_cnt(self, request):

        today = datetime.now(timezone('Asia/Tokyo'))

        customerCnt = MCustomer.objects.filter(delete_flg=False).count()

        # 期間指定は将来的にする？設定などで持つ？とりあえず2ヶ月でいいかな
        two_month_ago = today - relativedelta(months=2)

        logger.debug(SalesHeader.objects.filter(
            Q(delete_flg=False) &
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(close_flg=True) &
            Q(visit_time__range=[two_month_ago, today])
        ).values(
            # customer=Lower('sales_payment_sales_header__customer')
            customer=F('sales_payment_sales_header__customer') # 20221030検証up時lowerで落ちた・・・そもそもいらんかも
        ))

        activeCustomer = SalesHeader.objects.filter(
            Q(delete_flg=False) &
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(close_flg=True) &
            Q(visit_time__range=[two_month_ago, today])
        ).values(
            # customer=Lower('sales_payment_sales_header__customer')
            customer=F('sales_payment_sales_header__customer')
        ).annotate(
            cnt=models.Count(F('sales_payment_sales_header__customer'))
        ).order_by('-cnt')

        logger.debug('activeCustomer')
        logger.debug(activeCustomer)

        activeCustomerCnt = len(activeCustomer)
        nonActiveCustomerCnt = customerCnt - activeCustomerCnt

        res = {
            'totalCustomerCnt': customerCnt,
            'activeCustomerCnt': activeCustomerCnt,
            'nonActiveCustomerCnt': nonActiveCustomerCnt,
        }

        return Response(res, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def search_customer_by_customer_no(self, request):
        logger.debug('search_customer_by_customer_no')
        logger.debug(request.query_params)
        try:
            customer = MCustomer.objects.get(
                card__customer_no=request.query_params['customer_no'],
                delete_flg=False,
                # 削除されていたらどうする？
            )
            return Response({
                'status': 'success',
                'data': CustomerSerializer(customer).data,
            })
        except MCustomer.DoesNotExist:
            return Response({
                'status': 'failure',
                'msg': '該当の顧客は存在しません。'
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'failure',
            'data': '該当の顧客は存在しません。'
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def get_customer_exist(self, request):

        try:
            MCustomer.objects.get(pk=request.query_params['customer_id'])
            return Response({'status': 'success', 'data': True})
        except MCustomer.DoesNotExist:
            return Response({'status': 'success', 'data': False})

        return Response({'status': 'failure', 'data': None})

    @action(methods=['get'], detail=False)
    def search(self, request):

        logger.debug(request.query_params)
        queryset = self.filter_queryset(self.get_queryset())
        logger.debug('★')
        logger.debug(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True
            )
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(
            queryset,
            many=True
        )
        return Response(serializer.data)


class RankViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MRank.objects.all()
    serializer_class = RankSerializer


class TaxViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MTax.objects.all()
    serializer_class = TaxSerializer

# class QuestionViewSet(BaseModelViewSet):
#     """
#     """
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = MQuestion.objects.all()
#     serializer_class = QuestionSerializer


class CastViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MCast.objects.all()
    serializer_class = CastSerializer

    def create(self, request, *args, **kwargs):
        """
        キャスト作成
        　・必須項目
            name
            age

            ※後は要望に応じて
        """

        logger.debug('★キャスト作成')
        logger.debug(request.data)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(self.get_serializer(serializer.instance).data,
                status=status.HTTP_201_CREATED)

        logger.debug(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        logger.debug("★UPDATE")
        logger.debug(request.data)
        logger.debug(request.data['id'])

        queryset = self.queryset.get(pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        logger.debug(serializer)
        logger.debug(serializer.is_valid())
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def get_cast_avg_age(self, request):

        res = MCast.objects.aggregate(avg=models.Avg('age'))

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_cast_age(self, request):

        res = [
            MCast.objects.filter(age__lt=20).count(),
            MCast.objects.filter(age__gte=20, age__lt=25).count(),
            MCast.objects.filter(age__gte=25, age__lt=30).count(),
            MCast.objects.filter(age__gte=30, age__lt=35).count(),
            MCast.objects.filter(age__gte=35, age__lt=40).count(),
            MCast.objects.filter(age__gte=40).count(),
        ]

        return Response({'status': 'success', 'data': res}, status=status.HTTP_200_OK)



class ProductViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MProduct.objects.all()
    serializer_class = ProductSerializer


    @action(methods=['get'], detail=False)
    def get_product_by_category(self, request):
        """
        カテゴリ毎の商品を取得。
        マスタデータになるため、画面側のlocalStorageに持つ。
        """

        # res = {1:{}, 2:{}}
        # large = 0
        # middle = 0
        # small = 0
        # dict = {}
        # logger.debug('★★★★★★★★★★★★★★★★★★★★★★★★★★v★★★★★★★★★★★★★★★★★★★★★★★★★')
        # for item in MProductCategory.objects.all().order_by('large_category', 'middle_category', 'small_category').values():
        #     logger.debug(str(item['large_category']) + str(item['middle_category']) + str(large) + str(middle))
        #
        #     if large == item['large_category'] and middle == item['middle_category']:
        #         logger.debug('スキップ')
        #         continue
        #
        #     dict[item['middle_category']] = {}
        #
        #     large = item['large_category']
        #     middle = item['middle_category']


        res = {
            1: {
                0: {},
                1: {},
                2: {},
            },
            2: {
                0: {},
                1: {},
                2: {},
                3: {},
                4: {},
                5: {},
            },
        }

        logger.debug(res)

        for large, items in PRODUCT_CATEGORY.items():
            for middle in items:
                for small in items[middle]:
                    q = MProduct.objects.filter(Q(category__large_category=large), \
                        Q(category__middle_category=middle), \
                        Q(category__small_category=small)
                    )
                    data = ProductSerializer(q, many=True).data
                    # logger.debug('large=> ' + str(large) + ' middle=> ' + str(middle) + ' small=> ' + str(small))
                    res[large][middle][small] = data

        return Response(res, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_popular_product(self, request):
        """
        人気商品を取得
        　・明細追加時のトップに表示
            それぞれのタブ毎に表示するためなど

            トップ
            アルコール、ノンアルコール、ソフトドリンク
            メイン、サラダ、おかず、おつまみ、デザート
        """

        # 人気商品の算出ロジックは後で。とりあえず固定で

        try:
            res = MProduct.objects.filter(delete_flg=False)[:12]
            top = {
                0: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=0)[:12], many=True).data,
                1: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=1)[:12], many=True).data,
                2: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=2)[:12], many=True).data,
                3: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=0)[:12], many=True).data,
                4: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=1)[:12], many=True).data,
                5: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=2)[:12], many=True).data,
                6: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=3)[:12], many=True).data,
                7: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=4)[:12], many=True).data,
                8: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=5)[:12], many=True).data,
            }
            return Response({
                'status': 'success',
                'data': {
                    'popular': ProductSerializer(res, many=True).data,
                    'top': top,
                }
            }, status=status.HTTP_200_OK)
        except:
            import traceback
            traceback.print_exc()
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class SeatViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MSeat.objects.all()
    serializer_class = SeatSerializer


class SettingViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MSetting.objects.all()
    serializer_class = SettingSerializer


class CardViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = CardManagement.objects.all()
    serializer_class = CardSerializer


class BottleViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = BottleManagement.objects.all()
    serializer_class = BottleSerializer
    filter_class = BottleFilter

    # def update(self, request, pk=None):
    #     logger.debug('★UPDATE')
    #     logger.debug(request.data)
    #     logger.debug(request.data['id'])
    #
    #     queryset = self.queryset.get(pk=pk)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     logger.debug(serializer)
    #     logger.debug(serializer.is_valid())


    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete_flg = True
    #     instance.save()
    #     serializer = self.get_serializer(instance).data
    #     return Response(serializer, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_all_bottle(self, reuqest):
        """
        画面表示用の削除フラグを省いた全件ページング無で取得
        """

        bottle = self.get_queryset().filter(
            delete_flg=False,
        ).order_by(Concat('end_flg', 'end_date'), '-created_at')

        res = {
            'bottle': BottleSerializer(bottle, many=True).data,
            'count': bottle.count(),
        }

        return Response(
            res,
            status=status.HTTP_200_OK
        )

    @transaction.atomic
    @action(methods=['post'], detail=False)
    def create_bottle_data(self, request):
        logger.debug('★create_bottle_data')
        logger.debug(request.data)

        customer_type = request.data['customerType']
        customer_no = request.data['customerNo']

        # selected_bottle_list = request.data['selectedBottleList']
        selected_bottle = request.data['selectedBottle']
        remarks = request.data['remarks']

        # res = []
        # for item in selected_bottle_list:
        #     open_date_str = item['openDate']
        #     open_date = datetime.strptime(open_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))
        #
        #     try:
        #         product = MProduct.objects.get(pk=item['id'])
        #     except MProduct.DoesNotExist:
        #         return Response(status.status.HTTP_400_BAD_REQUEST)
        #
        #     if customer_type == 0:
        #         res.append(BottleManagement.objects.create(
        #             non_member_name=non_member_name,
        #             open_date=open_date,
        #             product=product,
        #         ))
        #
        #     elif customer_type == 1:
        #         try:
        #             customer = MCustomer.objects.get(card__customer_no=customer_no)
        #         except MCustomer.DoesNotExist:
        #             return Response(status.status.HTTP_400_BAD_REQUEST)
        #
        #         res.append(BottleManagement.objects.create(
        #             customer=customer,
        #             open_date=open_date,
        #             product=product,
        #         ))

        open_date = datetime.now(timezone('Asia/Tokyo'))

        open_date_str = request.data['openDate']

        if open_date_str != '' and open_date_str != None:
            open_date = datetime.strptime(open_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))

        try:
            product = MProduct.objects.get(pk=selected_bottle['id'])
        except MProduct.DoesNotExist:
            return Response(status.status.HTTP_400_BAD_REQUEST)


        if customer_type == 0:
            non_member_name = request.data['nonMemberName']

            res = BottleManagement.objects.create(
            non_member_name=non_member_name,
            open_date=open_date,
            product=product,
        )

        elif customer_type == 1:
            try:
                customer = MCustomer.objects.get(card__customer_no=customer_no)
            except MCustomer.DoesNotExist:
                return Response(status.status.HTTP_400_BAD_REQUEST)

            res = BottleManagement.objects.create(
                customer=customer,
                open_date=open_date,
                product=product,
                remarks=remarks,
            )

        # return Response({
        #     'status': 'success',
        #     'data': BottleSerializer(res, many=True).data
        # }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'success',
            'data': BottleSerializer(res).data
        }, status=status.HTTP_201_CREATED)


    @action(methods=['put'], detail=False)
    def update_bottle_data(self, request):

        logger.debug('update_bottle_data')
        logger.debug(request.data)

        customer_type = request.data['customerType']
        customer_no = request.data['customerNo']
        non_member_name = request.data['nonMemberName']

        selected_bottle = request.data['selectedBottle']
        id = request.data['id']
        open_date_str = request.data['openDate']
        open_date = datetime.strptime(open_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))
        try:
            product = MProduct.objects.get(pk=selected_bottle['id'])
        except MProduct.DoesNotExist:
            return Response(status.status.HTTP_400_BAD_REQUEST)

        try:
            instance = BottleManagement.objects.get(id=id)
        except BottleManagement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if instance.end_flg and instance.end_date < instance.open_date:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if customer_type == 0:
            instance.customer=None
            instance.non_member_name=non_member_name

        elif customer_type == 1:
            try:
                customer = MCustomer.objects.get(card__customer_no=customer_no)
            except MCustomer.DoesNotExist:
                return Response(status.status.HTTP_400_BAD_REQUEST)
            instance.non_member_name=None
            instance.customer=customer

        instance.open_date=open_date
        instance.product=product
        instance.save()

        return Response({
            'status': 'success',
            'data': BottleSerializer(instance).data
        },status=status.HTTP_200_OK)


    @action(methods=['put'], detail=False)
    def end_bottle_data(self, request):

        id = request.data['id']
        try:
            instance = BottleManagement.objects.get(id=id)
        except BottleManagement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if instance.end_flg:
            # 空き状態から基に戻す
            instance.end_date = None
        else:
            # 空き状態に更新
            end_date = datetime.now(timezone('Asia/Tokyo'))
            end_date_str = request.data['endDate']
            if end_date_str != '' and end_date_str != None:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').astimezone(timezone('Asia/Tokyo'))

            instance.end_date = end_date

        instance.end_flg = not bool(instance.end_flg)
        instance.save()
        return Response({
            'status': 'success',
            'data': BottleSerializer(instance).data,
        },status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False)
    def delete_bottle_data(self, request):

        id = request.data['id']
        try:
            instance = BottleManagement.objects.get(id=id)
        except BottleManagement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance.delete_flg = not bool(instance.delete_flg)
        instance.save()
        return Response({
            'status': 'success',
            'data': BottleSerializer(instance).data,
        },status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def search(self, request):

        logger.debug(request.query_params)
        queryset = self.filter_queryset(self.get_queryset())
        logger.debug('★')
        logger.debug(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True
            )
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(
            queryset,
            many=True
        )
        return Response(serializer.data)

class SalesViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = SalesHeader.objects.all()
    serializer_class = SalesSerializer

    @action(methods=['get'], detail=False)
    def get_all_sales(self, request):

        sales = self.get_queryset().filter(
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(close_flg=True) &
            Q(delete_flg=False)
        ).order_by('-leave_time')

        res = {
            'sales': SalesSerializer(sales, many=True).data,
            'count': sales.count(),
        }

        return Response(
            res,
            status=status.HTTP_200_OK
        )

    @transaction.atomic
    @action(methods=['post'], detail=False)
    def create_sales_data(self, request):

        logger.debug('★create_sales_data')
        logger.debug(request.data)

        user = mUser.objects.get(pk=1)

        sales_payment_list = []

        # customer_no = request.data['customer_no']
        # customer = None
        # if customer_no != None and customer_no != '':
        #     try:
        #         customer = MCustomer.objects.get(card__customer_no=customer_no)
        #
        #     except MCustomer.DoesNotExist:
        #         logger.error('顧客情報が取得出来ません。')
        #         return Response(status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     logger.error('会員IDが正しくありません')
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        male_visitors = request.data['male_visitors']
        female_visitors = request.data['female_visitors']
        basic_plan_type = request.data['basic_plan_type']
        seat_id = request.data['seat_id']
        total_sales = request.data['total_sales']
        total_tax_sales = request.data['total_tax_sales']
        basic_plan_service_tax = request.data['basic_plan_service_tax']
        basic_plan_tax = request.data['basic_plan_tax']
        basic_plan_card_tax = request.data['basic_plan_card_tax']
        fixed_total_tax_sales = request.data['fixed_total_tax_sales']
        remarks = request.data['remarks']

        try:
            service = MService.objects.get(pk=basic_plan_type)
        except MService.DoesNotExist:
            logger.error('サービス情報が取得出来ません。')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        visit_time = None
        leave_time = None
        visit_time_str = request.data['visit_time']
        leave_time_str = request.data['leave_time']
        if visit_time_str != '' and visit_time_str != None:
            visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        if leave_time_str != '' and leave_time_str != None:
            leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))

        seat = None
        if seat_id != None and seat_id != '' and seat_id != 0:
            try:
                seat = MSeat.objects.get(pk=seat_id)
            except MSeat.DoesNotExist:
                logger.error('座席情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        # 支払い方法は必要？★
        # payment = request.data['payment']
        #
        # try:
        #     payment = MPayment.objects.get(pk=payment)
        # except MPayment.DoesNotExist:
        #     logger.error('支払い方法が取得出来ません')
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        logger.debug('★★★★★★★★header作成するよーーーーーー')

        # SalesPayment作成

        header = SalesHeader.objects.create(
            # customer=customer, 2022/10/17 顧客事の会計が複数紐づく様に変更
            male_visitors=male_visitors,
            female_visitors=female_visitors,
            seat=seat,
            visit_time=visit_time,
            leave_time=leave_time,
            basic_plan_type=service,
            remarks=remarks,
            user=user,
            total_sales=total_sales,
            total_tax_sales=total_tax_sales,
            close_flg=True,
            # payment=payment,
            basic_plan_service_tax=basic_plan_service_tax,
            basic_plan_tax=basic_plan_tax,
            # basic_plan_card_tax=basic_plan_card_tax,
            fixed_total_tax_sales=fixed_total_tax_sales,
        )

        for sales_payment_dict in request.data['sales_payment']:
            try:
                customer = MCustomer.objects.get(pk=sales_payment_dict['customer_pk'])
            except MCustomer.DoesNotExist:
                logger.error('sales_paymentの顧客情報取得で失敗')
            sales_payment_list.append(
                SalesPayment(
                    sales_header=header,
                    customer=customer,
                    amount_paid=sales_payment_dict['amount_paid'],
                    amount_card_paid=sales_payment_dict['amount_card_paid'],
                    payment=sales_payment_dict['payment'],
                    basic_plan_card_tax=sales_payment_dict['basic_plan_card_tax'],
                )
            )

        SalesPayment.objects.bulk_create(sales_payment_list)

        logger.debug('SalesHeader, SalesPayment生成完了')

        # bulk_create用
        sales_service_detail_list = []
        sales_detail_list = []

        # ボトル消込処理
        for bottle_delete in request.data['bottle_delete_list']:
            try:
                bottle = BottleManagement.objects.get(pk=bottle_delete['id'])
                bottle.delete()
            except BottleManagement.DoesNotExist:
                logger.error('ボトル情報の取得に失敗しました。')

        open_date = leave_time

        logger.debug('サービス')

        for sales_service_detail in request.data['sales_service_detail']:
            logger.debug(sales_service_detail)
            service = MService.objects.get(
                large_category=sales_service_detail['service']['large_category'],
                middle_category=sales_service_detail['service']['middle_category'],
                small_category=sales_service_detail['service']['small_category'],
            )
            quantity = sales_service_detail['quantity']
            fixed_price = sales_service_detail['fixed_price']
            discount_flg = sales_service_detail['discount_flg']
            # tax_rate = sales_service_detail['tax_rate']

            sales_service_detail_list.append(
                SalesServiceDetail(
                    header=header,
                    service=service,
                    quantity=quantity,
                    fixed_price=fixed_price,
                    discount_flg=discount_flg,
                    # tax_rate=tax_rate,
                )
            )

        registered_bottle_product_list = []
        bottle_list = []
        disp_bottle_list = []

        logger.debug('明細')

        # 商品一覧が来る
        for item in request.data['sales_detail_list']:
            logger.debug('★★★★')
            logger.debug(item)
            try:
                product = MProduct.objects.get(id=item['id'])
            except:
                logger.error('商品が取得出来ません')

            salesDetailInstance = SalesDetail(
                header=header,
                product=product,
                quantity=item['quantity'],
                fixed_price=item['fixed_price'],
                tax_free_flg=item['tax_free_flg'],
                order_time=leave_time,
            )

            if 'bottle' in item and item['bottle'] == True:
                if item['id'] not in registered_bottle_product_list:
                    if 'customer' in item and item['customer'] != None:
                        logger.debug('★ボトル登録')
                        try:
                            bottleCustomer = MCustomer.objects.get(pk=item['customer']['customer_no'])
                        except MCustomer.DoesNotExist:
                            logger.error('sales_detailのボトル登録の顧客情報取得で失敗')
                            continue

                        bottle_list.append(
                            BottleManagement(
                                customer=bottleCustomer,
                                open_date=leave_time,
                                product=product,
                            )
                        )
                        # disp_bottle_list.append(
                        #     BottleSerializer(
                        #         BottleManagement(
                        #             customer=bottleCustomer,
                        #             open_date=leave_time,
                        #             product=product,
                        #         )
                        #     ).data
                        # )
                        salesDetailInstance.bottle_register = True
                        registered_bottle_product_list.append(item['id'])

            logger.debug('＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿')

            sales_detail_list.append(salesDetailInstance)

        logger.debug('★★★★★★最終局面★★★★★★')

        if len(sales_service_detail_list) > 0:
            SalesServiceDetail.objects.bulk_create(sales_service_detail_list)
        if len(bottle_list) > 0:
            BottleManagement.objects.bulk_create(bottle_list)
        if len(sales_detail_list) > 0:
            SalesDetail.objects.bulk_create(sales_detail_list)

        # 顧客のランク更新
        logger.debug('顧客毎のランク更新')
        for sales_payment in sales_payment_list:
            logger.debug(sales_payment)
            customer = sales_payment.customer
            total_sales_for_rank = SalesHeader.objects.filter(
                sales_payment_sales_header__customer=customer
            ).aggregate(total=Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_paid')), 0
                ) + Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_card_paid')), 0
                )
            )['total']
            update_customer_rank(customer, total_sales_for_rank)

        return Response({
            'data': SalesSerializer(header).data,
            # 'bottle': disp_bottle_list,
            'bottle': disp_bottle_list,
        }, status=status.HTTP_201_CREATED)

    @transaction.atomic
    @action(methods=['put'], detail=False)
    def update_sales_data(self, request):
        """
        とりあえず赤伝発行しないverで更新だけ実装しておく(2022/09/04)
        """

        user = mUser.objects.get(pk=1)

        logger.debug('★update_sales_data')
        logger.debug(request.data)

        sales_header_id = request.data['sales_header_id']

        try:
            header = SalesHeader.objects.get(id=sales_header_id)
        except:
            logger.error('売上ヘッダーを取得出来ません')
            logger.error('売上ヘッダーを取得出来ません')
            return Response(status.status.HTTP_400_BAD_REQUEST)

        # SalesPayment作成

        # customer_no = request.data['customer_no']
        # customer = None
        # if customer_no != None and customer_no != '':
        #     try:
        #         customer = MCustomer.objects.get(card__customer_no=customer_no)
        #     except MCustomer.DoesNotExist:
        #         logger.error('顧客情報が取得出来ません。')
        #         return Response(status.status.HTTP_400_BAD_REQUEST)
        # else:
        #     logger.error('会員IDが正しくありません')
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        male_visitors = request.data['male_visitors']
        female_visitors = request.data['female_visitors']

        basic_plan_type = request.data['basic_plan_type']
        seat_id = request.data['seat_id']
        total_sales = request.data['total_sales']
        total_tax_sales = request.data['total_tax_sales']
        fixed_total_tax_sales = request.data['fixed_total_tax_sales']

        basic_plan_service_tax = request.data['basic_plan_service_tax']
        basic_plan_tax = request.data['basic_plan_tax']
        # basic_plan_card_tax = request.data['basic_plan_card_tax']
        remarks = request.data['remarks']

        try:
            service = MService.objects.get(pk=basic_plan_type)
        except MService.DoesNotExist:
            logger.error('サービス情報が取得出来ません。')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        visit_time = None
        leave_time = None
        visit_time_str = request.data['visit_time']
        leave_time_str = request.data['leave_time']
        if visit_time_str != '' and visit_time_str != None:
            visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))
        if leave_time_str != '' and leave_time_str != None:
            leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))

        seat = None
        if seat_id != None and seat_id != '' and seat_id != 0:
            try:
                seat = MSeat.objects.get(pk=seat_id)
            except MSeat.DoesNotExist:
                logger.error('座席情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        # 支払い方法は必要？★
        # payment = request.data['payment']
        #
        # try:
        #     payment = MPayment.objects.get(pk=payment)
        # except MPayment.DoesNotExist:
        #     logger.error('支払い方法が取得出来ません')
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        logger.debug('★★★★★★★★header作成するよーーーーーー')

        # SalesPayment作成

        # header.customer = customer

        header.male_visitors = male_visitors
        header.female_visitors = female_visitors
        header.seat = seat
        header.visit_time = visit_time
        header.leave_time = leave_time
        header.basic_plan_type = service
        header.remarks = remarks
        header.user = user
        header.total_sales = total_sales
        header.total_tax_sales = total_tax_sales
        header.fixed_total_tax_sales = fixed_total_tax_sales

        header.close_flg = True
        # header.payment = payment
        header.basic_plan_service_tax = basic_plan_service_tax
        header.basic_plan_tax = basic_plan_tax
        # header.basic_plan_card_tax = basic_plan_card_tax

        logger.debug('明細の削除')

        # 一旦。deleteだとパフォーマンス悪いかもだから見直し必要★
        header.sales_service_detail.all().delete()
        header.sales_detail.all().delete()
        header.sales_payment_sales_header.all().delete()

        # bulk_create用
        sales_service_detail_list = []
        sales_detail_list = []

        # ボトル消込処理
        for bottle_delete in request.data['bottle_delete_list']:
            try:
                bottle = BottleManagement.objects.get(pk=bottle_delete['id'])
                bottle.delete()
            except BottleManagement.DoesNotExist:
                logger.error('ボトル情報の取得に失敗しました。')

        sales_payment_list = []

        for sales_payment_dict in request.data['sales_payment']:
            logger.debug('sales_payment_dict')
            logger.debug(sales_payment_dict)

            try:
                customer = MCustomer.objects.get(pk=sales_payment_dict['customer_pk'])
            except MCustomer.DoesNotExist:
                logger.error('sales_paymentの顧客情報取得で失敗')
            sales_payment_list.append(
                SalesPayment(
                    sales_header=header,
                    customer=customer,
                    amount_paid=sales_payment_dict['amount_paid'],
                    amount_card_paid=sales_payment_dict['amount_card_paid'],
                    payment=sales_payment_dict['payment'],
                    basic_plan_card_tax=sales_payment_dict['basic_plan_card_tax'],
                )
            )

        SalesPayment.objects.bulk_create(sales_payment_list)

        open_date = leave_time

        for sales_service_detail in request.data['sales_service_detail']:
            logger.debug(sales_service_detail)
            service = MService.objects.get(
                large_category=sales_service_detail['service']['large_category'],
                middle_category=sales_service_detail['service']['middle_category'],
                small_category=sales_service_detail['service']['small_category'],
            )
            quantity = sales_service_detail['quantity']
            fixed_price = sales_service_detail['fixed_price']
            discount_flg = sales_service_detail['discount_flg']
            # tax_rate = sales_service_detail['tax_rate']

            sales_service_detail_list.append(
                SalesServiceDetail(
                    header=header,
                    service=service,
                    quantity=quantity,
                    fixed_price=fixed_price,
                    discount_flg=discount_flg,
                    # tax_rate=tax_rate,
                )
            )

        registered_bottle_product_list = []
        bottle_list = []
        disp_bottle_list = []

        for item in request.data['sales_detail_list']:
            logger.debug('★★★★')
            logger.debug(item)
            try:
                product = MProduct.objects.get(id=item['id'])
            except:
                logger.error('商品が取得出来ません')

            salesDetailInstance = SalesDetail(
                header=header,
                product=product,
                quantity=item['quantity'],
                fixed_price=item['fixed_price'],
                tax_free_flg=item['tax_free_flg'],
                order_time=leave_time,
            )

            if 'bottle' in item and item['bottle'] == True:
                if item['id'] not in registered_bottle_product_list:
                    if 'customer' in item and item['customer'] != None:
                        logger.debug('★ボトル登録')
                        try:
                            bottleCustomer = MCustomer.objects.get(pk=item['customer']['customer_no'])
                        except MCustomer.DoesNotExist:
                            logger.error('sales_detailのボトル登録の顧客情報取得で失敗')
                            continue
                        bottle_list.append(
                            BottleManagement(
                                customer=bottleCustomer,
                                open_date=leave_time,
                                product=product,
                            )
                        )
                        disp_bottle_list.append(
                            BottleSerializer(
                                BottleManagement(
                                    customer=bottleCustomer,
                                    open_date=leave_time,
                                    product=product,
                                )
                            ).data
                        )
                        salesDetailInstance.bottle_register = True
                        registered_bottle_product_list.append(item['id'])

            sales_detail_list.append(salesDetailInstance)

        logger.debug('★★★★★★最終局面★★★★★★')

        if len(sales_service_detail_list) > 0:
            SalesServiceDetail.objects.bulk_create(sales_service_detail_list)
        if len(bottle_list) > 0:
            BottleManagement.objects.bulk_create(bottle_list)
        if len(sales_detail_list) > 0:
            SalesDetail.objects.bulk_create(sales_detail_list)

        header.save()

        # 顧客のランク更新
        logger.debug('顧客毎のランク更新')
        for sales_payment in sales_payment_list:
            logger.debug(sales_payment)
            customer = sales_payment.customer
            total_sales_for_rank = SalesHeader.objects.filter(
                sales_payment_sales_header__customer=customer
            ).aggregate(total=Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_paid')), 0
                ) + Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_card_paid')), 0
                )
            )['total']
            update_customer_rank(customer, total_sales_for_rank)
        # total_sales_for_rank = SalesHeader.objects.filter(
        #     customer=customer
        # ).aggregate(total=Coalesce(models.Sum(F('total_tax_sales')), 0))['total']
        # update_customer_rank(customer, total_sales_for_rank)

        return Response({
            'data': SalesSerializer(header).data,
            'bottle': disp_bottle_list,
        }, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_month_sales_analytics(self, request):
        """
        指定した日から~間の売上を取得（月単位）
            target_date無ければ全期間
            customer_noあれば顧客毎
            　=> 2022-08-21 とりあえず顧客詳細用に顧客毎の全期間を作る
        """

        if 'target_date' in request.data:
            pass

        else:
            queryset = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True))


        if 'customer_no' in request.query_params:
            try:
                customer = MCustomer.objects.get(card__customer_no=request.query_params['customer_no'])
                queryset = queryset.filter(sales_payment_sales_header__customer=customer)
            except MCustomer.DoesNotExist:
                logger.error('顧客情報の取得に失敗しました。')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        data = queryset.annotate(
            month=TruncMonth('leave_time')
        ).values('month').annotate(
            total=models.Sum(F('total_tax_sales')),
            total_visit=models.Count(F('total_tax_sales')),
        )

        return Response({
            'data': data,
        })



    @action(methods=['get'], detail=False)
    def get_day_sales_analytics(self, request):
        """
        指定した日から~間の売上を取得（日単位）
            => target_date=2022/6/18, range=3, かつ　MSetting.sales_separate_time
                => 2022/6/18 (2022/6/18 18:00 ~ 2022/6/19 17:59)
                => 2022/6/19 (2022/6/19 18:00 ~ 2022/6/20 17:59)
                => 2022/6/20 (2022/6/20 18:00 ~ 2022/6/21 17:59)

        全期間は死ぬからNG, 最高1年くらい?かな
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_month = int(target_date_str[1])
        target_date_day = int(target_date_str[2])

        # このrangeは繰り返しのcnt
        sales_separate_time = get_sales_separate_time()
        r = int(request.query_params['range'])

        res = []

        start_time = datetime(
            target_date_year,
            target_date_month,
            target_date_day,
            int(sales_separate_time[:2]),
            int(sales_separate_time[2:]),
        ).astimezone(timezone('Asia/Tokyo'))

        for i in range(1, r+1):

            # end_date = start_time + timedelta(days=1)
            # end_date = start_time
            # end_time = datetime(
            #     end_date.year,
            #     end_date.month,
            #     end_date.day,
            #     CLOSE_HOUR,
            #     CLOSE_MINUTE,
            # ).astimezone(timezone('Asia/Tokyo'))

            end_time = start_time + timedelta(days=0,
                                              hours=23,
                                              minutes=59)

            logger.debug('★')
            logger.debug(start_time)
            logger.debug(end_time)

            data = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True) &
                Q(leave_time__range=[start_time, end_time])
            ).aggregate(total=models.Sum(F('total_tax_sales')))

            res.append({
                'date': start_time.strftime('%Y-%m-%d'),
                'total': data['total'] if data['total'] is not None else 0,
            })
            start_time = start_time + timedelta(days=1)

        return Response({
            'status': 'success',
            'data': res,
        })


    @action(methods=['get'], detail=False)
    def get_day_total_visitors_analytics(self, request):
        """
        指定した日から~間の売上を取得（日単位）
            => target_date=2022/6/18, range=3, かつ　MSetting.sales_separate_time
                => 2022/6/18 (2022/6/18 18:00 ~ 2022/6/19 17:59)
                => 2022/6/19 (2022/6/19 18:00 ~ 2022/6/20 17:59)
                => 2022/6/20 (2022/6/20 18:00 ~ 2022/6/21 17:59)

        全期間は死ぬからNG, 最高1年くらい?かな
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        sales_separate_time = get_sales_separate_time()
        r = int(request.query_params['range'])

        res = []

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            int(sales_separate_time[:2]),
            int(sales_separate_time[2:]),
        ).astimezone(timezone('Asia/Tokyo'))

        for i in range(1, r+1):

            # end_date = start_time + timedelta(days=1)
            # end_date = start_time
            # end_time = datetime(
            #     end_date.year,
            #     end_date.month,
            #     end_date.day,
            #     CLOSE_HOUR,
            #     CLOSE_MINUTE,
            # ).astimezone(timezone('Asia/Tokyo'))
            end_time = start_time + timedelta(days=0,
                                              hours=23,
                                              minutes=59)

            data = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True) &
                Q(leave_time__range=[start_time,end_time])
            ).aggregate(total=models.Count(F('sales_payment_sales_header__customer')))

            res.append({
                'date': start_time.strftime('%Y-%m-%d'),
                'total': data['total'] if data['total'] is not None else 0,
            })
            start_time = start_time + timedelta(days=1)

        return Response({
            'status': 'success',
            'data': res,
        })


    @action(methods=['get'], detail=False)
    def get_customer_day_sales_analytics(self, request):
        """
        指定した日の顧客ごとの売上を取得
        ・target_date　かつ　MSetting.sales_separate_time
            sales_separate_time => 18:00
            => 2022/6/18 ・・・ 2022/6/18 18:00 ~ 2022/6/19 17:59
            => 2021/12/31 ・・・ 2021/12/31 18:00 ~ 2022/1/1 17:59

            sales_separate_time => 00:00
            => 2022/06/18 ・・・ 2022/06/18 00:00 ~ 2022/06/18 23:59
        """
        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_month = int(target_date_str[1])
        target_date_day = int(target_date_str[2])

        sales_separate_time = get_sales_separate_time()
        range = int(request.query_params['range'])

        start_time = datetime(
            target_date_year,
            target_date_month,
            target_date_day,
            int(sales_separate_time[:2]),
            int(sales_separate_time[2:]),
        ).astimezone(timezone('Asia/Tokyo'))

        end_time = start_time + timedelta(days=range-1,
                                          hours=23,
                                          minutes=59)

        data = SalesHeader.objects.filter(
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(close_flg=True) &
            Q(leave_time__range=[start_time, end_time])
        ).values(
            # customer=Lower('sales_payment_sales_header__customer')
            customer=F('sales_payment_sales_header__customer')
        ).annotate(
            total=Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_paid')), 0
                ) + Coalesce(
                    models.Sum(F('sales_payment_sales_header__amount_card_paid')), 0
                ),
            total_visit=models.Count(F('sales_payment_sales_header__amount_paid'))
        ).order_by('-total')

        serializer = CustomerSalesSerializer(data, many=True)

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            'data': serializer.data,
        })


    @action(methods=['get'], detail=False)
    def get_total_sales_analytics(self, request):
        """
        指定した日の売上の総計を取得
        ・target_date かつ　MSetting.sales_separate_time
            => 2022/6/18 ・・・ 2022/6/18 18:00 ~ 2022/6/19 17:59
            => 2021/12/31 ・・・ 2021/12/31 18:00 ~ 2022/1/1 17:59
        ・range => これがある場合、target_dateからrange(日)分取得する
            => target_date=2022/06/18, range=3 => 2022/06/18 18:0 ~ 2022/06/21 17:59

        ・日付指定なしならば全期間

        ・顧客のidがあれば顧客で絞る
        """

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の売上総計を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_month = int(target_date_str[1])
            target_date_day = int(target_date_str[2])
            result_target_date = target_date_str

            sales_separate_time = get_sales_separate_time()
            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_month,
                target_date_day,
                int(sales_separate_time[:2]),
                int(sales_separate_time[2:])
            ).astimezone(timezone('Asia/Tokyo'))

            end_time = start_time + timedelta(days=range-1,
                                              hours=23,
                                              minutes=59)

            queryset = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True) &
                Q(leave_time__range=[start_time, end_time]))

        else:
            queryset = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True))

        if 'customer_no' in request.query_params:
            try:
                customer = MCustomer.objects.get(pk=request.query_params['customer_no'])
                queryset = queryset.filter(sales_payment_sales_header__customer=customer)
            except MCustomer.DoesNotExist:
                logger.error('顧客情報の取得に失敗しました。')

        data = queryset.aggregate(
            total_price=Coalesce(models.Sum(F('total_tax_sales')), 0))

        return Response({
            'status': 'success',
            'data': data,
        })

    @action(methods=['get'], detail=False)
    def get_total_visitors_analytics(self, request):
        """
        指定した日の来店数を取得（団体単位）
        ・target_date かつ　MSetting.sales_separate_time
            => 2022/6/18 ・・・ 2022/6/18 18:00 ~ 2022/6/19 17:59
            => 2021/12/31 ・・・ 2021/12/31 18:00 ~ 2022/1/1 17:59

            日付指定なしならば全期間
        """
        result_target_date = ''

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の来店数を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_month = int(target_date_str[1])
            target_date_day = int(target_date_str[2])
            result_target_date = target_date_str

            sales_separate_time = get_sales_separate_time()
            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_month,
                target_date_day,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            end_time = start_time + timedelta(days=range-1,
                                              hours=23,
                                              minutes=59)

            queryset = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True) &
                Q(leave_time__range=[start_time, end_time]))

        else:
            queryset = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True))

        if 'customer_no' in request.query_params:
            try:
                customer = MCustomer.objects.get(pk=request.query_params['customer_no'])
                queryset = queryset.filter(sales_payment_sales_header__customer=customer)
            except MCustomer.DoesNotExist:
                logger.error('顧客情報の取得に失敗しました。')

        data = queryset.values(
            # customer=Lower('sales_payment_sales_header__customer')
            customer=F('sales_payment_sales_header__customer')
        ).annotate(
            models.Count(F('customer'))
        ).values(
            'customer'
        ).count()

        return Response({
            'status': 'success',
            'target_date': '-'.join(result_target_date),
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_basic_plan_type_ratio_analytics(self, request):
        """
        指定した日の基本料金比率
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00

            日付指定なしならば全期間
        """

        result_target_date = '全期間'

        if 'target_date' in request.query_params:
            # logger.debug(request.query_params['target_date'] + 'の基本料金比率を取得します。')
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_month = int(target_date_str[1])
            target_date_day = int(target_date_str[2])
            result_target_date = target_date_str

            range = int(request.query_params['range'])

            start_time = datetime(
                target_date_year,
                target_date_month,
                target_date_day,
                OPEN_HOUR,
                OPEN_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))
            end_date = start_time + timedelta(days=range)
            end_time = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                CLOSE_HOUR,
                CLOSE_MINUTE,
            ).astimezone(timezone('Asia/Tokyo'))

            logger.debug('open : ' + start_time.strftime('%Y-%m-%d %H:%M'))
            logger.debug('end : ' + end_time.strftime('%Y-%m-%d %H:%M'))

            data = SalesHeader.objects.filter(
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(delete_flg=False) &
                Q(close_flg=True) &
                Q(leave_time__range=[start_time,end_time])
                ).values(
                    'basic_plan_type'
                ).annotate(
                    total=models.Count(F('basic_plan_type'))
                )
        else:
            # logger.debug('全期間の基本料金比率を取得します')
            data = SalesHeader.objects.values(
                    'basic_plan_type'
                ).annotate(
                    total=models.Count(F('basic_plan_type'))
                )

        # if len(data) == 0:
        #     data = [{'basic_plan_type':0, 'total': 0}, {'basic_plan_type':0, 'total': 0}]
        # if len(data) == 1:
        #     type = 0
        #     if data[0]['basic_plan_type'] == 0:
        #         type = 1
        #     data.({'basic_plan_type': type, 'total': 0})

        # 一旦0件でも1件も変える可能性があるやつで・・querysetに突っ込み方が分からん
        # 取得方法考えるか、突っ込み方考える
        return Response({
            'status': 'success',
            'target_date': '-'.join(result_target_date),
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_sales_by_every_time_analytics(self, request):
        """
        時間帯毎の来店数、売上の取得
            →期間広いと大変だからとりあえず、1日指定のみ
        """

        sales_separate_time = get_sales_separate_time()
        sales_separate_time_h = sales_separate_time[:2]
        sales_separate_time_m = sales_separate_time[2:]

        if 'target_date' in request.query_params:
            target_date_str = request.query_params['target_date'].split('-')
            target_date_year = int(target_date_str[0])
            target_date_month = int(target_date_str[1])
            target_date_day = int(target_date_str[2])

            res = []

            start_time = datetime(
                target_date_year,
                target_date_month,
                target_date_day,
                int(sales_separate_time_h),
                int(sales_separate_time_m),
            ).astimezone(timezone('Asia/Tokyo'))

            # logger.debug('★target_dateの24時間分取得')

            for hour in range(0, 24):

                end_time = start_time + timedelta(hours=1)
                # logger.debug(start_time)
                # logger.debug(end_time)

                data = SalesHeader.objects.filter(
                    Q(delete_flg=False) &
                    Q(close_flg=True) &
                    Q(leave_time__gte=start_time) &
                    Q(leave_time__lt=end_time)
                ).aggregate(
                    total=Coalesce(models.Sum(F('fixed_total_tax_sales')), 0),
                    total_visit=models.Count(F('sales_payment_sales_header__customer'))
                )

                # data = SalesDetail.objects.filter(
                #     # Q(header__sales_payment_sales_header__customer__delete_flg=False) &
                #     Q(header__delete_flg=False) &
                #     Q(header__close_flg=True) &
                #     Q(delete_flg=False) &
                #     Q(order_time__gte=start_time) &
                #     Q(order_time__lte=end_time)
                # ).aggregate(
                #     total=Coalesce(models.Sum(F('fixed_price')), 0),
                #     total_visit=models.Count(F('header__sales_payment_sales_header__customer'))
                # )
                data['time'] = start_time.strftime('%H:%M') + ' ~ ' + end_time.strftime('%H:%M')
                res.append(data)
                start_time = start_time + timedelta(hours=1)

            return Response(res, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)



    @action(methods=['get'], detail=False)
    def get_customer_day_stay_hour_analytics(self, request):
        """
        顧客ごとの滞在時間 => その日で絞るだけ？・・・それだけだったらいらんかも。将来的になくすか検討
        """
        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_hour = int(target_date_str[1])
        target_date_minute = int(target_date_str[2])

        sales_separate_time = get_sales_separate_time()
        range = 1

        start_time = datetime(
            target_date_year,
            target_date_hour,
            target_date_minute,
            OPEN_HOUR,
            OPEN_MINUTE,
        ).astimezone(timezone('Asia/Tokyo'))
        end_time = start_time + timedelta(days=range-1,
                                          hours=23,
                                          minutes=59)

        data = SalesHeader.objects.filter(
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(close_flg=True) &
            Q(leave_time__range=[start_time,end_time]))

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            'data': SalesSerializer(
                data,
                many=True,
                fields=['id', 'sales_payment', 'visit_time', 'leave_time']).data
            })


    @action(methods=['get'], detail=False)
    def get_product_day_sales_analytics(self, request):
        """
        指定した日の商品ごとの売上を取得
        ・target_date
            => 2022/6/18 ・・・ 2022/6/18 20:30 ~ 2022/6/19 07:00
            => 2021/12/31 ・・・ 2021/12/31 20:30 ~ 2022/1/1 07:00
        """

        target_date_str = request.query_params['target_date'].split('-')
        target_date_year = int(target_date_str[0])
        target_date_month = int(target_date_str[1])
        target_date_day = int(target_date_str[2])

        sales_separate_time = get_sales_separate_time()
        range = int(request.query_params['range'])

        start_time = datetime(
            target_date_year,
            target_date_month,
            target_date_day,
            int(sales_separate_time[:2]),
            int(sales_separate_time[2:]),
        ).astimezone(timezone('Asia/Tokyo'))

        end_time = start_time + timedelta(days=range-1,
                                          hours=23,
                                          minutes=59)

        data = SalesHeader.objects.filter(
            # Q(sales_payment_sales_header__customer__delete_flg=False) &
            Q(delete_flg=False) &
            Q(close_flg=True) &
            Q(leave_time__range=[start_time, end_time]) &
            Q(sales_detail__isnull=False)
        ).values(
            'sales_detail__product',
        ).annotate(
            total=models.Sum(F('sales_detail__fixed_price')),
            total_cnt=models.Count(F('sales_detail__product'))
        ).order_by('-total')[:20]

        serializer = ProductSalesSerializer(data, many=True)

        return Response({
            'status': 'success',
            'target_date': start_time.strftime('%Y-%m-%d'),
            'data': serializer.data,
        })


    @action(methods=['get'], detail=False)
    def get_total_customer_sales_ranking(self, request):
        """
        指定した期間の指定した分だけの顧客の売上ランキングを取得
        """

        length = 10 if 'length' not in request.query_params else request.query_params['length']


        if 'target_date' in request.query_params:
            pass
        else:
            res = SalesHeader.objects.filter(
                Q(delete_flg=False) &
                # Q(sales_payment_sales_header__customer__delete_flg=False) &
                Q(close_flg=True) &
                Q(delete_flg=False)
            ).values(
                # customer=Lower('sales_payment_sales_header__customer')
                customer=F('sales_payment_sales_header__customer')
            ).annotate(
                total=Coalesce(
                        models.Sum(F('sales_payment_sales_header__amount_paid')), 0
                    ) + Coalesce(
                        models.Sum(F('sales_payment_sales_header__amount_card_paid')), 0
                    ),
                total_visit=models.Count(F('sales_payment_sales_header__amount_paid'))
            ).order_by('-total')[:length]

            rank = {
                'salesRanking': CustomerSalesSerializer(res, many=True).data
            }

            return Response(rank, status=status.HTTP_200_OK)



    @transaction.atomic
    @action(methods=['post'], detail=False)
    def create_sales_header(self, request):
        logger.debug('★create_sales_header')
        logger.debug(request.data)

        user = mUser.objects.get(pk=1)

        customer_no = request.data['customer_no']
        customer = None
        if customer_no != None and customer_no != '':
            try:
                customer = MCustomer.objects.get(card__customer_no=customer_no)

            except MCustomer.DoesNotExist:
                logger.error('顧客情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error('会員IDが正しくありません')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        not_end_sales_header_list = SalesHeader.objects.filter(
            sales_payment_sales_header__customer=customer,
            close_flg=False,
            delete_flg=False,
        )

        if len(not_end_sales_header_list) >= 1:
            logger.error('会計していない同一会員の伝票が存在します。')
            return Response(
                {
                    'msg': '会計していない同一会員の伝票が存在します。'
                },
                status=status.HTTP_400_BAD_REQUEST
            )



        male_visitors = request.data['male_visitors']
        female_visitors = request.data['female_visitors']
        basic_plan_type = request.data['basic_plan_type']
        seat_id = request.data['seat_id']
        remarks = request.data['remarks']

        try:
            service = MService.objects.get(pk=basic_plan_type)
        except MService.DoesNotExist:
            logger.error('サービス情報が取得出来ません。')
            return Response(status=status.HTTP_400_BAD_REQUEST)


        visit_time = datetime.now(timezone('Asia/Tokyo'))

        visit_time_str = request.data['visit_time']

        if visit_time_str != '' and visit_time_str != None:
            visit_time = datetime.strptime(visit_time_str, '%Y-%m-%d %H:%M').astimezone(timezone('Asia/Tokyo'))

        seat = None
        logger.debug('seat_id')
        logger.debug(seat_id == None)
        if seat_id != None and seat_id != '':
            try:
                seat = MSeat.objects.get(pk=seat_id)

                # 2022-08-19 => 同一座席の伝票もOK☞後から来た人とか。
                # not_end_same_seat_sales_header_list = SalesHeader.objects.filter(
                #     seat=seat,
                #     close_flg=False,
                #     delete_flg=False,
                # )
                #
                # if len(not_end_same_seat_sales_header_list) >= 1:
                #     logger.error('同一座席の伝票が存在します。')
                #     return Response(
                #         {
                #             'msg': '同一座席の伝票が存在します。'
                #         },
                #         status=status.HTTP_400_BAD_REQUEST
                #     )
            except MSeat.DoesNotExist:
                logger.error('座席情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)


        header = SalesHeader.objects.create(
            sales_payment_sales_header__customer=customer,
            male_visitors=male_visitors,
            female_visitors=female_visitors,
            seat=seat,
            visit_time=visit_time,
            basic_plan_type=service,
            remarks=remarks,
            user=user,
        )

        return Response({
            'status':'success',
            'data': SalesSerializer(header).data
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def update_sales_header(self, request):

        logger.debug('update_sales_header')
        logger.debug(request.data)

        try:
            header = SalesHeader.objects.get(pk=request.data['id'])
        except SalesHeader.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        seat = None
        seat_id = request.data['seat_id']

        male_visitors = request.data['male_visitors']
        female_visitors = request.data['female_visitors']
        basic_plan_type = request.data['basic_plan_type_id']
        remarks = request.data['remarks']

        try:
            service = MService.objects.get(pk=basic_plan_type)
        except MService.DoesNotExist:
            logger.error('サービス情報が取得出来ません。')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if seat_id != None and seat_id != '' and seat_id != 0:
            try:
                seat = MSeat.objects.get(pk=seat_id)
            except MSeat.DoesNotExist:
                logger.error('席情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)

        header.seat = seat
        header.basic_plan_type = service
        header.male_visitors = male_visitors
        header.female_visitors = female_visitors
        header.remarks = remarks
        header.save()
        return Response(SalesSerializer(header).data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=False)
    def get_non_close_sales_header(self, request):

        return Response(
            SalesSerializer(SalesHeader.objects.filter(
                close_flg=False,
                delete_flg=False,
            ),
            many=True).data
        )

    @action(methods=['get'], detail=False)
    def get_non_end_sales_food_detail(self, request):
        """
        締めていない伝票の食べ物で作っていない注文
        """
        return Response(
            SubSalesDetailSerializer(SalesDetail.objects.filter(
                end_flg=False,
                delete_flg=False,
                header__close_flg=False,
                header__delete_flg=False,
                product__category__large_category=2,
            ).order_by('order_time'),
            many=True).data
        )

    @action(methods=['get'], detail=False)
    def get_end_sales_food_detail(self, request):
        """
        締めていない伝票の食べ物の消込済注文
        """
        return Response(
            SubSalesDetailSerializer(SalesDetail.objects.filter(
                end_flg=True,
                delete_flg=False,
                header__close_flg=False,
                header__delete_flg=False,
                product__category__large_category=2,
            ),
            many=True).data
        )

    @action(methods=['post'], detail=False)
    def end_sales_detail(self, request):

        now = datetime.now().astimezone(timezone('Asia/Tokyo'))

        try:
            detail = SalesDetail.objects.get(pk=request.data['sales_detail_id'])
            detail.end_flg = True
            detail.end_time = now
            detail.save()
        except:
            logger.error('商品明細の締めフラグ更新失敗')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(
            SalesDetailSerializer(detail).data
        )

    @action(methods=['post'], detail=False)
    def not_end_sales_detail(self, request):

        try:
            detail = SalesDetail.objects.get(pk=request.data['sales_detail_id'])
            detail.end_flg = False
            detail.end_time = None
            detail.save()
        except:
            logger.error('商品明細の締めフラグ更新失敗')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(
            SalesDetailSerializer(detail).data
        )


    # @transaction.atomic
    @action(methods=['post'], detail=False)
    def add_sales_detail(self, request):
        """
        注文を取る
        """

        logger.debug('add_sales_detail')
        logger.info(request.data)

        try:
            sales_header = SalesHeader.objects.get(pk=request.data['sales_header_id'])
        except SalesHeader.DoesNotExist:
            logger.error('伝票情報が取得出来ません。')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order_time = datetime.now(timezone('Asia/Tokyo'))

        sales_detail_list = request.data['sales_detail_list']

        sales_detail_list_for_create = []

        for item in sales_detail_list:
            try:
                product = MProduct.objects.get(pk=item['id'])
            except MProduct.DoesNotExist:
                logger.error('商品情報が取得出来ません。')
                return Response(status=status.HTTP_400_BAD_REQUEST)

            sales_detail_list_for_create.append(
                SalesDetail(
                    header=sales_header,
                    product=product,
                    quantity=item['quantity'],
                    fixed_price=item['fixedPrice'],
                    tax_free_flg=item['taxFree'],
                    order_time=order_time,
                )
            )
            detail = SalesDetail.objects.create(
                header=sales_header,
                product=product,
                quantity=item['quantity'],
                fixed_price=item['fixedPrice'],
                tax_free_flg=item['taxFree'],
                order_time=order_time,
            )
            # detail.save()

        # SalesDetail.objects.bulk_create(sales_detail_list_for_create)

        logger.debug('注文データ作成完了 sales_header:' + str(sales_header.id))

        return Response({
            'status': 'success',
            'data': SalesSerializer(sales_header).data
        }, status=status.HTTP_200_OK)

    @transaction.atomic
    @action(methods=['put'], detail=False)
    def update_sales_detail(self, request):
        """
        明細更新
        """

        try:
            detail = SalesDetail.objects.get(pk=request.data['id'])
        except SalesDetail.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        detail.fixed_price = request.data['fixed_price']
        detail.tax_free_flg = request.data['tax_free_flg']
        detail.quantity = request.data['quantity']
        detail.save()

        try:
            header = SalesHeader.objects.get(pk=request.data['header_id'])
        except SalesHeader.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(SalesSerializer(header).data)


    @transaction.atomic
    @action(methods=['delete'], detail=False)
    def delete_sales_detail(self, request):
        """
        明細更新
        """
        logger.debug('★delete_sales_detail')
        logger.debug(request.data)

        res_detail = None

        try:
            detail = SalesDetail.objects.get(pk=request.data['id'])
            res_detail = copy.deepcopy(detail)
            detail.delete()
        except SalesDetail.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            header = SalesHeader.objects.get(pk=request.data['header_id'])
        except SalesHeader.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if res_detail.product.category.large_category == 2:
            channel_layer = get_channel_layer()
            logger.debug('食事の明細削除➡WS送信')
            async_to_sync(channel_layer.group_send)(
                res_detail.header.user.username,
                {
                    'type': 'delete_order',
                    'content': SalesDetailSerializer(res_detail).data,
                },
            )

        return Response(SalesSerializer(header).data)


    @transaction.atomic
    @action(methods=['post'], detail=False)
    def close_sales_header(self, request):
        """
        締め処理
        """
        # 売上でランク更新
        # 総計登録
        # サービス明細の作成
        # ボトル登録
        # 締めフラグ更新
        logger.debug('close_sales_header')
        logger.debug(request.data)

        try:
            header = SalesHeader.objects.get(pk=request.data['id'])
            customer = MCustomer.objects.get(pk=request.data['customer']['id'])
        except SalesHeader.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except MCustomer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        header.total_sales = request.data['total_sales']
        header.total_tax_sales = request.data['total_tax_sales']
        header.basic_plan_service_tax = request.data['basic_plan_service_tax']
        header.basic_plan_tax = request.data['basic_plan_tax']
        header.basic_plan_card_tax = request.data['basic_plan_card_tax']


        # 支払い方法は必要？★
        payment_pk = request.data['payment']

        try:
            payment = MPayment.objects.get(pk=payment_pk)
        except MPayment.DoesNotExist:
            logger.error('支払い方法が取得出来ません')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        header.payment = payment

        # ボトルの開封日は会計時の日付で良いよな？★
        open_date_str = request.data['leave_time']
        open_date = datetime.strptime(open_date_str, '%Y/%m/%d %H:%M').astimezone(timezone('Asia/Tokyo'))

        for bottle_delete in request.data['bottle_delete_list']:
            try:
                bottle = BottleManagement.objects.get(pk=bottle_delete['id'])
                bottle.delete()
            except BottleManagement.DoesNotExist:
                logger.error('ボトル情報の取得に失敗しました。')
                pass

        # 締め時のボトル登録は1本のみで良いよな？・・・

        registered_bottle_list = []

        for sales_detail in request.data['sales_detail']:
            if 'bottle' in sales_detail and sales_detail['bottle'] == True:
                # 明細1つにつき1登録のみ
                if sales_detail['id'] not in registered_bottle_list:
                    try:
                        product = MProduct.objects.get(pk=sales_detail['product']['id'])
                    except MProduct.DoesNotExist:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    logger.debug('ボトル登録有')
                    logger.debug('商品のid')
                    logger.debug(sales_detail['id'])

                    BottleManagement.objects.create(
                        customer=customer,
                        open_date=open_date,
                        product=product,
                    )

                    try:
                        detail = SalesDetail.objects.get(pk=sales_detail['id'])
                        detail.bottle_register = True
                        detail.save()
                    except SalesDetail.DoesNotExist:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

                    # registered_bottle_listに追加していなかった？
                    registered_bottle_list.append(detail.id)


        for sales_service_detail in request.data['sales_service_detail']:
            logger.debug(sales_service_detail)
            service = MService.objects.get(
                large_category=sales_service_detail['service']['large_category'],
                middle_category=sales_service_detail['service']['middle_category'],
                small_category=sales_service_detail['service']['small_category'],
            )
            quantity = sales_service_detail['quantity']
            fixed_price = sales_service_detail['fixed_price']
            discount_flg = sales_service_detail['discount_flg']
            tax_rate = sales_service_detail['tax_rate']

            SalesServiceDetail.objects.create(
                header=header,
                service=service,
                quantity=quantity,
                fixed_price=fixed_price,
                discount_flg=discount_flg,
                tax_rate=tax_rate,
            )

        header.close_flg = True
        header.leave_time = datetime.now(timezone('Asia/Tokyo'))
        header.save()

        # 顧客のランク更新
        total_sales_for_rank = SalesHeader.objects.filter(
            sales_payment_sales_header__customer=customer
        ).aggregate(total=Coalesce(models.Sum(F('total_tax_sales')), 0))['total']
        update_customer_rank(customer, total_sales_for_rank)

        return Response(SalesSerializer(header).data,
                        status=status.HTTP_200_OK)


class BookingViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = BookingManagement.objects.all()
    serializer_class = BookingSerializer

    # def list(self, request):
    #     queryset =


class ProductCategoryViewSet(BaseModelViewSet):
    """
    """
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    # def list(self, request):
    #     queryset =


# class AttendanceViewSet(BaseModelViewSet):
#     """
#     """
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = AttendanceManagement.objects.all()
#     serializer_class = AttendanceSerializer


class TimeViewSet(viewsets.ViewSet):

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    queryset = MCustomer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=False)
    def get_current_time(self, request):
        now = datetime.now().astimezone(timezone('Asia/Tokyo'))
        data = now.strftime('%Y-%m-%d %H:%M')
        return Response({
            'status': 'success',
            'data': data,
        })
