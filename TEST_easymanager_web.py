from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def to_index():
    username=''
    if request.method == 'POST' and 'username' in request.form:
        username = request.form.get('username')
        print render_template('TEST_index.html', username=username)
    return render_template('TEST_index.html', username=username)

@app.route("/test", methods=['GET', 'POST'])
def to_test():
    return render_template('test.html')

app.run()