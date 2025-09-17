# api to link frontend to backend
# frontend is html code
# backend is main.py 
# flask api

from flask import Flask, request, jsonify, render_template
import json
from bson import json_util
import os
import main

app = Flask(__name__, template_folder='templates', static_url_path='', static_folder='static')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        print('Filename: ', file)
        print('File path: ', file_path)
        text = main.pipeline(file_path)
        return json.loads(json_util.dumps(text))
        #return f"File uploaded successfully: {file.filename}"
    return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
