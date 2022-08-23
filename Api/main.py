from flask import Flask
from flask import jsonify,make_response,request
from flask_cors import CORS
from database import DbVisie

db = DbVisie()
app = Flask(__name__)
CORS(app,resources={r'/*' : {"origins": '*'}})



@app.route("/AllPeople")
def get_all_people():
    x = db.get_all_people()
    return make_response(x,200)


















if __name__ == "__main__":
    app.run(debug=True)