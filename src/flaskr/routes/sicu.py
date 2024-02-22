from flask import Blueprint, abort, jsonify,request 
from ..models import SICU, db


bp = Blueprint('sicu', __name__, url_prefix='/sicu')

@bp.route('', methods=['GET'])
def index():
    sicu = SICU.query.all()
    result = []
    for s in sicu:
        result.append(s.serialize())
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    if 'first_name' not in request.json or 'last_name' not in request.json or 'date_of_birth' not in request.json:
        return abort(400)
    

    s = SICU(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        date_of_birth=request.json['date_of_birth'],
        gender=request.json['gender']
    )
    db.session.add(s)
    db.session.commit()
    return jsonify(s.serialize())


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    s = SICU.query.get_or_404(id, 'Patient not found')
    return jsonify(s.serialize())


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id:int):
    s = SICU.query.get_or_404(id)

    if 'first_name' not in request.json or 'last_name' not in request.json or 'date_of_birth' not in request.json:
        return abort(400)
    
    if 'first_name' in request.json:
        if len(request.json['first_name']) < 3:
            return abort(400)
        s.first_name=request.json['first_name']

    if 'last_name' in request.json:
        if len(request.json['last_name']) < 3:
            return abort(400)
        s.last_name=request.json['last_name']

    if 'date_of_birth' in request.json:
        s.date_of_birth=request.json['date_of_birth']

    if 'gender' in request.json:
        s.gender=request.json['gender']

    try:
        db.session.commit()
        return jsonify(s.serialize())
    except:
        return jsonify(False)
    

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    s = SICU.query.get_or_404(id, 'Patient not found')

    try:
        db.session.delete(s)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)