from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.http import AsyncHttpConsumer
from django.db import connection
from django.db.utils import OperationalError
from channels.db import database_sync_to_async
from django.core import serializers
from django.utils import timezone
import json
from urllib.parse import urlparse
import datetime
import time
import json
import logging
logger = logging.getLogger(__name__)
from channels.generic.websocket import WebsocketConsumer

# class OrderConsumer(WebsocketConsumer):
#     def connect(self):
#         logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
#         self.accept()
#
#     def disconnect(self, close_code):
#         logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
#         pass
#
#     def receive(self, text_data):
#         logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         self.send(text_data=json.dumps({
#             'message': message
#         }))

class OrderConsumer(AsyncWebsocketConsumer):

    groups = ['broadcast']

    async def connect(self):
        logger.info('OrderConsumer connect')
        self.accept()
        try:
            self.user_group_name = self.scope['url_route']['kwargs']['username']
            await self.channel_layer.group_add(
                self.user_group_name,
                self.channel_name
            )
            await self.accept()
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise

    # async def websocket_connect(self, message):
    #     try:
    #         for group in self.groups:
    #             await self.channel_layer.group_add(group, self.channel_name)
    #     except AttributeError:
    #         logger.error('AttributeError')
    #         # raise InvalidChannelLayerError(
    #         #     "BACKEND is unconfigured or doesn't support groups"
    #         # )
    #     try:
    #         await self.connect()
    #     except AcceptConnection:
    #         logger.error('AcceptConnection')
    #         await self.accept()
    #     except DenyConnection:
    #         logger.error('DenyConnection')
    #         await self.close()

    async def disconnect(self, close_code):
        logger.info('OrderConsumer disconnect')
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )
        await self.close()

    async def new_order(self, event):
        logger.info('OrderConsumer new_order')
        try:
            content = event['content']
            await self.send(text_data=json.dumps({
                'type': 0,
                'content': content,
            }))
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise

    async def update_order(self, event):
        logger.info('OrderConsumer update_order')
        try:
            content = event['content']
            await self.send(text_data=json.dumps({
                'type': 1,
                'content': content,
            }))
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise

    async def delete_order(self, event):
        logger.info('OrderConsumer delete_order')
        try:
            content = event['content']
            await self.send(text_data=json.dumps({
                'type': 2,
                'content': content,
            }))
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise

    async def delete_sales_header(self, event):
        logger.info('OrderConsumer delete_sales_header')
        try:
            content = event['content']
            await self.send(text_data=json.dumps({
                'type': 10,
                'content': content,
            }))
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise

    async def close_sales_header(self, event):
        logger.info('OrderConsumer close_sales_header')
        try:
            content = event['content']
            await self.send(text_data=json.dumps({
                'type': 11,
                'content': content,
            }))
        except Exception as e:
            logger.critical('Websocket接続でエラーが発生しました。')
            logger.critical(e)
            # raise
