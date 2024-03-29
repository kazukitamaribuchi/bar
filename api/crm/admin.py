from django.contrib import admin

from .models import (
    mUser,
    MRank,
    MTax,
    MCustomer,
    MCast,
    MProduct,
    MProductCategory,
    MService,
    MServiceCategory,
    MSeat,
    # MQuestion,
    MPayment,
)

from .sub_models import (
    # QuestionAnswer,
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    SalesPayment,
    SalesServiceDetail,
    # SalesAppointDetail,
    BookingManagement,
    # AttendanceManagement,
)

admin.site.register(mUser)
admin.site.register(MRank)
admin.site.register(MTax)
admin.site.register(MCustomer)
admin.site.register(MCast)
admin.site.register(MProduct)
admin.site.register(MProductCategory)
admin.site.register(MService)
admin.site.register(MServiceCategory)
admin.site.register(MSeat)
admin.site.register(MPayment)
# admin.site.register(MQuestion)
# admin.site.register(QuestionAnswer)
admin.site.register(CardManagement)
admin.site.register(BottleManagement)
admin.site.register(SalesHeader)
admin.site.register(SalesDetail)
admin.site.register(SalesPayment)
admin.site.register(SalesServiceDetail)
# admin.site.register(SalesAppointDetail)
admin.site.register(BookingManagement)
# admin.site.register(AttendanceManagement)
