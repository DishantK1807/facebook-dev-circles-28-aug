from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import hashlib
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app.models import User


@app.route('/register')
def register():
	parser = reqparse.RequestParser()
	parser.add_argument('email', type=str)
	parser.add_argument('token', type=str)
	args = parser.parse_args()
	email = args['email']
	token = args['token']
	password = hashlib.md5(token.encode())
	user = User.query.filter_by(email = email)
	if user:
		return jsonify(user.password)
	else :
		user  = User(email = email , password = password)
		db.session.add(user)
		db.session.commit()
	return jsonify(password)

@app.route('/')
def home():
    pass

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    pass

# List all events
@app.route('/event/<id>')
def show_events():
    pass

# Add event
@app.route('/event', methods=['POST'])
def add_event():
    pass

# filters etc ..
@app.route('/event/<id>/query')
def query():
    pass

# populate db with data from csv
@app.route('/event/<id>/import_csv')
def import_csv():
    pass

# Attendee list for a event {ID}
@app.route('/event/<id>/attendees')
def attendees():

# Add walk-in for event {ID}
@app.route('/event/<id>/attendees/add_walkin')
def add_walkin():
    pass

# Send invite and update DB
@app.route('/event/<id>/send_invite')
def send_invite():
    pass

# Edit event
@app.route('/event/<id>/edit')
def edit():
    pass

# Event Analytics
@app.route('/event/<id>/stats')
def stats():
    pass

@app.route('/validate_qr/<id>')
def validate_qr():
    pass

if __name__ == "__main__":
    app.run(debug=True)
