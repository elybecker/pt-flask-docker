# pt-flask-docker
An example of serving a PyTorch model with Flask in Docker

## Usage
Build the Docker Container
> make build

Start & Connect to Docker Container
> make connect

Start Flask server
> python /app/server.py

Send request with an image to classify (outside container)
> python send_request.py img/horse.jpeg