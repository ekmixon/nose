from nose.plugins.attrib import attr

from unittest import TestCase

@attr("b")
def test_b():
    pass

class TestBase(TestCase):
    def test_a(self):
        pass

class TestDerived(TestBase):
    @attr("a")
    def test_a(self):
        pass
