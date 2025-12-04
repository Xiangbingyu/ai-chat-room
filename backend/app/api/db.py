from flask import Blueprint, jsonify, request
import uuid
from app.models import db, Room, Character, Conversation

db_bp = Blueprint('db', __name__, url_prefix='/api/db')

@db_bp.route('/rooms', methods=['GET'])
def get_all_rooms():
    """获取所有房间信息"""
    try:
        rooms = Room.query.all()
        rooms_data = []
        for room in rooms:
            rooms_data.append({
                'id': room.id,
                'name': room.name,
                'worldview': room.worldview,
                'created_at': room.created_at.isoformat()
            })
        return jsonify({
            'status': 'success',
            'data': rooms_data
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@db_bp.route('/rooms/<room_id>/characters', methods=['GET'])
def get_characters_by_room(room_id):
    """根据room_id获取所有角色信息"""
    try:
        characters = Character.query.filter_by(room_id=room_id).all()
        characters_data = []
        for character in characters:
            characters_data.append({
                'id': character.id,
                'name': character.name,
                'description': character.description,
                'room_id': character.room_id,
                'created_at': character.created_at.isoformat()
            })
        return jsonify({
            'status': 'success',
            'data': characters_data
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@db_bp.route('/rooms/<room_id>/conversations', methods=['GET'])
def get_conversations_by_room(room_id):
    """根据room_id获取所有对话内容及对应的角色信息"""
    try:
        # 查询该房间下的所有对话记录，按创建时间排序
        conversations = Conversation.query.filter_by(room_id=room_id).order_by(Conversation.created_at).all()
        
        conversations_data = []
        for conv in conversations:
            # 获取对应的角色信息
            character = Character.query.filter_by(id=conv.character_id).first()
            character_name = character.name if character else '未知角色'
            
            conversations_data.append({
                'id': conv.id,
                'room_id': conv.room_id,
                'character_id': conv.character_id,
                'character_name': character_name,
                'content': conv.content,
                'created_at': conv.created_at.isoformat()
            })
        
        return jsonify({
            'status': 'success',
            'data': conversations_data
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@db_bp.route('/rooms', methods=['POST'])
def create_room():
    """创建房间"""
    try:
        data = request.get_json()
        room_id = str(uuid.uuid4())
        new_room = Room(
            id=room_id,
            name=data.get('name'),
            worldview=data.get('worldview')
        )
        db.session.add(new_room)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'data': {
                'id': new_room.id,
                'name': new_room.name,
                'worldview': new_room.worldview,
                'created_at': new_room.created_at.isoformat()
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@db_bp.route('/characters', methods=['POST'])
def create_character():
    """创建角色"""
    try:
        data = request.get_json()
        character_id = str(uuid.uuid4())
        new_character = Character(
            id=character_id,
            name=data.get('name'),
            description=data.get('description'),
            room_id=data.get('room_id')
        )
        db.session.add(new_character)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'data': {
                'id': new_character.id,
                'name': new_character.name,
                'description': new_character.description,
                'room_id': new_character.room_id,
                'created_at': new_character.created_at.isoformat()
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
