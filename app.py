from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        form_data = FormData(name=name, email=email, phone=phone, message=message)

        try:
            db.session.add(form_data)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'Error submitting form data'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
