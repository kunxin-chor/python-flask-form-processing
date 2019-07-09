from flask import Flask, render_template, request
import os

app = Flask(__name__)


# # this is the ROOT route
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('bmi.html')


# @app.route('/', methods=['POST'])
# def calculate_bmi():
    
#     weight = float(request.form.get('weight'))
#     height = float(request.form.get('height'))
#     bmi = weight / (height * height)
#     return render_template('bmi.html', bmi=bmi)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = weight / (height * height)
        return render_template('bmi.html', bmi=bmi)
    else:
        # GET case: return the template normally
        return render_template('bmi.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)