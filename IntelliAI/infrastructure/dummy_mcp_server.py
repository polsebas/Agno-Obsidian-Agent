# infrastructure/dummy_mcp_server.py
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
VAULT_DIR = os.getenv("OBSIDIAN_VAULT", "./vault")

@app.route('/list_notes', methods=['GET'])
def list_notes():
    files = [f for f in os.listdir(VAULT_DIR) if f.endswith('.md')]
    return jsonify(files)

@app.route('/read_note/<note_id>', methods=['GET'])
def read_note(note_id):
    path = os.path.join(VAULT_DIR, note_id)
    with open(path, 'r') as f:
        return f.read()

@app.route('/write_note/<note_id>', methods=['POST'])
def write_note(note_id):
    path = os.path.join(VAULT_DIR, note_id)
    content = request.json.get('content', '')
    with open(path, 'w') as f:
        f.write(content)
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000)