import unittest
import testing
import add_utest

"""
make object of class TestSuite
"""
calc_test_suite = unittest.TestSuite()

"""
add tests from TestCase class...
"""
# calc_test_suite.addSubTest(unittest.makeSuite(testing.CalcTest)) ## old fasion call
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testing.CalcTest))

## add from other test file - u_test.py
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(add_utest.NewTest))

"""
make runner to config and run TestSuite...
"""
##                               verbosity - is a level of detailization    
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calc_test_suite)