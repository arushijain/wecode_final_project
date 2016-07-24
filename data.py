from tinydb import TinyDB, Query, where



def save_to_db(content):
	db = TinyDB('db/login_data.json')
	db.insert(content)

def get_from_db(field, value):
	db = TinyDB('db/login_data.json')
	return db.search(where(field) == value)

def get_all_from_db():
	db = TinyDB('db/login_data.json')
	all_items = db.all()
	print "all_items", all_items
	return all_items


# def save_user_to_db(content):
# 	db = TinyDB('db/login_data.json')
# 	if 'user' not in db.tables():
# 		table = db.table('user')
# 	table = db.table('user')
# 	table.insert(content)