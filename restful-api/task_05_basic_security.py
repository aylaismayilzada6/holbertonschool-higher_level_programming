from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


#curl -X POST -H "Content-Type: application/json" \
# -d '{"username": "user1", "password": "password"}' \
#  http://127.0.0.1:5000/login
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_super_secret_key'  # Change this in production!
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Change the password generation lines to this:
users = {
    "user1": {
        "username": "user1", 
        "password": generate_password_hash("password", method='pbkdf2:sha256'), 
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password", method='pbkdf2:sha256'), 
        "role": "admin"
    }
}

# --- Basic Authentication Logic ---
@app.route('/')
def home():
    return "API is running! Try /basic-protected or /login"


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# --- JWT Authentication Logic ---

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # We store the role in the identity (or as claims) to check later
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- Custom JWT Error Handlers (Mandatory for Tests) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()