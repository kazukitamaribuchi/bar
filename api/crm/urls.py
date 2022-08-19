from django.urls import path, include
from . import views, viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customer', viewsets.CustomerViewSet)
router.register('rank', viewsets.RankViewSet)
router.register('tax', viewsets.TaxViewSet)
router.register('cast', viewsets.CastViewSet)
router.register('product', viewsets.ProductViewSet)
router.register('seat', viewsets.SeatViewSet)
router.register('setting', viewsets.SettingViewSet)
router.register('card', viewsets.CardViewSet)
router.register('bottle', viewsets.BottleViewSet)
router.register('sales', viewsets.SalesViewSet)
router.register('booking', viewsets.BookingViewSet)
# router.register('attendance', viewsets.AttendanceViewSet)
# router.register('question', viewsets.QuestionViewSet)
router.register('time', viewsets.TimeViewSet)


app_name = 'crm'
urlpatterns = [
    path('', include(router.urls)),
    path('appinit/', views.AppInitView.as_view(), name='appinit'),
]
