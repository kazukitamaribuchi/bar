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

class OrderConsumer(WebsocketConsumer):
    def connect(self):
        logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        self.accept()

    def disconnect(self, close_code):
        logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        pass

    def receive(self, text_data):
        logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

# class OrderConsumer(AsyncWebsocketConsumer):
#
#     groups = ['broadcast']
#
#     async def connect(self):
#         logger.info('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
#         # logger.info('CONNECT')
#         # logger.info(self)
#         # logger.info(self.scope)
#         await self.accept()
#         # try:
#         #     self.user_group_name = self.scope['url_route']['kwargs']['username']
#         #     await self.channel_layer.group_add(
#         #         self.user_group_name,
#         #         self.channel_name
#         #     )
#         #     await self.accept()
#         # except Exception as e:
#         #     logger.error('Exception起きてるよ！！！！！！！！！！！！')
#         #     logger.error(e)
#         #     raise
#
#     async def websocket_connect(self, message):
#         """
#         Called when a WebSocket connection is opened.
#         """
#         try:
#             for group in self.groups:
#                 await self.channel_layer.group_add(group, self.channel_name)
#         except AttributeError:
#             logger.error('AttributeError')
#             # raise InvalidChannelLayerError(
#             #     "BACKEND is unconfigured or doesn't support groups"
#             # )
#         try:
#             await self.connect()
#         except AcceptConnection:
#             logger.error('AcceptConnection')
#             await self.accept()
#         except DenyConnection:
#             logger.error('DenyConnection')
#             await self.close()
#
#     async def disconnect(self, close_code):
#         logger.debug('【【DISCONNECT】】')
#         await self.channel_layer.group_discard(
#             self.user_group_name,
#             self.channel_name
#         )
#         await self.close()
#
#     async def order(self, event):
#         logger.debug('=====Order=====')
#         try:
#             content = event['content']
#             await self.send(text_data=json.dumps({
#                 'type': 'order',
#                 'content': content,
#             }))
#         except Exception as e:
#             raise


# class MessageConsumer(AsyncWebsocketConsumer):
#     """
#     メッセージ関連のコンシューマー
#     """
#
#     groups = ['broadcast']
#
#     async def connect(self):
#         logger.info('コネクト')
#         try:
#             await self.accept()
#             self.room_group_name = self.scope['url_route']['kwargs']['room_name']
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )
#         except Exception as e:
#             raise
#
#     async def disconnect(self, close_code):
#         logger.info('ディスコネクト')
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.close()
#
#     async def receive(self, text_data):
#         logger.info('受信')
#         try:
#             text_data_json = json.loads(text_data)
#             logger.info(text_data_json)
#             roomId = text_data_json['roomId']
#             content = text_data_json['content']
#             sender = text_data_json['sender']
#             receiver = text_data_json['receiver']
#             await self.createMessage(text_data_json)
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'chat_message',
#                     'roomId': roomId,
#                     'content': content,
#                     'sender': sender,
#                     'receiver': receiver,
#                 }
#             )
#         except Exception as e:
#             raise
#
#     async def chat_message(self, event):
#         try:
#             content = event['content']
#             sender = event['sender']
#             receiver = event['receiver']
#             await self.send(text_data=json.dumps({
#                 'type': 'chat_message',
#                 'content': content,
#                 'sender': sender,
#                 'receiver': receiver,
#                 'id': self.message_id,
#                 'deleted': False,
#             }))
#         except Exception as e:
#             raise
#
#     async def read_message(self, event):
#         try:
#             data = event['data']
#             await self.send(text_data=json.dumps({
#                 'type': 'read_message',
#                 'data': data,
#             }))
#         except Exception as e:
#             raise
#
#     @database_sync_to_async
#     def createMessage(self, event):
#         logger.info('作成')
#         try:
#             room = Room.objects.get(id=event['roomId'])
#             sender = mUser.objects.get(username=event['sender'])
#             receiver = mUser.objects.get(username=event['receiver'])
#             msg = Message.objects.create(
#                 room=room,
#                 content=event['content'],
#                 sender=sender,
#                 receiver=receiver,
#             )
#             self.message_id = str(msg.id)
#         except Exception as e:
#             raise
#
#
# class NotificationConsumer(AsyncWebsocketConsumer):
#     """
#     通知関連のコンシューマー
#     """
#
#     groups = ['broadcast']
#
#     async def connect(self):
#         logger.debug('【【CONNECT】】')
#         self.accept()
#         try:
#             self.user_group_name = self.scope['url_route']['kwargs']['username']
#             await self.channel_layer.group_add(
#                 self.user_group_name,
#                 self.channel_name
#             )
#             await self.accept()
#         except Exception as e:
#             raise
#
#     async def disconnect(self, close_code):
#         logger.debug('【【DISCONNECT】】')
#         await self.channel_layer.group_discard(
#             self.user_group_name,
#             self.channel_name
#         )
#         await self.close()
#
#     async def notification(self, event):
#         logger.debug('=====NOTIFICATION=====')
#         try:
#             content = event['content']
#             await self.send(text_data=json.dumps({
#                 'type': 'notification',
#                 'content': content,
#             }))
#         except Exception as e:
#             raise
#
#     async def message_notification(self, event):
#         logger.debug('=====MESSAGE_NOTIFICATION=====')
#         try:
#             content = event['content']
#             await self.send(text_data=json.dumps({
#                 'type': 'message_notification',
#                 'content': content,
#             }))
#         except Exception as e:
#             raise
