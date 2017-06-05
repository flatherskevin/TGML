
from lxml import etree
from os.path import splitext
from errors.py import *

#This is a Git Test Comment
#my milkshake brings all the boys to the yard

class TGML:
	properties = {
		'Id': '',
		'Name', '',
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
		'Name', '',
		'Background': '#FFFFFF',
		'Stretch': 'Uniform',
		'UseGlobalScripts': 'False',
		'DisablePanAndZoom': 'False',
		'GridSize': '10',
		'Height': '600',
		'Width': '800'
	}

	def __init__(self, obj_in, input_type='file'):
		self.obj_in = obj_in
		if input_type == 'file':
			read_tgml_file(self.obj_in)
		elif input_type == 'element':
			self.element = self.obj_in
		else:
			raise BadInputObject 'The object input to the TGML o'

	#Fixes CDATA issue with all scripts under 'element'
	def fix_scripts(self, element):
		for script in element.xpath('.//Script'):
			script.text = etree.CDATA(script.text)

	#Set a value to all exposed attributes nested beneath an element
	def set_exposed_properties(self, element, value=''):
		for item in element.xpath(".//*[@Name='RmLabel']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	#Compiles the TMGML object
	def compile(self):
		raise NotImplementedError

	#Sets TGML object properties
	def set_properties(self):
		raise NotImplementedError

	#Transforms the TGML object
	def transform(self):
		raise NotImplementedError

	#Prepares an element document for successful use
	def set_properties()(self, properties):
		for key in properties.keys():
			self.checkset_property(self.element, key, properties[key])

	#Check if property is set to a value, then set it to a new value
	def checkset_property(self, element,attribute, value, valueCheck='None'):
		if(str(element.get(attribute)) == valueCheck):
			element.set(attribute, value)

	#Return etree object from file
	def read_from_file(self, file):
		with open(highLight_Script_PATH, 'r') as file:
			if(check_file_contents(file)):
				return etree.fromstring(file.read())

	#Checks file for tmgl properties and returns etree object, or returns 0 if an error occurs
	def read_tgml_file(self, file):
		if(self.check_file_contents(file)):
			self.element = self.prepare_element((self.read_from_file(file)))
		else:
			return etree.Element('Tgml')

	#Writes content to a file
	def write_to_file(self, content, directory, name):
		with open(os.path.join(directory, name + '.tgml'), 'w') as save_file:
			save_file.write(content.decode('utf-8'))

	#Checks to see if a file is properly setup for use as a TGML
	def check_file_contents(self, file):
		try:
			if(str(splitext(file)[1]) != '.tgml'):
				raise BadTGMLFileError("File is not a .tgml file")
			tree = self.read_from_file(file)
			if(str(tree.tag) == 'Tgml'):
				return 1
			else:
				raise BadTGMLFileError("TGML file does not contain a <Tgml> or <Tgml/> tag at the beginning of the file")
		except:
			return 0

	def compile(self, element):
		self.fix_scripts(element)