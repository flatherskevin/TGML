"""
Last Edited By: Kevin Flathers
Date Last Edited: 06/26/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from lxml import etree
import os
from os.path import splitext
from .errors import *

class Tgml:
	properties = {
		'Id': '',
		'Name': '',
		'Background': '#FFFFFF',
		'Stretch': 'Uniform',
		'UseGlobalScripts': 'False',
		'DisablePanAndZoom': 'False',
		'GridSize': '10',
		'Height': '600',
		'Width': '800'
	}

	exposed_properties = {}
	
	DEFAULT_PROPERTIES = {
		'Id': '',
		'Name': '',
		'Background': '#FFFFFF',
		'Stretch': 'Uniform',
		'UseGlobalScripts': 'False',
		'DisablePanAndZoom': 'False',
		'GridSize': '10',
		'Height': '600',
		'Width': '800'
	}

	SUPPORTED_CHILDREN = (
		'Animate',
		'AnimatedImage',
		'Arc',
		'Bind',
		'Chord',
		'Component',
		'Curve',
		'Ellipse',
		'Expose',
		'Group',
		'Image',
		'Layer',
		'Line',
		'Metadata',
		'Path',
		'Pie',
		'Polygon',
		'Polyline',
		'Rectangle',
		'Script',
		'TargetArea',
		'Text',
		'TextBox'
	)

	def __init__(self, obj_in, input_type='file'):
		self.obj_in = obj_in
		
		#obj_in is a tgml file
		if input_type == 'file':
			self.element = self.read_tgml_file(self.obj_in)
		
		#obj_in is the immediate child of the Tgml tag in a file
		#Helps with creating objects from dependency files
		elif input_type == 'child':
			self.element = self.read_tgml_file(self.obj_in)
			self.element = self.element[0]
			
		#obj_in is an etree.Element object
		elif input_type == 'element':
			self.element = self.obj_in
			
		#obj_in is a string
		elif input_type == 'blank':
			self.element = etree.Element(obj_in)
		else:
			raise BadInputObject('Input type does not exist')

	def __call__(self):
		return self.element

	#Fixes CDATA issue with all scripts under 'element'
	def fix_cdata(self):
		for script in self.element.xpath('.//Script'):
			script.text = etree.CDATA(script.text)
		for text in self.element.xpath('.//Text'):
			content = None
			if text.get('Content') not in ['', None]:
				content = text.get('Content')
			else:
				if str(text.text).isspace():
					content = ''
				else:
					content = text.text
			text.text = etree.CDATA(content)
			etree.strip_attributes(text, 'Content')
		for text_box in self.element.xpath('.//TextBox'):
			if text_box.get('Content') not in ['', None]:
				content = text_box.get('Content')
				#text_box.text = etree.CDATA(text_box.get('Content'))
			else:
				if str(text_box.text).isspace():
					content = ''
				else:
					content = text_box.text
			text_box.text = etree.CDATA(content)
			etree.strip_attributes(text_box, 'Content')

	#Set a value to all exposed attributes nested beneath an element
	def set_exposed_properties(self, exposed_properties):
		for key in exposed_properties.keys():
			for item in self.element.xpath('.//*'):
				if item.get('ExposedAttribute') != '':
					expose = str(item.get('Name')).replace(' ', '')
				if expose == key:
					item.getparent().set(item.get('ExposedAttribute'), exposed_properties[key])

	#Compiles the Tgml object
	def compile(self, validate_element=True):
		try:
			if validate_element:
				self.validate_element()
			self.set_properties(self.properties)
			self.set_exposed_properties(self.exposed_properties)
			self.fix_cdata()
		except Exception as err:
			print(err)

	#Transforms the Tgml object
	def transform(self):
		raise NotImplementedError

	#Sets Tgml properties
	#Takes in a dictionary
	def set_properties(self, properties):
		for key in properties.keys():
			self.element.set(key, properties[key])

	#Check if property is set to a value, then set it to a new value
	def checkset_property(self, element, attribute, value, value_check='None'):
		if(str(element.get(attribute)) == value_check):
			element.set(attribute, value)

	#Return etree object from file
	def read_from_file(self, file):
		with open(file, 'r') as file:
			return etree.fromstring(file.read())

	#Checks file for Tgml properties and returns etree object, or returns 0 if an error occurs
	def read_tgml_file(self, file):
		if(self.validate_file(file)):
			self.element = self.read_from_file(file)
		else:
			self.element = etree.Element('Tgml')

	#Writes content to a file
	def write_to_file(self, directory, name):
		with open(os.path.join(directory, name + '.tgml'), 'w') as save_file:
			save_file.write(etree.tostring(self.element).decode('utf-8'))

	#Checks to see if a file is properly setup for use as a TGML
	def validate_file(self, file, extension_check=True, tag_check=False):
		try:
			if extension_check:
				if(str(splitext(file)[1]) != '.tgml'):
					raise BadTgmlFileError('File is not a .tgml file')
			if tag_check:
				if(etree.tostring(self.element.tag) != 'Tgml'):
					raise BadTGMLFileError('TGML file does not contain a <Tgml> or <Tgml/> tag at the beginning / end of the file')
			return 1
		except Exception as err:
			print(err)
			return 0

	#Checks that element contents are supported
	def validate_element(self, children_check=False):
		if children_check:
			for child in self.element.xpath('./*'):
				if child.tag not in self.SUPPORTED_CHILDREN:
					raise BadElementChildError('Element does not support this child: ' + str(child.tag))