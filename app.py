from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
finalTranscription = ''

# app.config["SECRET_KEY"] = "your_secret_key"  # Needed for session management
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

@app.route('/send_text', methods=['POST'])
def receive_text():
    if request.is_json:
        data = request.get_json()  # Get data sent as JSON
        finalTranscription = data.get('text', '')  # Extract text field from JSON data or default to empty string
        if finalTranscription:
            print("Received text:", finalTranscription)  # Optional: log to console or process text as needed

            return finalTranscription
            # return jsonify({"status": "success", "message": "Text received successfully"}), 200
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

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)