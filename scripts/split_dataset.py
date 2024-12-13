import os
import shutil

def split_dataset():
    dataset_dir = "data/bccd_dataset/BCCD"
    output_dir = "data/bccd_dataset"

    # Create directories
    os.makedirs(os.path.join(output_dir, "train/images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "train/labels"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "val/images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "val/labels"), exist_ok=True)

    # Read train/val splits
    with open(os.path.join(dataset_dir, "ImageSets/Main/train.txt")) as f:
        train_files = [line.strip() for line in f]
    with open(os.path.join(dataset_dir, "ImageSets/Main/val.txt")) as f:
        val_files = [line.strip() for line in f]

    # Move files
    for file_list, split in [(train_files, "train"), (val_files, "val")]:
        for file_name in file_list:
            shutil.copy(os.path.join(dataset_dir, "JPEGImages", f"{file_name}.jpg"),
                        os.path.join(output_dir, split, "images", f"{file_name}.jpg"))
            shutil.copy(os.path.join(dataset_dir, "Annotations", f"{file_name}.xml"),
                        os.path.join(output_dir, split, "labels", f"{file_name}.xml"))

if __name__ == "__main__":
    split_dataset()
