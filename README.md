# mongo-bdb

A MongoDB store of BDB documents.

## System requirements

* mongodb
* virtualenv
* virtualenvwrapper

## Data requirements

* A local copy of the BDB databank. Instructions for obtaining a mirror can be
  found [here][1]

## Installation

* Set up a virtual environment: `mkvirtualenv --no-site-packages mongo-bdb`.
* Switch to the mong-bdb environment with `workon mongo-bdb`.
* Obtain the latest source code from github:
  `git clone https://github.com/cmbi/mongo-bdb.git`
* Install module dependencies: `pip install -r requirements`. This command
  installs the required module dependencies into the virtual environment you've
  created, isolating the development environment from the rest of your system.
* Adjust the settings in `settings.json` if needed. The
  DOCUMENT_WILDCARD will be expanded in unix shell-style.

## Execution

* The program has to modi oparandi: insall and upsert.
  Run `python -m mongo_bdb -h` to see what you need.
* The file `mongo-bdb.log` will contain logs.

[1]: http://www.cmbi.ru.nl/bdb/about/
