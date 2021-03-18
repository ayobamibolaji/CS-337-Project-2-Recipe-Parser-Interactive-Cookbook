from download_file import download_file_from_google_drive
import os.path
from os import path
import pathlib

def downloadModel():
    if not path.exists("GoogleNews-vectors-negative300.bin.gz"):
        print("We need to download the model. This is a one time task, but it may take a few minutes.")
        print("Downloading model...")
        download_file_from_google_drive("0B7XkCwpI5KDYNlNUTTlSS21pQmM", pathlib.Path(__file__).parent.absolute() / "GoogleNews-vectors-negative300.bin.gz")
        print("\nFinished downloading model.")
