export APPLICATION_PORT := 7777
export USER_ID          := $(shell id -u | xargs)
export USER_NAME        := $(shell id -un | xargs)  
export PROJ_NAME        := pt-flask-docker
export COMPOSE_CMD      := docker-compose -f docker/docker-compose.yaml

build:
	$(COMPOSE_CMD) build
up:
	$(COMPOSE_CMD) up -d
down:
	$(COMPOSE_CMD) down
connect: up
	$(COMPOSE_CMD) exec interactive bash