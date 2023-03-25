from google.cloud import storage
from config import google_bucket_name as bucket_name, google_project_id as project_id

storage_client = storage.Client(project_id)

def ls(path: str) -> None:
    """List all blobs in the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    
    blobs = storage_client.list_blobs(bucket_name, prefix=path, delimiter="/")

    for blob in blobs:
        print(blob.name)


def write(blob_name: str, content: bytes) -> None:
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    with blob.open("wb") as f:
        f.write(content)


if __name__ == "__main__":
    # ls("data/")
    write("code/kg-torrent/test.txt", b"Hello, world!")
    ls("code/kg-torrent/")