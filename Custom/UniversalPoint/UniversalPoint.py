"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/26/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from ...Tgml import *

class UniversalPoint(Tgml):
	
	DEFAULT_PROPERTIES = {
		'Id': 'UP',
		'Name': 'Universal',
		'Opacity': '1.0',
		'Visibility': 'Visible',
		'Clip': 'False',
		'ContentHeight': '20',
		'ContentWidth': '125',
		'Left': '0.0',
		'Top': '0.0',
		'Height': '20',
		'Width': '125'
	}
	SUPPORTED_CHILDREN = {}

	def __init__(self, obj_in=os.path.join(os.path.dirname(__file__), 'UniversalPoint.tgml'), input_type='file'):
		super().__init__(obj_in, input_type=input_type, **kwargs)
		self.element = self.element[0]
		self.__properties = {
			'Id': 'UP',
			'Name': '',
			'Opacity': '1.0',
			'Visibility': 'Visible',
			'Clip': 'False',
			'ContentHeight': '20',
			'ContentWidth': '125',
			'Left': '0.0',
			'Top': '0.0',
			'Height': '20',
			'Width': '125'
		}
		self.__exposed_properties = {
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