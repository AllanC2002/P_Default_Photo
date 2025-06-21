from flask import Flask, request, jsonify
from services.functions import assign_default_photo

app = Flask(__name__)

@app.route("/default-photo", methods=["POST"])
def assign_photo():

    data = request.get_json()
    Id_User = data.get("Id_User")

    if not Id_User:
        return jsonify({"error": "Id_User is required"}), 400

    response, code = assign_default_photo(Id_User)
    return jsonify(response), code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
