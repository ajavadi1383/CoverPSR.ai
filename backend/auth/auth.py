from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Replace this with your user authentication logic
    if username == 'test' and password == 'test':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'Bad username or password'}), 401

if __name__ == "__main__":
    app.run()