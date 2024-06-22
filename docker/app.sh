#!/bin/bash

alembic upgrade head

uvicorn app.run:app --host 0.0.0.0 --port 80
