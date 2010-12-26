#!/usr/bin/env python
# encoding: utf-8
"""
assignment_tests.py

Created by Robert Höglund on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import unittest
from mock import Mock
from assignment import *

class ClientHelperMock(object):
	def send(self, message):
		self.sent_message = message
	
class TalkClientTests(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_login(self):
		helper = ClientHelperMock()
		talkClient = TalkClient(helper)
		talkClient.login('demouser', 'password')
		self.assertEquals({'command':'login','user':'demouser','password':'password'}, helper.sent_message)


    
if __name__ == '__main__':
	unittest.main()