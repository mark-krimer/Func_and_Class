from flask import Flask, render_template

app = Flask(__name__, template_folder="temp")

def say_hello(name):
    return f'Hello, {name}!'

@app.route("/")
def home():
    return render_template("index.html", say_hello=say_hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)