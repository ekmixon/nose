import unittest
from nose.config import Config
from nose.plugins.builtin import TestId
import mock

class TestTestIdPlugin(unittest.TestCase):

    def test_default_id_file_is_in_working_dir(self):
        tid = TestId()
        c = Config()
        opt = mock.Bucket()
        opt.testIdFile = '.noseids'
        tid.configure(opt, c)
        tid = TestId()
        assert tid.idfile.startswith(
            c.workingDir
        ), f"{tid.idfile} is not under {c.workingDir}"


if __name__ == '__main__':
    unittest.main()
