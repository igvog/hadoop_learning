# Glovo Live Coding

## Prepare Environment
- Get Docker if you don't have it yet: https://docs.docker.com/get-docker/

- Get docker-compose if you don't have it yet: https://docs.docker.com/compose/install/

## Test docker-compose
- Run the docker-compose:
```
docker-compose up
```

## Please make sure you can connect to the DB before the interview
The endpoint/credentials are:
```
DB_HOST = "localhost" (or "postgres" from inside the docker compose network)
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_SCHEMA = "public"
```

## (Optional) Test Jupyter environment
- If you want to use python/scala, we are providing a Jupyter notebook container which starts when running the `docker-compose up` command. 
- In order to connect to the notebook, follow the instructions from docker execution, for example:
```
[C 15:48:20.345 NotebookApp]

To access the notebook, open this file in a browser:
    file:///home/jovyan/.local/share/jupyter/runtime/nbserver-8-open.html
Or copy and paste one of these URLs:
    http://6f8a00b0e317:8888/?token=287e67cde7ae9efdffc8498b519a40282d9765aa55361a5f
 or http://127.0.0.1:8888/?token=287e67cde7ae9efdffc8498b519a40282d9765aa55361a5f
```
