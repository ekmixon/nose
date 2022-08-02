import unittest
from nose.config import Config
from nose import case
from nose.plugins import Plugin, PluginManager

class TestTestCasePluginCalls(unittest.TestCase):

    def test_describe_test_called(self):



        class Descrip(Plugin):
            counter = 0
            enabled = True
            def describeTest(self, test):
                return f"test #{id(test)}"

            def testName(self, test):
                self.counter += 1
                return f"({self.counter}) test"


        class TC(unittest.TestCase):
            def test_one(self):
                pass
            def test_two(self):
                pass

        config = Config(plugins=PluginManager(plugins=[Descrip()]))

        c1 = case.Test(TC('test_one'), config=config)
        c2 = case.Test(TC('test_two'), config=config)

        self.assertEqual(str(c1), '(1) test')
        self.assertEqual(str(c2), '(2) test')
        assert c1.shortDescription().startswith(
            'test #'
        ), f"Unexpected shortDescription: {c1.shortDescription()}"

        assert c2.shortDescription().startswith(
            'test #'
        ), f"Unexpected shortDescription: {c2.shortDescription()}"


if __name__ == '__main__':
    unittest.main()
