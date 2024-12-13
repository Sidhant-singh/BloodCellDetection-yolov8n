import os
import zipfile
import requests

def download_bccd_dataset():
    url = "https://github.com/Shenggan/BCCD_Dataset/archive/refs/heads/master.zip"
    dataset_dir = "data/bccd_dataset"

    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    zip_path = os.path.join(dataset_dir, "bccd_dataset.zip")

    print("Downloading BCCD Dataset...")
    response = requests.get(url, stream=True)
    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

    print("Extracting BCCD Dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dataset_dir)

    print("Dataset downloaded and extracted successfully!")

if __name__ == "__main__":
    download_bccd_dataset()
