import requests
from BeautifulSoup import BeautifulSoup, Tag


url_structure = [{"url": "https://10minutemail.com", "method": "find", "id": "mailAddress", "attr": "value"},
				{"url": "http://www.guerrillamail.com/", "method": "find", "id": "gm-host-select", "attr": "value"},
				#{"url": "https://trashmail.com/", "method": "find", "id": "fe-mob-domain", "attr": "value"},
				
				]

def get_value(i):
	if isinstance(i, Tag) and i.get("value"):
		val = i.get("value").split("@")
		print(val[1] if len(val) > 1 else val[0])

def print_values(result):
	if hasattr(result, '__iter__'):
		get_value(result)
		for i in result:
			get_value(i)

for url_option in url_structure:
	htmlSource = requests.get(url_option.get("url")).content
	soup = BeautifulSoup(htmlSource)
	result = getattr(soup, url_option.get("method"))(id=url_option.get("id"))
	
	print_values(result)
