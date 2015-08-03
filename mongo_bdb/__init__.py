"""Configure logging and user settings."""

import logging
# Configure logging
LOG = logging.getLogger(__name__)
FILE = logging.FileHandler('mongo-bdb.log', 'a')
LOG.addHandler(FILE)
FORMATTER = logging.Formatter('%(asctime)s | %(levelname)-7s | %(message)s ')
LOG.setLevel(logging.DEBUG)
FILE.setFormatter(FORMATTER)
LOG.debug('Initialized logger.')


import json
import pyconfig
with open('settings.json', 'r') as file_handle:
    settings = json.load(file_handle)
    for key, value in settings.iteritems():
        pyconfig.set(key, value)
LOG.debug('Read settings.')
