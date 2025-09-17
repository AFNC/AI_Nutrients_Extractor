from pymongo import MongoClient

def save_to_mongodb(text):
    
    CONNECTION_STRING = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'project_database'
    COLLECTION_NAME = 'nutrition_table'
    json_text = text
    
    client = MongoClient(CONNECTION_STRING)
    mydatabase = client[DATABASE_NAME]
    print('Database connection successful')
    mycollection = mydatabase[COLLECTION_NAME]
    mycollection.insert_one(json_text)
    
    return 'Nutrition info successfully saved to database'
    