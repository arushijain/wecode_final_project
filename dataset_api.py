import dataset, sqlalchemy, time, datetime
import PIL.Image
from cStringIO import StringIO
import os

drop_condition = True

class Data(object):
	def __init__(self):
		self.db = dataset.connect('postgresql://wecode_admin:wecode_password@localhost/wecode')
		
		if drop_condition:
			self.db['user'].drop()
			self.db['posts'].drop()
			print "dropped databases"

		if 'user' not in self.db.tables:
			user_table = self.db.create_table('user', primary_id='username', primary_type='String')
			user_table.create_column('photo', sqlalchemy.LargeBinary)

		if 'posts' not in self.db.tables:
			post_table = self.db.create_table('posts')
			post_table.create_column('username', sqlalchemy.String)
			post_table.create_column('content', sqlalchemy.String)
			post_table.create_column('timestamp', sqlalchemy.DateTime)

	def list_all_tables(self):
		return self.db.tables

	def add_user(self, user, filename):
		user_table = self.db.get_table('user')
		username = user_table.insert(user)
		user = self.db.get_table('user').find_one(username=username)
		user['photo'] = filename
		user_table.update(user, 'username')

	def get_image(self, username):
		imgfile = StringIO(self.db.get_table('user').find_one(username=username)['photo'])
		img = PIL.Image.open(imgfile)
		path = os.path.join('static', 'images', username + ".jpg")
		open(path, 'w')
		img.save(path, "JPEG")
		return path

	def add_post(self, post):
		post_table = self.db.get_table('posts')
		id = post_table.insert(post)
		post = self.db.get_table('posts').find_one(id=id)
		post['timestamp'] = datetime.datetime.utcnow()
		post_table.update(post, 'id')

	def get_all_users(self):
		return self.db.get_table('user').all()

	def get_all_posts(self):
		return self.db.get_table('posts').all()

	def get_user(self, username):
		return self.db.get_table('user').find_one(username=username)

	def user_exists(self, username):
		return (self.db.get_table('user').find_one(username=username) != None)

	def create_image(self, request):
		image_data = None
		file = request.files['photo']
		if file:
			image_data = file.read()
		return image_data


