import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from flask import Flask
from api_blueprints.users import users_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config.update({
        "JWT_SECRET_KEY": 'test',
    })
    app.register_blueprint(users_bp)
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header(app):
    from flask_jwt_extended import create_access_token
    with app.app_context():
        token = create_access_token(identity="1")
        return {'Authorization': f'Bearer {token}'}

class TestUsersAPI:
    def test_get_users_success(self, client, auth_header, mocker):
        mocker.patch('db.Users.read', return_value={'id': 1, 'username': 'test'})
        resp = client.get('/users/1', headers=auth_header)
        assert resp.status_code == 200
        assert resp.json['success'] is True

    def test_get_users_not_found(self, client, auth_header, mocker):
        mocker.patch('db.Users.read', return_value=None)
        resp = client.get('/users/999', headers=auth_header)
        assert resp.status_code == 404
        assert resp.json['success'] is False

    def test_create_users_success(self, client, auth_header, mocker):
        mocker.patch('db.Users.create', return_value={'id': 1, 'username': 'test'})
        data = {'username': 'test', 'password_hash': 'pw', 'role_id': 1, 'employee_id': 1, 'is_active': True, 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}
        resp = client.post('/users/', data=data, headers=auth_header)
        assert resp.status_code == 200
        assert resp.json['success'] is True

    def test_create_users_error(self, client, auth_header, mocker):
        mocker.patch('db.Users.create', return_value=None)
        data = {'username': 'test'}
        resp = client.post('/users/', data=data, headers=auth_header)
        assert resp.status_code == 500
        assert resp.json['success'] is False

    def test_update_users_success(self, client, auth_header, mocker):
        mocker.patch('db.Users.update', return_value={'id': 1, 'username': 'test'})
        data = {'username': 'newname'}
        resp = client.put('/users/1', data=data, headers=auth_header)
        assert resp.status_code == 200
        assert resp.json['success'] is True

    def test_update_users_error(self, client, auth_header, mocker):
        mocker.patch('db.Users.update', return_value=None)
        data = {'username': 'fail'}
        resp = client.put('/users/1', data=data, headers=auth_header)
        assert resp.status_code == 500
        assert resp.json['success'] is False

    def test_delete_users_success(self, client, auth_header, mocker):
        mocker.patch('db.Users.delete', return_value={'id': 1})
        resp = client.delete('/users/1', headers=auth_header)
        assert resp.status_code == 200
        assert resp.json['success'] is True

    def test_delete_users_error(self, client, auth_header, mocker):
        mocker.patch('db.Users.delete', return_value=None)
        resp = client.delete('/users/1', headers=auth_header)
        assert resp.status_code == 500
        assert resp.json['success'] is False