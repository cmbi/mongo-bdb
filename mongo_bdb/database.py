"""Open the connection to MongoDB."""

import logging
LOG = logging.getLogger(__name__)

import pyconfig as cfg

from pymongo import MongoClient


class Database(object):
    """MongoDB client."""
    def __init__(self):
        self.host = cfg.get('DBHOST')
        self.port = cfg.get('DBPORT')
        self.name = cfg.get('DBNAME')
        self.collection = cfg.get('COLLECTION')
        self.url = self.get_database_url()
        self.client = MongoClient(self.url)
        self.database = self.client[self.name]

    def get_database_url(self):
        """Return the url to the database."""
        return 'mongodb://{0:s}:{1:d}'.format(self.host, self.port)

    def store_json_files(self, documents):
        """Insert documents without checking if they are present already."""
        return self.database[self.collection].insert_many(documents)

    def upsert_json_file(self, document):
        """Upsert document.

        Update the document.
        Only add an extra document if its pdb_id is new.
        """
        return self.database[self.collection].replace_one(
            filter={'pdb_id': document['pdb_id']},
            replacement=document,
            upsert=True)
