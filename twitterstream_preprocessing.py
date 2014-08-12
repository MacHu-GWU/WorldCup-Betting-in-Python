##coding=utf8
##tweet json field guide: https://dev.twitter.com/docs/platform-objects/tweets

import os
import jsontree
import itertools
import pprint as ppt

def read_nth(f, n):
    c = itertools.count(1)
    for line in f.xreadlines():
        if c.next() == n:
            return line

for fname in os.listdir('tweets_raw'):
    with open(os.path.join('tweets_raw', fname), 'rb') as f:
        jt = jsontree.loads( read_nth(f, 4) )
        print jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))
        print jt.text
        print jt.created_at
        print ppt.pprint(jt.keys())
    break
