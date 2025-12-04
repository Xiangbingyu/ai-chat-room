# API 接口文档

本文档描述了 `db.py` 和 `llm.py` 中定义的所有 API 接口的使用方法和示例。

## 1. 获取所有房间信息

### 请求方式
GET

### URL
`/api/db/rooms`

### 请求示例
```bash
curl -X GET http://localhost:5000/api/db/rooms
```

### 响应示例
```json
{
  "status": "success",
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "测试房间",
      "worldview": "这是一个测试房间的世界观描述",
      "created_at": "2023-01-01T12:00:00"
    },
    {
      "id": "660e8400-e29b-41d4-a716-446655440000",
      "name": "第二个房间",
      "worldview": "第二个房间的世界观",
      "created_at": "2023-01-02T13:00:00"
    }
  ]
}
```

## 2. 根据房间ID获取角色信息

### 请求方式
GET

### URL
`/api/db/rooms/<room_id>/characters`

### 请求示例
```bash
curl -X GET http://localhost:5000/api/db/rooms/550e8400-e29b-41d4-a716-446655440000/characters
```

### 响应示例
```json
{
  "status": "success",
  "data": [
    {
      "id": "770e8400-e29b-41d4-a716-446655440000",
      "name": "角色A",
      "description": "这是角色A的描述",
      "room_id": "550e8400-e29b-41d4-a716-446655440000",
      "created_at": "2023-01-01T12:30:00"
    },
    {
      "id": "880e8400-e29b-41d4-a716-446655440000",
      "name": "角色B",
      "description": "这是角色B的描述",
      "room_id": "550e8400-e29b-41d4-a716-446655440000",
      "created_at": "2023-01-01T12:35:00"
    }
  ]
}
```

## 3. 根据房间ID获取对话内容

### 请求方式
GET

### URL
`/api/db/rooms/<room_id>/conversations`

### 请求示例
```bash
curl -X GET http://localhost:5000/api/db/rooms/550e8400-e29b-41d4-a716-446655440000/conversations
```

### 响应示例
```json
{
  "status": "success",
  "data": [
    {
      "id": "1110e840-e29b-41d4-a716-446655440000",
      "room_id": "550e8400-e29b-41d4-a716-446655440000",
      "character_id": "770e8400-e29b-41d4-a716-446655440000",
      "character_name": "角色A",
      "content": "你好，很高兴认识你！",
      "created_at": "2023-01-01T13:00:00"
    },
    {
      "id": "2220e840-e29b-41d4-a716-446655440000",
      "room_id": "550e8400-e29b-41d4-a716-446655440000",
      "character_id": "880e8400-e29b-41d4-a716-446655440000",
      "character_name": "角色B",
      "content": "你好，我也很高兴认识你！",
      "created_at": "2023-01-01T13:05:00"
    }
  ]
}
```

## 4. 创建房间

### 请求方式
POST

### URL
`/api/db/rooms`

### 请求示例
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"新房间","worldview":"这是一个新创建的房间的世界观"}' http://localhost:5000/api/db/rooms
```

### 响应示例
```json
{
  "status": "success",
  "data": {
    "id": "990e8400-e29b-41d4-a716-446655440000",
    "name": "新房间",
    "worldview": "这是一个新创建的房间的世界观",
    "created_at": "2023-01-03T10:00:00"
  }
}
```

## 5. 创建角色

### 请求方式
POST

### URL
`/api/db/characters`

### 请求示例
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"新角色","description":"这是一个新创建的角色的描述","room_id":"990e8400-e29b-41d4-a716-446655440000"}' http://localhost:5000/api/db/characters
```

### 响应示例
```json
{
  "status": "success",
  "data": {
    "id": "aaa0e840-e29b-41d4-a716-446655440000",
    "name": "新角色",
    "description": "这是一个新创建的角色的描述",
    "room_id": "990e8400-e29b-41d4-a716-446655440000",
    "created_at": "2023-01-03T10:05:00"
  }
}
```

## 6. 房间控制器API

### 请求方式
POST

### URL
`/api/llm/room_controller`

### 请求示例
```bash
curl -X POST -H "Content-Type: application/json" -d '{"history_messages":["角色A: 你好","角色B: 你好"],"world_background":"这是一个测试房间的世界观","character_settings":["角色A: 一个友好的人","角色B: 一个开朗的人"]}' http://localhost:5000/api/llm/room_controller
```

### 响应示例
（返回大模型原始JSON响应）

## 7. 人物控制器API

### 请求方式
POST

### URL
`/api/llm/character_controller`

### 请求示例
```bash
curl -X POST -H "Content-Type: application/json" -d '{"history_messages":["角色A: 你好"],"world_background":"这是一个测试房间的世界观","character_settings":["角色A: 一个友好的人","角色B: 一个开朗的人"],"admin_analysis":"两人初次见面，氛围友好","character_name":"角色B"}' http://localhost:5000/api/llm/character_controller
```

### 响应示例
（返回大模型原始JSON响应）
