from flask import render_template, url_for, request
from flask import Flask, send_from_directory
app = Flask(__name__)
# url_for('CSS', filename='CSS/style.css')
@app.route('/CSS/<path:path>')
def send_static(path):
    return send_from_directory('CSS', path)

@app.route('/info/')
def info(var=None):
    # print(dir(request))
    # print(request.if_modified_since)
    # print(request.headers)
    
    return render_template('info.html', request=request)