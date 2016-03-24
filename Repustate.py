import json
from repustate import Repustate

client = Repustate(api_key=key, version='v3')
client.sentiment("This is a great day to go for a run")


def script(data):
    with open(data, 'r') as file:
        data = json.loads(file)
    positive = 0
    negative = 0
    number_of_tweets = 0
    for i in data["statuses"]:
        if sentiment(i["text"]):
            positive += 1
            number_of_tweets += 1
        else:
            negative += 1
            number_of_tweets += 1
    else:
        pass
    return float(positive)/number_of_tweets, number_of_tweets




if __name__ == "__main__":
    script('fun.json')
