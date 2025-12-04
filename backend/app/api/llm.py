from flask import Blueprint, jsonify, request
from zai import ZhipuAiClient
from app.config import Config

llm_bp = Blueprint('llm', __name__, url_prefix='/api/llm')

# 初始化智谱AI客户端
client = ZhipuAiClient(api_key=Config.ZHIPU_API_KEY)

@llm_bp.route('/room_controller', methods=['POST'])
def handle_room_controller():
    """房间控制器API端点 - AI管理员：分析人物关系与剧情，引导剧情走向，指定下一轮对话角色"""
    try:
        data = request.get_json()
        print(f'AI管理员接收到数据: {data}')
        
        # 提取参数
        history_messages = data.get('history_messages', [])
        world_background = data.get('world_background', '')
        character_settings = data.get('character_settings', [])
        
        # 构建系统提示
        system_prompt = f"""
你是AI管理员，负责分析总结人物关系与剧情，引导剧情走向，同时必须指定下一轮对话的角色。

世界观：
{world_background}

所有人物设定：
{chr(10).join(character_settings)}

请分析历史对话，总结人物关系和剧情发展，然后引导剧情走向，同时必须指定下一轮对话的角色。
"""
        
        # 构建messages列表
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # 添加历史对话
        for msg in history_messages:
            messages.append({"role": "user", "content": msg})
        
        # 定义工具
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "analyze_and_guide",
                    "description": "分析人物关系与剧情，引导剧情走向，并指定下一轮对话角色（必须调用）",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "summary": {
                                "type": "string",
                                "description": "人物关系与剧情的总结"
                            },
                            "plot_guidance": {
                                "type": "string",
                                "description": "剧情引导的方向和建议"
                            },
                            "next_speaker": {
                                "type": "string",
                                "description": "下一轮对话的角色姓名"
                            }
                        },
                        "required": ["summary", "plot_guidance", "next_speaker"]
                    }
                }
            }
        ]
        
        print(f'调用大模型参数:')
        print(f'  系统提示: {system_prompt[:100]}...')
        print(f'  历史对话数: {len(history_messages)}')
        print(f'  人物设定数: {len(character_settings)}')
        
        # 调用大模型
        response = client.chat.completions.create(
            model="glm-4.6",
            messages=messages,
            thinking={"type": "enabled"},
            tools=tools,
            tool_choice="required",
            temperature=0.7
        )
        
        # 返回大模型原始JSON数据
        return response.to_json(), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        print(f'大模型调用错误: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@llm_bp.route('/character_controller', methods=['POST'])
def handle_character_controller():
    """人物控制器API端点 - AI扮演者：扮演指定角色回复，指定下一轮对话角色"""
    try:
        data = request.get_json()
        print(f'AI扮演者接收到数据: {data}')
        
        # 提取参数
        history_messages = data.get('history_messages', [])
        world_background = data.get('world_background', '')
        character_settings = data.get('character_settings', [])
        admin_analysis = data.get('admin_analysis', '')
        character_name = data.get('character_name', '')
        
        # 构建系统提示
        system_prompt = f"""
你是AI角色扮演者，负责按照指定的人物设定进行对话，并必须指定下一轮对话的角色。

世界观：
{world_background}

所有人物设定：
{chr(10).join(character_settings)}

你现在需要扮演的角色是：{character_name}

AI管理员的分析结果：
{admin_analysis}

请分析历史对话和管理员的分析结果，以指定角色的身份进行自然流畅的回复，并保持角色的性格特点和语言风格一致。同时，必须指定下一轮对话的角色。
"""
        
        # 构建messages列表
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # 添加历史对话
        for msg in history_messages:
            messages.append({"role": "user", "content": msg})
        
        # 定义工具
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "character_response_with_next",
                    "description": "角色的回复内容并指定下一轮对话角色（必须调用）",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "response_content": {
                                "type": "string",
                                "description": "角色的回复内容"
                            },
                            "next_speaker": {
                                "type": "string",
                                "description": "下一轮对话的角色姓名"
                            }
                        },
                        "required": ["response_content", "next_speaker"]
                    }
                }
            }
        ]
        
        print(f'调用大模型参数:')
        print(f'  系统提示: {system_prompt[:100]}...')
        print(f'  历史对话数: {len(history_messages)}')
        print(f'  人物设定数: {len(character_settings)}')
        print(f'  扮演角色: {character_name}')
        
        # 调用大模型
        response = client.chat.completions.create(
            model="glm-4.6",
            messages=messages,
            thinking={"type": "enabled"},
            tools=tools,
            tool_choice="required",
            temperature=0.7
        )
        
        # 返回大模型原始JSON数据
        return response.to_json(), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        print(f'大模型调用错误: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
