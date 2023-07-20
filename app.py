from flask import Flask, render_template

app = Flask(__name__, template_folder="temp")

class person:
    def __init__(self, name, age, prog):
        self.name = name
        self.age = age
        self.prog = prog

    def say_hello(self):
        return f'Hello, {self.name}!'
    
    def ver(self):
        if self.age >= 10:
            if self.prog == "yes":
                return "Welcome to the Flask course!"
            elif self.prog == "no":
                return "Programming experience required to learn the Flask course!"
        if self.age < 10:
            if self.prog == "yes":
                return "Welcome, young genius! Let's start learning Flask!"
            elif self.prog == "no":
                return "Access to the Flask course is closed."

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

@app.route("/")
def home():
    mike = person("mark", 13, "yes")
    return render_template("index.html",
                           review=review,
                           multiply=multiply,
                           user = mike)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)