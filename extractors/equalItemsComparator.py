__author__ = 'markadm'
import json

def equal_items(left, right):

    if left == None and right == None:
        return True

    if isinstance(right, basestring):
        jsonList = '{"list":' + right.replace("'", '"') + '}'

        try:
            right = json.loads(jsonList)['list']
        except:
            print('Could not read the "expected value"')

    if not isinstance(left, list) or not isinstance(right, list):
        return False

    return sorted(left) == sorted(right)
