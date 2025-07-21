import flask
import os
import uuid
from flask import Flask, request, send_from_directory, jsonify

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/upload', methods={'POST'})
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': "no selected file"}), 400
    filename_orig = file.filename or ""
    ext = os.path.splitext(filename_orig)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    url = request.host_url + 'i/' + filename
    return jsonify({'url': url})

@app.route('/i/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    