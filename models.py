##########################################
#             IMPORTATIONS               #
##########################################
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

##########################################
#            Database Connection        #
#            AND APP START              #
##########################################

#Variables d'environnement
username=os.getenv('username')
password=os.getenv('password')
host=os.getenv('host')

database_path = f'postgresql://{username}:{password}@{host}:5432/tp_api_iai'

app = Flask(__name__) #START A FLASK APP
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:90011784IB@localhost:5432/tp_api_iai' #To connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To avoid warnings


db=SQLAlchemy(app) #intance of the database


##########################################
#            CREATION OF THE MODELS      #
##########################################

##########################################
#            CLASS CATEGORIE             #
##########################################
class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(), nullable=False)
    livres = db.relationship('Livre', backref='categorie', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie=libelle_categorie

    ##########################################
    #            USUAL FONCTIONS             #
    ##########################################
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    ##########################################
    #            DATA FORMATTING             #
    ##########################################
    def format(self):
        return{
            'id': self.id,
            'libelle_categorie': self.libelle_categorie
        }
##########################################
#            CLASS LIVRE                 #
##########################################
class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(), nullable=False, unique=True)
    titre = db.Column(db.String(), nullable=False)
    date_publication = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String (30), nullable = False)
    editeur = db.Column(db.String(30), nullable = False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id

    ##########################################
    #            USUAL FONCTIONS             #
    ##########################################
    def insert(self):
        db.session.add(self)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    ##########################################
    #            DATA FORMATTING             #
    ##########################################
    def format(self):
        return{
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur' : self.auteur,
            'editeur' : self.editeur,
            'categorie_id' : self.categorie_id
        }
db.create_all()