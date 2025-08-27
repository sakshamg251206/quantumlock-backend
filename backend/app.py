# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Create an instance of the Flask application
app = Flask(__name__)

# Configure CORS to allow requests from your specific Vercel frontend URL
# Replace 'https://quantumlock-frontend.vercel.app' with your actual Vercel URL
CORS(app, origins='https://quantumlock-frontend.vercel.app')

# Placeholder for a Quantum-Random Number Generator. In the final version, this would be an API call.
def get_quantum_random_bytes(length):
    # This is a placeholder for a real API call to a QRNG service.
    # We'll mock it for now to get the project working.
    return os.urandom(length)

# A placeholder for the post-quantum encryption/decryption logic.
# In the final version, this would use a library like 'pqcrypto'.
class PostQuantumCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        # Placeholder logic: simple XOR for demonstration
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
    key_length = 32 # Example key length
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