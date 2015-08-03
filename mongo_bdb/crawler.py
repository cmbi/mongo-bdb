"""Find and read bdb documents."""

import glob
import json


class DocumentFinder(object):
    """Find and read bdb documents."""
    def __init__(self, document_wildcard):
        self.document_wildcard = document_wildcard
        self.document_paths = self.expand_document_wildcard()

    def expand_document_wildcard(self):
        """Return list of paths to bdb documents."""
        return glob.glob(self.document_wildcard)

    def read_all(self):
        """Return a list of bdb documents."""
        documents = []
        for path in self.document_paths:
            with open(path, 'r') as file_handle:
                document = json.load(file_handle)
                documents.append(document)
        return documents

    def read_and_replace(self, database):
        """Read and replace/upsert documents one by one."""
        upserted_ids = []
        for path in self.document_paths:
            with open(path, 'r') as file_handle:
                document = json.load(file_handle)
                result = database.upsert_json_file(document)
                upserted_ids.append(result.upserted_id)
        return upserted_ids
