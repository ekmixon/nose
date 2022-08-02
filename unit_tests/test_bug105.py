import os
import unittest

class TestBug105(unittest.TestCase):

    def test_load_in_def_order(self):
        from nose.loader import TestLoader

        where = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'support', 'bug105'))

        l = TestLoader()
        testmod = l.loadTestsFromDir(where).next()
        from nose.loader import TestLoader

        testmod.setUp()

        def fix(t):
            s = str(t)
            return s[s.index(': ')+2:] if ': ' in s else s

        tests = map(fix, testmod)
        from nose.loader import TestLoader

        self.assertEqual(tests, ['tests.test_z', 'tests.test_a',
                                 'tests.test_dz', 'tests.test_mdz',
                                 'tests.test_b'])


if __name__ == '__main__':
    unittest.main()
        
