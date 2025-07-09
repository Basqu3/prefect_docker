# prefect_docker
Testing running prefect workflow manager in docker containers.
Uv is used as a enviroment manager. Make sure that workers do not pull from remote storage (they will grab from github if allowed)

To start the Prefect server ported to localhost:4200
```
docker-compose up -d
```

To create a deployment to run flows found in example_flow.py
```
uv run prefect deploy flows/example_flow.py:example_flow --name example-deployment --pool default-pool
```

To create a worker in the work pool
```
uv run prefect worker start --pool 'default-pool'
```
