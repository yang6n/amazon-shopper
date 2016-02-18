from lxml import html
import requests

page = requests.get('http://www.amazon.com')
tree = html.fromstring(page.content)

itemsViewed = tree.xpath('//*[@id="desktop"]')
print (itemsViewed)
