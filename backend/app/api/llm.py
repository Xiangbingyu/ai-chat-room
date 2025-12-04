from flask import Blueprint, jsonify, request

llm_bp = Blueprint('llm', __name__, url_prefix='/api/llm')

@llm_bp.route('/room_controller', methods=['POST'])
def handle_room_controller():
    """房间控制器API端点"""
    try:
        data = request.get_json()
        print(f'房间控制器接收到数据: {data}')
        
        history_messages = data.get('history_messages', [])
        world_background = data.get('world_background', '')
        character_settings = data.get('character_settings', [])
        
        # 确保character_settings中的每个角色都包含姓名和背景信息
        processed_characters = []
        for character in character_settings:
            char_name = character.get('name', '未知角色')
            char_background = character.get('background', '')
            processed_characters.append({
                'name': char_name,
                'background': char_background
            })
        
        print(f'提取的历史对话记录: {history_messages}')
        print(f'提取的世界观背景: {world_background}')
        print(f'提取的角色设定信息: {processed_characters}')
        
        response = {
            'status': 'success',
            'message': '房间控制器处理成功',
            'data': {
                'original_data': data,
                'extracted_info': {
                    'history_messages': history_messages,
                    'world_background': world_background,
                    'character_settings': processed_characters
                }
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@llm_bp.route('/character_controller', methods=['POST'])
def handle_character_controller():
    """人物控制器API端点"""
    try:
        data = request.get_json()
        print(f'人物控制器接收到数据: {data}')
        
        history_messages = data.get('history_messages', [])
        world_background = data.get('world_background', '')
        character_settings = data.get('character_settings', [])
        character_name = data.get('character_name', '')
        
        # 确保character_settings中的每个角色都包含姓名和背景信息
        processed_characters = []
        for character in character_settings:
            char_name = character.get('name', '未知角色')
            char_background = character.get('background', '')
            processed_characters.append({
                'name': char_name,
                'background': char_background
            })
        
        print(f'提取的历史对话记录: {history_messages}')
        print(f'提取的世界观背景: {world_background}')
        print(f'提取的角色设定信息: {processed_characters}')
        print(f'提取的扮演角色名字: {character_name}')
        
        response = {
            'status': 'success',
            'message': '人物控制器处理成功',
            'data': {
                'original_data': data,
                'extracted_info': {
                    'history_messages': history_messages,
                    'world_background': world_background,
                    'character_settings': processed_characters,
                    'character_name': character_name
                }
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
