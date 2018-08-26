from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    print "Data Received"
    text = request.get_data()
    print text
    return 'Ok'
if __name__ == "__main__":
    print "First Called"
    app.run(host="0.0.0.0")
