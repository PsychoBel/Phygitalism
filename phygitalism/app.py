from flask import Flask, jsonify
import os, time


app = Flask(__name__)


def make_answer():
    data = []
    path = "/api/meta"
    files = os.listdir(path)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        stinfo = os.stat(path + '/' + file)
        date = time.asctime(time.localtime(stinfo.st_atime))
        data.append({'name': filename,
                     'type': file_extension,
                     'time': date})
    return data


@app.route('/')
def index():
    d = make_answer()
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')


