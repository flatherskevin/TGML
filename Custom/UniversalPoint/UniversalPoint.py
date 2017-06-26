"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from ...Tgml import *

class UniversalPoint(Tgml):
	properties = {
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
	exposed_properties = {
		'PointBind': 'Universal',
		'PointType': 'Analog',
		'BindValue': 'Value',
		'BindAlarm': 'Alarm',
		'Units': '',
		'Decimals': '1',
		'DigitalOff': 'Off',
		'DigitalOn': 'On',
		'Multistate Text': '',
		'Viconics': 'False',
		'AnalogConversion': 'False',
		'ConversionInputMin': '0',
		'ConversionInputMax': '10',
		'ConversionOutputMin': '0',
		'ConversionOutputMax': '100'
	}
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

	def __init__(self):
		super().read_tgml_file(os.path.join(os.path.dirname(__file__), 'UniversalPoint.tgml'))
		self.element = self.element[0]