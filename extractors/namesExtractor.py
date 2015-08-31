__author__ = 'Mark Polak'

from pyresttest.validators import AbstractExtractor
import json

class NamesExtractor(AbstractExtractor):
    extractor_type = 'names'
    is_header_extractor = False
    is_body_extractor = True

    def extract_internal(self, query=None, args=None, body=None, headers=None):
        if not body:
            return None
        return self.query_dictionary(query, json.loads(body))

    @staticmethod
    def query_dictionary(query, dictionary, delimiter='.'):
        """ Do an xpath-like query with dictionary, using a template if relevant """
        # Based on http://stackoverflow.com/questions/7320319/xpath-like-query-for-nested-python-dictionaries

        try:
            dictionary = [item['name'] for item in dictionary[query]]
        except:
            return None
        return dictionary

    @classmethod
    def parse(cls, config, extractor_base=None):
        base = NamesExtractor()

        return cls.configure_base(config, base)
