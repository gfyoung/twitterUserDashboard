import os
import sys

from csv import reader
from pymongo import MongoClient

filename = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'twitterSampleData.csv'))
reader = reader(open(filename, 'r'))

data = []
titleRow = reader.next()

for row in reader:
    dataDict = {}

    for key, value in zip(titleRow, row):
        dataDict[key] = value

    data.append(dataDict)

client = MongoClient()
db = client['twitterData']

posts = db.posts
posts.insert(data)

client.close()
