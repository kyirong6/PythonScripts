import json
from operator import itemgetter


def script(file):
  with open(file, 'r') as file:
    read_data = json.load(file)
    values = []
    for i in read_data['products']:
      if "Keyboard" in i['product_type'] or "Computer" in i['product_type']:
        for q in i["variants"]:
          values.append((q['price'], q['grams']))
        else:
          pass
  values = sorted(values, key=itemgetter(1))
    max = []
    num = 0
    for i in values:
      if num < 100000:
        max.append((float(i[0])))
          num += float(i[1])
    dollars = 0
    for i in max:
      dollars += i
    return dollars



if "__main__" == __name__:
  print(script('script.json'))
