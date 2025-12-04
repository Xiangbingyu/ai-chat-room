# API 接口文档

本文档描述了 `db.py` 中定义的所有 API 接口的使用方法和示例。

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

## 3. 创建房间

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

## 4. 创建角色

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

## 错误响应格式

### 响应示例
```json
{
  "status": "error",
  "message": "错误信息描述"
}
```
