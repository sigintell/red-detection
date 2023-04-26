from flask import Flask, request, jsonify, render_template

# Create a Flask application
app = Flask(__name__)


# Serve root index file
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/notifications", methods=["POST"])
def handle_notifications():
    name = request.form.get("name")
    if name == "Blood":
        result = "Blood detected!"
    else:
        result = "Nothing"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
