from flask import Flask, jsonify, request

app = Flask(__name__)

# Our data store
data_store = {}

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():
    return jsonify("Ich lebe!"), 200

@app.route('/resource/<int:id>', methods=['GET'])
def get_resource(id):
    if id in data_store:
        return jsonify(data_store[id]), 200
    else:
        return jsonify(message="Resource not found"), 404

@app.route('/resource', methods=['POST'])
def create_resource():
    new_data = request.get_json()
    if new_data:
        id = len(data_store) + 1
        data_store[id] = new_data
        return jsonify(message="Resource created", id=id), 201
    else:
        return jsonify(message="Request body cannot be empty"), 400

@app.route('/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    updated_data = request.get_json()
    if id in data_store:
        data_store[id] = updated_data
        return jsonify(message="Resource updated"), 200
    else:
        return jsonify(message="Resource not found"), 404

@app.route('/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    if id in data_store:
        del data_store[id]
        return jsonify(message="Resource deleted"), 200
    else:
        return jsonify(message="Resource not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
