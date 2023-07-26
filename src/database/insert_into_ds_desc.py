from src.database.connect_db import connect_db
import MySQLdb


def insert_into_ds_desc(ds_table_name: str, data:list):
    """insert description into dataset description table

    Args:
        ds_table_name (str): data set table name
        data (list): data to be inserted into description table
    """
    db = connect_db()

    cursor = db.cursor()

    DESC_TABLE_NAME = f"{ds_table_name}Desc"

    query = f"""
    INSERT INTO {DESC_TABLE_NAME}(
        column_name, 
        description, 
        descriptionPl)
        VALUES (%s, %s, %s);
    """

    try:
        cursor.executemany(query, data)
    except MySQLdb.Error as e:
        print('data added already')
        print("An error occurred:", e)
