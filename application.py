from flask import Flask, render_template

from wtform_fields import *
from  models import *



# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'postgres://itwpbnteihaupg:1a1204f0e914139fee598a3830ccbdc5fbec7bec0bb0dcb0120c36d002b04dcd@ec2-52-44-166-58.compute-1.amazonaws.com:5432/d39ct4ok2dqku6'
db = SQLAlchemy(app)

@app.route("/",methods=['GET','POST'])
def index():
    
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

     
        # Add username 
        user = User(username=username, Password=Password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into db"


    return render_template("index.html", form=reg_form)

if __name__ == '__main__':
 
    app.run(debug=True)