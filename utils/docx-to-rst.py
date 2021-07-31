import yaml
import os
from pathlib import Path

baseDir = 'articles'


# read config file, to get file name mapping

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)



configContent = read_yaml("filename-mapping.yaml")
index = 1
for key, value in configContent.items():
    print("%d: %s  ====> %s"%(index, key, value))
    index = index + 1



# begin to transform documents
for originName, newName in configContent.items():
    # check if folder exist
    targetDir = os.path.join(baseDir, newName)
    Path(targetDir).mkdir(parents=True, exist_ok=True)

    cmd = "pandoc -f docx '%s.docx' -t rst -o '%s'"%(originName, os.path.join(targetDir, newName + '.rst'))
    print("cmd: %s"%(cmd))
    os.system(cmd)

    # unzip docx
    cmd = "unzip -j '%s.docx' 'word/media/*'  -d '%s'"%(originName, os.path.join(targetDir, 'media'))
    print("cmd: %s"%(cmd))
    os.system(cmd)



