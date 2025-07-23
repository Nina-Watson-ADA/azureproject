from azure.data.tables import TableServiceClient
from azure.core.exceptions import AzureError
from flask import Flask, render_template, request
import os

#connection_string = "9iCfC19VTGC/s2Nf6CQq7lxFcIy9bJPRGAoJDe6Un71npsSuD3bNskAKpoYQi1pTEV4Prz5fm2rR+AStlg7+MA=="

#try:
   #table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
    #table_client = table_service.get_table_client(table_name="producttable")
   # print ("Connected to Azure producttable table! (may not display as it's an empty table")
#except AzureError as e:
    #print ("Couldn't connect to Azure table storage: {e}")

#this stuff to link tables seems to be working funky as I'm on the student plan from what I can recall, so I won't link to the blob or the table



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, file.filename))
        return 'File uploaded successfully!'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
