web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
heroku run "alembic upgrade head"