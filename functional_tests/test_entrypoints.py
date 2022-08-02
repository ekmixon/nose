import os
import sys
from nose.exc import SkipTest

try:
    from pkg_resources import EntryPoint
except ImportError:
    raise SkipTest("No setuptools available; skipping")

here = os.path.dirname(__file__)
support = os.path.join(here, 'support')
ep = os.path.join(support, 'ep')


def test_plugin_entrypoint_is_loadable():
    ep_path = os.path.join(ep, 'Some_plugin.egg-info', 'entry_points.txt')
    with open(ep_path, 'r') as ep_file:
        lines = ep_file.readlines()
    assert EntryPoint.parse_map(lines)
