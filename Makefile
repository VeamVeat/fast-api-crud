NAME_CONTAINER += 'web'

DC += docker-compose -f
MIGRATE += alembic upgrade head

DC_NAME += 'docker-compose.yml'

## build: Build dev python image.
build:
	$(DC) $(DC_NAME) build

## up: Start dev up containers.
up:
	$(DC) $(DC_NAME) up

## start: Start dev containers.
start:
	$(DC) $(DC_NAME) start

## down: destroy dev containers.
down:
	$(DC) $(DC_NAME) down -v

## stop: stop dev containers.
stop:
	$(DC) $(DC_NAME) stop

## restart: restart dev containers.
restart:
	$(DC) $(DC_NAME) stop
	$(DC) $(DC_NAME) up -d

## logs: get logs dev containers.
logs:
	$(DC) $(DC_NAME) logs --tail=100 -f

## ps: see running dev containers.
ps:
	$(DC) $(DC_NAME) ps

## login-api: enter the dev container web
login:
	$(DC) $(DC_NAME) exec $(NAME_CONTAINER) bash

## prune-all: clear all data container all
prune-all:
	docker system prune

## prune-volume: clear all data volume all
prune-volume:
	docker volume prune

## prune-image: clear all data image all
prune-image:
	docker image prune

## prune-container: clear all data container all
prune-container:
	docker container prune

migrate:
	$(DC) $(DC_NAME) exec $(NAME_CONTAINER) $(MIGRATE)

setup: build up migrate
