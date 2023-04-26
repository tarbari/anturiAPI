# Endpoints

## Sensors

### GET /sensors

- List all sensors

`Return:`

```json
[
  {
    "name": "t000",
    "block": "A13",
    "type": "t",
    "status_code": 0
  },
  {
    "name": "t001",
    "block": "A13",
    "type": "t",
    "status_code": 1
  }
]
```

---

### POST /sensors

- Add sensor

`Query parameters and return:`

```json
{
  "name": "t000",
  "block": "A13",
  "type": "t",
  "status_code": 0
}
```

---

### PUT /sensors/{name}/status_code

- Change sensor status
- This also creates an error event

`Query parameters:`

```json
{
  "status_code": 1
}
```

`Return:`
`HTTP 204 No Content`

- We do not return the updated sensor to minimize the amount of traffic

---

### PUT /sensors/{name}/block

- Change sensor block

`Query parameters:`

```json
{
  "block": "A14"
}
```

`Return:`
`HTTP 204 No Content`

- We do not return the updated sensor to minimize the amount of traffic

---

### GET /sensors/{name}

- Show one specific sensor
- By default 10 latest measurements
- Two optional query parameters for start and end timestamps
    - `start_time` (unix timestamp)
    - `end_time` (unix timestamp)

`Return:`

```json
{
  "name": "t000",
  "block": "A13",
  "type": "t",
  "status_code": 0,
  "measurements": [
    {
      "name": "t000",
      "value": 21.5,
      "type": "t",
      "timestamp": 1681976464
    },
    {
      "name": "t000",
      "value": 21.6,
      "type": "t",
      "timestamp": 1681976474
    }
  ]
}
```

---

### GET /sensors/{status_code}

- Search sensors by status

`Return:`

```json
[
  {
    "name": "t000",
    "block": "A13",
    "type": "t",
    "status_code": 0
  },
  {
    "name": "t001",
    "block": "A14",
    "type": "t",
    "status_code": 0
  }
]
```

---

### GET /sensors/block/{block}

- List sensors in a specific block
- Measurements include the latest measurement

`Return:`

```json
[
  {
    "name": "t000",
    "block": "A13",
    "type": "t",
    "status_code": 0,
    "measurements": {
      "name": "t000",
      "value": 21.5,
      "type": "t",
      "timestamp": 1681976464
    }
  },
  {
    "name": "t001",
    "block": "A13",
    "type": "t",
    "status_code": 0,
    "measurements": {
      "name": "t000",
      "value": 21.6,
      "type": "t",
      "timestamp": 1681976474
    }
  }
]
```

---

## Errors

### GET /errors

- Get all errors from all sensors

```json
[
  {
    "name": "t000",
    "timestamp": 1681976464,
    "status_code": 1
  },
  {
    "name": "t001",
    "timestamp": 1681976474,
    "status_code": 0
  }
]
```

---

### GET /errors/{name}

- Show sensors all status changes with timestamps

`Return:`

```json
[
  {
    "name": "t000",
    "status_code": 1,
    "timestamp": 1681976464
  },
  {
    "name": "t000",
    "status_code": 0,
    "timestamp": 1681976474
  }
]
```

---

## Measurement

### POST /measurement

- Sensor sends measurement

`Query parameters:`

```json
{
  "name": "t000",
  "value": 21.5,
  "type": "t",
  "timestamp": 1681976464
}
```

`Return:`
`HTTP 201 Created`

---

### DELETE /measurement

- Delete measurement

`Query parameters:`

```json
{
  "name": "t000",
  "timestamp": 1681976464
}
```

`Return:`
`HTTP 204 No Content`