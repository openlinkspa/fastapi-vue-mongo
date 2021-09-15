from pymongo import MongoClient

#coneccion a la db por connection string
conn_str = os.environ["MONGODB_URL"]
client = MongoClient(conn_str)
conn = client.get_database(os.environ["MONGODB_DB"])