#!/usr/bin/env python
# encoding: utf-8
"""
assignment.py

Created by Robert Höglund on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

class ChatClient(object):
    """docstring for ChatClient"""
    def __init__(self, chat_service):
        super(ChatClient, self).__init__()
        self.chat_service = chat_service
        self.chat_service.callback = self
        self._status = 'offline'
    
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
    
    def set_status(self, new_status):
        """sets the current status of the current user"""
        message = {'command':'set-status', 'value':new_status}
        self.chat_service.send(message)
    
    def get_friend_list(self):
        """returns a list of all the friends of the current logged in user"""
        pass
    
    def get_status(self):
        """returns the current status of the current user"""
        return self._status
    
    def get_messages(self):
        """returns a list of all the messages received since
        the last time this method was called
        """
        return []
    
    def response(self, message):
        """handles the callback from the chat_service"""
        command_response = message['response-to-command']
        if command_response == 'login':
            self._status = 'online'
        elif command_response == 'logout':
            self._status = 'offline'
        elif command_response == 'set-status':
            self._status = message['value']
