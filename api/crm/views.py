from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.db.models import Sum, Q

from django.db.models.functions import Concat

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
    # AttendanceSerializer,
    BookingSerializer,
    # QuestionSerializer,
    CustomerSalesSerializer,
    ProductSalesSerializer,
    ServiceSerializer,
)
from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
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
    # 2: [0,1,2,3,4],
    2: {
        # メイン => 和食、洋食、ファーストフード的な?
        0: [0],
        # サラダ
        1: [0],
        # 前菜
        2: [0],
        # 揚げ物
        3: [0],
        # 吸い物、御飯物
        4: [0],
    }
}



import logging

logger = logging.getLogger(__name__)

class AppInitView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            customers = CustomerSerializer(
                MCustomer.objects.filter(delete_flg=False).order_by('-rank_id'),
                many=True).data
            logger.debug('1')
            product = ProductSerializer(MProduct.objects.filter(delete_flg=False), many=True).data
            logger.debug('2')
            product_by_category = get_product_by_category()
            logger.debug('3')
            popular, top = get_popular_product()
            logger.debug('4')
            sales = SalesSerializer(
                SalesHeader.objects.filter(
                    Q(customer__delete_flg=False) &
                    Q(close_flg=True) &
                    Q(delete_flg=False)
                ).order_by('-leave_time'),
                many=True).data
            logger.debug('5')
            bottle = BottleSerializer(
                BottleManagement.objects.filter(
                    delete_flg=False
                ).order_by(Concat('end_flg', 'end_date'), '-created_at'),
                many=True).data
            logger.debug('6')
            seat = SeatSerializer(MSeat.objects.all(), many=True).data
            logger.debug('7')
            setting = SettingSerializer(MSetting.objects.all(), many=True).data
            logger.debug('8')
            service = ServiceSerializer(MService.objects.all(), many=True).data
            # cast = CastSerializer(MCast.objects.all(), many=True).data
            # question = QuestionSerializer(MQuestion.objects.all(), many=True).data

            return Response({
                'customers': customers,
                'product': product,
                'product_by_category': product_by_category,
                'popular': {'popular': popular, 'top': top},
                'sales': sales,
                'bottle': bottle,
                'seat': seat,
                'setting': setting,
                'service': service,
                # 'question': question,
                # 'cast': cast,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(e)
            logger.error('初期化処理に失敗しました。')
            return Response({
                'result': 'failure',
            }, status=status.HTTP_400_BAD_REQUEST)




def get_product_by_category():
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
        },
    }

    for large, items in PRODUCT_CATEGORY.items():
        for middle in items:
            for small in items[middle]:
                q = MProduct.objects.filter(Q(category__large_category=large), \
                    Q(category__middle_category=middle), \
                    Q(category__small_category=small), \
                    Q(delete_flg=False)
                )
                data = ProductSerializer(q, many=True).data
                # logger.debug('large=> ' + str(large) + ' middle=> ' + str(middle) + ' small=> ' + str(small))
                res[large][middle][small] = data

    return res

def get_popular_product():
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
        res = MProduct.objects.all()[:12]
        top = {
            0: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=0, delete_flg=False)[:12], many=True).data,
            1: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=1, delete_flg=False)[:12], many=True).data,
            2: ProductSerializer(MProduct.objects.filter(category__large_category=1, category__middle_category=2, delete_flg=False)[:12], many=True).data,
            3: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=0, delete_flg=False)[:12], many=True).data,
            4: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=1, delete_flg=False)[:12], many=True).data,
            5: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=2, delete_flg=False)[:12], many=True).data,
            6: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=3, delete_flg=False)[:12], many=True).data,
            7: ProductSerializer(MProduct.objects.filter(category__large_category=2, category__middle_category=4, delete_flg=False)[:12], many=True).data,
        }
        return ProductSerializer(res, many=True).data, top
        # return Response({
        #     'status': 'success',
        #     'data': {
        #         'popular': ProductSerializer(res, many=True).data,
        #         'top': top,
        #     }
        # }, status=status.HTTP_200_OK)
    except:
        import traceback
        traceback.print_exc()
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)
