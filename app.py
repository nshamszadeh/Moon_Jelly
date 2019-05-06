import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import LoginForm, UserForm, DeleteForm

# Some boilerplate setup stuff.

app = Flask(__name__)

# URL should be whatever database URL is being used (if testing on your own use a database different from the team's )

#let website reload properly 
app.config['ASSETS_DEBUG'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ricculxqdypnfh:d8283cc0c6d1c05d5874a972d5176b29c24751188711916086c6e4537f035274@ec2-23-21-136-232.compute-1.amazonaws.com:5432/dfuo44q4pq80o6'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = 'mOon_jElLy wAs oRiGiNa11y g0nNa b3 SuP3r MaRi0 gAlAxY' # need to change later
# im not mocking Aidan, this key actually needs to be secure which is why it looks all crazy
# I feel personally attacked

db = SQLAlchemy(app) # wow we have a database
migrate = Migrate(app, db)

# Create our database model. 
class User(db.Model):

  __tablename__ = "users"

  # Each user (doctor) will have all these things attributed to him or her
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text, unique=True)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  specialty = db.Column(db.Text)

  # initialize the object
  def __init__(self, email, first_name, last_name, specialty):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
    self.specialty = specialty
  
#user_form = UserForm()
# This is the main homepage for now. GET and POST are for web forms.
@app.route('/add', methods = ['GET', 'POST'])
def homepage():
  
  # define a form object
  user_form = UserForm()

  # if we are posting a form, i.e. submitting a form, store all the info in these variables
  if request.method == 'POST':
    first_name = request.form['first_name'] 
    last_name = request.form['last_name']
    email = request.form['email']
    specialty = request.form['specialty']

    # if the inputs we're all validated by WTforms (improve validation later)
    if user_form.validate(): 
      # then store info in an initialized User object and store the object in the database
      new_user = User(email, first_name, last_name, specialty)
      db.session.add(new_user) # add to database
      db.session.commit() # for some reason we also need to commit it otherwise it won't add
      return redirect('/schedule')#go to schedule after submit  ####This doesn't seem to work?
    else:
      print("Invalid input(s)!")

  # add html file here
  return render_template('home.html', form = user_form)


  @app.route('/remove', methods = ['GET', 'POST'])
def remove():
  
  delete_form = DeleteForm()

  if request.method == 'POST':
    Name2Rm = request.form['first_name']
   
    if delete_form.validate(): 
      toRM = User.query.filter_by(first_name = Name2Rm).first()
      db.session.delete(toRM)
      db.session.commit()
      return redirect('/schedule')#go to schedule after submit  ####This doesn't seem to work?
    else:
      print("Invalid input(s)!")

  # add html file here
  return render_template('remove.html', delete_form = delete_form)

"""

from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate=Migrate(app,db)
# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %I:%M %p")

# add html code here
return 

"""

@app.route('/about')
def about():
  return render_template('about.html')

#create a schedule page
@app.route('/schedule')
def schedule():
  u = User.query.all()
  cardi = User.query.filter_by(specialty="cardiologist").all()
  return render_template('schedule.html', users=u, cardi=cardi)

#create a log in page
@app.route('/', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if request.method == 'POST':
    email = request.form['email']
    if User.query.filter_by(email=email).first():
      return redirect('/add')#go to schedule after submit 
    else:
      print("Invalid input(s)!")
  return render_template('login.html', form=form)

#test to print out the first names of users 
@app.route('/users')
def users():
  u = User.query.all()
  return '<br/>'.join([a.first_name for a in u])

#return render_template('home.html', form = user_form)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
