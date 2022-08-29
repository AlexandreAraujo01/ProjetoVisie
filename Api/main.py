import json
from flask import Flask
from flask import jsonify,make_response
from flask import request
from flask_cors import CORS
from database import DbVisie

db = DbVisie()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route("/AllPeople")
def get_all_people():
    response = db.get_all_people()
    return make_response(response,200)

@app.route("/teste",methods=["POST"])
def teste():
    data = request.get_json()
    response = db.specific_search("id_pessoa",data["id"],data["column"])
    return response
    
@app.route("/alterValue",methods=["PUT"])
def alter_value():
    data = request.get_json()
    db.update_people(data['column'],data['value'],data['id'])
    return "valor alterado!"


@app.route("/deletePeople/<int:id>", methods=['DELETE'])
def delete_people(id):
    x = db.delete_people(id)
    return make_response(x,200)

@app.route("/filter", methods=['POST'])
def filtered_search():
    data = request.get_json()
    key = data.get('key',"null")
    value = data.get("value","null")
    if key != "null" and value != "null":
        response = db.specific_search2(data['key'],data['value'],'*')
    return response











if __name__ == "__main__":
    app.run(debug=True)