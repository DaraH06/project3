from flask import Flask,render_template,request,jsonify,redirect,url_for
from pymongo import MongoClient
import certifi

app = Flask(__name__)
pw = 'test'
conn_string = f'mongodb+srv://test:{pw}@cluster00.aw629as.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(conn_string)
db = client.DbNextGen

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/restaurants', methods=["GET"])
def get_restaurants():
    # This api endpoint should fetch a list of restaurants
    restaurants = list(db.restaurants.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'restaurants': restaurants})

@app.route('/restaurants/create',methods=["POST"])
def create_new():
    name = request.form.get('name')
    location = request.form.get('location')
    categories = request.form.get('categories')
    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')
    link = request.form.get('link')
    doc = {
        'name':name,
        'categories':categories,
        'location':location,
        'coordinate':[longitude,latitude],
        'link':link
    }
    db.restaurants.insert_one(doc)
    return jsonify({'msg':f'{name}, was created','status':'success'})

@app.route('/restaurants/delete',methods=['POST'])
def make_it_vanish():
    name = request.form.get('name')
    db.restaurants.delete_one({'name':name})
    return jsonify({'msg':f'{name}, was deleted','status':'success'})

@app.route('/map')
def map_prac():
    return render_template('prac_map.html')

@app.route('/map2')
def map_hwrk_prac():
    return render_template('homework_map.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
