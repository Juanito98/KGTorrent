import re
from typing import List, Pattern
from google.cloud import storage
from config import google_bucket_name as bucket_name, google_project_id as project_id

def ls(path: str, reg_filter: Pattern[str] = r'.*') -> List[str]:
    """List all blobs in the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    reg = re.compile(reg_filter)
    storage_client = storage.Client(project_id)
    blobs = storage_client.list_blobs(bucket_name, prefix=path, delimiter="/")

    filepaths = [blob.name for blob in blobs if reg.match(blob.name)]
    return filepaths


def rm(path: str) -> None:
    """Delete a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(path)

    blob.delete()


def write(blob_name: str, content: bytes) -> None:
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    with blob.open("wb") as f:
        f.write(content)


if __name__ == "__main__":
    # ls("data/")
    write("code/kg-torrent/test.txt", b"Hello, world!")
    print(ls("code/kg-torrent/"))
    rm("code/kg-torrent/test.txt")
    print(ls("code/kg-torrent/"))
