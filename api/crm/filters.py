from django.db.models import Q
from django_filters import rest_framework as django_filter


from .serializers import (
    CustomerSerializer,
    CastSerializer,
    RankSerializer,
    TaxSerializer,
    ProductSerializer,
    SeatSerializer,
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
)

from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MSeat,
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

import logging
logger = logging.getLogger(__name__)


class CustomerFilter(django_filter.FilterSet):

    name = django_filter.CharFilter(method="name_filter")
    customer_no = django_filter.CharFilter(method="customer_no_filter")

    class Meta:
        model = MCustomer
        fields = []

    def name_filter(self, queryset, name, value):
        logger.debug(queryset)
        res = queryset.filter(name__contains=value)
        return res

    def customer_no_filter(self, queryset, name, value):
        logger.debug(queryset)
        res = queryset.filter(card__customer_no=value)
        return res


class BottleFilter(django_filter.FilterSet):

    name = django_filter.CharFilter(method="name_filter")
    customer_no = django_filter.CharFilter(method="customer_no_filter")

    class Meta:
        model = BottleManagement
        fields = []

    def name_filter(self, queryset, name, value):
        logger.debug(queryset)
        res = queryset.filter(customer__name__contains=value)
        return res

    def customer_no_filter(self, queryset, name, value):
        logger.debug(queryset)
        res = queryset.filter(customer__card__customer_no=value)
        return res
