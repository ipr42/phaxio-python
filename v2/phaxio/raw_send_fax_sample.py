import requests

api_key = 'MY_API_KEY'
api_secret = 'MY_API_SECRET'

post_params = [
    ('to', '4145556984'),
    ('content_url[]', ['http://www.google.com', 'http://www.bing.com'])
]

files = [
    ('file[]', ('requirements.txt', open('/path/to/supported/file.txt', 'rb'))),
    ('file[]', ('bar.png', open('/path/to/supported/file.doc', 'rb')))
]

response = requests.post('https://api.phaxio.com/v2/faxes',
                         data=post_params,
                         files=files,
                         auth=(api_key, api_secret))
print('response={}'.format(response.text))
