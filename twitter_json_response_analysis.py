##encoding=utf8
##version =py27
##author  =sanhe
##date    =2013-10-01

'''This script is just to give user a brief concept about the structure of tweets
json response. 
tweet json field guide: https://dev.twitter.com/docs/platform-objects/tweets

Go repository tweetpy, HSH, Data-Science-in-Python find more help
'''

import os
import jsontree
import itertools
import pprint as ppt

def read_nth(f, n):
    c = itertools.count(1)
    for line in f.xreadlines():
        if c.next() == n:
            return line

def unit_test():
    for fname in os.listdir('tweets_raw'): # <===
        with open(os.path.join('tweets_raw', fname), 'rb') as f:
            jt = jsontree.loads( read_nth(f, 4) )
            print jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))
            print jt.text
            print jt.created_at
            print ppt.pprint(jt.keys())
        break

if __name__ == '__main__':
    unit_test()