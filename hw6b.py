import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ' )
num=int(input('enter count: ' ))
position=int(input('enter position: ' )) 

count= 0
while count < num:
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	url = soup.find_all('a')[position- 1].get('href')
	print (url)
	count += 1

