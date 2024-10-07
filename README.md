# Map tienda-py
```sh
app/
├── main.py            
├── database.py       
├── models/
│   ├── __init__.py   
│   ├── category.py    
│   └── ...            
├── schemas/
│   ├── __init__.py    
│   ├── category.py    
│   └── ...       
├── template/
│    └── ...  
│   
docker/
├── api/   
│   └── Dockerfile     
├── mysql/
│   ├── conf.d/
│   │   └── ...
│   ├── initdb.d/
│   │   ├──  schemas.sql
│   │   └──  testdata.sql
│   └── Dockerfile
...
```

## Run docker-compose:

```sh
docker-compose up --build -d
```

# API runs in:

[localhost:8000](http://localhost:8000/)

# DB UI runs in:
[localhost:8080](http://localhost:8080/index.php)


# API docs

Just go to: [localhost:8000/docs](http://localhost:8000/docs)

# ¿How create the tables?

When the API container is created, the tables are also created.

# ¿How use example data?

For now, copy and paste the SQL queries from docker/mysql/initdb.d/testdata.sql and run them in the MySQL UI.
