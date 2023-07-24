from src.database.connect_db import connect_db
import MySQLdb


def insert_topic(
    id: int,
    topicName: str,
    title: str,
    titlePl: str,
    country: str,
    countryPl: str,
    startYear: int,
    endYear: int,
    description: str,
    descriptionPl: str,
    sourceName: str,
    sourceNamePl: str,
    sourceLink: str,
    fileName: str,
    sourceFileExt: str,
):
    """creates topic in development database 
       for visualization on legalChart.org
    

    Args:
        id (int): topic id
        topicName (str): topic name
        title (str): topic title
        titlePl (str): topic title polish translation
        country (str): data origin country
        countryPl (str): data origin country polish translation
        startYear (int): year when data started to be collected
        endYear (int): year when data stopped to be collected
        description (str): topic description
        descriptionPl (str): topic description polish translation
        sourceName (str): data source name
        sourceNamePl (str): data source name polish translation
        sourceLink (str): data source lint
        fileName (str): name of file containing transformed data
        sourceFileExt (str): extension of file containing source data
        Defaults to False.
    """
    db = connect_db()

    cursor = db.cursor()

    new_topic = """
    INSERT INTO topics (
        id,
        topicName,
        title,
        titlePl,
        country,
        countryPl,
        startYear,
        endYear,
        description,
        descriptionPl,
        sourceName,
        sourceNamePl,
        sourceLink,
        fileName,
        sourceFileExt
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """

    try:
        cursor.execute(
            new_topic,
            (
                (
                    id,
                    topicName,
                    title,
                    titlePl,
                    country,
                    countryPl,
                    startYear,
                    endYear,
                    description,
                    descriptionPl,
                    sourceName,
                    sourceNamePl,
                    sourceLink,
                    fileName,
                    sourceFileExt,
                )
            ),
        )
    except MySQLdb.Error as e:
        print("An error occurred:", e)
