# from .models import (
# )

from .sub_models import (
    SalesHeader,
    SalesServiceDetail,
    SalesDetail
)

from .serializers import (
    SalesDetailSerializer,
    SubSalesDetailSerializer,
    SalesSerializer,
)

import logging
import requests
import json

from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)

from django.core.signals import (
    request_started,
    request_finished,
)


from django.dispatch import receiver

logger = logging.getLogger(__name__)


from ws.consumers import OrderConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=SalesDetail)
def sales_detail_receiver(sender, instance, created, **kwargs):

    logger.debug('★sales_detail_receiver')

    if not created:
        logger.debug('新規作成じゃないのでスルー')
        return

    # 新規作成の場合で食べ物のみリアルタイムで厨房行
    if instance.product.category.large_category != 2:
        logger.debug('食べ物オーダーじゃないのでスルー')
        return

    logger.debug(instance)
    logger.debug(kwargs)

    channel_layer = get_channel_layer()
    logger.debug('食事の明細新規作成➡WS送信')
    async_to_sync(channel_layer.group_send)(
        instance.header.user.username,
        {
            'type': 'new_order',
            'content': SalesDetailSerializer(instance).data,
        },
    )

@receiver(post_save, sender=SalesHeader)
def sales_header_receiver(sender, instance, created, **kwargs):

    logger.debug('sales_header_receiver')

    if created:
        logger.debug('伝票新規作成はスルー')
        return

    # if not instance.close_flg:
    #     logger.debug('締めフラグではないのでスルー')
    #     return

    if instance.delete_flg:
        logger.debug('伝票削除➡WS送信')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            instance.user.username,
            {
                'type': 'delete_sales_header',
                'content': SalesSerializer(instance).data,
            },
        )

    if instance.close_flg:
        logger.debug('伝票締め➡WS送信')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            instance.user.username,
            {
                'type': 'close_sales_header',
                'content': SalesSerializer(instance).data,
            },
        )
