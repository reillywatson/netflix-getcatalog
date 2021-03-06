import oauth2 as oauth
import time
import urlparse
import codecs

def make_api_request(url):
	oauth_key = 'ha2sffzbjae3amcqqfv5twfk'
	oauth_secret = 'Q639Mr6aHC'
	params = {
		'oauth_version' : '1.0',
		'oauth_nonce' : oauth.generate_nonce(),
		'oauth_timestamp' : int(time.time()),
	}
	token = oauth.Token(key=oauth_key, secret=oauth_secret)
	consumer = oauth.Consumer(key=oauth_key, secret=oauth_secret)
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

# get all 'play' links for a TV series (this is for Futurama)
#resp, content = make_api_request('http://api-public.netflix.com/catalog/titles/series/70153380/episodes')
#<id>http://api-public.netflix.com/catalog/titles/programs/70228172</id>
#http://movies.netflix.com/WiPlayer?movieid=70228171

out = codecs.open('test.xml', 'w', 'utf-8')
out.write(content)
out.close()
