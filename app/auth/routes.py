from flask import Blueprint, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
    return "Auth module fonctionne 👑"

@auth.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return "Email et mot de passe requis"

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return "Cet email existe déjà"

    hashed_password = generate_password_hash(password)

    user = User(email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return "Utilisateur créé avec succès 👑"


@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return "Utilisateur introuvable"

    if not check_password_hash(user.password, password):
        return "Mot de passe incorrect"

    # 🔥 Création de session
    session["user_id"] = user.id

    return "Connexion réussie 👑"
