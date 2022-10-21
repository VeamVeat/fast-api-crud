#!/bin/sh

sleep 1
alembic upgrade head
exec "$@"
