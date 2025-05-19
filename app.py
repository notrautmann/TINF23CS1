import os
import importlib.util
from flask import Flask, Blueprint, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token
)
import bcrypt
from dotenv import load_dotenv
import db


app = Flask(__name__)

load_dotenv()

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(
    os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600)
)

@app.route("/")
def hello():
    return "Hello, World!"

jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint to aquire a JWT which will be required for all requests except to "/" and "/login".
    
    Uses users from Users table of the DB.
    Assumes the passwords are hashed using bcrypt.
    The tokens store the username, accessible via get_jwt_identity() and the role (name, not id), accessible via get_jwt().get("role")
    """
    username = request.json.get("username", "")
    password = request.json.get("password", "").encode("utf-8")

    # Look up user
    user_rec = db.Users.read_username(username)
    if not user_rec:
        return jsonify({"msg": "Bad credentials"}), 401

    _, uname, pw_hash, role_id, is_active = user_rec

    # Active check
    if not is_active:
        return jsonify({"msg": "Account inactive"}), 401

    # Password check (bcrypt)
    if not bcrypt.checkpw(password, pw_hash.encode("utf-8")):
        return jsonify({"msg": "Bad credentials"}), 401

    # Fetch role name
    role_rec = db.Roles.read(role_id)
    role_name = role_rec[1] if role_rec else "unknown"

    # Create JWT: identity=username, plus a “role” claim
    additional_claims = {"role": role_name}
    access_token = create_access_token(
        identity=uname,                         # accessible via get_jwt_identity()
        additional_claims=additional_claims     # accessible via get_jwt().get("role")
    )

    return jsonify(access_token=access_token), 200

@jwt.unauthorized_loader
def missing_token(err_str):
    return jsonify({"msg": "Missing Authorization Header"}), 401

# Dynamically load and register blueprints from the api_blueprints directory
blueprint_dir = os.path.join(os.path.dirname(__file__), 'api_blueprints')
for filename in os.listdir(blueprint_dir):
    if filename.endswith('.py'):
        module_name = filename[:-3]  # Remove the .py extension
        filepath = os.path.join(blueprint_dir, filename)

        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, Blueprint):
                app.register_blueprint(attribute)