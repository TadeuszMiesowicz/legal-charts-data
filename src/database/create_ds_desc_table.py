from src.database.connect_db import connect_db
import MySQLdb


def create_ds_desc_table(ds_table_name: str):
    """create table with descriptions of dataset

    Args:
        ds_table_name (str): table name with data
    """
    db = connect_db()

    cursor = db.cursor()

    DESC_TABLE_NAME = f"{ds_table_name}Desc"

    query = f"""
    CREATE TABLE {DESC_TABLE_NAME} (
    column_name VARCHAR(255),
    description VARCHAR(255) NOT NULL,
    descriptionPl VARCHAR(255) NOT NULL,
    PRIMARY KEY (column_name)
    );
    """

    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print("An error occurred:", e)
