from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the 4-digit code
code_storage = {"code": "5678"}  # Pre-stored code

@app.route('/store_code', methods=['POST'])
def store_code():
    data = request.get_json()
    code = data.get('code')

    if not code or len(str(code)) != 4 or not str(code).isdigit():
        return jsonify({"error": "Invalid code"}), 400

    code_storage['code'] = code
    return jsonify({"message": "Code stored successfully"}), 200

@app.route('/get_code', methods=['GET'])
def get_code():
    code = code_storage.get('code')
    if code:
        return jsonify({"code": code}), 200
    else:
        return jsonify({"error": "No code stored"}), 404

if __name__ == '__main__':
    app.run(debug=True)
