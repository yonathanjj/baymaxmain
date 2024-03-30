import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, jsonify, session, url_for
from sqlalchemy import join
from user_model import Users
from flask_sqlalchemy import SQLAlchemy
from flask import request


def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jj1995123@localhost:3306/baymax_db'
    app.config['SQLALCHEMY_ECHO'] = True
    return app


app = create_app()
db = SQLAlchemy(app)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Database tables created!")


@app.route('/')
def index():
    static_url = url_for('static', filename='templates/website.css')
    print(f"Generated static URL for website.css: {static_url}")
    return render_template("website.html")


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    users = Users(email=email, password=password)
    db.session.add(users)
    db.session.commit()

    return 'Registration successful!'


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    users = Users.query.filter_by(email=email).first()
    if users and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"error": "Invalid email or password"}), 401


@app.route("/submit_symptoms", methods=["POST"])
def submit_symptoms():
    if 'users_id' not in session:
        return jsonify({"error": "Unauthorized access"}), 401

    symptoms = request.form["symptoms"]
    selected_symptoms = request.form.getlist("symptoms")
    illnesses_data = analyze_symptoms(selected_symptoms)

    if isinstance(illnesses_data, str):
        return jsonify({"error": illnesses_data}), 500
    else:
        return illnesses_analysis


analyze_symptoms = {
    "Malaria": {
        "symptoms": ["headache", "fever", "chills", "sweating"],
        "description": "A mosquito-borne infectious disease.",
        "related_illnesses": ["Dengue fever", "Typhoid fever"]
    },
    "Common cold": {
        "symptoms": ["cough", "sore throat", "runny nose", "congestion"],
        "description": "A viral infection of the upper respiratory tract.",
        "related_illnesses": ["Influenza (flu)", "Sinusitis"]
    },
    "Stroke": {
        "symptoms": ["sudden numbness", "confusion", "trouble speaking", "trouble walking"],
        "description": "A sudden interruption of blood supply to part of the brain.",
        "related_illnesses": ["Transient ischemic attack (TIA)"]
    },
    "Eczema": {
        "symptoms": ["itching", "rash", "dry skin"],
        "description": "A chronic inflammatory skin condition.",
        "related_illnesses": ["Psoriasis", "Hives"]
    },
    "Heart Disease": {
        "symptoms": ["chest pain", "shortness of breath", "fatigue"],
        "description": "A group of conditions affecting the heart and blood vessels.",
        "related_illnesses": ["Angina", "Heart failure"]
    }
}


def analyze_symptoms(symptoms):
    session = db.session

    illnesses = (
        session.query(Illnesses)
        .join(Symptoms, symptoms_illnesses)
        .filter(Symptoms.name.in_(symptoms))
        .all()
    )

    illnesses_data = []
    for illnesses in illnesses:
        illnesses_data.append({
            "name": illnesses.name,
        })
    return jsonify(illnesses=illnesses_data)


@app.route('/some_route')
def some_route():
    users = Users.query.all()
    return "Some route"


if __name__ == '__main__':
    app.run(debug=True)
