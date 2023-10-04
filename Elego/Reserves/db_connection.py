import pymongo 

url = 'mongodb+srv://esteban:admin123@testpau.27uhusq.mongodb.net/'
cliente = pymongo.MongoClient(url)

db = cliente['test_pau']
#collection = db['pau']
