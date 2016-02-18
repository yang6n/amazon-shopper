from lxml import html
import requests

page = requests.get('http://www.amazon.com/gp/goldbox/ref=nav_cs_gb')
tree = html.fromstring(page.content)

items = tree.xpath('//*[@id="widgetContent"]')
print (items)
