from flask import Flask, render_template, redirect, url_for
from passlib.hash import  pbkdf2_sha256
from wtform_fields import *
from models import *



# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://itwpbnteihaupg:1a1204f0e914139fee598a3830ccbdc5fbec7bec0bb0dcb0120c36d002b04dcd@ec2-52-44-166-58.compute-1.amazonaws.com:5432/d39ct4ok2dqku6'
db = SQLAlchemy(app)

@app.route("/",methods=['GET','POST'])
def index():
    
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        hashed_pswd = pbkdf2_sha256.hash(password)

     
        # Add username 
        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        return"logged in, finally"

    return render_template("login.html", form=login_form)



if __name__ == '__main__':
 
    app.run(debug=True)