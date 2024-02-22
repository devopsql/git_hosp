from flask import Blueprint, jsonify, abort, request
from ..models import Patient, Record, Nurse, db
import hashlib
import secrets


# def scramble(password: str):
#     """ Hash and salt the given password"""
#     salt = secrets.token_hex(16)
#     return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('',methods=['GET'])
def index():
    patients = Patient.query.all()
    result = []
    for p in patients:
        result.append(p.serialize())
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'first_name' not in request.json or 'last_name' not in request.json or 'date_of_birth'not in request.json:
        return abort(400)
    # user  with id of user_id must exist
    
    # construct user
    p = Patient(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        date_of_birth=request.json['date_of_birth'],
        gender=request.json['gender']
    )
    db.session.add(p) # prepare CREATE statement
    db.session.commit() #  execute CREATE statement
    return jsonify(p.serialize())


 
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Patient.query.get_or_404(id, 'Patient not found')
    return jsonify(p.serialize())



@bp.route('/<int:id>', methods=['PUT','PATCH'])
def update(id:int):
    p = Patient.query.get_or_404(id)

    if 'first_name' not in request.json or 'last_name' not in request.json or 'date_of_birth' not in request.json:
        return abort(400)
    
    if 'first_name' in request.json:
        if len(request.json['first_name']) < 3:
            return abort(400)
        p.first_name=request.json['first_name']

    if 'last_name' in request.json:
        if len(request.json['last_name']) < 3:
            return abort(400)
        p.last_name=request.json['last_name']

    if 'date_of_birth' in request.json:
        p.date_of_birth=request.json['date_of_birth']

    if 'gender' in request.json:
        p.gender=request.json['gender']

    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)



@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    p = Patient.query.get_or_404(id, 'Patient not found')

    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)