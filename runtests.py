#!/usr/bin/env python

from __future__ import print_function
from subprocess import check_output, CalledProcessError, STDOUT
import os
import glob


def getTestFiles():
    current_path = os.path.dirname(os.path.realpath(__file__))
    return glob.glob(current_path + '/*.yaml')


def runTestFile(file):
   check_output(["resttest.py", "https://apps.dhis2.org/dev", file], stderr=STDOUT)



def main():
    files = getTestFiles()
    passes = True
    for yaml in files:
        try:
            runTestFile(yaml)
        except CalledProcessError,e:
            print (e)
            passes = False
    return passes

if __name__ == "__main__":
    success = main()
    if not success:
        raise Exception
