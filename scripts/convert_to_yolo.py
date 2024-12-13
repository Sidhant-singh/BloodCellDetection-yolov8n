import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_file, classes, output_file, img_width=640, img_height=480):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    yolo_annotations = []
    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in classes:
            continue
        class_id = classes.index(class_name)
        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        x_center = ((xmin + xmax) / 2) / img_width
        y_center = ((ymin + ymax) / 2) / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")

    with open(output_file, "w") as f:
        f.write("\n".join(yolo_annotations))

def convert_all_annotations():
    classes = ["RBC", "WBC", "Platelets"]
    src_labels_dir = "data/bccd_dataset/train/labels"
    dest_labels_dir = "data/bccd_dataset/train/labels_yolo"
    os.makedirs(dest_labels_dir, exist_ok=True)

    for xml_file in os.listdir(src_labels_dir):
        if xml_file.endswith(".xml"):
            output_file = os.path.join(dest_labels_dir, xml_file.replace(".xml", ".txt"))
            convert_voc_to_yolo(os.path.join(src_labels_dir, xml_file), classes, output_file)

if __name__ == "__main__":
    convert_all_annotations()
