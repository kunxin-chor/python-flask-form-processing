from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/survey')
def show_survey():
    return render_template("survey.template.html")

# route for POST /survey
@app.route('/survey', methods=['POST'])
def process_survey_form():
    print (request.form)
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    
    if "prefer-spicy" in request.form:
        prefer_spicy = request.form['prefer-spicy']
    else:
        prefer_spicy = None
    
    # we must request.form.getlist('<name attribute of the checkboxes>')
    if "heard-about" in request.form:
        heard_about = request.form.getlist('heard-about')
    else:
        heard_about = []
    
    comments = request.form['comments']
  
    occupation = request.form['occu']
  
    return render_template("survey_results.template.html", fn=first_name, 
        ln=last_name, ps=prefer_spicy, ha=heard_about, c=comments, o=occupation)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
