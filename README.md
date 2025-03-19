# Gabay Gov API

## Database Setup

### Creation of Database using PostgreSQL

```sql
Psql -U postgres
CREATE DATABASE gabay_gov;
```

## Installation

Before running the application, install the required dependencies:

```sh
pip install -r requirements.txt
```

### After Creating PostgreSQL Database

Run the following script to initialize the database:

```sh
python init_db.py
```

This will create tables in the database and input data.

```sh
python app.py
```

This will start the backend server and make the API accessible for use.

## Project Structure

### `app.py`

This is the central backend file where all components connect.

### `init_db.py`

Handles database initialization and setup.

### `dao/`

Contains Data Access Object (DAO) files responsible for database interactions.

- `email_dao.py` - Manages email-related database operations.
- `event_dao.py` - Handles event-related database operations.
- `user_dao.py` - Manages user-related database operations.

### `endpoints/`

Contains API endpoint handlers.

- `assets.py` - Responsible for handling uploaded images.
- `emails.py` - Manages emails for subscriptions.
- `events.py` - Handles event management.
- `users.py` - Responsible for managing user accounts.

### `utils/`

Contains utility files for additional functionality.

- `gmail.py` - Handles Gmail integration.
