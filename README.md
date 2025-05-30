# api4friends
Backend Flask service for Food 4 Friends

## Local Setup

### Install dependencies in virtual env:

```
py -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### Starting the service:

```
py api.py
```

Default server http://127.0.0.1:5000
```
* Running on http://127.0.0.1:5000
```

## Setting Up Local DB

### If running db locally, install PostgreSQL:
http://postgresql.org/download/

### Create DB
1) Open pgAdmin 4
2) Create new database with name 'db_4_friends'

### Updating DB (also do this for new models)
3) In the terminal run
```
py create_db.py
```

### Add seed data
```
python seed_data.py
```

### Starting Postgres Server on Windows
Find the PostgreSQL database directory.
```
pg_ctl -D "C:\Program Files\PostgreSQL\17\data" start
```

### Stopping Postgres Server on Windows
```
pg_ctl -D "C:\Program Files\PostgreSQL\17\data" stop
```

### Remember to always start virtual env:

```
source .venv/Scripts/activate
```

## Testing API
Can test with curl
```
curl http://localhost:5000/api/users/
curl http://localhost:5000/api/users/1

curl http://localhost:5000/api/recipes/
curl http://localhost:5000/api/recipes/1
```

## Debugging

<details>
    <summary> ModuleNotFoundError: No module named 'flask'</summary>
    You may need to run the venv
</details>

<details>
    <summary> ModuleNotFoundError: No module named 'psycopg2'</summary>
    Run pip install psycopg2
</details>

<details>
    <summary> pg_ctl command is not found or recognized</summary>
    Setup up Postgres bin directory's path in environment variables. For Example:
    'C:\Program Files\PostgreSQL\17\bin'
</details>