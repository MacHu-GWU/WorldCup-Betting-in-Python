##encoding=utf8
##version =py27
##author  =sanhe
##date    =2013-10-01

import oauth2 as oauth
import urllib2 as urllib
import itertools
from datetime import datetime
import os
''' 设置验证信息 - setup authentication '''
api_key = "i5WuCmMYP7heGYdu9vf2FcYSg"
api_secret = "Ndk0yhckcrqYLRgmcR9L67KCQkuKh6Tp7TszHlMfL54en6LoN4"
access_token_key = "351985670-NEXiQ7rH3xW4JsHdlS7YGmGfPjATyQgMbsBtDVJQ"
access_token_secret = "TAeaj6mpAjTG3YtLKtNPyUQvGliknzxvjgF69nkWgyA2I"

_debug = 0

''' 连接验证服务器 - connect to tweeter server '''
oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

''' get public stream request '''

def twitterreq(url, method, parameters): 
    req = oauth.Request.from_consumer_and_token(oauth_consumer, ## 建立 requests
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
            encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data) ## 这个response的结构可以查 urllib.OpenerDirector.open()

    return response

def data_generator(response, arraysize = 10):
    ''' twitter数据流generator 
    从response数据流中，每10条保存为一个txt数据文档
    '''
    cy = itertools.cycle(xrange(10))
    res = list()
    for line in response:
        res.append(line.strip())
        if cy.next() == (arraysize - 1):
            yield res
            res = list()
            
def main_fetchsamples():
    '''
    '''
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    ## tweets stream Generator
    for res in data_generator(response, 10):
        fname = datetime.strftime(datetime.now(), '%Y_%m_%d__%H_%M_%S.txt') ## 根据日期重命名
        with open(os.path.join('tweets_raw', fname), 'wb') as f:
            f.write('\n'.join(res))

if __name__ == '__main__':
    main_fetchsamples()
        
