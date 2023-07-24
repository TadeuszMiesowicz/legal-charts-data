import os

import MySQLdb
from dotenv import load_dotenv


def connect_db():
    """connects to development MySQL database

    Returns:
        any: db MySQL connection
    """    
    load_dotenv()

    db = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USERNAME"),
        passwd=os.getenv("PASSWORD"),
        db=os.getenv("DATABASE"),
        autocommit=True,
        ssl_mode="VERIFY_IDENTITY",
        ssl={"ca": "/etc/ssl/cert.pem"}
    )
    
    return db
