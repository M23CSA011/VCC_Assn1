from flask import Flask, jsonify, request

app = Flask(__name__)

data_store = [
    {"id": 1, "message": "Hello from VCCI microservices!"},
    {"id": 2, "message": "This is a simple Flask API."}
]

@app.route("/api/data", methods=['GET'])
def get_all_data():
    """Fetch all messages"""
    return jsonify({"data": data_store})

@app.route("/api/data/<int:data_id>", methods=['GET'])
def get_data_by_id(data_id):
    """Fetch a specific message by ID"""
    result = next((item for item in data_store if item["id"] == data_id), None)
    if result:
        return jsonify(result)
    return jsonify({"error": "Data not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
