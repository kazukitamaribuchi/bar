from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampModel(models.Model):

    created_at = models.DateTimeField(
        _('作成時間'),
        null=True,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('更新時間'),
        null=True,
        auto_now=True
    )

    class Meta:
        abstract = True
