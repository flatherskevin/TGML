"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/26/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from ..UniversalPoint import *

class Standard(UniversalPoint):

	DEFAULT_PROPERTIES = {
		'Id': 'UP',
		'Name': 'Universal',
		'Opacity': '1.0',
		'Visibility': 'Visible',
		'Clip': 'False',
		'ContentHeight': '39.12',
		'ContentWidth': '138.16',
		'Left': '0.0',
		'Top': '0.0',
		'Height': '39.12',
		'Width': '138.16'
	}

	def __init__(self):
		super().read_tgml_file(os.path.join(os.path.dirname(__file__), 'Standard.tgml'))
		self.element = self.element[0]
		self.__properties = {
			'Id': 'UP',
			'Name': '',
			'Opacity': '1.0',
			'Visibility': 'Visible',
			'Clip': 'False',
			'ContentHeight': '39.12',
			'ContentWidth': '138.16',
			'Left': '0.0',
			'Top': '0.0',
			'Height': '39.12',
			'Width': '138.16'
		}
		self.__exposed_properties = {
			'Title': '',
			'Subtitle': '',
			'PointBind': 'Universal',
			'PointType': 'Analog',
			'BindValue': 'Value',
			'BindAlarm': 'Alarm',
			'Units': '',
			'Decimals': '1',
			'DigitalOff': 'Off',
			'DigitalOn': 'On',
			'MultistateText': '',
			'Viconics': 'False',
			'AnalogConversion': 'False',
			'ConversionInputMin': '0',
			'ConversionInputMax': '10',
			'ConversionOutputMin': '0',
			'ConversionOutputMax': '100',
			'Text Align': 'Center',
			'ToolTipText': '',
			'ToolTipFontSize': '48',
			'ToolTipFontStroke': '#404040',
			'ToolTipFill': '#E0E0E0',
			'ToolTipEnable': 'False'
		}

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