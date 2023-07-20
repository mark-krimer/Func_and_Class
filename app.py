from flask import Flask, render_template

app = Flask(__name__, template_folder="temp")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello, {self.name}!'

def multiply(*args):
    product = 1
    for n in args:
        product = product * n
    return product

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

@app.route("/")
def home():
    mike = person("mark", 13)
    return render_template("index.html",
                           ver=ver,
                           review=review,
                           multiply=multiply,
                           user = mike)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)