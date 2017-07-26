"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

import datetime
from .Tgml import *

class Metadata(Tgml):
	
	DEFAULT_PROPERTIES = {}
	SUPPORTED_CHILDREN = {}

	def __init__(self, *args, input_type='blank', **kwargs):
		super().__init__(*args, input_type=input_type, **kwargs)
		self.__properties = {
			'Id': '',
			'Name': '',
			'Value': ''
		}
		self.__exposed_properties = {}

	@property
	def properties(self):
		return self.__properties

	@properties.setter
	def properties(self, value):
		self.__properties = value

	@property
	def exposed_properties(self):
		return self.__properties

	@exposed_properties.setter
	def exposed_properties(self, value):
		self.exposed_properties = value

	def version_tag(self, name, version):
		self.__properties['Name'] = 'Creation Info'
		date = datetime.datetime.now().strftime('%B %d, %Y')
		self.__properties['Value'] = 'Created on {date} using {name} - {version}'.format(name=name, version=version, date=date)