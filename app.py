from flask import Flask, render_template, request, redirect, url_for
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

    def __repr__(self):
        return f'<Item {self.name}>'

"""
@app.before_first_request
def instantiate_item():
    global Item
    Item = Item()
"""

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    purchased = db.Column(db.Boolean, default=False, nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registry", methods=["GET", "POST"])
def registry():
    if request.method == "POST":
        # Add a new item to the registry
        name = request.form["name"]
        price = request.form["price"]
        item = Item(name=name, price=price)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("registry"))
    else:
        # Show the registry
        items = Item.query.all()
        return render_template("registry.html", items=items)
        
@app.route("/update-registry/<int:item_id>", methods=["PUT", "DELETE"])
def update_registry(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == "PUT":
        # Mark the item as purchased
        item.purchased = True
        db.session.commit()
        return "", 204
    else:
        # Delete the item from the registry
        db.session.delete(item)
        db.session.commit()
        return "", 204

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()

