import datetime
from datetime import date
from flask_sqlalchemy import SQLAlchemy
# is it possible to use: from sqlalchemy.orm import declorative_base ? is db = SQLAlchemy the same thing?
from collections import OrderedDict
db = SQLAlchemy() #this is a database adapter object

class Patient(db.Model):  
    __tablename__ = "patients" 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name: str, last_name: str, date_of_birth: date, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender


    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth
        }
        
    #        def serialize(self):
    #     ordered_dict = OrderedDict([
    #         ('id', self.id),
    #         ('first_name', self.first_name),
    #         ('last_name', self.last_name),
        
    # ])
    #     return ordered_dict

class Record(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diagnosis = db.Column(db.String(300), nullable=False)
    history = db.Column(db.String(300), nullable=False)
    


class CICU(db.Model):
    __tablename__ = "cicu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128),nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name: str, last_name: str, date_of_birth: date, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    def serialize(self):
        return {

            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }



class SICU(db.Model):
    __tablename__ = "sicu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128),nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(128), nullable=False)



    def __init__(self, first_name: str, last_name: str, date_of_birth: date, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    def serialize(self):
        return {

            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender
        }


class MICU(db.Model):
    __tablename__ = "micu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128),nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    

    def __init__(self, first_name: str, last_name: str, date_of_birth: date, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    def serialize(self):
        return {

            'id': self.id,
            'name': self.name
        }


class Nurse(db.Model):
    __tablename__ = "nurses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self,name: str, password: str):
        self.name = name
        self.password = password

    def serialize(self):
        return {

            'id': self.id,
            'name': self.name
        }