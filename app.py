from flask import Flask, render_template

app = Flask(__name__, template_folder="temp")

def review(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum


def ver(age, experience):
    if age >= 10:
        if experience == "yes":
            return "Welcome to the Flask course!"
        elif experience == "no":
            return "Programming experience required to learn the Flask course!"
    if age < 10:
        if experience == "yes":
            return "Welcome, young genius! Let's start learning Flask!"
        elif experience == "no":
            return "Access to the Flask course is closed."

def say_hello(name):
    return f'Hello, {name}!'

@app.route("/")
def home():
    return render_template("index.html",
                           say_hello=say_hello,
                           ver=ver,
                           review=review)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)