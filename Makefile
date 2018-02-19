.PHONY: all
all: pull build migrate run


# Pulls git
pull:
	git pull

# Build containers
# Images are automatically fetched, if necessary, from docker hub
build:
	docker-compose build

# Start a new web container to run migrations
# Use --rm to remove the container when the command completes
migrate:
	docker-compose run --rm web python manage.py migrate

# Run everything in the background with -d
run:
	docker-compose up -d