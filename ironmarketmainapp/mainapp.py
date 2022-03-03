from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from sqlalchemy import UniqueConstraint
#from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:admin1234@db/mainapp'
CORS(app)

db = SQLAlchemy(app)

#migrate = Migrate(app, db)

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    title=db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

#db.create_all()

@app.route('/api/products')
def index():
    return "Product List" #jsonify(Product.query.all())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')