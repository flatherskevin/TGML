"""
Last Edited By: Kevin Flathers
Date Las Edited: 06/07/2017

Author: Kevin Flathers
Date Created: 05/27/2017

Purpose:
"""

from lxml import etree
from os.path import splitext
from errors.py import *

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
			self.read_tgml_file(self.obj_in)
		
		#obj_in is the immediate child of the Tgml tag in a file
		#Helps with creating objects from dependency files
		elif input_type == 'child':
			self.read_tgml_file(self.obj_in)
			self.element = self.element[0]
			
		#obj_in is an etree.Element object
		elif input_type == 'element':
			self.element = self.obj_in
			
		#obj_in is a string
		elif input_type == 'blank':
			self.element == etree.Element(obj_in)
		else:
			raise BadInputObject('Input type does not exist')

	#Fixes CDATA issue with all scripts under 'element'
	def fix_scripts(self, element):
		for script in element.xpath('.//Script'):
			script.text = etree.CDATA(script.text)

	#Set a value to all exposed attributes nested beneath an element
	def set_exposed_properties(self, element, value=''):
		for item in element.xpath(".//*[@Name='RmLabel']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	#Compiles the Tgml object
	def compile(self):
		raise NotImplementedError

	#Sets Tgml object properties
	def set_properties(self):
		raise NotImplementedError

	#Transforms the Tgml object
	def transform(self):
		raise NotImplementedError

	#Sets Tgml properties
	#Takes in a dictionary
	def set_properties()(self, properties):
		for key in properties.keys():
			self.checkset_property(self.element, key, properties[key])

	#Check if property is set to a value, then set it to a new value
	def checkset_property(self, element, attribute, value, value_check='None'):
		if(str(element.get(attribute)) == value_check):
			element.set(attribute, value)

	#Return etree object from file
	def read_from_file(self, file):
		with open(highLight_Script_PATH, 'r') as file:
			if(validate_file(file)):
				return etree.fromstring(file.read())

	#Checks file for Tgml properties and returns etree object, or returns 0 if an error occurs
	def read_tgml_file(self, file):
		if(self.validate_file(file)):
			self.element = self.prepare_element((self.read_from_file(file)))
		else:
			self.element = etree.Element('Tgml')

	#Writes content to a file
	def write_to_file(self, content, directory, name):
		with open(os.path.join(directory, name + '.tgml'), 'w') as save_file:
			save_file.write(content.decode('utf-8'))

	#Checks to see if a file is properly setup for use as a TGML
	def validate_file(self, file, extension_check=True, tag_check=True):
		try:
			if extension_check:
				if(str(splitext(file)[1]) != '.tgml'):
					raise BadTgmlFileError("File is not a .tgml file")
			tree = self.read_from_file(file)
			if tag_check:
				if(str(tree.tag) == 'Tgml'):
					return 1
				else:
					raise BadTGMLFileError('TGML file does not contain a <Tgml> or <Tgml/> tag at the beginning / end of the file')
		except:
			return 0

	#Checks that element contents are supported
	def validate_element(self, children_check=True):
		if children_check:
			for child in self.element.xpath("./*"):
				if child.tag not in SUPPORTED_CHILDREN:
					raise BadElementChilderror('Element does not support this child: ' + str(child.tag))