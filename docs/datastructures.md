# Data structures and naming conventions

## Sensor

| Name (str) | Block (str) | Type (str) | Status code (int) |
|------------|-------------|------------|-------------------|
| "t000"     | "A00"       | t          | 0                 |
| "t001"     | "A01"       | t          | 0                 |

#### Naming convention:

- Name: `Type and a 3-digit running number`
    - This is the primary key
- Block: `Letter of the building and a 2-digit number of the zone`

#### Status codes:

| Code | Description   |
|------|---------------|
| 0    | OK            |
| 1    | GENERAL ERROR |

- This enables us to add more status codes in the future.

#### Type codes:

| Code | Description |
|------|-------------|
| t    | Temperature |

- This enables us to add more sensor types in the future.

---

## Measurements

| Name (str) | Value (float) | Type (str) | Timestamp (unix timestamp) |
|------------|---------------|------------|----------------------------|
| "t000"     | 21.5          | t          | 1681976464                 |
| "t001"     | 21.6          | t          | 1681976464                 |

- Measurements are sent to the api by the sensors

---

### Error

| Name (str) | Status code (int) | Timestamp (unix timestamp) |
|------------|-------------------|----------------------------|
| "t000"     | 1                 | 1681976464                 |
| "t001"     | 1                 | 1681976464                 |
| "t000"     | 0                 | 1681976474                 |
| "t001"     | 0                 | 1681976474                 |

- Error events are saved as a separate table
- When an error occurs the sensor sends an error message with the code and timestamp to the api
- We also save the status code change back to 0
    - This won't come from the sensor itself, but from the admin panel
    - If in the future the sensors are able to fix themselves, this should work as well

---

