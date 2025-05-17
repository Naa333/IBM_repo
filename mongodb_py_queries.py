from pymongo import MongoClient

uri = "mongodb+srv://jherliedee:XSQ6SCtOPSRyv0iF@learning0.onmyx.mongodb.net/?retryWrites=true&w=majority&appName=Learning0"
client = MongoClient(uri)

print("\n------------------Airbnb dataset queries---------------\n")
airbnb = client["sample_airbnb"]
listings_and_reviews = airbnb["listingsAndReviews"]
for item in listings_and_reviews.find({"address.country":"United States"},{"_id":0, "name":1}):
	print(item)
for item in listings_and_reviews.find({"minimum_nights": "3"},{"_id":0, "name":1}):
	print(item)
for item in listings_and_reviews.find({"bedrooms": {"$gte":5}},{"_id":0, "name":1, "description":1}):
    print(item)


print("\n------------------Mflix dataset queries---------------\n")
mflix = client["sample_mflix"]
movie_collection = mflix["movies"]
for movie in movie_collection.find({"imdb.rating":{"$gte":7}},{"_id":0, "title":1}):
	print(movie)

for movie in movie_collection.find({"genres":"Drama", "year":2007}, {"_id":0, "title":1}):
    print(movie)
	
for movie in movie_collection.find({"rated":"PG-13", "awards.wins":{"$gte":3}}, {"_id":0, "title":1}):
	print(movie)


print("\n------------------Restaurant dataset queries---------------\n")
restaurant_db = client["sample_restaurants"]
restaurant_collection = restaurant_db["restaurants"]
for restaurant in restaurant_collection.find({"borough":"Brooklyn"}, {"_id":0, "name":1}):
	print(restaurant)
for restaurant in restaurant_collection.find({"cuisine":"American","borough":"Queens"}, {"_id":0, "name":1, "borough":1}):
	print(restaurant)


