#!/usr/bin/env python
# encoding: utf-8
"""
assignment_tests.py

Created by Robert Höglund on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import unittest
from assignment import ChatClient

class ChatServiceMock(object):
    """Mock class for ChatService"""
    def __init__(self):
        super(ChatServiceMock, self).__init__()
        self.sent_message = None

    def send(self, message):
        """saves the message for assert"""
        self.sent_message = message

class ChatClientSendTests(unittest.TestCase):
    """Tests checking that the send methods works as expected"""

    def setUp(self):
        """set up a test case"""
        # Arrange
        self.chat_service_mock = ChatServiceMock()
        self.chat_client = ChatClient(self.chat_service_mock)

    def test_login_using_mock(self):
        """login calls our mock with a properly encoded message"""
        # Act
        self.chat_client.login('user-name', 'passw0rd')
        # Assert
        expected_message = {'command':'login',
                            'user':'user-name', 'password':'passw0rd'}
        self.assertEquals(expected_message,
                          self.chat_service_mock.sent_message)

    def test_logout_using_mock(self):
        """logout calls our mock with a properly encoded message"""
        # Act
        self.chat_client.logout()
        # Assert
        expected_message = {'command':'logout'}
        self.assertEquals(expected_message,
                          self.chat_service_mock.sent_message)

    def test_send_message_using_mock(self):
        """send_message calls our mock with a properly encoded message"""
        # Act
        self.chat_client.send_message('user123', 'Hello')
        # Assert
        expected_message = {'command':'send-message', 'to':'user123',
                            'message':'Hello'}
        self.assertEquals(expected_message,
                          self.chat_service_mock.sent_message)

    def test_send_friend_request_using_mock(self):
        """send_friend_request calls our mock with a properly encoded message"""
        # Act
        self.chat_client.send_friend_request('user123')
        # Assert
        expected_message = {'command':'send-friend-request', 'to':'user123'}
        self.assertEquals(expected_message,
                          self.chat_service_mock.sent_message)

    def test_set_status_using_mock(self):
        """set_status calls our mock with a properly encoded message"""
        # Act
        self.chat_client.set_status('away')
        # Assert
        expected_message = {'command':'set-status', 'value':'away'}
        self.assertEquals(expected_message,
                          self.chat_service_mock.sent_message)

class ChatClientResponseTests(unittest.TestCase):
    """Tests checking that the response method works as expected."""

    def test_get_status(self):
        """get_status returns offline when starting out"""
        # Arrange
        chat_client = self._create_chat_client()
        # Act
        status = chat_client.get_status()
        # Assert
        self.assertEquals('offline', status)

    def test_get_status_after_login(self):
        """get_status returns online after receiving response
        from login command
        """
        # Arrange
        chat_client = self._create_chat_client()
        # Act
        chat_client.response(self._ok_response_for('login'))
        status = chat_client.get_status()
        # Assert
        self.assertEquals('online', status)

    def test_get_status_after_logout(self):
        """get_status returns offline after receiving response
        from logout command
        """
        # Arrange
        chat_client = self._create_chat_client()
        chat_client.response(self._ok_response_for('login'))
        # Act
        chat_client.response(self._ok_response_for('logout'))
        status = chat_client.get_status()
        # Assert
        self.assertEquals('offline', status)

    def test_get_status_after_set_status(self):
        """get_status returns away after receiving response
        from set-status command
        """
        # Arrange
        chat_client = self._create_chat_client()
        # Act
        chat_client.response(self._ok_response_with_value('set-status', 'away'))
        status = chat_client.get_status()
        # Assert
        self.assertEquals('away', status)

    def test_get_friend_list_empty_list(self):
        """get_friend_list returns empty friend list"""
         # Arrange
        chat_client = self._create_chat_client()
        # Act
        friends = chat_client.get_friend_list()
        # Assert
        self.assertEquals([], friends)
        
    def test_get_friend_list_with_friends(self):
        """get_friend_list returns received friends"""
         # Arrange
        chat_client = self._create_chat_client()
        friend = self._friend('afriend', 'online')
        response = self._ok_response_with_value('friend-list', [friend])
        chat_client.response(response)
        # Act
        friends = chat_client.get_friend_list()
        a_friend = friends[0]
        # Assert
        self.assertEquals(a_friend, friend)

    def test_get_messages_empty_message_queue(self):
        """get_messages returns empty list when no messages
        have been received
        """
        # Arrange
        chat_client = self._create_chat_client()
        # Act
        messages = chat_client.get_messages()
        # Assert
        self.assertEquals([], messages)
        
    def _friend(self, name, status):
        return {'name':name,'id':name + '-id','status':status}

    def _ok_response_for(self, command):
        return {'response-to-command':command, 'response-code':'ok'}

    def _ok_response_with_value(self, command, value):
        return {'response-to-command':command, 'response-code':'ok', 
                'value':value}
        
    def _create_chat_client(self):
        """returns an instance of a ChatClient"""
        return ChatClient(ChatServiceMock())

if __name__ == '__main__':
    unittest.main()
