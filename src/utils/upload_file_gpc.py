import os

from google.cloud import storage


def upload_file(source_fileName: str, destination_blob_name: str) -> None:
    """uploads file to Google Cloud Storage and make it public

    Args:
        source_fileName (str): name of file
        destination_blob_name (str): destination blob in storage
    """

    client = storage.Client(project='legal-charts')
    bucket_name = os.getenv("GCP_BUCKET")
    bucket = client.bucket("legal-charts-datasets")
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_fileName)

    blob.make_public()

    print(f"File {source_fileName} uploaded to {bucket_name}/{destination_blob_name}.")
