import os
import unittest
from cStringIO import StringIO
from nose.core import TestProgram
from nose.config import Config
from nose.result import _TextTestResult

here = os.path.dirname(__file__)
support = os.path.join(here, 'support')


class TestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        self.result = _TextTestResult(
            self.stream, self.descriptions, self.verbosity)
        return self.result

    
class TestBuggyGenerators(unittest.TestCase):
    def test_run_buggy_generators(self):
        stream = StringIO()
        runner = TestRunner(stream=stream)
        prog = TestProgram(
            argv=['nosetests',
                  os.path.join(support, 'test_buggy_generators.py')],
            testRunner=runner,
            config=Config(),
            exit=False)
        res = runner.result
        stream = StringIO()
        self.assertEqual(
            res.testsRun, 12, f"Expected to run 12 tests, ran {res.testsRun}"
        )

        assert not res.wasSuccessful()
        assert len(res.errors) == 4
        assert not res.failures
    
