from flask import Flask, render_template, request, url_for, redirect, request
import LoginForm
import data, json

app = Flask(__name__, static_url_path='/static', template_folder='templates')

@app.route('/<username>')
def login_success(username):
    form = data.get_from_db('username', username)
    for f in form:
        print f['username']
        print "-----" 
    form =  form[0]
    return render_template('/user.html', username=username, form=form)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/list')
def list():
    all_users = data.get_all_from_db()
    return render_template('/list.html', all_users=all_users)

@app.route('/post')
def post():
    return "Yet to implement post"
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm.LoginForm(request.form)
    print request.method
    if request.method == 'POST': # and form.validate():
        print "post"
    	content =  request.form
        data.save_to_db(content)
        print "saved to db"
        username = content['username']
        #return redirect(url_for('login_success', username=content['username']))
        return redirect(username)
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = 's3cr3t'
    app.run(port=3000)











