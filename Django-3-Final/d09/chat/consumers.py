import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, Chatroom
from django.core.cache import cache

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']

        self.room_group_name = 'chat_%s' % self.room_id
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        if self.user.is_authenticated:
            
            cache_key = f'online_users_{self.room_group_name}'
            users_online = cache.get(cache_key, set())
            users_online.add(self.user.username)
            cache.set(cache_key, users_online)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list',
                    'users': list(users_online)
                }
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': f'{self.user.username} has joined the chat',
                    'username': self.user.username
                }
            )
    
    async def disconnect(self, close_code):

        if self.user.is_authenticated:
            cache_key = f'online_users_{self.room_group_name}'

            users_online = cache.get(cache_key, set())
            users_online.discard(self.user.username)
            cache.set(cache_key, users_online)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list',
                    'users': list(users_online)
                }
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': f'{self.user.username} has left the chat',
                    'username': self.user.username
                }
            )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': event['users']
        }))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        await self.save_message(user, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': user.username
            }
        )
    @database_sync_to_async
    def save_message(self, user, content):
        room = Chatroom.objects.get(id=self.room_id)
        return Message.objects.create(
            sender=user,
            content=content,
            room=room
        )
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        message_html = f"<div hx-swap-oob='beforeend:#messages'><p><b>{username}</b>: {message}</p></div>"
        await self.send(text_data=json.dumps({
            'message': message_html,
            'username': username
        }))