"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from .Tgml import *

class Metadata(Tgml):
	
	DEFAULT_PROPERTIES = {}
	SUPPORTED_CHILDREN = {}

	def __init__(self, *args, input_type='blank', **kwargs):
		super().__init__(*args, input_type, **kwargs)
		self.__properties = {}
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