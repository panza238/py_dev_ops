# Information on running this small application.

- One must be located in the `timer_api` directory to build the Docker image.
- The app will be available on port 8000 in the container. This port will have to be mapped to a port on the host machine when running the container.
- To build and run the app, run the following commands:
```zsh
docker build -t timer_api .
docker run --rm --name timer_api -p 8000:8000 timer_api
```
    