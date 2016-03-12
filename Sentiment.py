__author__ = 'Choenden'
import unirest
import json

def sentiment(tweet):
    response = unirest.post("https://japerk-text-processing.p.mashape.com/sentiment/",
  headers={
    "X-Mashape-Key": "Zm5QYhQqWqmsh4NI1DMsyF6fy8wdp1Dx3OJjsnPCGQbcgSKnW6",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "language": "english",
    "text": "{x}".format(x=tweet)
  }
)
    dict = response.body

    if dict['label'] == "pos" or dict['label'] == 'neutral':
        return True
    else:
        return False




if "__main__" == __name__:
    x = 'Apple is not the best stock to own right now'
    print(x+':')
    print(sentiment(x))

