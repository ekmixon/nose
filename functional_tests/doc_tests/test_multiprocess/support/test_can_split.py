import sys
called = []

_multiprocess_can_split_ = 1

def setup():
    print >> sys.stderr, "setup called"
    called.append('setup')


def teardown():
    print >> sys.stderr, "teardown called"
    called.append('teardown')


def test_a():
    assert len(called) == 1, f"len({called}) !=1"


def test_b():
    assert len(called) == 1, f"len({called}) !=1"


class TestMe:
    def setup_class(self):
        self._setup = True
    setup_class = classmethod(setup_class)

    def test_one(self):
        assert self._setup, "Class was not set up"
