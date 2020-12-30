import pymongo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# helper class for MongoDB manipulation
class UrlDatabase():
    def __init__(self, database_name='UrlConversion', collection_name='UrlCollections'):
        self.client = pymongo.MongoClient(config['db']['ConnectionString'] + '&ssl=true&ssl_cert_reqs=CERT_NONE')
        self.collection = self.client[database_name][collection_name]

    def __del__(self):
        self.client.close()

    def check(self, long_url):
        return self.collection.find_one({'LongUrl': long_url})

    def insert(self, long_url, short_url, url_code):
        try:
            self.collection.insert_one({
                'LongUrl': long_url,
                'ShortUrl': short_url,
                'UrlCode': url_code
            })
        except Exception as e:
            print(e)
