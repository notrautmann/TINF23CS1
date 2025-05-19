# save this as app.py
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# Gruppe 1 erzeugt API Routes & Methodenaufrufe
@app.route("/users/<id>", methods=['GET'])
def get_user(id):
    user = User.GetUser(id) 
    # Gruppe 3 erzeugt Business Logic zum Auslesen + Speichern + Löschen
    return user
# Gruppe 2 erzeugt eine Lösung für die Authentifizierung an der API und an der DB
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.filter_by(id=id).first()


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    ##user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404