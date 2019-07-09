from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('form.html')
    
@app.route('/', methods=['POST'])
def process_form():
    print (request.form)
    name = request.form.get('first_name')
    message = request.form.get('message')
    spam = request.form.get("spam")
    attribution = request.form.get('attribution')
    if spam == None: 
        spam = "N/A"
    accept = request.form.get("accept")
    if accept == None:
        return "Please accept our terms and conditions"
   
    activities = request.form.getlist('activities[]')
    
    return render_template('edit-form.html', first_name=name,
        message=message, spam=spam, accept=accept, attribution=attribution,
        activities = activities)
        
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)