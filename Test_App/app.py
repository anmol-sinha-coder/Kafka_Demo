# app.py

from flask import Flask, request, jsonify
from producer import produce_message

app = Flask(__name__)

@app.route('/produce', methods=['POST'])
def produce():
    data = request.json
    produce_message(data)
    return jsonify({"status": "Message produced", "data": data}), 200

if __name__ == "__main__":
    app.run(debug=True)
