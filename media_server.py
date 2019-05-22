from forms import RegistrationForm, LoginForm

from importlib import reload
import time
from flask_ngrok import run_with_ngrok
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,send_from_directory
import os,sys
from sqlalchemy.orm import sessionmaker
from tabledef import *

from flask_login import login_user, current_user, logout_user, login_required
engine = create_engine('sqlite:///tutorial.db', echo=True)

reload(sys)
video_dir = 'static/video/'

app = Flask(__name__)
video_files=[]
DEBUG =True

@app.route('/')
@app.route('/login')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def do_admin_login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
	 
	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
	result = query.first()
	
	if result:
    	
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return home()
	

@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()
	
'''
@app.route('/signup', methods=['GET','POST'])
def do_signup():
	POST_FIRSTNAME = str(request.form['firstname'])
	POST_LASTNAME  = str(request.form['lastname'])
	POST_USERNAME  = str(request.form['username'])
	POST_EMAIL     = str(request.form['email'])
	POST_PASSWORD  = str(request.form['password'])
	Session = sessionmaker(bind=engine)
	s = Session()
	user = User(username=POST_USERNAME,password=POST_PASSWORD,firstname=POST_FIRSTNAME,lastname=POST_LASTNAME,email=POST_EMAIL,)
	s.add(user)
	s.commit()

	return redirect(url_for('home'))
		
@app.route("/signup")
def signup():
	return render_template('signup.html')
'''		
@app.route('/signup', methods=['GET','POST'])
def signup():
	form = RegistrationForm()
	if form.validate_on_submit():
		print(form.password.data)
		POST_FIRSTNAME = form.firstname.data
		POST_LASTNAME  = form.lastname.data
		POST_USERNAME  = form.username.data
		POST_EMAIL     = form.email.data
		POST_PASSWORD  = form.password.data
		Session = sessionmaker(bind=engine)
		s = Session()
		user = User(username=POST_USERNAME,password=POST_PASSWORD,firstname=POST_FIRSTNAME,lastname=POST_LASTNAME,email=POST_EMAIL,)
		s.add(user)
		s.commit()
		return redirect(url_for('home'))
	return render_template('signup.html', title='Register', form=form)

@app.route('/index')
def index():
	if session.get('logged_in'):
		for root, dirs, files in os.walk("static/video", topdown=False):
			for name in files:
				#temporary fix to only grab mp4 files
				if name.find("mp4")!= -1:
					video_files.append([name,os.path.join(root, name)])
		video_files_number = len(video_files)
		return render_template("index.html", title='Home', video_files_number=video_files_number, video_files=video_files)



	
@app.route('/play')
def play():
    if session.get('logged_in'):
    	return render_template('play.html')
 
'''
@app.route('/<filename>')
def video(filename):
    return render_template('play.html', title=filename, video_file=filename)
'''

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	if DEBUG == True:
		app.run(host='0.0.0.0', debug=True,port=5001)
	else:
		run_with_ngrok(app)
		app.run()
