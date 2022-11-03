import pymongo;
import os
from bson.json_util import dumps

# configuration stored in local.env
# user 'env file' plugin by Borys Pierov
# MONGO_USER_NAME=my_user
# MONGO_USER_PASS=my_password


username = os.environ.get('MONGO_USER_NAME', "default_value")
userpass = os.environ.get('MONGO_USER_PASS', "default_value")
print(f"user name: {username}")
print(f"user pass: {userpass}")

mongo_url = "mongodb://localhost:27017/"
mongo_url = f'mongodb://{username}:{userpass}@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/aggregations?replicaSet=Cluster0-shard-0&authSource=admin&tls=true'


def connect_to_mongo(dbname):
    print(mongo_url)
    myclient = pymongo.MongoClient(mongo_url)
    mydb = myclient[dbname]
    dblist = myclient.list_database_names()
    if dbname in dblist:
        print("connected.")
        print(f"The db '{dbname}' exists.")
        return mydb
    else:
        print(f"The db '{dbname}' not found.")
        return None
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    db = connect_to_mongo("aggregations");


    cursor = db.solarSystem.aggregate([
    # {
    #     # "$match": {
    #     #     "atmosphericComposition": {"$regex": "O"},
    #     #     "meanTemperature": {"$gte": -40, "$lte": 40}
    #     # }
    # },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "atmosphericComposition": 1,
            "numberOfMoons": 1
        }
    }])
    list_cur = list(cursor)
    json_data = dumps(list_cur, indent=4)
    print(json_data)
    for element in list_cur:
        print(f"{element['name']} {element['atmosphericComposition']} {element['numberOfMoons']} moons.")


if __name__ == '__main__':
    print_hi('PyCharm')


