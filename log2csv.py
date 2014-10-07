#!/usr/bin/env python
# coding: utf-8

"""
Small tool to convert Apache log files to csv.
Written by Paul Biester (http://isonet.fr)
This package is © 2014 Paul Biester, released under the terms of the GNU GPL v3 (or at your option a later version)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = "Paul Biester"
__copyright__ = "Copyright 2014, Paul Biester"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Paul Biester"
__email__ = "p.biester@isonet.fr"
__status__ = "Beta"

import csv
import apache_log_parser
import argparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def main(**kwargs):

    print('Converting, please wait...')

    line_parser = apache_log_parser.make_parser(kwargs['format'])
    header = True

    with open(kwargs['input'], 'rb') as inFile, open(kwargs['output'], 'w') as outFile:

        lines = inFile.readlines()
        writer = csv.writer(outFile, delimiter=';')

        for line in lines:
            try:
                log_line_data = line_parser(line)
            except apache_log_parser.LineDoesntMatchException as ex:
                print(bcolors.FAIL + 'The format specified does not match the log file. Aborting...' + bcolors.ENDC)
                print('Line: ' + ex.log_line + 'RegEx: ' + ex.regex)
                exit()

            if header:
                writer.writerow(list(log_line_data.keys()))
                header = False
            else:
                writer.writerow(list(log_line_data.values()))

    print(bcolors.OKGREEN + 'Conversion finished.' + bcolors.ENDC)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Apache logs to csv', version='%(prog)s 1.0')
    parser.add_argument('format', type=str, help='Apache log format (see http://httpd.apache.org/docs/2.2/logs.html)')
    parser.add_argument('input', type=str, help='Input log file ex. /var/log/apache/access.log')
    parser.add_argument('output', type=str, help='Output csv file ex. ~/accesslog.csv')
    args = parser.parse_args()
    main(**vars(args))