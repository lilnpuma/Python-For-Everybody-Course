import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')


print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
info = json.loads(data)
print('User count:', len(info['comments']))
count = 0
for item in info['comments']:
    count += int(item['count'])
print('Count', count)
