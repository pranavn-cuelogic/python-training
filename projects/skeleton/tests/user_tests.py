from nose.tools import *
import user


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"

# In this exercise we've learned how to run the test cases
# using the nosetests, also get to know if the test ran 0
# it means something has went wrong in our setup.
