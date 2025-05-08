import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello", methods=['POST'])
def recieved_data():
        if request.method == 'POST':
           data = request.get_json() 
           print(data)
           return data, 200
        else:
            return "The post method did not work"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))