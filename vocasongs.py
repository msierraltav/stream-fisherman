import requests
from lxml.html import fromstring

url = 'http://tiermaker.com/create/vocaloid-classics-1659722'  # Replace with the desired URL
response = requests.get(url)

soup = fromstring(response.text)

# Select elements using XPath
elements = soup.xpath("//div[@class='character']/img/@src")  # Replace with your XPath expression

# Iterate over the selected elements
for element in elements:
    # Access element properties or extract data
    # print(element.get('href'))
    print (element)

    

