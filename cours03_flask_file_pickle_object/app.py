# Lancer le serveur : flask run
# Tutoriel : https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# Images : C:\Users\René\Documents\Rene\IA\IA297\Jupyter\420-A62-BB_ProjetSynthese\A62-EquipeCV\cell_images\Parasitized
import os.path
import imghdr
import utils

from flask import Flask, \
    abort, \
    redirect, \
    render_template, \
    request, \
    send_from_directory, \
    url_for

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=50 * 1024 #50 Ko
app.config["UPLOAD_EXTENSIONS"] = [".png"]
app.config["UPLOAD_PATH"] = "uploaded_img" # Le répertoire doit exister avant d'être utilisé.

@app.route("/")
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route("/", methods=["POST"])
def upload_file():
    print("upload_file")
    # uploaded_file = request.files['img_file'] # Mettre le "name" du champ dans le formulaire HTML

    for uploaded_file in request.files.getlist("img_file"): # Mettre le "name" du champ dans le formulaire HTML
        filename =  secure_filename(uploaded_file.filename) # Élimine les caractères indésirables du nom du fichier.

        if filename != "":
            print("filename", filename)
            file_ext = os.path.splitext(filename)[1]

            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return "Invalid image", 400
            elif not is_valid_png_img(uploaded_file.stream):
                return "Invalid image", 400
            else:
                uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

    return redirect(url_for("index"))

def is_valid_png_img(stream)->bool:
    result=False

    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    print("format", format)

    if not format:
        result=False
    elif format == "png":
        result=True

    return result

# Retourne la liste des fichiers dans le répertoire
@app.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)