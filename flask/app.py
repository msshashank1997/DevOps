from flask import Flask, jsonify, request
from compontintrest import Compoundintrest
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"msg":"hello world"})

@app.route("/about", methods=["POST"])
def about():
    data = request.get_json()
    """print(type(data))
    print(data['name'])
    print(type(data['name']))
    print(type(data['age']))"""
    if data['age'] > 18:
        return "allow"
    else:
        return "not allow"

@app.route("/compontintrest", methods=["POST"])
def compontintrest():
    data = request.get_json()
    amount = data['principle']
    rateofintrest = data['rateofintrest']
    year = data['time']
    countintest, totalamount = Compoundintrest(amount,rateofintrest,year)
    return jsonify({
        "principle amount": amount,
        "year": year,
        "intest amount": round(countintest), 
        "total amount":round(totalamount)
        })

@app.route('/contact/<string:name>')
def contact(name):
    return name

if __name__ == "__main__":
    app.run(debug=True, port=5050)