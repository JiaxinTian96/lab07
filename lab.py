from flask import Flask, render_template, request

app = Flask(__name__)

@app.route ('/')

def index():
    return render_template('base.html')

@app.route ('/index',methods=['GET'])

def index():
    if form.validate_on_submit():
        return redirect(url_for('list_student'))

@app.route ('/report',methods=['GET'])

def index():
    return render_template('report.html')

@app.route ('/reportf',methods=['GET'])

def index():
    return render_template('reportf.html')

if __name__ == '__main__':
    app.run()