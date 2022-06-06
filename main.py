from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URL'] = 'postgres://postgres:1312@localhost/fox_glass'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)
    
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))

db.create_all()


@app.route('/')
def index():
    myfile = open("templates/index.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page



if __name__ == "__main__":
    app.run()