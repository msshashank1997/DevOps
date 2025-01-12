from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://demoteam88:888888@cluster0.gdzal.mongodb.net/todo"
mongo = PyMongo(app)

@app.route('/', methods=["GET"])
def hello():
    return jsonify({"msg" : "Hello world"})

@app.route('/user', methods=["GET"])
def showuser():
    user = list(mongo.db.user.find())
    for i in user:
        print(i)
        i['_id'] = str(i['_id'])
    return jsonify(user)


# add into mongodb
@app.route('/user', methods=["POST"])
def adduser():
    data =  request.get_json()
    print(data)
    result = mongo.db.user.insert_one(data)
    return "hi"

# update into mongodb
@app.route('/user', methods=["PUT"])
def updateuser():
    data =  request.get_json()
    print(data)
    # what if email is not present
    result = mongo.db.user.update_one({'email': data['email']}, {'$set': data})
    #mongo.db.user.delete_one({'email': data['email']})
    return "hi"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
