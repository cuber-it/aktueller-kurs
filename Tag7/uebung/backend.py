from flask import Flask, jsonify, request

import lotto_tools

lotto = lotto_tools.LottoBude()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():
    return jsonify("LOTTOBUDE 2023 up"), 200

@app.route('/tipp', methods=['POST'])
def enter_tipp():
    tipp = request.get_json().get('tipp', '')
    delim = request.get_json().get('delim', '.')
    lotto.enter_tipp(tipp, delim)
    return jsonify({"message": "Tipp entered successfully"}), 200

@app.route('/play', methods=['POST'])
def play():
    lotto.play()
    return jsonify({"message": "Game started"}), 200

@app.route('/result', methods=['GET'])
def fetch_result():
    tipp, ziehung, result = lotto.fetch_result()
    return jsonify({
        "tipp": tipp,
        "ziehung": ziehung,
        "result": result
    }), 200


app.run(debug=True)
