"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template,url_for, flash, redirect
from form import RegisterFrom,LoginFrom
app = Flask(__name__)
app.config['SECRET_KEY']='20476bc8ecf00cebf5ea68c052af4947'

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20,2018',

        },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Seconde post content',
        'date_posted':'April 10,2019',
            
            
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
        form = RegisterFrom()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!','success')
            return redirect(url_for('home'))
        return render_template('register.html',title='Register',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
        form = LoginFrom()
        if form.validate_on_submit():
            if form.email.data ==  'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else :
                flash('Login Unsuccessful. Please check username and password', 'error')
        return render_template('login.html',title='Login',form=form)



if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.run(debug=True, host='0.0.0.0')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    ##app.run(HOST, PORT, debug=True)
