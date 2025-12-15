
import os, shutil, json
from datetime import datetime

CATALOG = "catalog.json"

name = input("Nome do projeto: ")
template = input("Template (api-python): ")
dest = input("Pasta destino: ")
owner = input("Responsável: ")

src = os.path.join("templates", template)
dst = os.path.join(dest, name)

shutil.copytree(src, dst)

entry = {
    "name": name,
    "type": template,
    "date": datetime.now().isoformat(),
    "owner": owner
}

if not os.path.exists(CATALOG):
    data = []
else:
    with open(CATALOG) as f:
        data = json.load(f)

data.append(entry)
with open(CATALOG, "w") as f:
    json.dump(data, f, indent=2)

print("Projeto criado com sucesso!")
