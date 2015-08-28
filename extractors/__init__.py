__author__ = 'Mark Polak'

from namesExtractor import NamesExtractor
from equalItemsComparator import equal_items

EXTRACTORS = {'names': NamesExtractor.parse}
COMPARATORS = {'equal_items': equal_items}
