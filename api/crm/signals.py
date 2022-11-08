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
from threading import Thread


@receiver(post_save, sender=SalesDetail)
def sales_detail_receiver(sender, instance, created, **kwargs):

    logger.debug('★sales_detail_receiver')
    logger.debug(instance)
    logger.debug(kwargs)

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
    try:
        thread = WorkerThread(
            'new_order',
            SalesDetailSerializer(instance).data,
            instance,
            instance.header.user.username,
        )
        thread.start()
        # async_to_sync(channel_layer.group_send)(
        #     instance.header.user.username,
        #     {
        #         'type': 'new_order',
        #         'content': SalesDetailSerializer(instance).data,
        #     },
        # )
    except Exception as e:
        logger.critical('明細新規作成時のWebSocket送信でエラーが発生しました。')
        logger.critical(e)

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
        try:
            thread = WorkerThread(
                'delete_sales_header',
                SalesSerializer(instance).data,
                instance,
                instance.user.username,
            )
            thread.start()
            # async_to_sync(channel_layer.group_send)(
            #     instance.user.username,
            #     {
            #         'type': 'delete_sales_header',
            #         'content': SalesSerializer(instance).data,
            #     },
            # )
        except Exception as e:
            logger.critical('伝票削除時のWebSocket送信でエラーが発生しました。')
            logger.critical(e)

    if instance.close_flg:
        logger.debug('伝票締め➡WS送信')
        channel_layer = get_channel_layer()
        try:
            thread = WorkerThread(
                'close_sales_header',
                SalesSerializer(instance).data,
                instance,
                instance.user.username
            )
            thread.start()
            # async_to_sync(channel_layer.group_send)(
            #     instance.user.username,
            #         'type': 'close_sales_header',
            #     {
            #         'content': SalesSerializer(instance).data,
            #     },
            # )
        except Exception as e:
            logger.critical('伝票締め時のWebSocket送信でエラーが発生しました。')
            logger.critical(e)


class WorkerThread(Thread):

    channel_layer = get_channel_layer()

    def __init__(self, target_type, content, instance, user):
        super().__init__()
        self.target_type = target_type
        self.content = content
        self.instance = instance
        self.user = user

    def run(self) -> None:
        try:
            async_to_sync(self.channel_layer.group_send)(
                self.user,
                {
                    'type': self.target_type,
                    'content': self.content,
                },
            )
        except Exception as e:
            logger.critical('SignalのWebSocket送信でエラーが発生しました。')
            logger.critical(e)
