from flask import Blueprint, jsonify, abort, request
from ..models import Patient, Record, Nurse, db
import hashlib
import secrets

def scramble(password: str):
    '''Hash and salt the given password'''
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('nurses', __name__, url_prefix='/nurses')


@bp.route('', methods=['GET'])
def index():
    nurses = Nurse.query.all()
    results = []
    for n in nurses:
        results.append(n.serialize())
    return jsonify(results)


@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'username' in request.json:
        if len(request.json['name']) < 3:
            return abort(400)
        n.name=request.json['name']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        n.password=scramble(request.json['password'])

    n = Nurse(
        name=request.json['name'],
        password=scramble(request.json['password'])
    )
    db.session.add(n)
    db.session.commit()
    return jsonify(n.serialize())
       

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    n = Nurse.query.get_or_404(id, "Nurse not on duty")
    return jsonify(n.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    n = Nurse.query.get_or_404(id)

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        n.username=request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        n.password=request.json['password']

    try:
        db.session.commit()
        return jsonify(n.serialize())
    except:
        return jsonify(False)