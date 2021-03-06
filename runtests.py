#!/usr/bin/env python
import glob, unittest, os, sys

from trace import fullmodname
from tests.utils import cleanup

# try to start in a consistent, predictable location
sys.path.insert(0, os.getcwd())

# find all of the planet test modules
modules = map(fullmodname, glob.glob(os.path.join('tests', 'test_*.py')))

# load all of the tests into a suite
try:
    suite = unittest.TestLoader().loadTestsFromNames(modules)
except Exception, exception:
    # attempt to produce a more specific message
    for module in modules: 
        __import__(module)
    raise

verbosity = 1
if "-q" in sys.argv or '--quiet' in sys.argv:
    verbosity = 0
if "-v" in sys.argv or '--verbose' in sys.argv:
    verbosity = 2

# run test suite
unittest.TextTestRunner(verbosity=verbosity).run(suite)

cleanup()

