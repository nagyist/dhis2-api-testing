#!/usr/bin/env python

from __future__ import print_function
from subprocess import check_output, CalledProcessError, STDOUT
from glob import glob
import os
import sys
import ConfigParser


# TODO: Include this as part of the configuration file
def getTestFiles(current_path):
    return glob(current_path + '/**/*.yaml') + glob(current_path + '/**/**/*.yaml')


def runTestFile(file, server):
    check_output(["resttest.py", server, file, \
                  '--import_extensions', 'extractors'], stderr=STDOUT)


# TODO: Make sure there are defaults here, or abort otherwise
def initConfig(filename):
    config = ConfigParser.ConfigParser()
    config.read( filename )
    return config


def main():
    current_path = os.path.dirname(os.path.realpath(__file__))
    if (len(sys.argv)) > 1:
        config_file = current_path  + '/' + sys.argv[1]
    else:
        config_file = current_path  + '/' + 'apitests.default'
    config = initConfig( config_file )
    server = config.get('Server', 'baseurl')
    files = getTestFiles( current_path )
    passes = True
    for yaml in files:
        try:
            runTestFile(yaml, server)
        except CalledProcessError, e:
            print(e)
            passes = False
    return passes


if __name__ == "__main__":
    success = main()
    print(success)
    if not success:
        raise Exception
