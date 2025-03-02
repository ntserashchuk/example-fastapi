uvicorn main:app
uvicorn app.main:app —reload
alembic revision -m "create posts table”


alembic init alembic
alembic revision -m "create posts table”
alembic current
alembic upgrade <rev_number>
alembic downgrade -1