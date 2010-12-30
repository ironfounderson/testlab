#!/usr/bin/env python
# encoding: utf-8
"""
assignment.py

Created by Robert Höglund on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class ChatService(object):
    def __init__(self, callback):
        super(ChatService, self).__init__()
        self.callback = callback
        
    def send(self, message):
        """sends a message to the server"""
        pass
        
class SimplifiedChatClient(object):
    """Simplified ChatClient"""
    def __init__(self):
        super(SimplifiedChatClient, self).__init__()
        self.chat_service = ChatService(self)
        
    def response(self, message):
        """invoked from chat_service when there is a response or message 
            from the server"""
        print message
        
    def send(self, message):
        """passes on the message to the chat_service"""
        self.chat_service(message)
        
class ChatClient(object):
    """docstring for ChatClient"""
    def __init__(self, chat_service):
        super(ChatClient, self).__init__()
        self.chat_service = chat_service
        self.chat_service.callback = self
    
    def login(self, user, password):
        """Sends a properly encoded login message to the chat_service"""
        message = {'command':'login', 'user':user, 'password':password}
        self.chat_service.send(message)
    
    def logout(self):
        """Sends a properly encoded logout message to the chat_service"""
        message = {'command':'logout'}
        self.chat_service.send(message)        
    
    def send_message(self, user_id, message):
        """sends a message to the user with user_id"""
        message = {'command':'send-message', 'to':user_id, 'message':message}
        self.chat_service.send(message)        
    
    def send_friend_request(self, user_id):
        """sends a friend request to the user with user_id"""
        message = {'command':'send-friend-request', 'to':user_id}
        self.chat_service.send(message)        
    
    def set_status(self, status):
        """sets the current status of the current user"""
        pass
    
    def get_friend_list(self):
        """returns a list of all the friends of the current logged in user"""
        pass
    
    def get_status(self):
        """returns the current status of the current user"""
        pass
    
    def get_messages(self):
        """returns a list of all the messages received since 
            the last time this method was called"""
        pass
    
    def response(self, message):
        """handles the callback from the chat_service"""
        pass
    
