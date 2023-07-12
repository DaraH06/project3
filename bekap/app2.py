from flask import Flask,render_template,request,jsonify,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__)
pw = 'test'
conn_string = f'mongodb+srv://test:{pw}@cluster00.aw629as.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(conn_string)
db = client.DbNextGen

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map_prac():
    return render_template('prac_map.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5050,debug=True)