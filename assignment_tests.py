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
        self.sent_message = message
        
class ChatClientTests(unittest.TestCase):
    """Tests for implementing the chat client"""
    
    def test_login_using_mock(self):
        """login calls our mock with a properly encoded message"""
        # Arrange
        chat_service_mock = ChatServiceMock()
        chat_client = ChatClient(chat_service_mock)
        # Act
        chat_client.login('user-name', 'passw0rd')
        # Assert
        expected_message = {'command':'login', 
                            'user':'user-name', 'password':'passw0rd'}
        self.assertEquals(expected_message, chat_service_mock.sent_message)
        
if __name__ == '__main__':
    unittest.main()