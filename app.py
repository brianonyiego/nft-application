from flask import Flask, request, jsonify, send_file
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for NFTs and users
nfts = {}
users = {}

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/create_nft', methods=['POST'])
def create_nft():
    data = request.json
    nft_id = str(uuid4())
    nfts[nft_id] = {
        'id': nft_id,
        'name': data['name'],
        'description': data['description'],
        'owner': data['owner']
    }
    return jsonify({'message': 'NFT created', 'nft_id': nft_id}), 201

@app.route('/transfer_nft', methods=['POST'])
def transfer_nft():
    data = request.json
    nft_id = data['nft_id']
    new_owner = data['new_owner']
    if nft_id in nfts:
        nfts[nft_id]['owner'] = new_owner
        return jsonify({'message': 'NFT transferred'}), 200
    return jsonify({'message': 'NFT not found'}), 404

@app.route('/get_nft/<nft_id>', methods=['GET'])
def get_nft(nft_id):
    if nft_id in nfts:
        return jsonify(nfts[nft_id]), 200
    return jsonify({'message': 'NFT not found'}), 404

@app.route('/get_user_nfts/<user_id>', methods=['GET'])
def get_user_nfts(user_id):
    user_nfts = [nft for nft in nfts.values() if nft['owner'] == user_id]
    return jsonify(user_nfts), 200

if __name__ == '__main__':
    app.run(debug=True)
