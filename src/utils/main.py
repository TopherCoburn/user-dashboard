import os
from flask import Flask, render_template, request, redirect, url_for
from user_dashboard.models import User, Dashboard

app = Flask(__name__)
app.config.from_object('user_dashboard.config.Config')

# Create database tables if they don't exist
with app.app_context():
    User.init_db()
    Dashboard.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for('dashboard', username=username))
    return render_template('login.html')

@app.route('/dashboard/<string:username>')
def dashboard(username):
    user = User.query.filter_by(username=username).first()
    if user:
        dashboard_data = Dashboard.query.filter_by(user_id=user.id).first()
        return render_template('dashboard.html', username=username, dashboard_data=dashboard_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    if os.environ.get('DATABASE_URL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.run(debug=True)