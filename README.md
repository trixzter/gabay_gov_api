# Gabay Gov API

## Database Setup

### Creation of Database using PostgreSQL

```sql
Psql -U postgres
CREATE DATABASE gabay_gov;
```

### After Creating PostgreSQL Database

Run the following script to initialize the database:

```sh
python init_db.py
```

This will create tables in the database and input data.

## Installation

Before running the application, install the required dependencies:

```sh
pip install -r requirements.txt
```

## Project Structure

### `app.py`

This is the central backend file where all components connect.

### `assets.py`

Responsible for handling uploaded images.

### `emails.py`

Manages emails for subscriptions.

### `events.py`

Handles event management.

### `users.py`

Responsible for managing user accounts.
