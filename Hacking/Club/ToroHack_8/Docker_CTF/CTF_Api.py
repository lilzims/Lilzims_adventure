from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Dummy token storage
tokens = set()

@app.route('/get_token', methods=['GET'])
def get_token():
    token = secrets.token_hex(16)  # Generate a random token
    tokens.add(token)              # Store the token
    return jsonify({'token': token})

@app.route('/validate_token', methods=['POST'])
def validate_token():
    token = request.json.get('token')
    if token in tokens:
        return jsonify({'valid': True, 'message': 'The flag is ctf(ap1_fl4g)'})
    else:
        return jsonify({'valid': False, 'message': 'Token is invalid'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
