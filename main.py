from flask import Flask, render_template, session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'
# db:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# db = SQLAlchemy(app)
# Migrate(app, db)
class InfoForm(FlaskForm):
    password = StringField('Enter the password:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route ('/',methods=['GET','POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['password']=form.password.data
        pass_num = session['password']
        upper=False
        if len(str(pass_num))>8 and pass_num[-1].isdigit():
            for l in pass_num:
                if l.isupper():
                    upper=True
            if upper:
                return redirect(url_for('report'))
            else:
                return redirect(url_for('reportf'))
        else:
            return redirect(url_for('reportf'))
    return render_template('index.html',form=form)

@app.route ('/report')

def report():
    return render_template('report.html')

@app.route ('/reportf')

def reportf():
    return render_template('reportf.html')

if __name__ == '__main__':
    app.run(debug=True)