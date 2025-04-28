import os
import pymysql

def reader_connect_to_db():
    if os.getenv('IS_APP_ENGINE'):
        # connect from cloud to real database
        dbc = pymysql.connect(unix_socket='/cloudsql/ice-d-version-2:us-east1:berkeley-db-prod-210',user='reader',password='beryllium-10',database='iced')
    else:
        # connect to local database locally
        dbc = pymysql.connect(host='localhost',user='reader',password='beryllium-10',database='iced')


    return dbc
