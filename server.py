import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import main

UPLOAD_FOLDER = r"/Users/nathi/OneDrive/Desktop/Pdf Parser Python/uploads/"
ALLOWED_EXTENSIONS = {'pdf'}
FILE_PATHS = []
FILES_JSON = {}
FILE_COUNT = 0

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist("file") 
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        print(files)
        for file in files: 
            print(file)
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                FILE_PATHS.append(UPLOAD_FOLDER + filename)
                print(f"File Paths: {FILE_PATHS}")
                FILES_JSON[len(FILES_JSON)] = filename
        
        return redirect(url_for('upload_file', name=filename, data=FILES_JSON))
    else:
        return render_template('index.html', data=FILES_JSON) 

@app.route('/combine', methods=['GET'])
def combine_files():
    main.init(FILE_PATHS)
    return render_template('combined.html') 

if __name__ == "__main__":
    app.run(debug=True)