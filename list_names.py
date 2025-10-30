from pathlib import Path
import xml.etree.ElementTree as ET

xml_dir = Path("/Users/enke/Projects/Hirnventile/YOLO/xml_Dateien")

for xml_path in sorted(xml_dir.glob("*.xml")):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall("object"):
        name = obj.findtext("name", default="(missing)")
        print(f"{xml_path.name}: {name}")