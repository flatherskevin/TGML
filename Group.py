"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from Tgml import Tgml

class Group(Tgml):
	properties = {}
	DEFAULT_PROPERTIES = {}
	SUPPORTED_CHILDREN = {}

	def __init__(self, *args, input_type='blank', **kwargs):
		super(Table, self).__init__(*args, input_type, **kwargs)