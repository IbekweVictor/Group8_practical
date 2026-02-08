from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        text = request.form["text"]
        messages.append({"sender": sender, "receiver": receiver, "text": text})
        return "Message Sent! <a href='/'>Go Home</a>"
    return render_template("send.html")

@app.route("/view")
def view():
    return render_template("view.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
