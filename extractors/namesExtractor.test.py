__author__ = 'Mark Polak'

import unittest
from namesExtractor import NamesExtractor
from pyresttest import validators

class TestNamesExtractor(unittest.TestCase):

  def test_has_extract_internal_method(self):
      NamesExtractor().extract_internal()

  def test_has_class_method_parse(self):
      NamesExtractor.parse(config={'template': ''})

  def test_extends_AbstractExtractor(self):
      self.assertTrue(issubclass(NamesExtractor, validators.AbstractExtractor))

  def test_should_have_extractor_name(self):
      self.assertEqual(NamesExtractor().extractor_type, 'names')

  def test_should_not_be_a_header_extractor(self):
      self.assertFalse(NamesExtractor().is_header_extractor)

  def test_should_be_a_body_extractor(self):
      self.assertTrue(NamesExtractor().is_body_extractor)

  def test_should_return_the_name_properties(self):
      source_body = """{"attributes": [{"name":"aggregationType","simple":true},{"name":"dimensionType","simple":true},{"name":"code","simple":true},{"name":"access","simple":false},{"name":"numberType","simple":true},{"name":"domainType","simple":true},{"name":"displayName","simple":true},{"name":"publicAccess","simple":true},{"name":"description","simple":true},{"name":"type","simple":true},{"name":"displayShortName","simple":true},{"name":"externalAccess","simple":true},{"name":"lastUpdated","simple":true},{"name":"optionSet","simple":false},{"name":"categoryCombo","simple":false},{"name":"formName","simple":true},{"name":"commentOptionSet","simple":false},{"name":"href","simple":true},{"name":"id","simple":true},{"name":"dimension","simple":true},{"name":"displayDescription","simple":true},{"name":"userGroupAccess","simple":false},{"name":"allItems","simple":true},{"name":"created","simple":true},{"name":"attributeValue","simple":false},{"name":"dataElementGroup","simple":false},{"name":"textType","simple":true},{"name":"displayFormName","simple":true},{"name":"zeroIsSignificant","simple":true},{"name":"url","simple":true},{"name":"filter","simple":true},{"name":"aggregationOperator","simple":true},{"name":"legendSet","simple":false},{"name":"name","simple":true},{"name":"dataSet","simple":false},{"name":"aggregationLevels","simple":true},{"name":"dataDimension","simple":true},{"name":"shortName","simple":true},{"name":"item","simple":true},{"name":"user","simple":false},{"name":"optionSetValue","simple":true}]}"""
      expected_list = ["aggregationType", "dimensionType", "code", "access", "numberType", "domainType", "displayName", "publicAccess", "description", "type", "displayShortName", "externalAccess", "lastUpdated", "optionSet", "categoryCombo", "formName", "commentOptionSet", "href", "id", "dimension", "displayDescription", "userGroupAccess", "allItems", "created", "attributeValue", "dataElementGroup", "textType", "displayFormName", "zeroIsSignificant", "url", "filter", "aggregationOperator", "legendSet", "name", "dataSet", "aggregationLevels", "dataDimension", "shortName", "item", "user", "optionSetValue"]

      self.assertItemsEqual(NamesExtractor().extract_internal(query='attributes', body=source_body), expected_list)

  def test_should_return_an_empty_list_when_the_list_does_not_exist(self):
      source_body = """{"name": "Mark"}"""

      self.assertEqual(NamesExtractor().extract_internal(query='attributes', body=source_body), None)

  def test_should_return_None_when_the_body_does_not_exist(self):
      source_body = None

      self.assertEqual(NamesExtractor().extract_internal(query='attributes', body=source_body), None)

  def test_should_return_an_empty_list_when_the_property_is_an_empty_list(self):
      source_body = """{"attributes": []}"""
      expected_list = []

      self.assertItemsEqual(NamesExtractor().extract_internal(query='attributes', body=source_body), expected_list)

if __name__ == '__main__':
    unittest.main()
