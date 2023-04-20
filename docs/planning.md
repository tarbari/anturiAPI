# Planning

## Rest API

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

---

## Resources

### Sensor

| ID (str)  | Block (str) | Type (int) | Status code (int) |
|-----------|-------------|------------|-------------------|
| "A00_000" | "A00"       | 0          | 0                 |
| "A01_001" | "A01"       | 0          | 0                 |

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
| 0    | Temperature |

This could come in handy if we ever decide to add other types of sensors.

### Block

- Do we need this?

### Measurement

| ID (str)  | Value (float) | Type (int) | Timestamp (unix timestamp) |
|-----------|---------------|------------|----------------------------|
| "A13_000" | 21.5          | 0          | 1681976464                 |
| "A13_001" | 21.6          | 0          | 1681976464                 |

### Error

| ID (str)  | Status code (int) | Timestamp (unix timestamp) |
|-----------|-------------------|----------------------------|
| "A13_000" | 1                 | 1681976464                 |
| "A13_001" | 1                 | 1681976464                 |
| "A13_000" | 0                 | 1681976474                 |
| "A13_001" | 0                 | 1681976474                 |

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
  "id": "A13_000",
  "value": 21.5,
  "type": 0,
  "timestamp": 1681976464
}
```

### Error

```json
{
  "id": "A13_000",
  "status_code": 1,
  "timestamp": 1681976464
}
```

---

