# 10.1 - TWP420 Hackeando o Facebook Profile
# pratique os conceitos de python usando os dados do Facebook

import urllib.request
import json
from pprint import pprint

url = 'http://graph.facebook.com/4'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
pprint(data)
