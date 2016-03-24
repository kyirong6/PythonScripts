import urllib.request
import urllib.parse
__author__ = 'Choenden'


user_message = input("Message: ")
designated_number = input("Number: ")

values = {'number': designated_number, 'message': user_message}

url = r"http://textbelt.com/canada"
values = urllib.parse.urlencode(values)

bytes = str.encode(values)

resp = urllib.request.urlopen(url, bytes)
respData = resp.read()

print(respData)
