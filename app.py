from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text) 


@app.route('/')
def home():
    return {
        "msg": "ok",
        "user": "prem",
    }


@app.route('/test')
def test():
    try: 
        data = Blog.query.all()
        blogs = []

        for b in data:
            blog = {}
            blog['id'] = b.id
            blog['title'] = b.title
            blog['description'] = b.description
            blogs.append(blog)
        return blogs
    except Exception as e:
        print(e)
        return {"error": "Something went wrong!!"}


if __name__ == '__main__':
    app.app_context().push()
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)