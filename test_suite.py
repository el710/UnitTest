import unittest
import test_theme
import add_utest

"""
make object of class TestSuite
"""
calc_test_suite = unittest.TestSuite()

"""
add tests from TestCase class...
"""
# calc_test_suite.addSubTest(unittest.makeSuite(test_theme.CalcTest)) ## old fasion call
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_theme.CalcTest))

## add from other test file - add_utest.py
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(add_utest.NewTest))

"""
make runner to config and run TestSuite...
"""
##                               verbosity - is a level of detailization    
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calc_test_suite)