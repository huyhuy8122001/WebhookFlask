from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hook():
    print(request.data)
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
