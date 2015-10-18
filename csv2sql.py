#!/usr/bin/env python

"load train and test data into a SQLite database, using Pandas"

import pandas as pd
import sqlite3

train_file = 'data/train.csv'
test_file = 'data/test.csv'
db_file = 'data/sales.sqlite'

train = pd.read_csv( train_file )
test = pd.read_csv( test_file )
conn = sqlite3.connect( db_file )

train.to_sql( 'train', conn, index = False, if_exists = 'replace' )
test.to_sql( 'test', conn, index = False, if_exists = 'replace' )
