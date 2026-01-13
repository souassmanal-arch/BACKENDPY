from flask import Blueprint, request, jsonify
from models import db
from models.room import Room

bp = Blueprint('rooms', __name__, url_prefix='/api/rooms')

@bp.route('/', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.to_dict() for room in rooms])

@bp.route('/', methods=['POST'])
def create_room():
    data = request.get_json()
    # Validator could go here
    new_room = Room(
        name=data['name'],
        capacity=data['capacity'],
        type=data['type'],
        equipment=data.get('equipment', '')
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify(new_room.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_room(id):
    room = Room.query.get_or_404(id)
    data = request.get_json()
    
    room.name = data.get('name', room.name)
    room.capacity = data.get('capacity', room.capacity)
    room.type = data.get('type', room.type)
    room.equipment = data.get('equipment', room.equipment)
    
    db.session.commit()
    return jsonify(room.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
def delete_room(id):
    room = Room.query.get_or_404(id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted'})
