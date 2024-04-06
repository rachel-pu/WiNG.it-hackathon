from flask import Flask, render_template

app = Flask(__name__)

@app.route('/send_text', methods=['POST'])
def receive_text():
    if request.is_json:
        data = request.get_json()  # Get data sent as JSON
        text = data.get('text', '')  # Extract text field from JSON data or default to empty string
        if text:
            print("Received text:", text)  # Optional: log to console or process text as needed
            return jsonify({"status": "success", "message": "Text received successfully"}), 200
        else:
            return jsonify({"status": "error", "message": "No text provided"}), 400
    else:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 415

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/interview")
def interview():
    return render_template("interview.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)