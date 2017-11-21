from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'c:/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('TEST_index.html')

if __name__ == "__main__":
    app.run()
