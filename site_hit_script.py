import urllib.request
import urllib.error


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError



req = Request('http://www.google.com')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    # everything is fine
    #print(response.read());
    webcontent = response.read();
    webcontent = str(webcontent,"UTF-8");
    contentlength = len(webcontent);
    print(contentlength);
