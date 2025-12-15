"""
from flask import Flask, render_template, request, redirect, url_for, send_file
import shutil, os, json, datetime, zipfile

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
PROJECTS_DIR = os.path.join(BASE_DIR, "generated-projects")
CATALOG_FILE = os.path.join(os.path.dirname(__file__), "catalog.json")

os.makedirs(PROJECTS_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        template = request.form["template"]
        owner = request.form["owner"]

        src = os.path.join(TEMPLATES_DIR, template)
        dst = os.path.join(PROJECTS_DIR, name)

        shutil.copytree(src, dst)

        # Registar no catálogo
        project = {
            "name": name,
            "template": template,
            "owner": owner,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        with open(CATALOG_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(project)
            f.seek(0)
            json.dump(data, f, indent=2)

        # Criar ZIP
        zip_path = f"{dst}.zip"
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for folder, _, files in os.walk(dst):
                for file in files:
                    full_path = os.path.join(folder, file)
                    zipf.write(full_path, arcname=os.path.relpath(full_path, dst))

        return send_file(zip_path, as_attachment=True)

    return render_template("index.html")

@app.route("/catalog")
def catalog():
    with open(CATALOG_FILE, encoding="utf-8") as f:
        projects = json.load(f)
    return render_template("catalog.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)



"""
from flask import Flask, render_template, request
import shutil, os, json
from datetime import datetime
from flask import Flask, render_template, request, send_file
import zipfile


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
CATALOG = os.path.join(BASE_DIR, "catalog.json")
GENERATED = os.path.join(BASE_DIR, "generated")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    project_name = None

    if request.method == "POST":
        name = request.form["name"]
        template = request.form["template"]
        owner = request.form["owner"]

        src = os.path.join(TEMPLATES_DIR, template)
        dst = os.path.join(GENERATED, name)

        os.makedirs(GENERATED, exist_ok=True)

        if not os.path.exists(src):
            msg = "Template não encontrado!"
        else:
            shutil.copytree(src, dst)

            # Criar ZIP
            zip_path = os.path.join(GENERATED, f"{name}.zip")
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for folder, _, files in os.walk(dst):
                    for file in files:
                        full_path = os.path.join(folder, file)
                        zipf.write(
                            full_path,
                            arcname=os.path.relpath(full_path, dst)
                        )

            entry = {
                "name": name,
                "type": template,
                "date": datetime.now().isoformat(),
                "owner": owner
            }

            if os.path.exists(CATALOG):
                with open(CATALOG) as f:
                    data = json.load(f)
            else:
                data = []

            data.append(entry)
            with open(CATALOG, "w") as f:
                json.dump(data, f, indent=2)

            msg = "Projeto criado com sucesso!"
            project_name = name

    return render_template(
        "index.html",
        msg=msg,
        project_name=project_name
    )

    
    msg = ""
    if request.method == "POST":
        name = request.form["name"]
        template = request.form["template"]
        owner = request.form["owner"]

        src = os.path.join(TEMPLATES_DIR, template)
        dst = os.path.join(GENERATED, name)

        os.makedirs(GENERATED, exist_ok=True)

        if not os.path.exists(src):
            msg = "Template não encontrado!"
        else:
            shutil.copytree(src, dst)
            entry = {
                "name": name,
                "type": template,
                "date": datetime.now().isoformat(),
                "owner": owner
            }

            if os.path.exists(CATALOG):
                with open(CATALOG) as f:
                    data = json.load(f)
            else:
                data = []

            data.append(entry)
            with open(CATALOG, "w") as f:
                json.dump(data, f, indent=2)

            msg = "Projeto criado com sucesso!"

    return render_template("index.html", msg=msg)

@app.route("/download/<project_name>")
def download(project_name):
    zip_path = os.path.join(GENERATED, f"{project_name}.zip")

    if os.path.exists(zip_path):
        return send_file(zip_path, as_attachment=True)
    else:
        return "Arquivo não encontrado", 404


if __name__ == "__main__":
    app.run(debug=True)


