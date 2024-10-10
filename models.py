from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

# License Model
class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(120), unique=True, nullable=False)  # Correct, unique and required
    product_id = db.Column(db.String(100), nullable=False)  # Product ID required
    user = db.Column(db.String(100), nullable=False)  # User required
    active = db.Column(db.Boolean, default=True)  # Default active status is True
    expiration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Required expiration date

    def __repr__(self):
        return f"License('{self.license_key}', '{self.active}', '{self.expiration_date}')"

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)  # Username should be unique
    password = db.Column(db.String(60), nullable=False)  # Password field should be hashed

    def set_password(self, password):  # Use bcrypt to hash the password
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):  # Check the password using bcrypt
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.username}')"
