from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/logo.svg', methods=['GET'])
def logo():
    stop_color_1 = request.form.get('color1')
    if stop_color_1:
        return render_template('azure-logo.svg', 
            stop_color_1 = stop_color_1,
            mimetype="image/svg")
    else:
        return render_template('azure-logo.svg', 
            stop_color_1 = 'red',
            mimetype='image/svg')

if __name__ == '__main__':
   app.run()