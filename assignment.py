#!/usr/bin/env python
# encoding: utf-8
"""
assignment.py

Created by Robert Höglund on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class TalkClient(object):
	"""docstring for TalkClient"""
	def __init__(self):
		super(TalkClient, self).__init__()

	def send(self, message):
		"""sends a message to the server"""
		pass
	
	def receive(self, message):
		"""called when a message is received from the server"""
		pass
		
	def timeout(self, message):
		"""called when there was a timeout sending a message"""
		pass