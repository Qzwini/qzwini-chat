from flask import Flask, render_template, redirect, url_for
from passlib.hash import  pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user, login_required,logout_user

from wtform_fields import *
from models import *



# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://itwpbnteihaupg:1a1204f0e914139fee598a3830ccbdc5fbec7bec0bb0dcb0120c36d002b04dcd@ec2-52-44-166-58.compute-1.amazonaws.com:5432/d39ct4ok2dqku6'
db = SQLAlchemy(app)

# Configure flask login 
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


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
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

        

    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET','POST'])
def chat():
    if not current_user.is_authenticated:
        return"Pleas login befor accessing Chat!"
    return "Chat with me :)"

@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return "Logged out using flask-login!"

if __name__ == '__main__':
 
    app.run(debug=True)