from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
import os
import logging
logging.basicConfig(level=logging.DEBUG)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gift_registry.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Item = None

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    purchased = db.Column(db.Boolean, default=False)

@app.before_first_request
def instantiate_item():
    global Item
    Item = Item()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registry')
def registry():
    global Item
    items = Item.query.all()
    logging.debug(items)
    return render_template('registry.html', items=items)

@app.route('/update-registry', methods=['POST'])
def update_registry():
    items = request.form['items']
    for item in items:
        item = Item.query.filter_by(name=item).first()
        item.purchased = True
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()
