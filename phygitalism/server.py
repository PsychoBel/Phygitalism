from flask import Flask, jsonify
import os, time
#import SOAPpy


app = Flask(__name__)

def make_answer():
    data = []
    path = "/home/michael/programming/Python/teaching"
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
    app.run()
'''
    try:
        SOAPpy.Config.debug = 1
        server = SOAPpy.SOAPServer(("localhost", 8080))
        server.registerFunction(app.run())
        server.serve_forever()
    except KeyboardInterrupt:
        exit(0)
'''