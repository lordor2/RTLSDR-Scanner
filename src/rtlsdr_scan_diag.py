#! /usr/bin/env python

#
# rtlsdr_scan_diag
#
# http://eartoearoak.com/software/rtlsdr-scanner
#
# Copyright 2012 - 2014 Al Brown
#
# A frequency scanning GUI for the OsmoSDR rtl-sdr library at
# http://sdr.osmocom.org/trac/wiki/rtl-sdr
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ctypes.util import find_library
import sys

LIBS = [('wx', 'wxPython', 'http://www.wxpython.org/download.php#stable', True, True),
        ('numpy', 'Numpy', 'http://sourceforge.net/projects/numpy/files/NumPy/', True, True),
        ('matplotlib', 'matplotlib', 'http://matplotlib.org/downloads.html', True, True),
        ('serial', 'pySerial', 'https://pypi.python.org/pypi/pyserial', True, True),
        ('rtlsdr', 'pyrtlsdr', 'https://github.com/roger-/pyrtlsdr', False, False),
        ('PIL.Image', 'Pillow', 'https://pypi.python.org/pypi/Pillow/2.6.1', True, True)]


def try_import(library):
    try:
        __import__(library)
    except:
        return False

    return True

if __name__ == '__main__':

    try:
        input = raw_input
    except:
        pass

    print 'rtlsdr_scan_diag\n'
    print 'Tests for missing libraries\n'

    version = sys.version_info
    if version < (2, 7):
        print 'Warning unsupported version, please use Python 2.7 or greater'

    problem = False

    if not find_library('rtlsdr') and not find_library('librtlsdr'):
        print 'librtlsdr not found in path'
        print "Download from 'http://sdr.osmocom.org/trac/wiki/rtl-sdr'"
        print ''
    else:
        platform = sys.platform
        for lib, name, url, package, ports in LIBS:
            print 'Testing for {}'.format(name)
            if not try_import(lib):
                problem = True
                print '{} not found'.format(name)
                if platform == 'linux' or platform == 'linux2':
                    if package:
                        print "\tInstall using the system package manager or download from '{}'".format(url)
                    else:
                        print "\tDownload from '{}'".format(url)
                elif platform == 'darwin':
                    if ports:
                        print "\tInstall using MacPorts or download from '{}'".format(url)
                    else:
                        print "\tDownload from '{}'".format(url)
                else:
                    print "\tDownload from '{}'".format(url)

                print ''

        if problem:
            print 'Problems found, please install the libraries for Python {}.{}'.format(version[0], version[1])
        else:
            print 'No problems found'

    input('\nPress [Return]')
