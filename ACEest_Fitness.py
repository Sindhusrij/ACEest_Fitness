from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness & Gym API!",
        "status": "running"
    })

@app.route('/members')
def members():
    members_list = ["Alice", "Bob", "Charlie"]
    return jsonify({
        "members": members_list
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
