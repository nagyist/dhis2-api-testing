#!/usr/bin/env python

from __future__ import print_function
from subprocess import check_call, CalledProcessError
from glob import glob
import os

def getTestFiles():
    current_path = os.path.dirname(os.path.realpath(__file__));
    return glob(current_path + '/**/*.yaml') + glob(current_path + '/**/**/*.yaml');


def runTestFile(file):
    try:
        output = check_call(["resttest.py", "https://apps.dhis2.org/dev", file, '--import_extensions', 'extractors'])
    except CalledProcessError as e:
        print(e.returncode)

map(lambda file: runTestFile(file), getTestFiles())
