from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags= soup('span')
numbers= []
for tag in tags:
	for t in tag:
		numbers.append(t)
		
sum_numbers= sum(list(map(int, numbers)))	
print (sum_numbers)


