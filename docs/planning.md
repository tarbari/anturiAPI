# Planning

## Specsing

- Receive temperature data from sensors (.1f, Celsius)
    - Futureproof for other data
    - Save in database
- Receive error from sensor
    - No specific error code needed
- Send 'zero error' to sensor?
    - Is this actually required in the spec? Maybe ask?
- Add sensor
- Modify sensor status?
    - What does this mean?
    - Maybe it's 'OK' or 'ERROR'
- Change the block of a sensor
- Delete data point
- List all sensors
    - Lists at least ID, block, status
- List sensors in a specific block
    - ID, status, latest measurement along with timestamp
- Show one specific sensor
    - ID, block, status, measurements with timestamps
    - By default 10 latest measurements
    - Filter by a range of time
- Show sensors all status changes with timestamps
- Search sensors by status
    - ID, block, status
- Show graph with errors and their times
    - This should not need anything special from the api?
- POST is used for adding new data
- PUT is used for updating data
- DELETE is used for deleting data
- GET is used for getting data

---

## Resources

### Sensor

| ID (str) | Block (str) | Type (str) | Status code (int) |
|----------|-------------|------------|-------------------|
| "t000"   | "A00"       | t          | 0                 |
| "t001"   | "A01"       | t          | 0                 |

Naming convention:

- ID
    - Block, underscore and a 3-digit running number
    - This is a bad idea. We need to be able to change the block of a sensor and the id should be considered static
- Block
    - Letter of the building and a 2-digit number of the zone

Status codes:

| Code | Description   |
|------|---------------|
| 0    | OK            |
| 1    | GENERAL ERROR |

This enables us to add more status codes in the future.

Type codes:

| Code | Description |
|------|-------------|
| t    | Temperature |

This could come in handy if we ever decide to add other types of sensors.

### Block

- Do we need this?

### Measurement

| ID (str) | Value (float) | Type (int) | Timestamp (unix timestamp) |
|----------|---------------|------------|----------------------------|
| "t000"   | 21.5          | t          | 1681976464                 |
| "t001"   | 21.6          | t          | 1681976464                 |

### Error

| ID (str) | Status code (int) | Timestamp (unix timestamp) |
|----------|-------------------|----------------------------|
| "t000"   | 1                 | 1681976464                 |
| "t001"   | 1                 | 1681976464                 |
| "t000"   | 0                 | 1681976474                 |
| "t001"   | 0                 | 1681976474                 |

- Error events are saved as a separate table
- When an error occurs the sensor sends an error message with the code and timestamp to the api
- Lets also save when the sensor is back to normal
    - This won't come from the sensor itself, but from the admin panel
    - But if in the future the sensors are able to fix themselves, this should work as well

---

## Messages from sensors

### Measurement

```json
{
  "id": "t000",
  "value": 21.5,
  "type": "t",
  "timestamp": 1681976464
}
```

### Error

```json
{
  "id": "t000",
  "status_code": 1,
  "timestamp": 1681976464
}
```

---

## Endpoints

### GET /sensors

- List all sensors

```json
[
  {
    "id": "t000",
    "block": "A13",
    "status_code": 0
  },
  {
    "id": "t001",
    "block": "A13",
    "status_code": 1
  }
]
```

---

### POST /sensors

- Add sensor

```json
{
  "id": "t000",
  "block": "A13",
  "type": "t",
  "status_code": 0
}
```

---

### PUT /sensors/{id}

- Change sensor status
- This should also save an error event by calling the PUT /errors endpoint

```json
{
  "status_code": 1
}
```

---

### PUT /sensors/{id}/block

- Change sensor block

```json
{
  "block": "A14"
}
```

---

### GET /sensors/{id}

- Show one specific sensor
- By default 10 latest measurements
- Two query parameters:
    - `start` (unix timestamp)
    - `end` (unix timestamp)

```json
{
  "id": "t000",
  "block": "A13",
  "status_code": 0,
  "measurements": [
    {
      "id": "t000",
      "value": 21.5,
      "type": "t",
      "timestamp": 1681976464
    },
    {
      "id": "t000",
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

```json
[
  {
    "id": "t000",
    "block": "A13",
    "status_code": 0
  },
  {
    "id": "t001",
    "block": "A13",
    "status_code": 0
  }
]
```

---

### GET /errors

- TODO: This needs to be thought through
- Show graph with errors and their times

```json
[
  {
    "timestamp": 1681976464,
    "status_code": 1
  },
  {
    "timestamp": 1681976474,
    "status_code": 0
  }
]
```

---

### POST /errors

- Add error

```json
{
  "id": "t000",
  "status_code": 1,
  "timestamp": 1681976464
}
```

---

### GET /errors/{id}

- Show sensors all status changes with timestamps

```json
[
  {
    "id": "t000",
    "status_code": 1,
    "timestamp": 1681976464
  },
  {
    "id": "t000",
    "status_code": 0,
    "timestamp": 1681976474
  }
]
```

---

### GET /block/{block}

- List sensors in a specific block

```json
[
  {
    "id": "t000",
    "status_code": 0,
    "latest_measurement": {
      "value": 21.5,
      "type": "t",
      "timestamp": 1681976464
    }
  },
  {
    "id": "t001",
    "status_code": 0,
    "latest_measurement": {
      "value": 21.6,
      "type": "t",
      "timestamp": 1681976474
    }
  }
]
```

---

### POST /measurement

- Sensor sends measurement

```json
{
  "id": "t000",
  "value": 21.5,
  "type": "t",
  "timestamp": 1681976464
}
```

---

### DELETE /measurement

- Delete measurement

```json
{
  "id": "t000",
  "timestamp": 1681976464
}
```