Flask Application Folder Details

file_data :- folder have all the file we need to read if you want to read more file Please add that file into file_data folder

templates :- templates folder have 2 template index.html for data rendering and error.html for error display

flask_env :- folder have virtual env Details

requrements.txt :- file have all the requirements for this application to run

app.py :- this is the main file where all the code and flask application is running

URL Details:

base_url :- http://127.0.0.1:5000/parse/ :- this will give you the file1.txt details because we set that value if no file name is given

file_url :- http://127.0.0.1:5000/parse/file3.txt/ :- if you given the file name in the URL then its give you the all the lines into this file

start_end_line_url :- http://127.0.0.1:5000/parse/file3.txt?start_line=5&end_line=17 :- if you give the start and end line details then application give you that line as output only

errors :- if user give the wrong file name error raised for that case
          we are assuming user know the file line values
