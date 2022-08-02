#!/usr/bin/env python

from docutils.core import publish_string, publish_parts
from docutils.readers.standalone import Reader
from nose.config import Config
from nose.plugins.manager import BuiltinPluginManager
import nose
import nose.commands
import nose.tools
import os
import re
import time

def doc_word(node):
    print "Unknown ref %s" % node.astext()    
    node['refuri'] = 'doc/' \
        + '_'.join(map(lambda s: s.lower(), node.astext().split(' '))) \
        + '.html'
    del node['refname']
    node.resolved = True
    return True
doc_word.priority = 100

class DocReader(Reader):
    unknown_reference_resolvers = (doc_word,)


root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

doc_word.priority = 100

tpl = open(os.path.join(root, 'index.html.tpl'), 'r').read()

pat = re.compile(r'^.*(Basic usage)', re.DOTALL)
txt = nose.__doc__.replace(':: python','::')
txt = pat.sub(r'\1', txt)

# cut from 'about the name' down (goes to end of page)
pat = re.compile(r'^(.*?)(About the name.*$)', re.DOTALL)
txt, coda = pat.search(txt).groups()

docs = publish_parts(txt, reader=DocReader(), writer_name='html')
docs.update({'version': nose.__version__,
             'date': time.ctime()})
docs['coda'] = publish_parts(coda, writer_name='html')['body']

doc_word.priority = 100

cmds = publish_parts(nose.commands.__doc__, reader=DocReader(),
                     writer_name='html')
docs['commands'] = cmds['body']

doc_word.priority = 100

changes = open(os.path.join(root, 'CHANGELOG'), 'r').read()
changes_html = publish_parts(changes, reader=DocReader(), writer_name='html')
docs['changelog'] = changes_html['body']

doc_word.priority = 100

news = open(os.path.join(root, 'NEWS'), 'r').read()
news_html = publish_parts(news, reader=DocReader(), writer_name='html')
docs['news'] = news_html['body']

doc_word.priority = 100

conf = Config(plugins=BuiltinPluginManager())
usage_txt = conf.help(nose.main.__doc__).replace(
    'mkindex.py', 'nosetests')
docs['usage'] = f'<pre>{usage_txt}</pre>'

out = tpl % docs

with open(os.path.join(root, 'index.html'), 'w') as index:
    index.write(out)
with open(os.path.join(root, 'README.txt'), 'w') as readme:
    readme.write(nose.__doc__)
