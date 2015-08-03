"""Create MongoDB store of BDB documents."""

import logging
LOG = logging.getLogger(__name__)

import argparse
import pyconfig as cfg

from mongo_bdb.crawler import DocumentFinder
from mongo_bdb.database import Database


def insert_all(database, crawler):
    """Insert all documents without checking existing document pdb_ids."""
    bdb_documents = crawler.read()
    result = database.store_json_files(bdb_documents)
    LOG.debug('Inserted {0:d} bdb documents.'.format(len(result.inserted_ids)))


def upsert_all(database, crawler):
    """Replace all documents while checking existing document pdb_ids."""
    result = crawler.read_and_replace(database)
    LOG.debug('Upserted {0:d} bdb documents.'.format(len(result)))


def main():
    """Create mongo-bdb."""

    parser = argparse.ArgumentParser(
        description='Create a MongoDB document store from bdb json files.')
    parser.add_argument(
        '-q', '--quiet',
        help='show less verbose output',
        action='store_true')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-i', '--insall', help='Insert all documents without ' +
                      'checking if they already exist in the store.',
                      action='store_true')
    mode.add_argument('-u', '--upsert', help='Update all documents. If the ' +
                      'document does not yet exist, it is created.',
                      action='store_true')
    args = parser.parse_args()

    # Set the log level depending on verbosity
    if args.quiet:
        LOG.setLevel(logging.INFO)
        LOG.debug('Configured less verbose logging.')

    crawler = DocumentFinder(cfg.get('DOCUMENT_WILDCARD'))
    LOG.info('Preparing to store {0:d} bdb documents...'.format(
        len(crawler.document_paths)))
    database = Database()

    if args.insall:
        insert_all(database, crawler)
    elif args.upsert:
        upsert_all(database, crawler)

    LOG.info('Finished creating mongo-bdb.')
