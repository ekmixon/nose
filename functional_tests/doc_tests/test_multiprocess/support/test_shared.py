import os
import sys

here = os.path.dirname(__file__)
flag = os.path.join(here, 'shared_flag')

_multiprocess_shared_ = 1

def _log(val):
    with open(flag, 'a+') as ff:
        ff.write(val)
        ff.write("\n")


def _clear():
    if os.path.isfile(flag):
        os.unlink(flag)


def logged():
    flag_file = open(flag, 'r')
    try:
        lines = list(flag_file)
    finally:
        flag_file.close()
    return lines


def setup():
    print >> sys.stderr, "setup called"
    _log('setup')


def teardown():
    print >> sys.stderr, "teardown called"
    _clear()


def test_a():
    assert len(logged()) == 1, f"len({called}) !=1"


def test_b():
    assert len(logged()) == 1, f"len({called}) !=1"


class TestMe:
    def setup_class(self):
        self._setup = True
    setup_class = classmethod(setup_class)

    def test_one(self):
        assert self._setup, "Class was not set up"
