from flask import Flask, request, jsonify
from uds.uds_handler import UDSHandler

app = Flask(__name__)
uds = UDSHandler()

@app.route('/session', methods=['POST'])
def session():
    data = request.json

    if not data or "request" not in data:
        return jsonify({"error": "Invalid request"}), 400

    response = uds.session_control(data.get("request"))

    return jsonify({
        "service": "session_control",
        "request": data.get("request"),
        "response": response
    })


@app.route('/read_did', methods=['GET'])
def read_did():
    did = request.args.get("did")

    if not did:
        return jsonify({"error": "Missing DID"}), 400

    response = uds.read_did(did)

    return jsonify({
        "service": "read_did",
        "did": did,
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)