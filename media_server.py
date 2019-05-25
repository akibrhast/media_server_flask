#import click #for command line arguments
#from flask.ext.runner import Runner(also for comand line arguments)
from forms import RegistrationForm, LoginForm
from flask import jsonify
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

'''
Things to change in this script
1: Modify to add command line arguments when running script
	-> python media_server.py -d 0( set debug to false, app is then accesible globally. Default/no args is debug true, app hosted only on local network)
	-> python media_server.py -port (set port to host at, defaults to 5001. -port option only avilable if -d 0 is not used)
'''
DEBUG =True
PORT = 5001



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


def partialListGen():
		for i in range(0,len(video_files),10):
			yield video_files[i:i+10]
v=partialListGen()
@app.route('/index',methods=['GET'])
def index():
	if session.get('logged_in'):
		for root, dirs, files in os.walk("static/video", topdown=False):
			for name in files:
				#temporary fix to only grab mp4 files
				if name.find("mp4")!= -1:
					video_files.append([name,os.path.join(root, name)])
		video_files_number = len(video_files)
		
		return render_template("index.html", title='Home', video_files_number=video_files_number, video_files=next(v))
	else:
		return redirect(url_for('do_admin_login'))

@app.route('/index',methods=['POST'])
def something():
	
	return str(next(v))
	
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
	if DEBUG:
		app.run(host='0.0.0.0', debug=True,port=PORT)
	else:
		run_with_ngrok(app)

		app.run()

