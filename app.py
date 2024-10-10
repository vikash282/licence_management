from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from models import db, License, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route (License Validation)
@app.route('/validate-license', methods=['POST'])
def validate_license():
    data = request.get_json()
    license_key = data.get('licenseKey')

    license = License.query.filter_by(license_key=license_key).first()

    if license and license.active:
        if license.expiration_date > datetime.utcnow():
            return jsonify({'valid': True}), 200  # Returns valid if license is active and not expired
        else:
            return jsonify({'valid': False, 'message': 'License expired'}), 400  # License expired message
    return jsonify({'valid': False, 'message': 'Invalid license key'}), 400  # Invalid license key message

# Admin Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard after successful login
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')  # Handle login failure
    return render_template('login.html')

# Admin Dashboard (View and Revoke Licenses)
@app.route('/admin', methods=['GET'])
@login_required
def admin_dashboard():
    licenses = License.query.all()  # Fetch all licenses for admin
    return render_template('admin_dashboard.html', licenses=licenses)

# Revoke License
@app.route('/revoke-license/<int:license_id>', methods=['POST'])
@login_required
def revoke_license(license_id):
    license = License.query.get_or_404(license_id)  # Fetch the license by ID or return 404 if not found
    license.active = False  # Deactivate the license
    db.session.commit()  # Commit the changes
    flash('License revoked successfully!', 'success')  # Flash success message
    return redirect(url_for('admin_dashboard'))

# Add New License (Admin Functionality)
@app.route('/add-license', methods=['POST'])
@login_required
def add_license():
    license_key = request.form.get('license_key')
    product_id = request.form.get('product_id')
    user = request.form.get('user')
    expiration_date = request.form.get('expiration_date')

    new_license = License(
        license_key=license_key,
        product_id=product_id,
        user=user,
        expiration_date=datetime.strptime(expiration_date, '%Y-%m-%d')  # Convert expiration date from string to datetime
    )
    db.session.add(new_license)  # Add new license to the database
    db.session.commit()  # Commit the transaction

    flash('New license added successfully!', 'success')  # Flash success message
    return redirect(url_for('admin_dashboard'))

# Admin Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))  # Redirect to login page after logout

if __name__ == '__main__':
    app.run(debug=True)
