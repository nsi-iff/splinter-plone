import unittest
import doctest

from Testing import ZopeTestCase as ztc

from splinterplone.testcase import TestCase


def test_suite():
    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'tests/basic_features.txt', package='splinterplone',
            test_class=TestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
