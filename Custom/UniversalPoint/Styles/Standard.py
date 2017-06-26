"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/26/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from .UniversalPoint import *

class Standard(UniversalPoint):
	exposed_properties['Title'] = ''
	exposed_properties['Subtitle'] = ''

	def __init__(self):
		super().read_tgml_file(os.path.join(os.path.dirname(__file__), 'Standard.tgml'))
		self.element = self.element[0]