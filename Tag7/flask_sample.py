from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_method():
    return jsonify(message="GET request successful"), 200

@app.route('/post', methods=['POST'])
def post_method():
    data = request.get_json()
    return jsonify(message="POST request successful", data=data), 201

@app.route('/put', methods=['PUT'])
def put_method():
    data = request.get_json()
    return jsonify(message="PUT request successful", data=data), 200

@app.route('/delete', methods=['DELETE'])
def delete_method():
    return jsonify(message="DELETE request successful"), 200

@app.route('/patch', methods=['PATCH'])
def patch_method():
    data = request.get_json()
    return jsonify(message="PATCH request successful", data=data), 200

if __name__ == '__main__':
    app.run(debug=True)
