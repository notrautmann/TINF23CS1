"""
   Main Logic of flask App
"""
import os
import importlib.util
from flask import Flask, Blueprint, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token
)
import bcrypt
from dotenv import load_dotenv

from app.db.crud import read
from app.db.records.roles import Roles
from app.db.records.users import Users
from environment_constants import API_BLUEPRINTS_PATH


app = Flask(__name__)

# load .env before accessing information for app config
load_dotenv()

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(
    os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600)
)

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

    user_rec = read(Users, username=username)
    if not user_rec:
        return jsonify({"msg": "Bad credentials"}), 401

    _, user_name_db, pw_hash_db, role_id_db, is_active_db = user_rec

    if not is_active_db:
        return jsonify({"msg": "Account inactive"}), 401

    if not bcrypt.checkpw(password, pw_hash_db.encode("utf-8")):
        return jsonify({"msg": "Bad credentials"}), 401

    role_rec = read(Roles, id=role_id_db)
    role_name = role_rec[1] if role_rec else "unknown"

    additional_claims = {"role": role_name}
    access_token = create_access_token(
        identity=user_name_db,
        additional_claims=additional_claims
    )

    return jsonify(access_token=access_token), 200

@jwt.unauthorized_loader
def missing_token(err_str):
    """Handles the missing JWT token

    Args:
        err_str (Any): Reason for not finding a valid JWT

    Returns:
        Flask response: Missing Authorization Header Error 401
    """
    return jsonify({"msg": err_str}), 401

def load_and_register_api_blueprints():
    """
    Dynamically loads and registers the blueprints from the api/blueprints directory
    """
    for filename in os.listdir(API_BLUEPRINTS_PATH):
        if filename.endswith('.py'):
            module_name = filename[:-3]  # Remove the .py extension
            filepath = os.path.join(API_BLUEPRINTS_PATH, filename)

            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, Blueprint):
                    app.register_blueprint(attribute)

# Ensure that the blueprints were registered at program start
load_and_register_api_blueprints()
