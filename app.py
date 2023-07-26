from flask import Flask, render_template

app = Flask(__name__, template_folder="temp")


class person:
    # defining the variables 
    def __init__(self, name, age, prog):
        self.name = name
        self.age = age
        self.prog = prog

    # Says hello to you
    def say_hello(self):
        return f'Hello, {self.name}!'
    
    # Checks your age and if you have programming experience and responds acordingly
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

# Mulitplies given digits together
def multiply(*args):
    product = 1
    for n in args:
        product = product * n
    return product

# Adds given digits together
def review(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

# Defines directory 
@app.route("/")
def home():
    p1 = person("Mark", 13, "yes")
    return render_template("index.html",
                           review=review,
                           multiply=multiply,
                           user = p1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
