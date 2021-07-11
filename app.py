from flask import Flask, request, render_template
from datetime import datetime
import json
import codecs

app = Flask(__name__,template_folder='templates')

@app.route('/parse/', defaults={'filename': 'file1.txt'})
@app.route('/parse/<filename>/')
def get_file_data(filename):
    start = 0
    end = 100000
    start_line = request.args.get('start_line')
    if start_line:
        start = int(start_line)
    end_line = request.args.get('end_line')
    if end_line:
        end = int(end_line)
    results= []
    file_data_path = "file_data"
    path = file_data_path + "/"+ filename
    try:
        try:
            with open(path, 'r', encoding="utf-8") as file_data:
                for item in file_data:
                    results.append(item)
            return render_template('index.html',lines=results[start:end+1])
        except:
            file_data = open(path, 'r', encoding="utf-16")
            for item in file_data:
                results.append(item)
            return render_template('index.html',lines=results[start:end+1])
    except Exception as e:
           return render_template('error.html', error = str(e), filename=filename)




if __name__ == "__main__":
  app.run(debug=True)
