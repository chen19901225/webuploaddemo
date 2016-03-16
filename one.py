import os
from flask import Flask, request, jsonify, render_template

__author__ = 'Administrator'

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/upload_apk', methods=['POST'])
def upload_apk():
    post_file = request.files['file']

    save_file_path = os.path.join(os.path.abspath('.'), 'apk', post_file.filename)
    post_file.save(save_file_path)

    return jsonify(status='success')


if __name__ == '__main__':
    app.run(debug=True)
