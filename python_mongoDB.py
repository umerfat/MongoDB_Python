from pymongo import MongoClient
import datetime
from bson import ObjectId

# Connect to mongoDB cluster - using MongoDB Atlas - cloud based mongodb
cluster = "mongodb+srv://umer:mongodb%400319@cluster0.2vpb1li.mongodb.net/?TodoDB?retryWrites=true&w=majority"
client  = MongoClient(cluster)

# printing available databases
print(client.list_database_names())

#printing collections present in database 'TodoDB'
database = client.TodoDB
print(database.list_collection_names())


# Inserting data (Documents) into collections
todo1 = {
    "name": "Umer",
    "text": "My todo list",
    "status": "open",
    "tags":["Python", "DevOps", "MongoDB"],
    "date": str(datetime.datetime.utcnow())
}
todos = database.todosCollection
result1 = todos.insert_one(todo1)

todos2= [{
    "name": "Asif",
    "text": "My todo list",
    "status": "open",
    "tags":["Hardware", "Firmware"],
    "date": str(datetime.datetime(2023, 3, 2, 2, 13))
},
{
    "name": "Professor",
    "text": "My todo list",
    "status": "closed",
    "tags":["Hacking", "Pyschology"],
    "date": str(datetime.datetime.utcnow())
}]

result2 = todos.insert_many(todos2)

# Retrieving data from database, you can search with any key value or set of key value pairs

resultMultiple = todos.find_one({"name": "Professor",
    "text": "My todo list",})

resultTags = todos.find_one({"tags": "Hacking"})
print(resultTags)

# retrieve all
resultsAll = todos.find({})
for result in resultsAll:
    print (result)

# searching by particular key
resultsKey = todos.find({"name": "Professor"})
for result in resultsKey:
    print (result)

# seach by object id
resultId = todos.find_one({"_id": ObjectId("63ffb7765e9a69c70a7e7451")
                         })
print(resultId)

# searching for documents with particular date
d = datetime.datetime(2022, 3, 3)
resultsDateMatch = todos.find({"date": {"$gt": d}})
for result in resultsDateMatch:
    print(result)

# Counting documents in collections
print(todos.count_documents({}))

# Deleting document in collection, we can use delete_many() to delete mulitple entries by 
# passing particular key which exits multiple times, delete_many({}) -- will delete all deocuments in collection
resultRemove = todos.delete_one({"_id": ObjectId("63ffb9640a570c49221c4d39")})

# Updating document, using $unset we can remove field from the document
resultUpdate = todos.update_one({"tags": "Python"}, {"$set": {"status": "Done"}})




