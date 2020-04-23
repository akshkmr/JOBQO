from pymongo import MongoClient

client = MongoClient("mongodb+srv://cryptoduh:arya0792@jobqo-usud6.mongodb.net/test?retryWrites=true&w=majority")
recipes = client['jobqo_db']['job_record']


def search_recipe(search_word):
    cursor = recipes.find({'$text': {'$search': search_word}}).limit(5).sort("time", -1)
    result = []
    for data in cursor:
        result.append(data)
    return result