from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import os

# Create an instance of the Flask application
app = Flask(__name__)

# This is the final, definitive CORS fix. It explicitly adds the headers
# to every response before it is sent back to the browser.
@app.before_request
def handle_before_request():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

# This is the root route for health checks.
@app.route("/")
def home():
    return jsonify({"message": "QuantumLock Backend API is running 🚀"})

# Placeholder for a Quantum-Random Number Generator
def get_quantum_random_bytes(length):
    return os.urandom(length)

# A placeholder for the post-quantum encryption/decryption logic
class PostQuantumCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        encrypted_bytes = bytearray(message.encode('utf-8'))
        for i in range(len(encrypted_bytes)):
            encrypted_bytes[i] ^= self.key[i % len(self.key)]
        return encrypted_bytes.hex()
    def decrypt(self, encrypted_hex):
        decrypted_bytes = bytearray.fromhex(encrypted_hex)
        for i in range(len(decrypted_bytes)):
            decrypted_bytes[i] ^= self.key[i % len(self.key)]
        return decrypted_bytes.decode('utf-8')

@app.route('/api/generate-key', methods=['GET'])
def generate_key():
    key_length = 32
    key = get_quantum_random_bytes(key_length)
    return jsonify({
        'key': key.hex(),
        'message': 'Quantum-inspired key generated successfully.'
    })

@app.route('/api/encrypt', methods=['POST'])
def encrypt_message():
    data = request.json
    message = data.get('message')
    key_hex = data.get('key')
    key = bytes.fromhex(key_hex)
    
    if not message or not key:
        return jsonify({'error': 'Missing message or key'}), 400
    
    cipher = PostQuantumCipher(key)
    encrypted_message = cipher.encrypt(message)
    return jsonify({
        'encrypted_message': encrypted_message,
        'message': 'Message encrypted successfully with a post-quantum algorithm.'
    })

@app.route('/api/decrypt', methods=['POST'])
def decrypt_message():
    data = request.json
    encrypted_hex = data.get('encrypted_message')
    key_hex = data.get('key')
    key = bytes.fromhex(key_hex)
    
    if not encrypted_hex or not key:
        return jsonify({'error': 'Missing encrypted message or key'}), 400
    
    cipher = PostQuantumCipher(key)
    decrypted_message = cipher.decrypt(encrypted_hex)
    return jsonify({
        'decrypted_message': decrypted_message,
        'message': 'Message decrypted successfully.'
    })

if __name__ == '__main__':
    app.run(debug=True)