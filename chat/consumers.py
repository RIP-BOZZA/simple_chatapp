import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

'''
incomming connetions divided into 3 parts or functions mainly

def connect ---   what to do when arriving incoming connections

def recieve -- what to do with new messages

def disconnect -- what to do when disconnectiong

'''

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='test'# we can create dynamic group name if we want

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept() # accepting the connection

        # self.send(text_data=json.dumps(
        #     {
        #         'type':'connection-established',
        #         "message":"success,you are connected"
        #     }
        # ))


    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json=json.loads(text_data)
        message=text_data_json["message"]

        # print("mes=",message)

        # self.send(text_data=json.dumps(
        #     {
        #         "type":"chat",
        #         "message":message
        #     }
        # ))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":'chat_message',# function name to handle the message
                "message":message
            }
        )

    def chat_message(self,event):
        message=event["message"]

        self.send(text_data=json.dumps(
            {
                "type":"chat",
                "message":message
            }
        ))


'''
to get send messsage across multiple tabs/multiple persons in real time ,we need to enable channel layers

chanel has group and layers
groups are chat roooms which stores user data ..etc these rooms stored in an inmemory database

in a bunch of groups we have channles/users 
so we need to add user/channel  into groups so that the message receive in that room

so we need to add channel layer settings in django
'''