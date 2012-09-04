import oauth2 as oauth
import time
import urlparse
import codecs

def make_api_request(url):
	params = {
		'oauth_version' : '1.0',
		'oauth_nonce' : oauth.generate_nonce(),
		'oauth_timestamp' : int(time.time()),
	}
	token = oauth.Token(key='ha2sffzbjae3amcqqfv5twfk', secret='Q639Mr6aHC')
	consumer = oauth.Consumer(key='ha2sffzbjae3amcqqfv5twfk', secret='Q639Mr6aHC')
	params['oauth_consumer_key'] = consumer.key
	req = oauth.Request(method="GET", url=url, parameters=params)
	signature_method = oauth.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, token)
	request_token_url = 'http://api.netflix.com/oauth/request_token'
	client = oauth.Client(consumer)
	resp, content = client.request(request_token_url, "GET")
	access_token = dict(urlparse.parse_qsl(content))
	return client.request(url, "GET")

resp, content = make_api_request('http://api.netflix.com/catalog/titles/index')

out = codecs.open('test.xml', 'w', 'utf-8')
out.write(content)
out.close()
