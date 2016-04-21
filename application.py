from flask import Flask
from flask import render_template

application = Flask(__name__)
	
@application.route("/")
def index():
	return render_template('index.html')
	
@application.route("/about")
def about():
	return render_template('about.html')
	
@application.route("/blog")
def blog():
	return render_template('blog.html')
	
@application.route("/projects")
def projects():
	return render_template('projects.html')
	
	
if __name__ == '__main__':
	application.run()