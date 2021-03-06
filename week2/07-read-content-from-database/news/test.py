from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    file = db.relationship('File')

    def __init__(self,name):
        self.name = name


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content


if __name__ == '__main__':
    
    file_id = db.session.query(File.id).filter_by(id=1).first()
    title = db.session.query(File.title).filter_by(id=file_id).first()
    content = db.session.query(File.content).filter_by(id=file_id).first()
    created_time = db.session.query(File.created_time).filter_by(id=file_id).first()
    name = db.session.query(Category.name).filter_by(id=file_id).first()
    files_id = db.session.query(File.id).all()
    if file_id in files_id:
        print(files_id)
    else:
        print(error)
#    print(title,name,created_time,content,files_id)


