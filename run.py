# From the flask module, import an object named Flask
from flask import Flask, render_template, request

# adding in functionality to access the operating system
import os

app = Flask(__name__)

@app.route('/hello')
def foobar():
    return render_template("hello.html")

@app.route('/greet_the_person', methods=['POST'])
def process_form():
    print(request.form)
    n = request.form.get('person_name')
    age = request.form.get('age')
    return "Hi, {}, welcome to the website!".format(n)
    

# @app.route('/hello', methods=['GET', 'POST'])
# def foobar():
#     if request.method == 'GET':
#         return render_template("hello.html")
#     elif request.method == 'POST':
#         print(request.form)
#         n = request.form.get('person_name')
#         age = request.form.get('age')
#         return "Hi, {}, welcome to the website".format(n)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)