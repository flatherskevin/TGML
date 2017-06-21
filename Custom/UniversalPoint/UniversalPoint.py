"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from Tgml import Tgml

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
	exposed_properties{
		'Point Bind': 'Universal',
		'Point Type': 'Analog',
		'Bind Value': 'Value',
		'Bind Alarm': 'Alarm',
		'Units': '',
		'Decimals': '1',
		'Digital Off': 'Off',
		'Digital On': 'On',
		'Multistate Text': '',
		'Viconics': 'False',
		'Analog Conversion': 'False',
		'Conversion Input Min': '0',
		'Conversion Input Max': '10',
		'Conversion Output Min': '0',
		'Conversion Output Max': '100'
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
		super().read_tgml_file('./UniversalPoint.tgml')
		self.element = self.element[0]