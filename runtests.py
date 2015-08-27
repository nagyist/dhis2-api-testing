#!/usr/bin/env python

from __future__ import print_function
from subprocess import call
import os
import glob

def getTestFiles():
    current_path = os.path.dirname(os.path.realpath(__file__));
    return glob.glob(current_path + '/*.yaml');    

def runTestFile(file):
    call(["resttest.py", "https://apps.dhis2.org/dev/", file])

map(lambda file: runTestFile(file), getTestFiles())
