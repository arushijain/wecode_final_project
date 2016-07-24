from flask import Flask, render_template, request, url_for, redirect, request
import LoginForm, PostForm
import data, json, dataset_api
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', template_folder='templates')
db = dataset_api.Data()

UPLOAD_FOLDER = '/public/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/<username>')
def login_success(username):
    form = db.get_user(username)
    return render_template('/user.html', username=username, form=form)

@app.route('/',  methods=['GET', 'POST'])
def home():
    form = PostForm.PostForm(request.form)
    posts = db.get_all_posts()
    if request.method == 'POST': # and form.validate():
        content = request.form
        username = content['username']
        if db.user_exists(username) is True:
            db.add_post(content)
        else:
            error = "User " + username + " is not valid"
            return render_template('error.html', error=error)
        return redirect('/')
    return render_template('/home.html', form=form, posts=posts)

@app.route('/list')
def list():
    all_users = db.get_all_users()
    return render_template('/list.html', all_users=all_users)

@app.route('/error/<error>')
def error(error):
    return render_template('error.html', error=error)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm.LoginForm(request.form)
    if request.method == 'POST': # and form.validate():
    	content =  request.form
        username = content['username']
        # print "PHOTO IS:", form.photo
        # print "PHOTO DATA:", form.photo.data
        file = request.files['photo']
        filename = secure_filename(form.photo.data)
        #print "FILE ", file

        image_data = None
        if file:
            print "image exists"
            image_data = file.read()
            #
        if db.user_exists(username) is False:
            db.add_user(content, image_data.decode('utf-8'))
        else:
            error = "Username " + username + " is already taken"
            return render_template('error.html', error=error)
        #return redirect(url_for('login_success', username=content['username']))
        return redirect(username)
    return render_template('register.html', form=form)
        


if __name__ == "__main__":
    app.debug = True
    app.config("upload_folder") = UPLOAD_FOLDER
    app.secret_key = 's3cr3t'
    app.run(port=3000)











