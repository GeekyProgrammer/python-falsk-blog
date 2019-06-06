from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
from werkzeug import secure_filename
import json
import math
import os

with open('config.json', 'r') as c:
	params = json.load(c)['params']

local_server = params["local_server"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.secret_key = "super-secret-key"

app.config.update(
	MAIL_SERVER = 'smtp.gmail.com',
	MAIL_PORT = '465',
	MAIL_USE_SSL = True,
	MAIL_USERNAME = params['gmail_username'],
	MAIL_PASSWORD = params['gmail_password']
	)

mail = Mail(app)

if(local_server):
	app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
	srno = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(40), nullable=False)
	phone_no = db.Column(db.String(14), nullable=False)
	message = db.Column(db.String(180), nullable=False)
	date = db.Column(db.String(12), nullable=True)

class posts(db.Model):
	srno = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	slug = db.Column(db.String(40), nullable=False)
	content = db.Column(db.String(180), nullable=False)
	caption = db.Column(db.String(60), nullable=False)
	date = db.Column(db.String(12), nullable=True)
	img_file = db.Column(db.String(30), nullable=False)
	




@app.route("/")
def index():
	post = posts.query.filter_by().all()
	#[0:params['no_of_posts']]
	last = math.ceil(len(post) /int(params['no_of_posts']))

	page = request.args.get('page')

	if (not str(page).isnumeric()):
		page = 1

	page = int(page)

	post = post[(page-1)*int(params['no_of_posts']) : (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]


	if (page==1):
		prev = "#"
		nxt = "/?page="+ str(page+1)
	elif (page==last):
		nxt = "#"
		prev = "/?page="+ str(page-1)
	else:
		prev = "/?page="+ str(page-1)
		nxt = "/?page="+ str(page+1)


	
	return render_template("index.html", param=params, posts = post, prev=prev, nxt=nxt)

@app.route("/posts/<string:post_slug>", methods=["GET"])
def post_route(post_slug):
	post = posts.query.filter_by(slug = post_slug).first()
	return render_template("post.html", param=params, post = post)


@app.route("/about")
def about():
	return render_template("about.html", param=params)

@app.route("/contact", methods=["GET","POST"])
def contact():
	if(request.method == "POST"):
		name = request.form.get("name")
		email = request.form.get("email")
		phone = request.form.get("phone")
		message = request.form.get("msg")
		date = datetime.now()
		#ADD to Database
		entry = Contacts(name = name, email = email, phone_no = phone, message = message, date = date)
		db.session.add(entry)
		db.session.commit()

		mail.send_message(
			"A Message From "+ name,
			sender = email,
			recipients=[params['gmail_username']],
			body=message + '\n \n' + "Contact : " + phone + '\n \n' + "Email : " + email
			)

	return render_template("contact.html", param=params)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
	post = posts.query.filter_by().all()

	if ('user' in session and session['user']==params['admin_user']):
		return render_template("dashboard.html", param=params, posts=post)

	if (request.method=="POST"):
		username = request.form.get("uname")
		password = request.form.get("password")
		
		if (username == params['admin_user'] and password == params['admin_password']):
			session['user'] = username
			return render_template("dashboard.html", param=params, posts=post)
		else:
			return render_template("login.html", param=params)

	else:
		return render_template("login.html", param=params)

@app.route("/edit/<string:sno>", methods=["GET", "POST"])
def edit(sno):
	if ('user' in session and session['user']==params['admin_user']):
		if (request.method=="POST"):
			new_title = request.form.get("title")
			new_slug = request.form.get("slug")
			new_content = request.form.get("content")
			new_caption = request.form.get("caption")
			new_img = request.form.get("img_file")
			date = datetime.now()

			if (sno == '0'):
				post = posts(
					title = new_title,
					slug = new_slug,
					content = new_content,
					caption = new_caption,
					date = date,
					img_file = new_img
					)
				
				db.session.add(post)
				db.session.commit()
				return redirect('/edit/'+ str(post.srno))

				

			else:
				post = posts.query.filter_by(srno=sno).first()
				
				post.title = new_title
				post.slug = new_slug
				post.content = new_content
				post.caption = new_caption
				post.img_file = new_img
				post.date = date
				db.session.commit()
				return redirect('/edit/'+ sno)

		post = 	posts.query.filter_by(srno=sno).first()
		return render_template("edit.html", param=params, sno=sno, post=post)

@app.route("/uploader", methods=["GET", "POST"])
def uploader():
	if ('user' in session and session['user']==params['admin_user']):
		if (request.method=="POST"):
			f = request.files['file1']
			f.save(os.path.join(app.config['UPLOAD_FOLDER']), secure_filename(f.filename))
			return "UPLOADED SYCCESSFULLY!!!!!"

@app.route("/logout")
def logout():
	session.pop('user')
	return redirect('/dashboard')

@app.route("/delete/<string:sno>", methods=["GET", "POST"])
def delete(sno):
	if ('user' in session and session['user']==params['admin_user']):
		post = posts.query.filter_by(srno=sno).first()
		db.session.delete(post)
		db.session.commit()
		return redirect('/dashboard')



if __name__ == '__main__':
	app.run(debug = True)